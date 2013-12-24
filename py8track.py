import requests
import json
import urllib

class Mix(object):
	def __init__(self, data):
		self.id = data['id']
		self.name = data['name']

	def play():
		pass

	# TODO : give this binding some Object-Oriented goodness

class Client8track(object):
	BASE_URL = 'http://8tracks.com'

	def __init__(self, api_key, api_version=2):
		self.key = api_key
		self.version = api_version

	def _request(self, path, additional_params=None):
		params = dict(api_key=self.key, api_version=self.version)
		if additional_params:
			params.update(additional_params)

		# Building the query url
		query_url = '{}/{}.json'.format(Client8track.BASE_URL, path)

		response = requests.get(query_url, params=params)
		if not response.ok:
			raise requests.HTTPError("Error while consuming the API.")
		else:
			return response.json()

	def mixset(self, safe=True, tags=None, sort=None, includes=None):
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
		params = dict(includes=includes)

		return self._request(path, params)

	def play_token(self):
		return self._request('sets/new')['play_token']

	def play_mix(self, mix_id, play_token):
		path = 'sets/{}/play'.format(play_token)
		params = dict(mix_id=mix_id)
		return self._request(path, params)['set']

	def next_track(self, mix_id, play_token):
		path = 'sets/{}/next'.format(play_token)
		params = dict(mix_id=mix_id)
		return self._request(path, params)['set']


	def report_track(self, mix_id, track_id):
		params = dict(track_id=track_id, mix_id=mix_id)
		return self._request('sets/{}/report', params)



if __name__ == '__main__':
	# Loading the API key from a configuration file
	with open('config.json') as config_file:
		config = json.loads(config_file.read())
		api_key = config['api_key']

	# Initializing the API
	api = Client8track(api_key)

	# Search mixes based on multiple criterias
	tags = ['classical', 'baroque']
	mixset = api.mixset(tags=tags, sort='hot') 
	mixes = mixset['mixes']
	print 'Found {} mixes for the tags: {}'.format(len(mixes), ', '.join(tags))

	hottest_mix = mixes[0]
	print '  - Playing the hottest mix: {}'.format(hottest_mix['name'])

	play_token = api.play_token()
	playback = api.play_mix(hottest_mix['id'], play_token)

	while not playback['at_end']:
		name, url = playback['track']['name'].encode('utf-8'), playback['track']['url']
		print '    . Track : {}'.format(name)
		print '    . Url   : {}'.format(url)
		print '    ' + '-'*60
		playback = api.next_track(hottest_mix['id'], play_token)
