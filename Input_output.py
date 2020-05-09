# John Asare
# May 9 2020 14:45


""" Tunning my skills in I\O. A code to open myfile.txt and return the number of letter as a
dictionary"""


def count_word():
    my_file = open('myfile.txt')

    for line in my_file:
        print(line)

count_word()



