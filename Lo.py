#This Python program does some calculations with the winning numbers of the Powerball lottery game.
#The file \"BasePower.txt\" has the winning numbers from 2007 to Sep 2018.
#This is not a suggestion to play lottery or to use those numbers.
#I do it to practice my GitHub and share a Python program.

#num1 to num5 are the 5 numbers of the Powerball game, and the 6th number (num6) is the Power number.
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
#When you add the smallest numbers of the Powerball you get 15 (=1+2+3+4+5) by the way, that combination was never a winner from 2007.
#When you add the bigest numbers of the Powerball you get 335 (=65+66+67+68+69) by the way, this also never was a winner from 2007.
#So there are 335 options of adding the 5 numbers of the PowerBall. 
sum12345=[0]*335
#In the PowerBall you need to choose 5 numbers from 1 to 69. 
most69=[0]*70
#The maximum Power number (the 6th one) right now in 2018 is 26, but during the years from 2007 the maximum number was changed.
#So we will take 45 numbers (1 to 45).
most26=[0]*46 
#The file \"BasePower.txt\" has the Powerball winning numbers from 2007 to around Sep 2018.
with open('BasePower.txt','r') as baseFile:
	try:
		for line in baseFile:
			str1 = line
			num1 = int(str1[13:15])
			num2 = int(str1[16:18])
			num3 = int(str1[19:21])
			num4 = int(str1[22:24])
			num5 = int(str1[25:27])
			num6 = int(str1[28:30])
			
			sumNum=num1+num2+num3+num4+num5
			sum12345[sumNum]=sum12345[sumNum]+1
			
			most69[num1]=most69[num1]+1
			most69[num2]=most69[num2]+1
			most69[num3]=most69[num3]+1
			most69[num4]=most69[num4]+1
			most69[num5]=most69[num5]+1
			most26[num6]=most26[num6]+1
			

			
	except Exception:
		print("Something wrong with the \"BasePower.txt\" file, check the spaces between the numbers")
		
	print("\nThe most frequent summation of the 5 PowerBall numbers\n")		
	
	for i in range(1,335):
		if sum12345[i] > 14: #14 is a random number, you can decrease it to see more option.
			print("num1+num2+num3+num4+num5 =" ,i," apear ", sum12345[i], " times from 2007")
		
	print("\nThe most winners numbers (from 1 to 69) in the PowerBall form 2007\n")
	
	for i in range(1,70):
		if most69[i] > 108: #108 is a random number, you can decrease it to see more winning numbers.
			print("The number =",i, " was a winer " ,most69[i], " times")
	
	print("\nThe most winning Power number, (the 6th number) from 2007\n")
	
	for i in range(1,46):
		if most26[i]> 40: # 40 is a random number, you can decrease it to see more winning numbers.
			print("The Power number =",i," appear ",most26[i])


