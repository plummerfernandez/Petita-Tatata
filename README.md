# Petita-Tatata
https://soundcloud.com/petita_tatata
A Soundcloud Bot

by Matthew Plummer-Fernandez 
http://www.plummerfernandez.com

Petita recites abstract poetry and posts to Soundcloud. 

To make a soundcloud bot you open up an account on soundcloud with a unique email address (and password), and then you request a client ID and Client Secret by registering your app. https://developers.soundcloud.com/docs

Put those details into a settings.cfg file (see sample):


		client = soundcloud.Client(
		    client_id="xxxxxxxxxx", 
		    client_secret="xxxxxxxxxxxx", 
		    username='youremail',
		    password='yourpassword'
		)

The posting to soundcloud is pretty straightforward after that, its inside a function called 'postToSC'.
You can add more features to your upload, check the soundcloud docs: 
https://developers.soundcloud.com/docs/api/reference#tracks

Petita works by making some jumbled nonsense (mixing vowels and consontants in different patterns) and then it gets Google to read it out and return an audio file. Thats done by the function 'makeSpeech'. I use the python module gTTS (google text to speech). Its very easy too:

		def makeSpeech(poem,poem_filename, voice):
			tts = gTTS(text=poem, lang=voice)
			tts.save(poem_filename)
	
Petita also has some code for slowing down the file using 'sox' but its not using that at the moment.
