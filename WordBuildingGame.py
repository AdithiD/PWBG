import random
f1 = open("dictionary.txt","r")
words = [x.replace("\n","") for x in f1.readlines()]
temp = []
computerChoice = ""
print(words[0].startswith())
while True:
    userChoice = input("You : ")
    lastchar = userChoice[-1]
    for i in range(0,len(words),1):
        computerChoice = words[i].startswith(lastchar)

        print(computerChoice)
        break


    """computerChoice = words[random.randrange(0,len(words))]
    print("Computer :",computerChoice)
    userChoice = input("You : ")
    lastchar = userChoice[-1]
    temp.append(words[i].startswith(lastchar))
    print(lastchar)"""
    """if userChoice.startswith(lastchar) and (userChoice in words):
        ...
    else:
        print("GAME OVER!")
        break"""