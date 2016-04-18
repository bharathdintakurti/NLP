import math
import stopwords


def positiveinit(data):

    #Create Positive MegaDoc

	reviews_file = open(data, "r")
	megadoc = ""


	for line in reviews_file:

    		megadoc  = megadoc + line

    #Create Vocabulary List

	words = megadoc.split()

	words.sort()
	global cpl
	cpl = words.count('+')

	for i in range(cpl):
		words.remove('+')

	#print(words)

	global positivefreq
	positivefreq=[]
	global positivevocab
	positivevocab =[]

	while len(words) > 0:

		temp = words[0]
		#print(temp)


		count = words.count(temp)
		#print(count)
		if count > 1 :
			positivevocab.append(str(temp))
			positivefreq.append(count)

		for i in range(count):
			words.remove(temp)



	reviews_file.close()

	#print("Positive Init Completed")
	return

def negativeinit(data):

    #Create Negative MegaDoc

	reviews_file = open(data, "r")

	megadoc = ""


	for line in reviews_file:

		megadoc  = megadoc + line

    #Create Vocabulary List

	words = megadoc.split()
	words.sort()

	global cnl
	cnl = words.count('-')

	for i in range(cnl):
		words.remove('-')



	global negativefreq
	negativefreq=[]
	global negativevocab
	negativevocab =[]

	while len(words) > 0:

		temp = words[0]


		count = words.count(temp)

		if count > 1 :

			negativevocab.append(str(temp))
			negativefreq.append(count)

		for i in range(count):
			words.remove(temp)


	reviews_file.close()

	#print("Negative Init Completed")
	return


def calculate_positive(sentence):

	prob = math.log2(cpl /(cpl + cnl))

	for word in sentence:

		if word in positivevocab :

			index = positivevocab.index(word)
			count = positivefreq[index]

			#Calculate Unigram probability of a word using add-one smoothing
			probword = math.log2((count + 1)/(sum(positivefreq)+int(len(positivevocab))))

			prob = prob + probword
		else :
			prob = prob + math.log2((1)/(int(len(positivevocab))))

	return prob

def calculate_negative(sentence):

	prob = math.log2(cnl /(cpl + cnl))

	for word in sentence:

		if word in negativevocab :

			index = negativevocab.index(word)
			count = negativefreq[index]

			#Calculate Unigram probability of a word using add-one smoothing
			probword = math.log2((count + 1)/(sum(negativefreq)+int(len(negativevocab))))

			prob = prob + probword
		else :
			prob = prob + math.log2((1)/(int(len(negativevocab))))

	return prob

def create_posneg(data):


	stopwords.remove_stopwords(data)
	training_without_stopwords = open("data_without_stopwords.txt", "r")
	positive_superdoc = open("positivedata.txt", "w")
	negative_superdoc = open("negativedata.txt", "w")

	for line in training_without_stopwords:

		words_in_line = line.split()

		FLAG = 0

		for word in words_in_line :
			if word == '+' :
				positive_superdoc.write(word)
				FLAG = 1
				continue
			if word == '-' :
				negative_superdoc.write(word)
				FLAG = 0
				continue
			if FLAG == 1 :
				positive_superdoc.write(" " + word)
			else :
				negative_superdoc.write(" " + word)

		if FLAG == 1 :
			positive_superdoc.write("\n")
		else :
			negative_superdoc.write("\n")

	positive_superdoc.close()
	negative_superdoc.close()

	#print("Positive and Negative files created")


	return




def multinomial_naive_bayes(data,test):



	create_posneg(data)


	positiveinit("positivedata.txt")

	negativeinit("negativedata.txt")

	tp = 0
	tn = 0
	fp = 0
	fn = 0

	stopwords.remove_stopwords2(test)
	test_file = open("test_without_stopwords.txt", "r")

	for line in test_file:

		sentence = line.split()

		#print(sentence)

		if sentence[0] == '+' :
			ACTUAL = 1
			sentence.remove('+')
		else :
			ACTUAL = 0
			sentence.remove('-')




		posprob = calculate_positive(sentence)
		negprob = calculate_negative(sentence)

		if posprob >=negprob :
			REVIEW = 1
			#print("POSITIVE\n")

		else :
			REVIEW = 0
			#print("NEGATIVE\n")

		#print(i)

		if ACTUAL==1 and REVIEW==1:
			tp=tp+1
		elif ACTUAL==1 and REVIEW==0:
			fn=fn+1
		elif ACTUAL==0 and REVIEW==1:
			fp=fp+1
		else:
			tn=tn+1

	print("tp = "+ str(tp) )
	print("fn = "+ str(fn) )
	print("fp = "+ str(fp) )
	print("tn = "+ str(tn) )

	accuracy = (tp+tn)/(tp+tn+fp+fn)

	print("Accuracy : "+ str(accuracy) + "  ")

	#print("Unigram completed!")

	return accuracy
