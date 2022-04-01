from colorama import init
init()
import random
import time
import playerstats
#all definitions by Shaan Singh
def e():
	print("""
	""")
# coinflip() will flip a coin
def coinflip(prc=False):
	global flip
	fl=random.randint(1,2)
	if fl==1:
		flip="Heads"
	else:
		flip="Tails"
	if prc==True:
		print(flip)
	return fl

# dieroll() will roll a die
def dieroll(prd=False):
	global roll
	de=random.randint(1,6)
	if de==1:
		roll=str("one")
	elif de==2:
		roll=str("two")
	elif de==3:
		roll=str("three")
	elif de==4:
		roll=str("four")
	elif de==5:
		roll=str("five")
	elif de==6:
		roll=str("six")
	if prd==True:
		print(roll)
	return de

#namegen() will create a random name
def namegen():
	#these tell which letters are consonants and which are vowels
	consonant=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "r", "v", "w", "x", "z","y"]
	vowel= ["a","e","i","o","u","y"]

	#these choose the letters for the first name
	l1n1=random.choice(consonant)
	l2n1=random.choice(vowel)
	l3n1=random.choice(consonant)
	l4n1=random.choice(vowel)
	l5n1=random.choice(consonant)
	
	#these choose the letters for the second name
	l1n2=random.choice(consonant)
	l2n2=random.choice(vowel)
	l3n2=random.choice(consonant)
	l4n2=random.choice(vowel)

	#capitalize the first letters
	l1n1=str(l1n1).upper()
	l1n2=str(l1n2).upper()

	#now we put it all together
	return l1n1 + l2n1 + l3n1 + l4n1 + l5n1 + " " + l1n2 + l2n2 + l3n2 + l4n2

def death():
	print("""
██╗░░░██╗░█████╗░██╗░░░██╗  ██████╗░██╗███████╗██████╗░
╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔══██╗██║██╔════╝██╔══██╗
░╚████╔╝░██║░░██║██║░░░██║  ██║░░██║██║█████╗░░██║░░██║
░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░██║██║██╔══╝░░██║░░██║
░░░██║░░░╚█████╔╝╚██████╔╝  ██████╔╝██║███████╗██████╔╝
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═════╝░╚═╝╚══════╝╚═════╝░""")
	#stretch your console window if you can't see the text art
	exit()

#attack
def attack(**npc):
	print('\033[91m'"You are attacked by " + npc["name"] + " the " + npc["species"] + "!")
	time.sleep(2)
	print(npc["name"]+ "'s stats are:")
	time.sleep(2)
	e()
	print("Attack:" + str(npc["attack"]))
	time.sleep(1)
	print("Defense:" + str(npc["defense"]))
	time.sleep(1)
	print("Health:" + str(npc["health"]))
	time.sleep(2)
	ho = npc["health"] #record the original health for later
	fight=True
	while fight == True:
		e()
		print('\033[91m'"""Choose quickly!
		1. Offensive Attack
		2. Defensive Attack""")
		od=input("(1/2):")
		e()
		if od == str(1):
			ef=random.randint(1,2)
			if ef == 2:
				hb=npc["health"]
				npc["health"]=npc["health"]-((playerstats.attack*5)-npc["defense"])#alter dictionary
				print("you successfully attacked " + npc["name"])
				time.sleep(1)
				print(npc["name"] + "'s health is now " + str(round(npc["health"])))#round
				time.sleep(1)
				if hb == npc["health"]:
					print("Your attack was not effective!")
				else:
					print("Your attack was effective!")
				time.sleep(1)
			if ef == 1:
				print("Your attack has failed!")
				time.sleep(1)
				print(npc["name"] + " attacks!")
				time.sleep(1)
				hb1=playerstats.health
				playerstats.health = playerstats.health - (npc["attack"] - (playerstats.defense))
				if playerstats.health > hb1:
					playerstats.health = hb1 #this makes sure an attack can't raise your health
				print("Your health is now " + str(round(playerstats.health)))
				time.sleep(1)
				if hb1 == playerstats.health:
					print(npc["name"] + "'s attack was not effective!")
				else:
					print(npc["name"] + "'s attack was effective!")
				time.sleep(1)
		elif od == str(2):
			print(npc["name"] + " attacks!")
			time.sleep(1)
			hb2=playerstats.health
			playerstats.health = playerstats.health - ((npc["attack"]) - (playerstats.defense*3))
			if playerstats.health > hb2:
				playerstats.health = hb2 #this makes sure an attack can't raise your health
			print("Your health is now " + str(round(playerstats.health)))
			time.sleep(1)
			if hb2 == playerstats.health:
					print(npc["name"] + "'s attack was not effective!")
			else:
					print(npc["name"] + "'s attack was effective!")
			time.sleep(1)
			e()
			hb=npc["health"]
			npc["health"]=npc["health"]-((playerstats.attack*2)-npc["defense"])
			print("You successfully attacked " + npc["name"])
			time.sleep(1)
			print(npc["name"] + "'s health is now " + str(round(npc["health"])))
			time.sleep(1)
			if hb == npc["health"]:
				print("Your attack was not effective!")
			else:
				print("Your attack was effective!")
			time.sleep(1)
		else:
			print("1 or 2, my guy.")
			time.sleep(1)
		if npc["health"] < 1:
			e()
			print("You won the fight!")
			time.sleep(0.5)
			playerstats.xp = playerstats.xp + (ho*4)
			playerstats.coins = playerstats.coins + ho
			print("Your XP is now " + str(playerstats.xp))
			time.sleep(0.5)
			print(("You now have {coins} coins").format(coins = playerstats.coins))
			fight=False
		elif playerstats.health < 1:
			e()
			fight=False
			death()
		orangejuice()
		

#create a random enemy to attack			
def randomenemy(diff):#"diff" is the difficulty, or strength of the enemy
	if diff == 1:
		etypelist = ["goblin", "human", "skeleton"]
		enemy = {"name":namegen(), "attack":random.randint(1,10), "defense":random.randint(0,5), "health":random.randint(5,35), "species":random.choice(etypelist)}#manipulate list
	elif diff == 2:
		etypelist = ["knight", "ghost", "zombie"]
		enemy = {"name":namegen(), "attack":random.randint(10,40), "defense":random.randint(5,20), "health":random.randint(40,80), "species":random.choice(etypelist)}
	elif diff == 3:
		etypelist = ["dragon", "sorcerer", "ice giant"]
		enemy = {"name":namegen(), "attack":random.randint(50,100), "defense":random.randint(20,50), "health":random.randint(80,200), "species":random.choice(etypelist)}
	return enemy

#orange juice, which replenishes Health
def orangejuice():
	q=False
	while q == False:
		o=input("Drink Orange Juice? (Y/N):").upper()#upper
		if o == "Y":
			if playerstats.orangejuice > 0:
				print('\033[94m'"*You drank one Orange Juice")
				playerstats.health=playerstats.health + 25
				playerstats.orangejuice=playerstats.orangejuice-1
				print("Your health is now " + str(playerstats.health))
				print("Mmm")
			else:
				print('\033[94m'"You don't have any Orange Juice!")
			q=True
		elif o == "N":
			print('\033[94m'"Okay, no Orange Juice this time!")
			q=True
		else:
			print('\033[94m'"y or n, dude!")


#the first quest
def quest1():
	print('\033[92m'"...")
	time.sleep(5)
	print("where am i...")#I left out the "You:" to create more confusion
	time.sleep(5)
	print('\033[94m'"*You have been teleported to the Stoney Mountain by Master Suyka*")
	time.sleep(3)
	print("'\033[92m'You: Oh, that's where I am!")
	time.sleep(3)
	print("You: Master Suyka seemed to be avoiding my question... Oh well. I will ask him later.")
	time.sleep(3)
	print("You: Right, now I've gotta get that crystal!")
	time.sleep(5)
	rocktypelist = ["rock monster", "stone flinger", "mountain troll", "snowman"]
	for g in range(1,6):
		rockenemy = {"name":namegen(), "attack":random.randint(1,10), "defense":random.randint(0,5), "health":random.randint(5,35), "species":random.choice(rocktypelist)}
		attack(**rockenemy)
		time.sleep(random.randint(5,20))
	
	print('\033[92m'"How did you get past my guards?!")
	time.sleep(3)
	print("You: Who said that?!")
	time.sleep(3)
	print("Stone Protector: I am the Stone Protector, the one who defends the Rock Crystal from all those who try to take it.")
	time.sleep(3)
	print("Stone Protector: You are attempting to take the Rock Crystal! You will not get away with this!")
	stoneprotector={"name":"Stone", "attack":10, "defense":5, "health":80, "species":"Crystal Protector"}
	time.sleep(3)
	e()
	attack(**stoneprotector)
	e()
	time.sleep(3)
	print('\033[92m'"Stone Protector: Ah... you have defeated me...")
	time.sleep(3)
	print("Stone Protector: But will you defeat the Master?")
	time.sleep(3)
	print("You: Which Mast-")
	time.sleep(0.5)

#the second quest
def quest2():
	print('\033[92m'"...")
	time.sleep(5)
	print("not this again...")
	time.sleep(5)
	print('\033[94m'"*You have been teleported to the Icy Cave by Master Suyka*")
	time.sleep(3)
	print('\033[92m'"You: I'm sure Master Suyka meant the plan to defeat Dr. Parallaz, right?")
	time.sleep(3)
	print("You: Oh well, I need to focus on getting that Crystal! I'm running out of time!")
	time.sleep(5)
	icetypelist = ["cold assassin", "ice giant", "freezing ninja", "snowman"]
	for f in range(1,4):
		iceenemy = {"name":namegen(), "attack":random.randint(5,20), "defense":random.randint(5,10), "health":random.randint(20,60), "species":random.choice(icetypelist)}
		attack(**iceenemy)
		time.sleep(random.randint(5,20))
	print('\033[92m'"I have failed...")
	time.sleep(3)
	print("You: Who are you?")
	time.sleep(3)
	print("Ice Protector: I am the Ice Protector. Or at least I was, until Captain Axis took my crystal!")
	time.sleep(3)
	print("You: Wait, who is Captain Axis?")
	time.sleep(3)
	print("Ice Protector: He was one of that dirty Dr. Parallaz's thugs!")
	time.sleep(3)
	print("You: Oh no! They've gotten it before me!")
	time.sleep(3)
	print("Ice Protector: Wait, you were here for the crystal as well?!")
	time.sleep(3)
	print("Ice Protector: Of course! You're SteelQuake! YOU HURT MY BROTHER!!!")
	time.sleep(3)
	print("Ice Protector: I may be weakened, but I SHALL DESTROY YOU!!!")
	time.sleep(3)
	e()
	iceprotector={"name":"Ice", "attack":20, "defense":5, "health":50, "species":"former Crystal Protector"}
	attack(**iceprotector)
	e()
	print('\033[92m'"Ice Protector: No! You have defeated me!")
	time.sleep(3)
	print("Ice Protector: If you're going to do this to me, at least do the same to Captain Axis!")
	time.sleep(3)
	print("You: Oh, I intend to!")
	time.sleep(10)
	print("You: Captain Axis! I have caught up with you!")
	time.sleep(3)
	print("Captain Axis: No! SteelQuake! I will not let you destroy everything I have worked so hard for!")
	time.sleep(3)
	e()
	axis={"name":"Axis", "attack":15, "defense":3, "health":75, "species":"Captain of Dr. Parallaz"}
	attack(**axis)
	e()
	time.sleep(3)
	print('\033[92m'"Captain Axis: No! What have you done?!")
	time.sleep(3)
	print("Captain Axis: You are unleashing a true evil on the world!")
	time.sleep(3)
	print("You: You and Dr. Parallaz are the true evil!")
	time.sleep(3)
	print("Captain Axis: Has Master Suyka truly not told you anything?")
	time.sleep(3)
	print("You: Master Suyka told me enough! You are evil!")
	time.sleep(3)
	print("Captain Axis: You will be attacked by Master-")
	time.sleep(0.5)

#the third quest
def quest3():
	print('\033[92m'"...")
	time.sleep(5)
	print("I assume this is the Hellish Pit...")
	time.sleep(5)
	print('\033[94m'"*You have been teleported to the Hellish Pit by Master Suyka*")
	time.sleep(3)
	print("'\033[92m'You: Of course.")
	time.sleep(3)
	print("You: Okay, last one!")
	time.sleep(5)
	firetypelist = ["fire ghost", "flame flinger", "lava monster", "magma man"]
	for y in range(1,6):
		fireenemy = {"name":namegen(), "attack":random.randint(10,30), "defense":random.randint(5,15), "health":random.randint(20,50), "species":random.choice(firetypelist)}
		attack(**fireenemy)
		time.sleep(random.randint(5,20))
	print('\033[92m'"STEELQUAKE!!!")
	time.sleep(3)
	print("You: And that, of course, would be the Protector.")
	time.sleep(3)
	print("Flame Protector: You and your kind will NEVER steal the Fire Crystal, as you have the Ice and Rock!")
	time.sleep(3)
	print("You: Ah, good, I'm here before Dr. Parallaz!")
	time.sleep(3)
	print("You: I've already defeated a Protector twice, I can do it again!")
	time.sleep(3)
	print("Flame Protector: Twice the pride, double the fall!")
	flameprotector={"name":"Flame", "attack":20, "defense":10, "health":80, "species":"Crystal Protector"}
	time.sleep(3)
	e()
	attack(**flameprotector)
	e()
	time.sleep(3)
	print('\033[92m'"Flame Protector: Ah... how could this happen...")
	time.sleep(3)
	print('\033[94m'"*The Crystals have significantly increased your stats!*")
	playerstats.health=250
	playerstats.defaulthealth=250
	playerstats.attack=6
	playerstats.defense=15
	playerstats.xp=playerstats.xp + 3000
	playerstats.coins=playerstats.coins + 1000
	print('\033[92m'"Stone Protector: Wait, who is that?")
	time.sleep(3)
	print('\033[93m'"Dr. Parallaz: IT IS ME.")
	time.sleep(3)
	print('\033[92m'"You: Dr. Parallaz!")
	time.sleep(3)
	print("Dr. Parallaz: Yes, it is me. I do not want to fight you SteelQuake, I simply need the Crystals!")
	time.sleep(3)
	print("You: And why would I give you them? You are evil! You have so many electronics on your body, you look like a cyborg!")
	time.sleep(3)
	print("Dr. Parallaz: I am not evil, just because I have a passion for robotics! If you would let me explain-")
	time.sleep(3)
	print("You: I will not give my time to you, robot!")
	time.sleep(3)
	print("Dr. Parallaz: So be it, then. I will have those crystals, one way or another!")
	time.sleep(3)
	e()
	parallaz={"name":"Dr. Parallaz", "attack":30, "defense":10, "health":150, "species":"Cyborg"}
	attack(**parallaz)
	e()
	time.sleep(3)
	print('\033[92m'"Dr. Parallaz: No! How could you do this?!")
	time.sleep(3)
	print("Dr. Parallaz: You should not be working for Master Suyka! You should be MY ally!")
	time.sleep(3)
	print("You: I will never join you, Parallaz!")
	time.sleep(3)
	print('Dr. Parallaz: So be it. As the late Master Diche once said, "You cannot help one who does not wish to be helped".')
	time.sleep(5)
	e()
	print('\033[94m'"*Dr. Parallaz has escaped with his Jetpack*")
	e()
	time.sleep(3)
	print('\033[92m'"You: He's escaped! I will have to find him! But for now, I should return to the Dojo.")
	time.sleep(3)
	print("You: Master Suyka will need to hear this news!")
	time.sleep(5)

#the final quest
def quest4():
	print('\033[92m'"...")
	time.sleep(5)
	print("Is... this the dark castle...?")
	time.sleep(5)
	print('\033[94m'"*You have been teleported to the Dark Castle by Master Suyka*")
	time.sleep(3)
	print("'\033[92m'You: Huh. The colour theme is pretty light, for a place called the 'Dark Castle'")
	time.sleep(3)
	print("You: Hey, there's a map to the throne room right here! It's as if Dr. Parallaz wants me to come there!")
	time.sleep(15)
	print("Dr. Parallaz: SteelQuake, you have finally arrived!")
	time.sleep(3)
	print("You: I know you are going to try and turn me to your side, Doctor!")
	time.sleep(3)
	print("Dr. Parallaz: Yes, of course! I do not believe you truly know who you are serving.")
	time.sleep(3)
	print("Dr. Parallaz: Master Suyka was the one who actually betrayed Master Diche, and tried to defeat me!")
	time.sleep(3)
	print("You: You are lying!")
	time.sleep(3)
	print("Dr. Parallaz: I had to turn myself into a cyborg because of my injuries!")
	time.sleep(3)
	print("You: Not true! You will pay for your lies!")
	time.sleep(3)
	print("Dr. Parallaz: SO BE IT!!!")
	time.sleep(3)
	sparallaz={"name":"Dr. Parallaz", "attack":40, "defense":10, "health":200, "species":"Cyborg"}
	e()
	attack(**sparallaz)
	e()
	print('\033[92m'"Dr. Parallaz: What have you done... You must realize...")
	time.sleep(3)
	print("Dr. Parallaz: It was Master Suyka who took you from your home world! He took you so he could make you defeat me!")
	time.sleep(3)
	print("You: Impossible!")
	time.sleep(3)
	print("Dr. Parallaz: It's the truth! Feel the crystals, they will reveal the truth to you!")
	time.sleep(3)
	print("You: ...")
	time.sleep(3)
	print("You: So you are telling the truth? I still dont' believe it!")
	time.sleep(3)
	print('\033[93m'"Master Suyka: Believe it, apprentice!")
	time.sleep(3)
	print('\033[92m'"Dr. Parallaz: Oh NO! He's here!")
	time.sleep(3)
	print("You: Master? Is this true?")
	time.sleep(3)
	print('\033[93m'"Master Suyka: Of course it's true, SteelQuake! I have been evil this whole time!")
	time.sleep(3)
	print("Master Suyka: You will serve by my side, along with Dr. Parallaz, and we will rule the world!")
	time.sleep(3)
	print("And you will never, EVER, FOREVER have the chance to go home!!!")
	time.sleep(3)
	print('\033[92m'"You: NO!!!")
	time.sleep(3)
	print("Dr. Parallaz: You must defeat him. SteelQuake!")
	time.sleep(3)
	print("You: How can I? He's a Master!")
	time.sleep(3)
	print("Dr. Parallaz: Give me the Crystals! I will use them to make you as strong as him! You must trust me!")
	time.sleep(3)
	print("You: Fine! I have no other choice!")
	time.sleep(5)
	e()
	print('\033[94m'"*Dr. Parallaz has made you a Master*")
	e()
	playerstats.health=playerstats.health + 500
	playerstats.attack=playerstats.attack + 10
	playerstats.defense=playerstats.defense + 15
	time.sleep(5)
	print('\033[92m'"""Dr. Parallaz: I have sacrificed myself for you! The crystals will slowly drain my life force,
	so that you will have enough power to defeat him!""")
	time.sleep(3)
	print('\033[92m'"Dr. Parallaz: Your stats now match his! But defeating him will still be a difficult feat!")
	time.sleep(3)
	print('\033[93m'"Master Suyka: Exactly!")
	time.sleep(3)
	print("Master Suyka: That's enough talking! NOW GIVE ME THOSE CRYSTALS!")
	time.sleep(3)
	print('\033[92m'"Dr. Parallaz: Good luck, Master SteelQuake!")
	time.sleep(3)
	suyka={"name":"Suyka", "attack":50, "defense":15, "health":500, "species":"Master"}
	e()
	attack(**suyka)
	e()
	time.sleep(5)
	print('\033[92m'"...")
	time.sleep(3)
	print("Master Suyka: Uh... I am defeated.")
	time.sleep(3)
	print("Master Suyka: What are you going to do now? Destroy me?")
	time.sleep(3)
	print('\033[93m'"You: Yes. But I am not just going to destroy you, I have something specific in mind.")
	time.sleep(3)
	e()
	print('\033[94m'"*You have used the crystals to revive Dr. Parallaz*")
	e()
	time.sleep(3)
	print('\033[92m'"Dr. Parallaz: Oof... Am I in heaven?")
	time.sleep(3)
	print('\033[93m'"You: Let's get back to the Dojo, Doctor. It's been a long day.")

#Wow, you've made it to the end! Thanks for playing!