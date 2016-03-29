from unigram import multinomial_naive_bayes

def tenfold(data):
	

	
	train = open(data, "r")
	training = []	
	for line in train :
		training.append(line)
	
	
	num_folds = 10
	subset_size = int(len(training)/num_folds)
	for i in [0,2,4,6]:
		testing_this_round = training[i*subset_size:(i+1)*subset_size]
		training_this_round = training[:i*subset_size] + training[(i+1)*subset_size:]

		#print(len(testing_this_round))
		#print(len(training_this_round))
	
		
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
			
		

			#testingwrite.close()
			#trainingwrite.close()
		print(i)
		multinomial_naive_bayes("datathisround.txt","testthisround.txt")

		


tenfold("dtaanand.txt")
