import random
import time
import defs
import playerstats

def e():#make a function
	print("""
	""")

print('\033[92m'" _______________________ ")#the text will be green
print("|                       |")#print
print("|   The Adventures of   |")
print("|      SteelQuake i     |".replace("i", "I"))#replace
print("|                       |")
print("|                       |")
print("|_______________________|")
e()#call a function
time.sleep(3)#give time to read dialogues, notices, etc
npc1={"name":defs.namegen(), "attack":2, "defense":0, "health":25, "species":"human"}#dictionary #variable
print("You have woken up in "+ npc1["name"] +"'s land")#concatenate
e()
time.sleep(3)
print(npc1["name"] + ": Who are you?")
time.sleep(2)
print("You: Uh... My name is John")
time.sleep(2)
print(npc1["name"] + ": Well, John, GET OUT!!!")
time.sleep(2)
e()
defs.attack(**npc1)#use the attack 
time.sleep(3)
e()
print('\033[92m'"You: Oh no! I've killed someone!")
time.sleep(3)
print("You: Where will I go now?")
time.sleep(3)
e()
print(('\033[94m'"*John goes into {npc1name}'s house*").format(npc1name = npc1["name"]))
e()
time.sleep(3)
print('\033[92m'"You: Hey, there's a flyer here! And a level 1 tactical set!")
time.sleep(3)
e()
print('\033[94m'"*The level 1 tactical set has increased your stats*")
e()
playerstats.defaulthealth=playerstats.defaulthealth + 10#operator
playerstats.attack=playerstats.attack + 1
playerstats.defense=playerstats.defense + 1
playerstats.ts=playerstats.ts+1
time.sleep(3)
print('\033[92m'"You: Now I need to see this flyer!")
time.sleep(3)
print("""
╭╮╭╮╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮
┃┃┃┃┃┃╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╰╮╭╮┃╱╱╭╮
┃┃┃┃┃┣━━┳━┳━┳┳━━┳━┫┣━━╮╱┃┃┃┣━━╋╋━━╮
┃╰╯╰╯┃╭╮┃╭┫╭╋┫╭╮┃╭┻┫━━┫╱┃┃┃┃╭╮┣┫╭╮┃
╰╮╭╮╭┫╭╮┃┃┃┃┃┃╰╯┃┃╱┣━━┃╭╯╰╯┃╰╯┃┃╰╯┃
╱╰╯╰╯╰╯╰┻╯╰╯╰┻━━┻╯╱╰━━╯╰━━━┻━━┫┣━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯

Come train with Master Suyka!""")
e()
time.sleep(10)
print("You: I must go there!")
time.sleep(3)
e()
print('\033[94m'"*You are now travelling to the Warrior's Dojo*")
e()
time.sleep(5)
for loop in range(1,3):
	defs.attack(**defs.randomenemy(1))
	time.sleep(random.randint(5,20))
	e()
print('\033[94m'"*You have arrived at the Dojo*")
e()
time.sleep(5)

#Master Suyka's Wisdom
wisdom=["An offensive attack may be more powerful, but it is also more risky!", "A tactical set is a combination of armour and weapons, making it easier to smash bad guys.", "Coins are essential in buying cool things!", "Having a higher XP will earn you more respect, making it easier to get into certain places.", "You can get Orange Juice from the Tavern!"]#list

#I will put all the definitions for the menu items here, instead of defs.py, because they contain much of the story.

#quests
def queststart():
	qe=playerstats.quest
	if qe==0:#comparison #if with conditional
		print('\033[92m'"Master Suyka: Ah, I can see this is your first quest!")
		time.sleep(3)
		print("Master Suyka: The evil Dr. Parallaz is trying to take over the world! You must retrieve all 3 crystals to defeat him!")
		time.sleep(3)
		print("You: Wait, what? Master, you still haven't told me what this world is!")
		time.sleep(3)
		print("Master Suyka: Get going then! The Rock Crystal is in the Stoney Mountain!")
		e()
		defs.quest1()
		e()
		print('\033[94m'"*You have been teleported back to the Dojo by Master Suyka*")
		time.sleep(3)
		print('\033[92m'"You: Woah, that guy was about to say something about a Master!")
		time.sleep(3)
		print("Master Suyka: If there truly is another Master, the world may be in huge danger. You must get the other crystals quickly!")
		time.sleep(3)
		print("Master Suyka: Oh, and you should probably upgrade your tactical set before going to find the next crystal! It will be harder!")
		time.sleep(3)
		print("Yes, Master.")
		time.sleep(3)
		print('\033[94m'"Crystals: 1/3")
		time.sleep(3)
		playerstats.quest=1
		dojomenu()
	elif qe==1:
		print("Master Suyka: You must now go on your second quest. It will be more difficult.")
		time.sleep(3)
		print("Master Suyka: Dr. Parallaz has sent one of his personal assistants to retrieve the Ice Crystal!")
		time.sleep(3)
		print("Master Suyka: You must retrieve it before then, or my entire plan will be under danger!")
		time.sleep(3)
		print("You: Wait, what plan?")
		time.sleep(3)
		print("Master Suyka: No time to explain! Go, now!")
		time.sleep(3)
		print("You: Wait, wh-")
		time.sleep(0.5)
		e()
		defs.quest2()
		e()
		print('\033[94m'"*You have been teleported back to the Dojo by Master Suyka*")
		e()
		time.sleep(3)
		print('\033[92m'"Master Suyka: So, how was your journey?")
		time.sleep(3)
		print("You: Unsettling. Captain Axis called me evil, can you believe that?")
		time.sleep(3)
		print('Master Suyka: Actually, I can. Dr. Parallaz has misled many. As the late Master Diche once said, "You cannot help one who does not wish to be helped".')
		time.sleep(3)
		print("You: Yes, Master. Axis also mentioned another Master who was going to attack me..")
		time.sleep(3)
		print("Master Suyka: This cements our evidence that another Master exists. Be cautious on your next mission!")
		time.sleep(3)
		print("You: Yes, Master.")
		time.sleep(3)
		print('\033[94m'"Crystals: 2/3")
		time.sleep(3)
		playerstats.quest=2
		dojomenu()
	elif qe==2:
		print("Master Suyka: You must retrieve the third Crystal.")
		time.sleep(3)
		print("Master Suyka: Be warned, I can feel Dr. Parallaz himself is going after this one!")
		time.sleep(3)
		print("Master Suyka: The Fire Crystal is in the Hellish Pit. No time for questions!")
		time.sleep(3)
		e()
		defs.quest3()
		e()
		print('\033[94m'"*You have been teleported back to the Dojo by Master Suyka*")
		e()
		time.sleep(3)
		print('\033[92m'"You: Master Suyka! I've gotten the last crystal!")
		time.sleep(3)
		print("Master Suyka: Good, SteelQuake! We finally have the power to defeat him!")
		time.sleep(3)
		print("You: Master, why does everyone keep calling us evil?")
		time.sleep(3)
		print("Master Suyka: That's what they want you to believe, SteelQuake. Do not listen to them, and clear that thought from your mind.")
		time.sleep(3)
		print("You: Yes, Master. One more thing, Dr. Parallaz quoted Master Diche just like you. How could he know that quote?")
		time.sleep(3)
		print("Master Suyka: Yes, it's about time I told you that story.")
		time.sleep(3)
		print("""Master Suyka: Me and Dr. Parallaz were apprentices under Master Diche.
		Dr. Parallaz betrayed and destroyed him. Ever since that day,
		I have been trying to avenge that betrayal. I couldn't do it alone, though.
		I needed an apprentice. And as luck would have it, I have gotten quite a fine one.""")
		time.sleep(10)
		print("Master Suyka: Now get ready for your final showdown with Dr. Parallaz! He will be even stronger the next time you meet him.")
		time.sleep(3)
		print("You: Yes, Master.")
		time.sleep(3)
		print('\033[94m'"Crystals: 3/3")
		time.sleep(3)
		playerstats.quest=3
		dojomenu()
	elif qe==3:
		print("Master Suyka: The time has come, for you to go and face Dr. Parallaz. He has many guards in his castle, but I believe he will not order them to attack you.")
		time.sleep(5)
		print("Master Suyka: He will try and turn you to his side first. If you don't turn, he will deal with you himself.")
		time.sleep(5)
		print("You: Yes, Master. I have prepared myself, both physically and mentally. Send me!")
		time.sleep(3)
		print("Master Suyka: Good! Bring that same determination to the Dark Castle!")
		time.sleep(3)
		e()
		defs.quest4()
		e()
		time.sleep(5)
		print('\033[94m'"*You have teleported yourself back to the Dojo with Dr. Parallaz*")
		e()
		time.sleep(3)
		print("Dr. Parallaz: Wow, it's been such a long time since I was here last. It makes me imagine all that could have been...")
		print('\033[92m'"You: Doctor, I'm sorry for everything I did, without knowing who I was doing it for.")
		time.sleep(3)
		print("Dr. Parallaz: Don't worry, Master Suyka tricked us all. What really matters is, you did the right thing in the end, Master SteelQuake.")
		time.sleep(3)
		print("You: Yes, Doctor. But I want to do the right thing one more time. I don't think 'Master' really fits me.")
		time.sleep(3)
		e()
		print('\033[94m'"*You have transfered your Master powers to Dr. Parallaz*")
		e()
		print('\033[92m'"Master Parallaz: You have made me a Master? But why?")
		time.sleep(3)
		print("You: Master Parallaz, you are much more trained and ready for the role than me. Plus, what I really want to do is go home. You don't mind using the crystals to send me back, do you?")
		time.sleep(3)
		print("Master Parallaz: No, I don't mind. But is this truly what you want?")
		time.sleep(3)
		print("You: Yes. Goodbye, Master Parallaz.")
		time.sleep(3)
		print("Master Parallaz: Goodbye, SteelQuake.")
		time.sleep(3)
		print('\033[96m'"""
████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗
░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║
░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║
░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░""")
		time.sleep(10)

#adventure
def adventure():
	print("You: I'm heading out, Master Suyka!")
	print("Master Suyka: Okay! Be back soon!")
	hd=input("Input Adventure Difficulty (1-3):")
	if hd==str(1) or str(2) or str(3):#or
		adv=True#boolean logic
		while adv:#loop
			enmy=defs.randomenemy(int(hd))
			defs.attack(**enmy)
			rn=(input("Return to Dojo? (Y/N):")).upper()
			if rn=="Y":
				dojomenu()
				break#break loop
	else:
		print("Please input a value between 1 and 3")
		dojomenu()

#tavern
def tavern():
	print("""Welcome to the Tavern!
	1. Restore your Health (50 Coins)
	2. Play Die
	3. Play Coin Flip
	4. Back to Dojo""")
	tv=int(input("(1-4):"))
	if tv == 1:
		if playerstats.coins > 49:
			playerstats.health=playerstats.defaulthealth
			print("Your Health is now " + str(playerstats.health))
			playerstats.coins=playerstats.coins - 50
		else:
			print("You don't have enough Coins")
	elif tv ==  2:
		dr=defs.dieroll()
		if dr==1:
			print("You won 60 coins!")
			playerstats.coins=playerstats.coins + 60
		else:
			print("You lost 10 coins!")
			playerstats.coins=playerstats.coins - 10
	elif tv ==  3:
		cf=defs.coinflip()
		if cf==1:
			print("You won 20 coins!")
			playerstats.coins=playerstats.coins + 20
		else:
			print("You lost 20 coins!")
			playerstats.coins=playerstats.coins - 20
	elif tv==4:
		print("Ok, going back to the Dojo")
		dojomenu()
	else:
		print("We need a number between 1 and 4, please.")
		dojomenu()
	dojomenu()

#shop
def shop():
	print("""Welcome to the Shop!
	1. Buy Orange Juice (25 Coins)
	2. Upgrade Tactical Set (50 Coins)
	3. Back to Dojo""")
	tc=int(input("(1-3):"))
	if tc == 1:
		if playerstats.coins > 24:
			playerstats.orangejuice=playerstats.orangejuice + 1
			print("You now have " + str(playerstats.orangejuice) + " Orange Juice")
			playerstats.coins=playerstats.coins - 25
		else:
			print("You don't have enough Coins")
	elif tc == 2:
		if playerstats.coins > 49:
			playerstats.defaulthealth=playerstats.defaulthealth + 10
			playerstats.attack=playerstats.attack + 1
			playerstats.defense=playerstats.defense + 1
			playerstats.ts=playerstats.ts+1
			print("You now have a " + str(playerstats.ts) + " level Tactical Set")
			playerstats.coins=playerstats.coins - 50
		else:
			print("You don't have enough Coins")
	elif tc == 3:
		print("Ok, going back to the Dojo")
		dojomenu()
	else:
		print("We need a number between 1 and 3, please.")
		dojomenu()
	dojomenu()

#the dojo menu
def dojomenu():
	print('\033[92m'"""Welcome to the Dojo, SteelQuake.
	1. Quest
	2. Adventure
	3. Go to Tavern
	4. Go to Shop
	5. Ask for Wisdom
	6. View Stats
	""")
	dc=int(input("(1-5):"))
	if dc==1:
		queststart()
	elif dc==2:
		adventure()
	elif dc==3:
		tavern()
	elif dc==4:
		shop()
	elif dc==5:
		print("Master Suyka: All right, here's some wisdom for ya;")
		e()
		time.sleep(3)
		print(random.choice(wisdom))
		e()
		time.sleep(3)
		dojomenu()
	elif dc==6:
		print("Health: " + str(playerstats.health))#casting
		print("Attack: " + str(playerstats.attack))
		print("Defense: " + str(playerstats.defense))
		print("Tactical Set Level: " + str(playerstats.ts))
		print("XP: " + str(playerstats.xp))
		print("Coins: " + str(playerstats.coins))
		print("Crystals: " + str(playerstats.quest))
		dojomenu()
	else:
		print("Master Suyka: Choose a number between 1 and 6 please, our Dojo doesn't do existentialism.")


print('\033[92m'"Master Suyka: Welcome to the Dojo! What is your name?")
time.sleep(3)
print("You: It's John, Master.")
time.sleep(3)
print("Master Suyka: Well, John, John is a bit of a boring name.")
time.sleep(3)
print("Master Suyka: From this moment on, you shall be known as SteelQuake!")
time.sleep(3)
print("Master Suyka: We have to defeat the evil Dr. Parallaz! I'll give you more info when you start the Quest.")
time.sleep(3)
print("Master Suyka: But please, come in! I'll give you a free health regeneration for now, but next time you'll have to buy it!")
playerstats.health=playerstats.defaulthealth
e()
time.sleep(5)
dojomenu()