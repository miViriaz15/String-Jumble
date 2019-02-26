"""
stringjumble.py
Author: miviriaz15
Credit: https://dbader.org/blog/python-reverse-list 
https://www.tutorialspoint.com/python/string_split.htm 

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
words=str(input("Please enter a string of text (the bigger the better): "))
print("You entered " + '"' + words + '"' + ". Now jumble it:")

newwords=list(words)
newwords.reverse()

new="".join(newwords)
print(new)

second=words.split(" ")

second.reverse()
newer=" ".join(second)
print(newer)

newest=new.split(" ")
newest.reverse()
newestest=" ".join(newest)
print(newestest)



