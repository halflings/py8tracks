# py8tracks

A minimal Python binding for 8tracks. Supports searching and playing mixes. WIP.

## Example

Let's see an example showing many features of the 8tracks API:

	# Initializing the API
	api = API8tracks(api_key)

	# Search mixes based on multiple criterias
	tags = ['classical', 'baroque']
	mixset = api.mixset(tags=tags, sort='hot') 
	mixes = mixset['mixes']
	print 'Found {} mixes for the tags: {}'.format(len(mixes), ', '.join(tags))

	for mix in mixes:
		print ""
		print mix
		print ""
		for song in mix:
			print song
			print '-' * 80


Here's the output of this program:

	Found 12 mixes for the tags: classical, baroque

	Mix #3010408 ('Baroque II') - 9 tracks

	. Track : Canon in D major (best version)
	. Url   : http://api.soundcloud.com/tracks/1769106/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	--------------------------------------------------------------------------------
	. Track : Bach , Sinfonia in G
	. Url   : https://api.soundcloud.com/tracks/33741868/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	--------------------------------------------------------------------------------
	. Track : III. allegro assai
	. Url   : https://api.soundcloud.com/tracks/25188290/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	--------------------------------------------------------------------------------
	. Track : Concerto For Guitar, Violin And Orche
	. Url   : https://api.soundcloud.com/tracks/52184301/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	--------------------------------------------------------------------------------
	. Track : 14 心的依歸／耶穌，世人仰望的喜悅 Jesu ,Joy of Man s Desiring, BWV147,from Herz und Mund und Tat und Leben
	. Url   : https://api.soundcloud.com/tracks/93540992/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	--------------------------------------------------------------------------------
	. Track : Rondeau from Premiere Suite de Symphonies (Mouret)
	. Url   : https://api.soundcloud.com/tracks/53051723/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	--------------------------------------------------------------------------------
	. Track : HANDEL Water Music Suite No.2: Alla hornpipe
	. Url   : https://api.soundcloud.com/tracks/54774872/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	--------------------------------------------------------------------------------
	. Track : Bach, Air on G String
	. Url   : https://api.soundcloud.com/tracks/46696885/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	--------------------------------------------------------------------------------
	. Track : Handel – Messiah Hallelujah Chorus (from 50 Best Baroque Hits)
	. Url   : https://api.soundcloud.com/tracks/50091148/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	--------------------------------------------------------------------------------

	Mix #2940510 ('Baroque') - 15 tracks

	. Track : Der Motettenchor: Heinrich Schütz „Die mit Tränen säen“
	. Url   : https://api.soundcloud.com/tracks/49034525/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	--------------------------------------------------------------------------------
	. Track : Canzon prima detta la Roveta
	. Url   : https://api.soundcloud.com/tracks/54688348/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	--------------------------------------------------------------------------------
	. Track : Magnificat
	. Url   : https://api.soundcloud.com/tracks/58035110/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	--------------------------------------------------------------------------------
	. Track : Prelude
	. Url   : https://api.soundcloud.com/tracks/58934014/stream?client_id=3904229f42df3999df223f6ebf39a8fe
	--------------------------------------------------------------------------------

	....