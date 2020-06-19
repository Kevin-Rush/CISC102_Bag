import random 

correct = 0
its = 10000
case80 = 0
case62 = 0
case44 = 0
case26 = 0
totalCase80 = 0
totalCase62 = 0
totalCase44 = 0
totalCase26 = 0
totalGuess80 = 0
totalGuess62 = 0
totalGuess44 = 0
totalGuess26 = 0
rightF  = open("rightF.txt", "w+")
wrongF  = open("wrongF.txt", "w+") 
for i in range(its):
    case = False
    while not case:
        bag =[]
        red = 0
        green = 0
        i = 0
        while i < 8:                            #generate random bag
            colour = random.randint(0,1)
            if colour == 0:
                red += 1
                bag.append(colour)
                i += 1
            else:
                if green < 7:
                    green += 1
                    bag.append(colour)
                    i += 1   
        bagSum = 0
        for i in range(8):
            bagSum += bag[i]
        if bagSum != 1 and bagSum != 3 and bagSum != 5 and bagSum != 7 and bagSum != 8: #check if it's a valid set, I know there's overkill in this 
            #print("BagSum: "+ str(bagSum))
            case = True

    #0 is a red and 1 is a green

    choices = []
    for i in range(2):                  #pick 3 random positions in the bag array (pull three random balls) and do this twice.
        pick1 = random.randint(0,7)
        pick2 = random.randint(0,7)
        pick3 = random.randint(0,7)
        while pick2 == pick1:
            pick2 = random.randint(0,7)
        while pick3 == pick1 or pick3 == pick2:
            pick3 = random.randint(0,7)
        
        choices.append(bag[pick1])      #add the findings to the choices array to keep track of what "colours" we picked.
        choices.append(bag[pick2])
        choices.append(bag[pick3])

    total = 0
    bagSum = 0
    for i in range(6):
        total += choices[i]     #get total from choices (each green is worth 1)
    for i in range(8):      
        bagSum += bag[i]        #get total from the bag to compare

    if bagSum == 0:             #just counting the number of cases for recording
        totalCase80 += 1
    elif bagSum == 2:
        totalCase62 += 1
    elif bagSum == 4:
        totalCase44 += 1
    elif bagSum == 6:
        totalCase26 += 1

    if total == 0:          #Check what our guess is
        totalGuess80 +=1    #keep track of the guess per case
        if bagSum == 0:     
            correct += 1     #keep track of correct guesses
            case80 +=1         #keep track of correct guesses per case
    elif 1 == total or total == 2:
        totalGuess62 +=1
        if bagSum == 2:
            correct += 1
            case62 +=1
    elif total == 3 or total == 4:
        totalGuess44 +=1
        if bagSum == 4:
            correct += 1
            case44 +=1
    elif total == 6 or total == 5:
        totalGuess26 +=1
        if bagSum == 6:
            correct += 1
            case26 +=1
            

print("\nCorrectness Average: "+str(correct/its))   #pring out information

print("\nTotal Cases 80's: "+str(totalCase80))
print("Total Cases 62's: "+str(totalCase62))
print("Total Cases 44's: "+str(totalCase44))
print("Total Cases 26's: "+str(totalCase26))

print("\nGuessed 80's: "+str(totalGuess80))
print("Guessed 62's: "+str(totalGuess62))
print("nGuessed 44's: "+str(totalGuess44))
print("nGuessed 26's: "+str(totalGuess26))

print("\nPercentage of Correct Guesses for 80: "+str(case80/totalCase80))
print("Percentage of Correct Guesses for 62's: "+str(case62/totalCase62))
print("Percentage of Correct Guesses for 44's: "+str(case44/totalCase44))
print("Percentage of Correct Guesses for 26's: "+str(case26/totalCase26))

print("\nNumber of 80's Guessed Wrong: "+str(totalGuess80-case80))
print("Number of 62's Guessed Wrong: "+str(totalGuess62-case62))
print("Number of 44's Guessed Wrong: "+str(totalGuess44-case44))
print("Number of 26's Guessed Wrong: "+str(totalGuess26-case26))