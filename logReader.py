def readLog(showKeys):
    '''
    Params:
        showKeys: boolean variable to know if to show keys like shift esc enter etc as typed or implemented
        Example: if true: ab[space][shift]Cd[enter]ef[backspace]
                 if false: abC def
    '''
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
            if showKeys:
                # print shift as [shift],etc
                print("["+i[4:-1]+"]",end="")
        print()

if __name__ == "__main__":
    validInput=False
    while(not validInput):

        # asking if we want the keys to be shown like shift ctrl etc...
        showKeys=input("Do You Want to see Key Presses like Shift, Ctrl etc?? [Y/N] ").upper()
        
        # handling wrong inputs by user
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