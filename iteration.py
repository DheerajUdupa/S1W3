import math
import re
import string
def ex1a():
    list = []
    flag = False
    while not flag:
        userInput = input("Enter a negative number here: ")
        if int(userInput) < 0:
            flag = True
        else:
            list.append(int(userInput))
    return list

# print(ex1())

def ex1b():
    list = ex1a()
    return (sum(list)/len(list))

# ex1b()

def ex1c():
    list = ex1a()
    list2 = []
    for number in list:
        if number % 2 == 0:
            list2.append(number)

    return len(list2)

# ex1c()

def ex2a():
    userInput = input("Input a positive integer here: ")
    list = []
    for number in range(int(userInput)):
        if number % 2 == 0:
            list.append(int(number))

    return sum(list)

# ex2a()

def ex2b():
    userInput = input("Input a positive integer here: ")
    list1 = []
    list2 = []
    for i in range (1,13):
        print(i, i*int(userInput))

# ex2b()

def factorial(n: int):
    if n == 2:
        return n
    return n * factorial(int(n)-1)

def ex2c():
    userInput = input("Enter a positive integer here: ")
    print(factorial(int(userInput)))

# ex2c()

def palindrome(userInput):
    inputLength = len(userInput)
    flag = True
    for i in range(math.floor(inputLength/2)):
        if not (userInput[i] == userInput[inputLength - (i+1)]):
            flag = False

    return flag

# palindrome()

def palindromeAdvanced():
    userInput = input("Enter a palindromic word here: ").lower()

    regexp = re.compile("[^0-9a-zA-Z]+")
    userInput = re.sub(regexp, "", userInput)
    return palindrome(userInput)

# palindromeAdvanced()

def ex4a():
    userInput = input("Enter a sentence: ")
    list = userInput.split()
    return "".join(list)


# ex4a()

def ex4b():
    userInput = input("Enter a sentence: "). lower()
    list = userInput.split()
    for word in list[:]:
        list.remove(word)
        list.append(word.capitalize())
    return "".join(list)

# ex4b()

def ex4c():
    string = ex4b()
    list = re.findall("[A-Z][a-z]*", string)
    return list

# ex4c()

def ex5a():
    shift = input("Enter the number of characters to shift by: ")
    userInput = input("Enter the string to encrypt: ").lower()
    for character in userInput:
        oldIndex = string.ascii_lowercase.find(character)
        newIndex = (int(oldIndex) + int(shift)) % 26
        print(newIndex)


ex5a()