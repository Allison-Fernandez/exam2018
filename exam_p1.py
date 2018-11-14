lv = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 
'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 
'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

import string
import operator

def name_value(name):
    result = 0
    for letter in name:
        result += lv.get(letter)
    
    return result
    

def get_names():
    cr = open('roster.txt')
    name_list = []

    for line in cr:
        name = line.split(' ', 1)[0]
        name = name.lower()
        # print(name) #testing

        name_list.append(name)

    return name_list


def who_has_highest_value(name_list):
    vn = {}
    values = []
    get_names()
    for name in name_list:
        vn[name] = name_value(name)
    # print(vn)  #for testing/debugging  
    return max(vn.items(), key=operator.itemgetter(1))[0]
    

def get_words():
    pw = open('positive-words.txt')
    positive_words = []

    for line in pw:
        word = line.strip()
        word = word.lower()
        # print(name) #testing

        positive_words.append(word)

    return positive_words


def get_words_with_same_value(words, value):
    # return a list of matched words
    svw = []
    for word in words:
        if name_value(word) == value:
            svw.append(word)        
    return svw


def main():
    print(name_value('abound'))
    name_list = get_names()
    print(who_has_highest_value(name_list))
    words = get_words()
    print(get_words_with_same_value(words, 57))





    # get_names()
    # print(who_has_highest_value(names))
    # pass
#     process_roster()
#     for name in names:
#         name_value(name)


if __name__ == '__main__':
    main()


# print(process_roster()) #testing
# print(name_value('ricardo'))

# print(get_words())

# who_has_highest_value(get_names)