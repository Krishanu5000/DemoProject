from itertools import chain
b = """The Project Gutenberg eBook of The Complete Works of William Shakespeare

This ebook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this ebook or online
at www.gutenberg.org. If you are not located in the United States,
you will have to check the laws of the country where you are located
before using this eBook.

Title: The Complete Works of William Shakespeare

Author: William Shakespeare

Release date: January 1, 1994 [eBook #100]
Most recently updated: October 29, 2024

Language: English



          *** START OF THE PROJECT GUTENBERG EBOOK THE COMPLETE WORKS OF WILLIAM SHAKESPEARE ***
                                                                                 The Complete Works of William Shakespeare

by William Shakespeare"""

def wordCount(b):
    # print(b.split(" "))
    # l = b.split("\n")
    #print(b.splitlines())
    l = b.splitlines()
    l2 = []
    for i in l:
            l2.append(i.split(" "))
    print(l2)
    l3 = list(chain(*l2))
    print(l3)
    d = {}
    for i in l3 :
        if i.strip() != '':
            d[i.strip()] = 0

    for i in l3:
        if i.strip() != '':
            d[i.strip()] += 1

    print(d)

    max = 1
    for i in d:
        if d[i]> max:
            max = d[i]

    for i in d.keys():
        if d[i] == max:
            print("max freq word - ", i , " ", max)




wordCount(b)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)