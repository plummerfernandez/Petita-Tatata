#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# INSTALL NOTES
# sudo pip install gTTS
# pip install soundcloud

from gtts import gTTS
import soundcloud
import random
from random import shuffle
import tempfile
import os, time

# GTTS SUPPORTED LANGUAGES
"""
'af' : 'Afrikaans'
'sq' : 'Albanian'
'ar' : 'Arabic'
'hy' : 'Armenian'
'ca' : 'Catalan'
'zh' : 'Chinese',
'zh-cn' : 'Chinese (Mandarin/China)'
'zh-tw' : 'Chinese (Mandarin/Taiwan)'
'zh-yue' : 'Chinese (Cantonese)'
'hr' : 'Croatian'
'cs' : 'Czech'
'da' : 'Danish'
'nl' : 'Dutch'
'en' : 'English'
'en-au' : 'English (Australia)'
'en-uk' : 'English (United Kingdom)'
'en-us' : 'English (United States)'
'eo' : 'Esperanto'
'fi' : 'Finnish'
'fr' : 'French'
'de' : 'German'
'el' : 'Greek'
'ht' : 'Haitian Creole'
'hi' : 'Hindi'
'hu' : 'Hungarian'
'is' : 'Icelandic'
'id' : 'Indonesian'
'it' : 'Italian'
'ja' : 'Japanese'
'ko' : 'Korean'
'la' : 'Latin'
'lv' : 'Latvian'
'mk' : 'Macedonian'
'no' : 'Norwegian'
'pl' : 'Polish'
'pt' : 'Portuguese'
'pt-br' : 'Portuguese (Brazil)'
'ro' : 'Romanian'
'ru' : 'Russian'
'sr' : 'Serbian'
'sk' : 'Slovak'
'es' : 'Spanish'
'es-es' : 'Spanish (Spain)'
'es-us' : 'Spanish (United States)'
'sw' : 'Swahili'
'sv' : 'Swedish'
'ta' : 'Tamil'
'th' : 'Thai'
'tr' : 'Turkish'
'vi' : 'Vietnamese'
'cy' : 'Welsh' #robotic
"""





client = soundcloud.Client(
    client_id="xxxxxxxxxxxxxxxxxxxxxxxx", #Client ID
    client_secret="xxxxxxxxxxxxxxxxxxxxxxxx", #Client secretion
    username='youremail@emailprovider.com',
    password='yourpassword'
)
print "client credentials ok"

def makeSpeech(poem,poem_filename, voice):
	tts = gTTS(text=poem, lang=voice)
	tts.save(poem_filename)

def postToSC(poem_filename, poem_title):
	track = client.post('/tracks', track={
    	'title': poem_title,
    	'sharing': 'public', #private or public
    	'asset_data': open(poem_filename, 'rb')
	})


def voice():
	voices = ['fr','de','ko','ja','it','zh','es','es-us','no','sv']
	shuffle(voices)
	shuffle(voices)
	return voices[0]


def genPoem():

	#Gadji beri bimba
	hugoball = """gadji beri bimba glandridi laula lonni cadori
	gadjama gramma berida bimbala glandri galassassa laulitalomini
	gadji beri bin blassa glassala laula lonni cadorsu sassala bim 
	gadjama tuffm i zimzalla binban gligla wowolimai bin beri ban 
	o katalominai rhinozerossola hopsamen laulitalomini hoooo 
	gadjama rhinozerossola hopsamen 
	bluku terullala blaulala loooo 

	zimzim urullala zimzim urullala zimzim zanzibar zimzalla zam 
	elifantolim brussala bulomen brussala bulomen tromtata 
	velo da bang band affalo purzamai affalo purzamai lengado tor 
	gadjama bimbalo glandridi glassala zingtata pimpalo ögrögöööö 
	viola laxato viola zimbrabim viola uli paluji malooo 

	tuffm im zimbrabim negramai bumbalo negramai bumbalo tuffm i zim 
	gadjama bimbala oo beri gadjama gaga di gadjama affalo pinx 
	gaga di bumbalo bumbalo gadjamen 
	gaga di bling blong 
	gaga blung"""

	s = " "
	hb = hugoball.split()
	shuffle(hb)
	hba = hb + hb

	vh1 = hba[1]+s+hba[0]+s+hba[1]+s+hba[0]+". "
	vh2 = hba[1]+s+hba[1]+". "
	vh3 = hba[0]+s+hba[1]+s+hba[0]+s+hba[1]+". "
	vh4 = hba[0]+s+hba[0]+". "
	vh5 = hba[1]+s+hba[0]+s+hba[1]+s+hba[0]+". "
	vh6 = hba[1]+". "
	vh7 = hba[0]+". "
	vh8 = hba[2]+s+hba[2]+". "
	vh9 = hba[3]+s+hba[3]+". "
	vh10 = hba[3]+s+hba[1]+s+hba[1]+s+hba[0]+". "
	

	vs = ['a','e','i','o','u']
	cs = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','y','z']
	
	#shuffle(vs)
	#shuffle(cs)

	### WORD TRIPLETS
	w1 = cs[0]+vs[0]+cs[1]+vs[0]+cs[2]+vs[0]
	w2 = cs[0]+vs[1]+cs[1]+vs[1]+cs[2]+vs[0]
	w3 = cs[1]+vs[1]+cs[2]+vs[1]+cs[3]+vs[1]
	w4 = cs[3]+vs[1]+cs[3]+vs[1]+cs[3]+vs[1]
	w5 = cs[4]+vs[2]+cs[5]+vs[0]+cs[4]+vs[2]
	w6 = cs[4]+vs[2]+cs[4]+vs[1]+cs[2]+vs[2]
	w7 = cs[4]+vs[2]+cs[5]+vs[2]+cs[4]+vs[0]
	w8 = cs[4]+vs[2]+cs[4]+vs[3]+cs[2]+vs[0]
	## petita tatata
	w9 = cs[6]+vs[2]+cs[5]+vs[3]+cs[5]+vs[0]
	w10 = cs[5]+vs[0]+cs[5]+vs[0]+cs[5]+vs[0]

	### WORD DOUBLIES
	#shuffle(vs)
	shuffle(cs)
	d1 = cs[0]+vs[0]+vs[0]+cs[0]+vs[0]+vs[0]
	d2 = cs[1]+vs[0]+vs[0]+cs[0]+vs[0]+vs[0]
	d3 = cs[2]+vs[0]+vs[0]+cs[2]+vs[0]+vs[0]
	d4 = cs[3]+vs[0]+vs[0]+cs[3]+vs[0]+vs[0]

	### PAPAPAPAPAPA
	#shuffle(vs)
	shuffle(cs)
	p1 = cs[5]+vs[4]+cs[5]+vs[4]+cs[5]+vs[4]+cs[5]+vs[4]+cs[5]+vs[4]+cs[5]+vs[0]
	p2 = cs[8]+vs[4]+cs[8]+vs[4]+cs[8]+vs[4]+cs[8]+vs[4]+cs[8]+vs[4]+cs[8]+vs[0]
	p3 = cs[8]+vs[0]+cs[8]+vs[0]+cs[8]+vs[0]+cs[8]+vs[0]+cs[8]+vs[0]+cs[8]+vs[0]
	p4 = cs[8]+vs[1]+cs[8]+vs[0]+cs[8]+vs[0]+cs[8]+vs[0]+cs[8]+vs[0]+cs[8]+vs[0]

	### ti 
	#shuffle(vs)
	#shuffle(cs)
	t1 = cs[0]+vs[0]
	t2 = cs[1]+vs[0]
	t3 = cs[2]+vs[1]
	t4 = cs[3]+vs[1]

	### laklak
	#shuffle(vs)
	#shuffle(cs)
	l1 = cs[4]+vs[0]+cs[4]+cs[4]+vs[0]+cs[4]
	l2 = cs[3]+vs[0]+cs[4]+cs[3]+vs[0]+cs[4]
	l3 = cs[3]+vs[1]+cs[4]+cs[3]+vs[0]+cs[4]
	l4 = cs[4]+vs[1]+cs[4]+cs[3]+vs[0]+cs[4]

	### WORD LISTS
	ws = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10]
	ds = [d1,d2,d3,d4]
	ps = [p1,p2,p3,p4]
	ts = [t1,t2,t3,t4]
	ls = [l1,l2,l3,l4]

	shuffle(ws)
	shuffle(ds)
	shuffle(ps)
	shuffle(ts)
	shuffle(ls)

	### MAKE VERSES
	v1 = w1+s+w2+s+w3+s+w4+". "
	v2 = w2+s+w1+s+w4+s+w3+". "
	v3 = w5+s+w6+s+w7+s+w8+". "
	v4 = w6+s+w5+s+w8+s+w7+". "
	v5 = ws[1]+s+ws[0]+s+ws[0]+s+ws[0]+". "
	v6 = ws[1]+s+ws[0]+s+ws[3]+s+ws[3]+". "
	v7 = ws[1]+s+ws[2]+s+ws[3]+s+ws[4]+". "
	v8 = ws[2]+s+ws[2]+s+ws[3]+s+ws[3]+". "
	v9 = ds[0]+s+ds[1]+". "
	v10 = ds[1]+s+ds[1]+". "
	v11 = ds[2]+s+ds[2]+". "
	v12 = ds[2]+s+ts[0]+s+ds[2]+". "
	v13 = ds[2]+s+ts[1]+s+ds[2]+". "
	v14 = ts[1]+s+ts[0]+s+ts[0]+s+ts[0]+". "
	v15 = ts[1]+s+ts[0]+s+ts[3]+s+ts[3]+". "
	v16 = ps[1]+s+ts[2]+s+ts[3]+s+ts[3]+". "
	v17 = ts[2]+s+ts[2]+s+ts[3]+s+ts[3]+". "
	v18 = ps[0]+". "
	v19 = ps[1]+". "
	v20 = ps[1]+s+ps[1]+". "
	v21 = ls[1]+s+ls[1]+". "
	v22 = ls[0]+s+ls[1]+". "
	v23 = ls[0]+s+ls[0]+". "
	v24 = ls[1]+". "
	v25 = ts[1]+". "
	v26 = ts[1]+". "

	verses1 = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26, vh1, vh2, vh3, vh4, vh5, vh6, vh7, vh8, vh9, vh10]

	verses = verses1 + verses1 + verses1 + verses1 + verses1 + verses1

	shuffle(verses)

	numverses = random.randrange(6, 24, 2)
	print "Number of verses = " + str(numverses)

	poem = ""
	poemname = verses[1]



	for i in range(1,numverses):
		poem = poem + verses[i]


	#poemname = w1+s+w2
	#poem = v1 + v2 + v3 + v4
	print poem
	return poemname,poem

def makeSlow(input_filename, output_filename): #use sox to slow down file
	temp3 = tempfile.mkstemp(suffix = ".wav")
	temp4 = tempfile.mkstemp(suffix = ".wav")
	os.system("lame --decode " + input_filename + " " + temp3[1])
	tempo = random.uniform(0.8, 0.92)
	os.system('sox '+temp3[1]+ " " +temp4[1] + " tempo 0.8")
	os.system("lame --decode " + temp4[1] + " " + output_filename)

# GENERATE POEM
poemname, newpoem = genPoem()
# MAKE TEMP MP3 FILENAME
temp = tempfile.mkstemp(suffix = ".mp3")
# GET GOOGLE TO SAY IT
v = voice()
makeSpeech(newpoem, temp[1], 'ja')
#SLOW IT
#temp2 = tempfile.mkstemp(suffix = ".mp3")
#makeSlow(temp[1],temp2[1])
#time.sleep(5)
# POST ON SOUNDCLOUD
postToSC(temp[1],poemname)



#postToSC("hugoball-es.mp3","Gadji -es")


print "finished"
