# Q2. Write a Python program that accepts a word from the user and reverse it.

str1=input("Enter the word: ")
for i in range(len(str1)-1,-1,-1):
    print(str1[i],end="")