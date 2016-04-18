import stopwords
import addstartstop
import unigramvocabulary
import bigramvocabulary
import createposneg
import math


def datainit(data):

    stopwords.remove_stopwords(data)
    global unigrams
    unigrams = unigramvocabulary.unigramvocabulary("data_without_stopwords.txt","vocabulary.txt")
    #print(unigrams)
    addstartstop.add_start_stop("data_without_stopwords.txt")
    global bigrams
    bigrams = bigramvocabulary.bigramvocabulary("data_with_startstop.txt","vocabulary.txt")
    #print(bigrams)
    createposneg.create_posneg("data_with_startstop.txt")

    bigram_file = open("vocabulary.txt", "r")

    global vocab_count
    vocab_count = 0
    for line in bigram_file :
        vocab_count += 1
    #print(vocab_count)

    return

def posinit(data):

    global posunigrams
    posunigrams = unigramvocabulary.unigramvocabulary(data,"positivevocabulary.txt")
    global posbigrams
    posbigrams = bigramvocabulary.bigramvocabulary(data,"positivevocabulary.txt")


    #print(posunigrams)

    for bigram in posbigrams:
        if (posbigrams[bigram] >= 3):
            (word1, word2) = bigram
            if word1 in posunigrams:
                posunigrams[word1] = int(posunigrams[word1]) - int(posbigrams[bigram])
            if word2 in posunigrams:
                posunigrams[word2] = int(posunigrams[word2]) - int(posbigrams[bigram])

    #print(posunigrams)


    return


def neginit(data):

    global negunigrams
    negunigrams = unigramvocabulary.unigramvocabulary(data,"negativevocabulary.txt")
    global negbigrams
    negbigrams = bigramvocabulary.bigramvocabulary(data,"negativevocabulary.txt")

    #print(negunigrams)

    for bigram in negbigrams:
         if (negbigrams[bigram] >= 3):
            (word1, word2) = bigram
            if word1 in negunigrams :
                negunigrams[word1] = int(negunigrams[word1]) - int(negbigrams[bigram])
            if word2 in negunigrams:
                negunigrams[word2] = int(negunigrams[word2]) - int(negbigrams[bigram])

    #print(negunigrams)




    return

def bigrammodel(data,test):

    datainit(data)
    accuracy = 0

    posinit("positivedata.txt")
    neginit("negativedata.txt")

    stopwords.remove_stopwords2(test)
    addstartstop.add_start_stop2("test_without_stopwords.txt")

    tp = 0
    tn = 0
    fp = 0
    fn = 0


    test_file = open("test_with_startstop.txt", "r")

    for line in test_file:

        sentence = line.split()

		#print(sentence)

        if sentence[0] == '+' :
            ACTUAL = 1
            sentence.remove('+')
        else :
            ACTUAL = 0
            sentence.remove('-')




        posprob = calculate_positive2(sentence)
        negprob = calculate_negative2(sentence)

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

    #print("tp = "+ str(tp) )
    #print("fn = "+ str(fn) )
    #print("fp = "+ str(fp) )
    #print("tn = "+ str(tn) )

    accuracy = (tp+tn)/(tp+tn+fp+fn)

    print("Accuracy : "+ str(accuracy) + "   ")

    #print("Task Accomplished")

    return accuracy



def calculate_positive2(words_in_review):

    prob_pos = math.log2(float(posunigrams["+"])/(float(posunigrams["+"]) + float(negunigrams["-"])))

    probability = prob_pos
    total_pos_vocab=0

    for key in posunigrams:
        total_pos_vocab = total_pos_vocab + float(posunigrams[key])

    for key in posbigrams:
        total_pos_vocab = total_pos_vocab + float(posbigrams[key])

    total_pos_vocab = total_pos_vocab - float(posunigrams["+"])


    for i  in range(len(words_in_review) - 1):


        word1 = words_in_review[i]
        word2 = words_in_review[i+1]

        bigram = (word1, word2)

        if bigram in posbigrams:

            countb = float(posbigrams[bigram])

        else:

            countb = 0



        probability = probability + math.log2((countb + 1)/(total_pos_vocab + vocab_count) )


    return probability

def calculate_negative2(words_in_review):

    prob_neg = math.log2(float(negunigrams["-"])/(float(posunigrams["+"]) + float(negunigrams["-"])))

    probability = prob_neg
    total_neg_vocab=0

    for key in negunigrams:
        total_neg_vocab = total_neg_vocab + float(negunigrams[key])

    for key in negbigrams:
        total_neg_vocab = total_neg_vocab + float(negbigrams[key])

    total_neg_vocab = total_neg_vocab - float(negunigrams["-"])


    for i  in range(len(words_in_review) - 1):


        word1 = words_in_review[i]
        word2 = words_in_review[i+1]

        bigram = (word1, word2)

        if bigram in negbigrams:

            countb = float(negbigrams[bigram])

        else:
            countb = 0


        probability = probability + math.log2((countb + 1)/(total_neg_vocab + vocab_count) )


    return probability






#bigrammodel("data.txt","data.txt")
