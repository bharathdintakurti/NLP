
def create_posneg(data):
    
    training_without_stopwords = open(data, "r")
    positive_superdoc = open("positivedata.txt", "w")
    negative_superdoc = open("negativedata.txt", "w")

    for line in training_without_stopwords:

        words_in_line = line.split()
        FLAG = 0

        for word in words_in_line :
            if word == '+':
                positive_superdoc.write(word)
                FLAG = 1
                continue
            if word == '-':
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

    print("Positive and Negative files created")

    return
