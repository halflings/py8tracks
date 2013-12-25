#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import urllib

class MixSet(object):
	def __init__(self, data, api):
		self.api = api
		self.data = data
		self.mixes = [Mix(mix_data, api=self.api) for mix_data in self.data['mixes']]

	def __str__(self):
		return "MixSet '{}' ({}) - {} mixes".format(self.data['name'], self.data['smart_id'], len(self.mixes))

class Track(object):
	def __init__(self, data, mix_id, api):
		self.api = api

		self.data = data
		self.mix_id = mix_id
		
	def report(self):
		self.api.report_track(self.mix_id, self.data['id'])

	def __str__(self):
		string = str()
		string += '. Track : {}\n'.format(self.data['name'].encode('utf-8'))
		string += '. Url   : {}'.format(self.data['url']) 

		return string

class Mix(object):
	def __init__(self, data, api):
		self.api = api

		self.data = data

		self.play_token = None
		
		# Current 'playback' value. Contains a track. (unless it's the end of the mix)
		self.current = None

		self.tracks_cache = []

	def __iter__(self):
		return self

	def next(self):
		# If the mix haven't been played yet ...
		if self.current is None:
			self.play_token = api.play_token()
			self.current = self.api.play_mix(self.data['id'], self.play_token, first=True)
		else:
			self.current = self.api.play_mix(self.data['id'], self.play_token, first=False)

		# If we played all the mix's songs
		if self.current and self.current['at_end']:
			raise StopIteration("Mix exhausted: No more tracks to play")

		self.tracks_cache.append(self.current['track'])	

		return self.current['track']

	def similar(self):
		# TODO : Implement this
		pass


	def __str__(self):
		return "Mix #{} ('{}') - {} tracks".format(self.data['id'], self.data['name'], self.data['tracks_count'])

class API8tracks(object):
	BASE_URL = 'http://8tracks.com'

	def __init__(self, api_key, api_version=3):
		self.key = api_key
		self.version = api_version

	def _request(self, path, sup_params=None):
		params = dict(api_key=self.key, api_version=self.version)
		if sup_params:
			params.update(sup_params)

		# Building the query url
		query_url = '{}/{}.json'.format(API8tracks.BASE_URL, path)


		response = requests.get(query_url, params=params)
		if not response.ok:
			raise requests.HTTPError("Error while consuming the API.")
		else:
			return response.json()

	def mixset(self, safe=False, tags=None, sort=None, include=None):
		smart_id = None

		if tags:
			tags = map(lambda s : urllib.quote(s), tags)
			smart_id = 'tags:{}'.format('+'.join(tags))
		if smart_id is None:
			smart_id = 'all'
		if sort:
			if not sort.lower() in {'hot', 'recent', 'popular'}:
				raise ValueError("Unknown sort type")
			smart_id += ':' + sort
		if safe:
			smart_id += ':safe'

		path = 'mix_sets/{}'.format(smart_id)
		params = dict(include='mixes')
		if include:
			params['include'] += '+' + '+'.join(include)

		mixset_data = self._request(path, sup_params=params)['mix_set']

		mixset = MixSet(mixset_data, api=self)

		return mixset

	def play_token(self):
		return self._request('sets/new')['play_token']

	def play_mix(self, mix_id, play_token, first=False):
		if first:
			path = 'sets/{}/play'.format(play_token)
		else:
			path = 'sets/{}/next'.format(play_token)
		params = dict(mix_id=mix_id)
		playback = self._request(path, params)['set']
		playback['track'] = Track(playback['track'], mix_id, api=self)
		return playback

	def report_track(self, mix_id, track_id):
		params = dict(track_id=track_id, mix_id=mix_id)
		return self._request('sets/{}/report', params)



if __name__ == '__main__':
	# Loading the API key from a configuration file
	with open('config.json') as config_file:
		config = json.loads(config_file.read())
		api_key = config['api_key']

	# Initializing the API
	api = API8tracks(api_key)

	# Search mixes based on multiple criterias
	tags = ['classical', 'baroque']
	mixset = api.mixset(tags=tags, sort='popular') 
	print mixset
	for mix in mixset.mixes:
		print mix
		for song in mix:
			print song
			print '-' * 80