def readLog(showKeys):
    with open('keyLog.txt','rt') as f:
        for i in f.readlines():
            if i[0]=="'":
                print(i[1],end="")
            elif i[4:-1]=="space":
                print(" ",end="")
            elif i[4:-1]=="enter":
                print("\n",end="")
            elif i[4:-1]=="backspace":
                print("\b",end="")
            elif showKeys:
                print("[",i[4:-1],"]",end="")
        print()

if __name__ == "__main__":
    validInput=False
    while(not validInput):
        showKeys=input("Do You Want to see Key Presses like Shift, Ctrl etc?? [Y/N] ").upper()
        if not len(showKeys):
            showKeys="Y"
        else:
            showKeys=showKeys[0]
        if showKeys=="Y":
            validInput=True
            readLog(True)
        elif showKeys=="N":
            validInput=True
            readLog(False)
        else:
            print("Please Enter Valid Choice.")