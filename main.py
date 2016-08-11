#!/usr/bin/python2

import os,platform,time,random
from commands import getstatusoutput
distri=platform.dist()

def ani():
	c=5
	while c>0:
		os.system("dialog --backtitle 'ANAGRAM GAME' --title 'Play the game' --infobox 'Lets continue with the fun!!!\n..#####..................' 10 40")	
		time.sleep(0.02)		
		os.system("dialog --backtitle 'ANAGRAM GAME' --title 'Play the game' --infobox 'Lets continue with the fun!!!\n........#####............' 10 40")
		time.sleep(0.02)		
		os.system("dialog --backtitle 'ANAGRAM GAME' --title 'Play the game' --infobox 'Lets continue with the fun!!!\n.............#####.......' 10 40")
		time.sleep(0.02)
		os.system("dialog --backtitle 'ANAGRAM GAME' --title 'Play the game' --infobox 'Lets continue with the fun!!!\n.................#####...' 10 40")
		time.sleep(0.02)		
		os.system("dialog --backtitle 'ANAGRAM GAME' --title 'Play the game' --infobox 'Lets continue with the fun!!!\n....................#####' 10 40")
		time.sleep(0.02)		

		c-=1
	
x=os.system("dialog  --backtitle 'ANAGRAM GAME' --title 'ANAGRAM GAME ' --yesno 'Lets see whether you can play with letters to make meaningfull words.\nThe game is as follows\n\n\nGiven the letter in a jumbled manner , you need to make a meaning full word from it.??\n\n\nWANT TO PLAY ' 20 50")
if x!= 0:
	os.system("dialog --backtitle 'ANAGRAM GAME' --infobox 'Terminating the program!\nThanks for using my game\n\n\n BY ADARSH' 10 40 ")
	time.sleep(0.4)
	exit()
	
#time.sleep(0.5)
x=os.system("dialog --backtitle \"USER DIFICULTY LEVEL\" --radiolist \"CHOOSE AS YOU DESIRE\" 10 40 3  1 EASY on 2 MEDIUM off 3 HARD off 2>/usr/tmp/choice.txt")
if x!=0:
	os.system("dialog --backtitle \"ANAGRAM GAME\" --infobox 'Terminating the program!\nThanks for using my game\nBY ADARSH' 10 40")
	time.sleep(0.4)
	exit()
loc=""
fh=open("/usr/tmp/choice.txt","r+")
choice=fh.readlines()
fh.close()	
loc="/PROJECT_ANAGRAM/words.txt"
os.system("rm -rf '/usr/tmp/choice.txt'")
#print loc
fread=open(loc,"rw+")
words=list()
if choice[0] == '1':
	life=5
	score=100
	for lines in fread:
		if(len(lines) >=4 and len(lines)<=5):
			if lines[:-1].isalpha():
				words.append(lines[:-1].upper())
elif choice[0] == '2':
	life=6
	score=300
	for lines in fread:
		if(len(lines) >= 5 and len(lines)<=7):
			if lines[:-1].isalpha():
				words.append(lines[:-1].upper())
else:
	life=8
	score=500
	for lines in fread:
		if(len(lines) >= 6):
			if lines[:-1].isalpha():
				words.append(lines[:-1].upper())
	
#print words
fread.close()
totalwords=len(words)
ani()
time.sleep(0.8)
level=1
yscore=0
while life>=0 :
	sublife=1	
	word=words[random.randint(0,totalwords-1)]
	shuffle=list(word)
	random.shuffle(shuffle)
#	print shuffle
#	print word
	x=os.system("dialog --backtitle 'ANAGRAM GAME' --title 'LEVEL {}     SCORE {}     LIFE {}' --inputbox 'The letters are {}\n\n\n\nEnter a possible word made of these characters' 20 50 2>/usr/tmp/ans.txt".format(level,yscore,life,shuffle))
	if x!=0:
		os.system("dialog --backtitle \"ANAGRAM GAME\" --infobox 'Terminating the program!\nThanks for using my game\n\n\nBY ADARSH' 10 40")
		time.sleep(0.4)
		exit()
	fr=open("/usr/tmp/ans.txt","r")
	inp=fr.readlines()
	fr.close()
	if len(inp)==0:
		os.system("dialog --backtitle 'ANAGRAM GAME' --title 'WRONG INPUT' --msgbox 'Enter a valid value' 10 40")
		continue
			
	inp[0]=inp[0].upper()
	t1=random.randint(0,len(word)/2)
	t2=random.randint(2,len(word))
	if t1 == t2:
		t2=random.randint(3,len(word))	
	hint=""
	for i in range(0,len(word)):
		if(t1==i or t2==i):
			hint=hint+word[i]
		else:
			hint=hint+'*'
	os.system("rm -rf /usr/tmp/ans.txt")	
	if inp[0] in words:
		level+=1
		yscore+=score
		os.system("dialog --backtitle 'ANAGRAM GAME' --msgbox 'CONTRATULATIONS!!! YOU HAVE REACHED LEVEL {}'  20 40 ".format(level))
	elif sublife != 0:
		os.system("dialog --backtitle 'ANAGRAM GAME' --msgbox 'One of the possible word hint  is {}\n\nTRY AGAIN'  20 40 ".format(hint))		
		time.sleep(0.4)
		x=os.system("dialog --backtitle 'ANAGRAM GAME' --title 'LEVEL {}     SCORE {}     LIFE {}' --inputbox 'The letters are {}\n\n\n\nEnter a possible word made of these characters' 20 50 2>/usr/tmp/ans.txt".format(level,yscore,life,shuffle))
		if x!=0:
			os.system("dialog --backtitle \"ANAGRAM GAME\" --infobox 'Terminating the program!\nThanks for using my game\n\n\nBY ADARSH' 10 40")
			time.sleep(0.4)
			exit()		
		fr=open("/usr/tmp/ans.txt","r")
		inp=fr.readlines()
		fr.close()	
		inp[0]=inp[0].upper()
		if inp[0] in words:
			level+=1
			os.system("dialog --backtitle 'ANAGRAM GAME' --msgbox 'CONTRATULATIONS!!! YOU HAVE REACHED LEVEL {}'  15 40 ".format(level))
			yscore+=score		
		else:
			os.system("dialog --backtitle 'ANAGRAM GAME' --msgbox 'You lost a life!!!\n\n\nMoving on to next word\n\nThe correct answer was {} '  25 40 ".format(word))		
			life-=1
		os.system("rm -rf /usr/tmp/ans.txt")		


os.system("dialog --backtitle 'ANAGRAM GAME' --msgboxbox 'YOUR FINAL SCORE IS {}' 20 20".format(yscore))
os.system("dialog --backtitle 'ANAGRAM GAME' --inputbox 'Enter your name to save your score\n\n\n' 40 20 2>>/usr/tmp/name.txt")
fh=open("/usr/tmp/name.txt",'r+')
fw=open("/PROJECT_ANAGRAM/leaderboard.txt","a+")
fw.write("line   {}".format(yscore))		
fw.close()



