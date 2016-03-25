


def build_vocabulary(data): 

    reviews_file = open(data, "r")
    megadoc = ""

    
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
       
        freq.append(str(count))    
    print(vocab)
    print(words)
    print(freq)    
    reviews_file.close()
    
    output = open("frequency.txt", "w")

    output.write("Name  :  Frequency \n")

    for i in range(len(freq)):
        output.write( vocab[i] +"  :  "+ freq[i])
        output.write("\n")
    output.close()
    
    output = open("vocabulary.txt", "w")
    

    for i in range(len(freq)):
        if int(freq[i]) > 1:
            output.write(vocab[i])
            output.write("\n")

    output.close()



    return
    

build_vocabulary("data_without_stopwords.txt")  



print("Program Successfully Terminated!")
            
