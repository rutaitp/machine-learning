#My sentence
myTEDTalk = "Ladies and gentlemen, what gives me tremendous \
confidence in the future is the fact that we are now more empowered \
as individuals to take on the grand challenges of this planet. We have \
the tools with this exponential technology. We have the passion of the DIY \
innovator. We have the capital of the techno-philanthropist. And we have three \
billion new minds coming online to work with us to solve the grand challenges, to \
do that which we must do. We are living into extraordinary decades ahead."

#Put all characters to lower case
myTEDTalk = myTEDTalk.lower()

#Turn my string into array of objects
myArray = list (myTEDTalk)

#Sort them by alphabet
myArray.sort()
print myArray

#implement run-length encoding
def rle(myArray):
	timesShown = 1
	myEncodedList = []
	for i in range(1, len(myArray)):
		if myArray[i-1] == myArray[i]:
			timesShown += 1 
		else:
			myEncodedList.append((myArray[i-1], timesShown))
			timesShown = 1
		if i == len(myArray) - 1 :
			myEncodedList.append((myArray[i], timesShown)) #how to put new line here?
	return myEncodedList

print rle(myArray)