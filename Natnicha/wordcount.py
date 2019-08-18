import operator


def main():
    # read
    f = open("simplewiki.txt", "r")
    text = f.read()
    f.close()

    # split
    text = text.lower()
    list_text = text.split()

    # clean text
    required = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    list_text_clean = []
    for text in list_text:
        firstc = text[0]
        last = len(text)-1
        lastc = text[last]
        if last > 0:
            if text[last] not in required:
                #print (lastc)
                text = text.replace(lastc, '')
        if text != '':
            if text[0] not in required:
                #print (firstc)
                text = text.replace(firstc, '')
        list_text_clean.append(text)
    #print (list_text_clean)

    # count frequency
    list_word = {}
    for word in list_text_clean:
        if word not in list_word:
            list_word[word] = 0
        list_word[word] += 1

    # sort
    list_word_sorted = sorted(
        list_word.items(), key=operator.itemgetter(1), reverse=True)
    #print (list_word_sorted)

    # frequency of frequency
    list_num = []
    for i in range(0, len(list_word_sorted)):
        list_num.append(list_word_sorted[i][1])

    list_num_count = {}
    for i in list_num:
        if i not in list_num_count:
            list_num_count[i] = 0
        list_num_count[i] += 1

    # sort
    list_num_sorted = sorted(
        list_num_count.items(), key=operator.itemgetter(1), reverse=True)
    #print (" ")
    #print (list_num_sorted)

    f = open("frequencyOfword.txt", "a")
    for word in list_word_sorted:
        f.write("%s " % word[0])
        f.write("%d \n" % word[1])
    f = open("frequencyOffrequency.txt", "a")
    for word in list_num_sorted:
        f.write("%s " % word[0])
        f.write("%d \n" % word[1])
    f.close()


if __name__ == "__main__":
    main()
