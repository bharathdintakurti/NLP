
def unigramvocabulary(data,vocabfile):

    reviews_file = open(data, "r")
    megadoc = ""


    unigrams = {}

    for line in reviews_file:

       megadoc  = megadoc + line

    words = megadoc.split()

    words.sort()

    count=1
    freq=[]
    vocab =[]
    while len(words) > 0:
        temp = words[0]

        vocab.append(str(temp))
        count = words.count(temp)
        for i in range(count):
            words.remove(temp)

        freq.append(count)
    #print(vocab)
    #print(words)
    #print(freq)
    reviews_file.close()

    #output = open("frequency.txt", "w")

    #output.write("Name  :  Frequency \n")

    unigram_count = 0

    for i in range(len(freq)):
        unigrams[vocab[i]] = freq[i]
        #output.write("\n")
    #output.close()

    for unigram in unigrams:

        if unigrams[unigram] >= 2:

            unigram_count += 1
        else:
            unigrams[unigram] = 0

    output = open(vocabfile, "w")


    for i in range(len(freq)):
        if int(freq[i]) > 1:
            output.write(vocab[i])
            output.write("\n")

    output.close()

    print("Unigram Vocabulary created")

    return unigrams


#build_vocabulary("data_without_stopwords.txt")
