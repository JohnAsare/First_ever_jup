# John Asare
# May 9 2020 14:45


""" Tunning my skills in I\O. A code to open myfile.txt and return the number of letter as a
dictionary"""


# count_word will count the words in the file
def count_word():
    my_file = open('myfile.txt')
    aj_dict = {}

    for line in my_file:
        remove_space = line.strip()
        print(remove_space)



count_word()



