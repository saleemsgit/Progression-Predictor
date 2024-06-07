import random
#create varibles
Count = 0
Name = ""
RandomList = []

Name = input("Player Name: ")

print("_________________________________________________________________________")
print("---------------------------Welcome",Name,"to Gameint--------------------------\n")
print("Number to Guess: XXXX",end="\t\t")
print("Color Mapping: White=1 Blue=2 Red=3","\n\t\t\t\t\t\tYellow=4 Green=5 Purple=6")
print("_________________________________________________________________________")
print("\nGuess Count\t\t    Guess Number\t\t     Guess Result\n")

Int1 = int(random.randint(1,6))
Int2 = int(random.randint(1,6))
Int3 = int(random.randint(1,6))
Int4 = int(random.randint(1,6))
RandomList = [Int1, Int2, Int3, Int4]
#print(RandomList)

while Count == 0:
    Count += 1

    while Count <= 8:

        Number = input("\nEnter Number to Guess: ")

        if Number == "0000":
            exit()

        while len(Number) > 4:
            Number = input("Enter 4 Digit Number to Guess: ")

        while len(Number) < 4:
            Number = input("Enter 4 Digit Number to Guess: ")    

        NumberList = []
        for x in range(0, len(Number)):
            NumberList.insert(x,int(Number[x]))
        if NumberList[0] and NumberList[1] and NumberList[2] and NumberList[3] in range(1,7):
            pass
        else:
            print("Enter Values between 1-6")
            continue

        print(Count,"\t\t\t      ",Number,"\t\t\t      ",end=" ")

        
        if NumberList[0]==RandomList[0] or NumberList[0]==RandomList[1] or NumberList[0]==RandomList[2] or NumberList[0]==RandomList[3]:
            if NumberList[0]==RandomList[0]:
                print("1",end=" ")
            else:
                print("0",end=" ")
        else:
            print("-",end=" ")

        if NumberList[1]==RandomList[0] or NumberList[1]==RandomList[1] or NumberList[1]==RandomList[2] or NumberList[1]==RandomList[3]:
            if NumberList[1]==RandomList[1]:
                print("1",end=" ")
            else:
                print("0",end=" ")
        else:
            print("-",end=" ")

        if NumberList[2]==RandomList[0] or NumberList[2]==RandomList[1] or NumberList[2]==RandomList[2] or NumberList[2]==RandomList[3]:
            if NumberList[2]==RandomList[2]:
                print("1",end=" ")
            else:
                print("0",end=" ")
        else:
            print("-",end=" ")

        if NumberList[3]==RandomList[0] or NumberList[3]==RandomList[1] or NumberList[3]==RandomList[2] or NumberList[3]==RandomList[3]:
            if NumberList[3]==RandomList[3]:
                print("1")
            else:
                print("0")
        else:
            print("-")

        Count = Count + 1

        if NumberList == RandomList:
            print("Congragulations")
            print("Your score : 100%")
            Rerun = input("Do you want to play again (Yes/No): ")
            if Rerun == "Yes":
                Count = Count - (Count-1)
                RandomList = []
                Int1 = int(random.randint(1,6))
                Int2 = int(random.randint(1,6))
                Int3 = int(random.randint(1,6))
                Int4 = int(random.randint(1,6))
                RandomList = [Int1, Int2, Int3, Int4]
                Name = input("Player Name: ")
                print("_________________________________________________________________________")
                print("---------------------------Welcome",Name,"to Gameint--------------------------\n")
                print("Number to Guess: XXXX",end="\t\t")
                print("Color Mapping: White=1 Blue=2 Red=3","\n\t\t\t\t\t\tYellow=4 Green=5 Purple=6")
                print("_________________________________________________________________________")
                print("\nGuess Count\t\t    Guess Number\t\t     Guess Result\n")
                continue
            elif Rerun == "No":
                break

        if Count == 9:
            print("Sorry :( You Lost")
            Rerun = input("Do you want to play again (Yes/No): ")
            if Rerun == "Yes":
                Count = Count - (Count-1)
                RandomList = []
                Int1 = int(random.randint(1,6))
                Int2 = int(random.randint(1,6))
                Int3 = int(random.randint(1,6))
                Int4 = int(random.randint(1,6))
                RandomList = [Int1, Int2, Int3, Int4]
                Name = input("Player Name: ")
                print("_________________________________________________________________________")
                print("---------------------------Welcome",Name,"to Gameint--------------------------\n")
                print("Number to Guess: XXXX",end="\t\t")
                print("Color Mapping: White=1 Blue=2 Red=3","\n\t\t\t\t\t\tYellow=4 Green=5 Purple=6")
                print("_________________________________________________________________________")
                print("\nGuess Count\t\t    Guess Number\t\t     Guess Result\n")
                continue
            elif Rerun == "No":
                break
            

            
