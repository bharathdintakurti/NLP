def bigramvocabulary(data,vocabfile):


    vocab_file = open(vocabfile,'a');
    data_file = open(data,"r")

    datacontent = data_file.read()


    bigrams = {}

    words = datacontent.split()

    bigram_count = 0
    for index in range(len(words)-1):
        #if index < len(words) - 1:

            w1 = words[index]
            w2 = words[index + 1]

            bigram = (w1, w2)

            if bigram in bigrams:
                bigrams[ bigram ] = bigrams[ bigram ] + 1
            else:
                bigrams[ bigram ] = 1


    bigrams[ ('+','START') ]=0
    bigrams[ ('-','START') ]=0
    bigrams[ ('STOP','-') ]=0
    bigrams[ ('STOP','+') ]=0
    #sorted_bigrams = sorted(bigrams.items(), key = lambda pair:pair[1], reverse = False)



    for bigram in bigrams:
        (word1, word2) = bigram
        if bigrams[bigram] >= 2:
            vocab_file.write(word1 + ' ' + word2 + '\n');
            bigram_count += 1
        else:
            bigrams[bigram] = 0




    vocab_file.close();
    data_file.close();

    print("Bigram Vocabulary created")

    return bigrams
