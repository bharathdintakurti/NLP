from unigram import multinomial_naive_bayes
import stopwords
import math
import os

def tenfold(data):


	accuracy = []
	train = open(data, "r")
	training = []
	for line in train :
		training.append(line)


	num_folds = 10
	subset_size = int(len(training)/(num_folds*2))
	for i in range(10):

		testing_this_round = training[i*subset_size:(i+1)*subset_size] + training[250+i*subset_size:250+(i+1)*subset_size]
		training_this_round = training[:i*subset_size] + training[(i+1)*subset_size:250+i*subset_size] + training[250+(i+1)*subset_size:]

		print("\n\n\n\n")
		print("Iteration : " + str(i+1) + "   ")
		#print("Reviews in Test File " + str(len(testing_this_round)))
		#print("Reviews in Data File " + str(len(training_this_round)))

		#print(testing_this_round)

		testingwrite = open("testthisround.txt", "w")
		trainingwrite = open("datathisround.txt", "w")

		for j in range(len(testing_this_round)):

			tests = testing_this_round[j].split()

			for word in tests :
				if word == '+' :
					testingwrite.write(word)
					FLAG = 1
					continue
				if word == '-' :
					testingwrite.write(word)
					FLAG = 0
					continue
				if FLAG == 1 :
					testingwrite.write(" " + word)
				else :
					testingwrite.write(" " + word)


			testingwrite.write("\n")

		for k in range(len(training_this_round)):

			train = training_this_round[k].split()

			for word in train :
				if word == '+' :
					trainingwrite.write(word)
					FLAG = 1
					continue
				if word == '-' :
					trainingwrite.write(word)
					FLAG = 0
					continue
				if FLAG == 1 :
					trainingwrite.write(" " + word)
				else :
					trainingwrite.write(" " + word)

			trainingwrite.write("\n")



		testingwrite.close()
		trainingwrite.close()


		accuracy.append(multinomial_naive_bayes("datathisround.txt","testthisround.txt"))

		AverageAccuracy = sum(accuracy)/10

	print ("Average Accuracy = " + str(AverageAccuracy) + "   ")

	return


if os.path.exists("datathisround.txt"):

	os.remove("datathisround.txt")

	os.remove("testthisround.txt")

	os.remove("positivedata.txt")

	os.remove("negativedata.txt")

	os.remove("data_without_stopwords.txt")

	os.remove("test_without_stopwords.txt")


tenfold("data.txt")
