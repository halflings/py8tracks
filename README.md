# py8tracks

A minimal Python binding for 8tracks. Supports searching and playing mixes. WIP.

## Example

Let's see an example showing many features of the 8tracks API:

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


Here's the output of this program:

	MixSet 'Baroque + classical' (tags:classical+baroque:popular) - 12 mixes
	Mix #2940510 ('Baroque') - 15 tracks
	. Track : Der Motettenchor: Heinrich Schütz „Die mit Tränen säen“
	. Url   : http://8tracks.com/tracks/22695024
	--------------------------------------------------------------------------------
	. Track : Canzon prima detta la Roveta
	. Url   : http://8tracks.com/tracks/22694904
	--------------------------------------------------------------------------------
	. Track : Magnificat
	. Url   : http://8tracks.com/tracks/22694816
	--------------------------------------------------------------------------------
	. Track : Prelude
	. Url   : http://8tracks.com/tracks/22695205
	--------------------------------------------------------------------------------
	. Track : Marche pour la cérémonie des Turcs
	. Url   : http://8tracks.com/tracks/21153796
	--------------------------------------------------------------------------------
	. Track : Domenico Scarlatti Sonata L 366
	. Url   : http://8tracks.com/tracks/22694599
	--------------------------------------------------------------------------------
	. Track : Samuel Scheidt: Variationen über Bergamasca
	. Url   : http://8tracks.com/tracks/22694983
	--------------------------------------------------------------------------------
	. Track : Michael Praetorius
	. Url   : http://8tracks.com/tracks/22694765
	--------------------------------------------------------------------------------
	. Track : Largo
	. Url   : http://8tracks.com/tracks/22694736
	--------------------------------------------------------------------------------
	. Track : Arcangelo Corelli 'La Follia Variations' Op. 5
	. Url   : http://8tracks.com/tracks/22694939
	--------------------------------------------------------------------------------
	. Track : Allegro
	. Url   : http://8tracks.com/tracks/22695072
	--------------------------------------------------------------------------------
	. Track : Claudio Monteverdi, Si ch'io vorrei morire
	. Url   : http://8tracks.com/tracks/22694848
	--------------------------------------------------------------------------------
	. Track : Antoine Charpentier
	. Url   : http://8tracks.com/tracks/21526639
	--------------------------------------------------------------------------------
	. Track : 1630): "Lehre uns bedenken"
	. Url   : http://8tracks.com/tracks/22694626
	--------------------------------------------------------------------------------
	. Track : Christy Panchal, Mezzo
	. Url   : http://8tracks.com/tracks/22695117
	--------------------------------------------------------------------------------
	Mix #3010408 ('Baroque II') - 9 tracks
	. Track : Canon in D major (best version)
	. Url   : http://8tracks.com/tracks/7808034
	--------------------------------------------------------------------------------
	. Track : Bach , Sinfonia in G
	. Url   : http://8tracks.com/tracks/22697906
	--------------------------------------------------------------------------------