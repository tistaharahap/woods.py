import sys

class OutOfTheWoods(object):
	
	def __init__(self):
		print chr(27) + "[2J"
		
		self.name = "John Doe"
		self.fragileObjectInFrontOfTree = ""
		self.fragileObjectCondition = ""
		self.wildAnimalSeen = ""
		self.takeTheWildAnimalWithMe = False
		self.stayWithGranny = False
		self.torchCarried = 0
		self.jumpToPond = False
		self.askTheEntity = False
		self.fightBack = True
		
		self.beginStory()
		
	def beginStory(self):
		sys.stderr.write("\x1b[2J\x1b[H")
		print "Before we start, what is your name?",
		self.name = raw_input()
		
		print "\nOk", self.name, "let's start.."
		
		print "\n\n>> It is a sun shining brightly day and you are on your way climbing a mountain with your friends."
		print ">> As you are enjoying the views surrounding you, somehow you were separated from your friends."
		print ">> You find yourself now all alone where woods and forest is all around you."
		
		self.pressAnyKey()
		
		self.theFragilityOfYourHeart()
		
	def theFragilityOfYourHeart(self):
		self.clearScreen()
		
		print ">> Just when you thought things couldn't be any worse than this, you are shocked to see there's this fragile object in front of a big tree."
		
		self.thisIsYourHeart()
		
		self.yourHeartNow()
		
		print "\n>> You just stood there but it didn't take long to continue your way around the forest."
		self.pressAnyKey()
		
		self.whoAreYou()
		
	def yourHeartNow(self):
		print "\nHow is the condition of the %s? Is it broken, cracked or still whole?" % (self.fragileObjectInFrontOfTree),
		self.fragileObjectCondition = raw_input()
		
		if not (self.fragileObjectCondition == "broken" or self.fragileObjectCondition == "cracked" or self.fragileObjectCondition == "whole"):
			self.yourHeartNow()
	
	def thisIsYourHeart(self):
		print "\nWhat fragile object do you see in front of that big tree?",
		self.fragileObjectInFrontOfTree = raw_input()
		
		if self.fragileObjectInFrontOfTree == "":
			self.thisIsYourHeart()
		
	def whoAreYou(self):
		self.clearScreen()
		
		print ">> As you are walking, you are put into a narrow path."
		print ">> Out of nowhere, you see a wild animal right in front of you."
		
		self.thisIsYou()
		
		self.naturalBornLeader()
		
		self.pressAnyKey()
		
		self.areYouCautious()
		
	def areYouCautious(self):
		self.clearScreen()
		
		print ">> The sun is setting and darkness will follow, soon."
		print ">> You see some light not far from where you are, you follow the light."
		print ">> When you get there, you see a hut with an old fashioned water well just in front of it."
		print ">> In its frontyard, there's an old lady brooming the leaves away from her frontyard."
		print "\n>> You have 2 options: ask for directions or stay the night, it's dark."
		
		self.soAreYouCautious()
		
		self.pressAnyKey()
		
		self.theFidelity()
		
	def theFidelity(self):
		self.clearScreen()
		
		print ">> You are continuing your journey, no matter you asked or stayed, it's getting dark, again."
		print ">> Just in front of you, there's an abandoned cave with lots of torches lying around."
		print ">> Let's just say you have a lighter and you can light the torches."
		
		print "\nHow many torches are you taking with you?",
		self.torchCarried == raw_input()
		
		self.pressAnyKey()
		
		self.marvinStyle()
		
	def marvinStyle(self):
		self.clearScreen()
		
		print ">> With your torch lighted, you come across a river stream just ahead."
		print ">> The tide is gentle and you can see it's deep enough to get soakingly fresh."
		
		print "\n>> You have 2 options: you freshen things up a little or you get wet all in."
		
		self.barryIsThePapa()
		
		self.pressAnyKey()
		
		self.theEntity()
		
	def theEntity(self):
		self.clearScreen()
		
		print ">> You are refreshed and on your way through the woods."
		print ">> In a blink of an eye, there's an unknown entity in front of you, hovering from the ground!"
		print ">> You're really frustrated at this point."
		
		print "\n>> You have 2 options: run for your life or ask for directions"
		
		self.higherBeing()
		
		self.pressAnyKey()
		
		self.fightOrSurrender()
		
	def fightOrSurrender(self):
		self.clearScreen()
		
		print ">> The skies are getting its daily dose of light from the sun."
		print ">> It's early morning and you can see a way out from the woods."
		print ">> You reacted and started to walk faster towards the exit."
		print ">> When you got out, a war in the middle of nowhere has just started."
		print ">> One of the soldiers is pointing a gun on your forehead."
		
		print "\n>> You have 2 options: fight for your life or just surrender?"
		
		self.fight()
		
		self.pressAnyKey()
		
		self.concludeNow()
		
	def concludeNow(self):
		self.clearScreen()
		
		print ">> Thank you %s for answering all of the questions." % self.name
		print ">> Now is the time to know more about yourself."
		
		print "\n>> For every answer, the questions represent a part of your identity and of course your personality."
		print ">> Any conclusions you are about to read can change in the future depending on yourself."
		print ">> Some people struggle to change, some just change. It's your call."
		
		self.pressAnyKey()
		
	def fight(self):
		print "\nFight or Surrender?",
		self.fightBack = raw_input()
		
		if self.fightBack == "fight" or self.fightBack == "surrender":
			if self.fightBack == "fight":
				self.fightBack = True
			elif self.fightBack == "surrender":
				self.fightBack = False
			else:
				self.fight()
		else:
			self.fight()
		
	def higherBeing(self):
		print "\nRun or Ask?",
		self.askTheEntity = raw_input()
		
		if self.askTheEntity == "run" or self.askTheEntity == "ask":
			if self.askTheEntity == "run":
				self.askTheEntity = False
			elif self.askTheEntity == "ask":
				self.askTheEntity = True
			else:
				self.higherBeing()
		else:
			self.higherBeing()
		
	def barryIsThePapa(self):
		print "\nFreshen or Wet?",
		self.jumpToPond = raw_input()
		
		if self.jumpToPond == "freshen" or self.jumpToPond == "wet":
			if self.jumpToPond == "freshen":
				self.jumpToPond = False
			elif self.jumpToPond == "wet":
				self.jumpToPond = True
			else:
				self.barryIsThePapa()
		else:
			self.barryIsThePapa()
		
	def soAreYouCautious(self):
		print "\nAsk or Stay?",
		self.stayWithGranny = raw_input()
		
		if self.stayWithGranny == "ask" or self.stayWithGranny == "stay":
			if self.stayWithGranny == "ask":
				self.stayWithGranny == False
			elif self.stayWithGranny == "stay":
				self.stayWithGranny == True
			else:
				self.soAreYouCautious()
		else:
			self.soAreYouCautious()
		
	def thisIsYou(self):
		print "\nWhat animal do you see?",
		self.wildAnimalSeen = raw_input()
		
		if self.wildAnimalSeen == "":
			self.thisIsYou()
	
	def naturalBornLeader(self):
		print "\n>> You are thinking of 2 things, either run away from it or instead you cautiously try to tame it and take it with you.",
		
		print "\n\nDo you run or tame?",
		self.takeTheWildAnimalWithMe = raw_input()
		
		if self.takeTheWildAnimalWithMe == "run" or self.takeTheWildAnimalWithMe == "tame":
			if self.takeTheWildAnimalWithMe == "tame":
				self.takeTheWildAnimalWithMe = True
			else:
				self.takeTheWildAnimalWithMe = False
		else:
			self.naturalBornLeader()
		
	def clearScreen(none):
		sys.stderr.write("\x1b[2J\x1b[H")
		
	def pressAnyKey(none):
		print "\nPress any key to continue >>",
		dummy = raw_input()
		

me = OutOfTheWoods()