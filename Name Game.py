#Name Game

print("Welcome to Name Game")
print("Hello, the duty is write your names and then starts the challenge!")
print("Warning: Your names cannot have two or more than one number! Be careful.")
print("Also, if you have two or more names just write your favorite one :)")
print("Now, I am going to close my eyes in 3 seconds. 3..2..1...  You can start...")

player1 = str(input("Haha, it's started! :D Write your name first person: "))

player2 = str(input("... And now it's turn second player. Write your cool name: "))

print("Okay, you all wrote your names and now, the game is exited for progress...")
e = [3,2,1]

print("Please wait just for 3 seconds...")

for i in e:
    if i >=0:
        print(i)
        print()
        i -=1

print("Okay, everything's fine. You have to say that which charachter I will have selected. Okay:D")
print("Fine")

print("I am going to guess name of player1, okay? If so, please write: Yes")
print()
a = str(input())
if a == "Yes" or a=="yes" or a == "YES":
    print(a, "... Perfect!")
else:
    print("This place is my palace and I do not admit to change it. If you want to play game with me. You need to accept my offer. Hahaha")
    print("If you want to play one more time then fresh the page.")
for k in range(0,1):
    if a == "Yes" or a =="yes" or a == "YES":
        print("I guess your name is: ", player1, "!" )
        print("Okay, you have a really nice name like me but I have no idea what it's meaning.")
    else:
        print("Sorry babe, you have to write Yes for me not negative or other thing :S")
        print("Okay, I do not want to play more then this second. You have to write Yes because i believe this is true.")
        break

print("Let's continue with player2...")
print("OMG... I have to work to access your name but my codewriter is not wanting it. This time is more difficult hermana/o.")
print("System error... Please wait...")
print("Omg... Are you from Spain or from America Continents? si o no")
v = str(input())
if v == "si" or v == "SI" or v == "Si":
    print("Wow, I am so clever! Like you my human buddies :D")
    print("Your name is... your name is... Okay, I finally found it. Your name is ", player2, "!")
    print("That's made me happy. Thank you spending your time with me!")
    print("Bye :)")
else:
    print("Omg, I think I have a problem... I am so sorry.")
    print("Let's give me one more chance to success. I just want to some tips to guess your name.")
    print("Please, write your gender: a = male, b = female, and f = I do not want to declare my gender(Please, do not select it. :()")
    k = str(input("My choice is: "))
    print("Okay, thx for your helps. I am going to do this. Just believe me.")
    if k == "a" or k == "A":
        print("Hmmm, your gender is male. Perfect. I have an idea just wait")
        print("I think your name is ", player2, "!")
        print("Is it correct? If so, write OK or NO")
        s = str(input())
        if s == "OK" or s == "ok" or s =="Ok":
            print("That's made me happy. Thank you spending your time with me!")
            print("Bye :)")
        elif s == "NO" or s == "no" or s == "No":
            print("I am so sorry but you wrote wrong name then because there is no chance to do wrong it. I am the super machine!")
        else:
            print("Ohh no, I just wanted to write OK or NO, doesn't want to read a story dude.")
            print("Sorry, you've lost your chance. You've been trying to just failure of mine. And I cannot do this. Game over!")
    elif k == "b" or k == "B":
        print("Hmmm, your gender is female. Perfect. I have an idea just wait")
        print("I think your name is: ", player2, "!")
        print("Is it correct? If so, write OK or NO")
        t = str(input())
        if t == "OK" or t == "Ok" or t == "ok":
            print("That's made me happy. Thank you spending your time with me!")
            print("Bye :)")
        elif t == "NO" or t == "No" or t == "no":
            print("I am so sorry but you wrote wrong name then because there is no chance to do wrong it. I am the super machine!")
        else:
            print("Ohh no, I just wanted to write OK or NO, doesn't want to read a story dude.")
            print("Sorry, you've lost your chance. You've been trying to just failure of mine. And I cannot do this. Game over!")








