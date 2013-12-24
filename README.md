# py8tracks

A minimal Python binding for 8tracks. Supports searching and playing mixes. WIP.

## Example

Let's see an example showing many features of the 8tracks API:

	api_key = 'YOUR API KEY HERE'

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


Here's the output of this program:

	Found 12 mixes for the tags: classical, baroque
	  - Playing the hottest mix: Baroque II
	    . Track : Canon in D major (best version)
	    . Url   : http://api.soundcloud.com/tracks/1769106/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	    ------------------------------------------------------------
	    . Track : Bach , Sinfonia in G
	    . Url   : https://api.soundcloud.com/tracks/33741868/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	    ------------------------------------------------------------
	    . Track : III. allegro assai
	    . Url   : https://api.soundcloud.com/tracks/25188290/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	    ------------------------------------------------------------
	    . Track : Concerto For Guitar, Violin And Orche
	    . Url   : https://api.soundcloud.com/tracks/52184301/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	    ------------------------------------------------------------
	    . Track : 14 心的依歸／耶穌，世人仰望的喜悅 Jesu ,Joy of Man s Desiring, BWV147,from Herz und Mund und Tat und Leben
	    . Url   : https://api.soundcloud.com/tracks/93540992/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	    ------------------------------------------------------------
	    . Track : Rondeau from Premiere Suite de Symphonies (Mouret)
	    . Url   : https://api.soundcloud.com/tracks/53051723/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	    ------------------------------------------------------------
	    . Track : HANDEL Water Music Suite No.2: Alla hornpipe
	    . Url   : https://api.soundcloud.com/tracks/54774872/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	    ------------------------------------------------------------
	    . Track : Bach, Air on G String
	    . Url   : https://api.soundcloud.com/tracks/46696885/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	    ------------------------------------------------------------
	    . Track : Handel – Messiah Hallelujah Chorus (from 50 Best Baroque Hits)
	    . Url   : https://api.soundcloud.com/tracks/50091148/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	    ------------------------------------------------------------