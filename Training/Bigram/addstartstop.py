def add_start_stop(input_file):

    data_file = open(input_file, "r")
    output = open("data_with_startstop.txt","w")

    for line in data_file:

        words_in_line = line.split();
        START_OF_REVIEW = 1;

        for word in words_in_line:
            if (word == '+' or word == '-') and START_OF_REVIEW == 1:
                output.write(word + " START")
                START_OF_REVIEW = 0
                continue

            output.write(" " + word.lower())

        output.write(" STOP\n")

    data_file.close()
    output.close()

    #print("START and STOP added to data")

    return

def add_start_stop2(input_file):

    data_file = open(input_file, "r")
    output = open("test_with_startstop.txt","w")

    for line in data_file:

        words_in_line = line.split();
        START_OF_REVIEW = 1;

        for word in words_in_line:
            if (word == '+' or word == '-') and START_OF_REVIEW == 1:
                output.write(word + " START")
                START_OF_REVIEW = 0
                continue

            output.write(" " + word.lower())

        output.write(" STOP\n")

    data_file.close()
    output.close()

    #print("START and STOP added to test")

    return
