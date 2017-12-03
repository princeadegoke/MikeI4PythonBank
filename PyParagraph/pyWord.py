
import re,csv,os




sentences=[]

words=[]


wordcount=0

sentencecount=0



filepath=os.path.join("Resources","paragraph_1.txt")



with open(filepath) as txtfile:

	

	text=txtfile.read()

	words=re.split(r'\s*',text)

	
	sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)



del sentences[-1]



sentencecount=len(sentences)



wordcount=len(words)




averagesentence=wordcount/sentencecount



averagewords=round(sum(len(word) for word in words)/len(words),2)





print("\nPargraph Analysis")

print("-------------------")

print("Approximate Word Count: " + str(wordcount))

print("Aprroximate Sentence Count: " + str(sentencecount))

print("Average Letter Count: " + str(averagewords))

print("Average Sentence Count: " + str(averagesentence))



filename=os.path.join("Output","output.txt")



with open(filename, 'w') as fileobject:

    fileobject.write("\nPargraph Analysis" + "\n")

    fileobject.write("-------------------" + "\n")

    fileobject.write("Approximate Word Count: " + str(wordcount) + "\n")

    fileobject.write("Aprroximate Sentence Count: " + str(sentencecount)+ "\n")

    fileobject.write("Average Letter Count: " + str(averagewords) + "\n")

    fileobject.write("Average Sentence Count: " + str(averagesentence) + "\n")



 