def step1():
	print "What happens with an 8 vs 2 - A...?"
	answer = raw_input()

	if answer == "Hit":
		print "\tRight"
		step2()
	elif answer == "Double down":
		print "\tSorry sir but your fuckin retarted."
		step1()
	elif answer == "Stay":
		print "\tAre you drunk sir?"
		step1()
	else:
		print "What the fuckin hell was that do it over again."
		step1()

          
		  
		  
def step2():
	print "What happens with a 9 vs 2...?"
	answer = raw_input()
	
	if answer == "Hit":
		print "\tYou fucking geniues you."
		step3()
	elif answer == "Stay":
		print "OK what the \nH\nE\nL\nFuckinL"
		step3()
	
	else:
		print "\tWrong"
		step2()
	

def step3():
	print "What happens with a 9 vs a 3 - 6...?"
	answer = raw_input()
	
	if answer == "Double down":
		print "\tCorrect you champ you. Look at this snail !!@"
	elif answer == "Stay":
		print "\tDude come on you can focus better than that check the question again."
		step3()
	elif answer == "Hit":
		print "\tSorry your a bitch sir read it again."
		step3()
	else:
		print "\tWhere are you from plantet asshole, read the question over again..."
		step3()

		
def step4():
	print "What happens with a 9 vs 7 - A???"
	answer = raw_input()
	
	if answer == "Stay":
		print "Im sorry sir plz read the quesion again!."
		step4()
	elif answer == "Double down":
		print "Still wrong! you must be one of those drink-o drive-o type guys."
		step4()
	elif answer == "Hit":
		print "You got it sir congradulations!!!!"
		step5()
	else:
		print "Let's try to type in an actuall move in this game ok????..."
		step5()

		
def step5():
	print "What happens with a 10 vs 2 - 9...?"
	answer = raw_input()
	
	if answer == "Double down":
		print "Your a smart person i can tell."
		step5()
	elif answer == "Stay":
		print "This is a wrong answer."
        step5()
	elif answer == "Hit":
		print "This answer is wrong again."
		step5()
		
	else:
		print "What the hell kind of an answer is that that isnt even a move in black jack..."
		step5()
	

		

def start():
	print "Here we go."
	step1()
	
step1()


