# John Asare
# May 9 2020 14:45


""" Tunning my skills in I\O. A code to open myfile.txt and return the number of letter as a
dictionary"""


# count_word will count the words in the file
def count_word():
    my_file = open('myfile.txt')
    aj_dict = {}

    for statement in my_file:
        remove_spaces = statement.strip().lower()
        for letter in remove_spaces:
            if letter not in aj_dict:
                aj_dict[letter] = 1
    print(aj_dict)

count_word()



