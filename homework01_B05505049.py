file = open("./sample.txt","r")
t = file.read()
file.close()

t = t.replace('?',"")
t = t.replace(',',"")
t = t.replace('"',"")
t = t.replace('.',"")
t = t.replace('-',"")
t = t.replace('\n'," ")
t = t.replace('2000th','2,000th')


T = t.split(' ')

sampleWordList = []
l = len(T)
for n in range(0,l):
    if len(T[n]) > 5:
        sampleWordList.append(T[n])

print(sampleWordList)


while True:
	k = input("Please key in a word with more than five characters :\n")
	if len(k) < 5:
		print("the word you key in is less than five characters!\n")
		continue
	if k in sampleWordList:
		print("The word is in the sampleWordList!\n")
	else:
		print("The word is NOT in the sampleWordList.\n")