
#simulate  a connect 4 game
#there are 5 columns which is similar to the tic tac toe  , but here there should be a pattern of 4 at a time
#here the user plays with the computer
#the number of columns is 6
#here there are two colored coins , red and yellow
#here we put coins in a row and column
import random
def put_coin(n,universal_row,user_color,computer_color):  #write computer_color if you want the computer is making the first chance
    for i in range(len(universal_row)):
        l=universal_row[i]
        if l[n-1]=="-":
            l[n-1]=user_color
            break
    return universal_row
def termination_status(universal_row,user_color,computer_color): #the termination can be when 4 in a row,4 in a column,4 in a diagonal
    for i in range(5): #termination by one column
        if row_1[i]==row_2[i]==row_3[i]==row_4[i] and row_1[i]==user_color:
            print("GAME FINISHED , YOU WON !!!")
            return 1
        if row_2[i]==row_3[i]==row_4[i]==row_5[i] and row_3[i]==user_color:
            print("GAME FINISHED , YOU WON !!!")
            return 1
        if row_3[i]==row_4[i]==row_5[i]==row_6[i] and row_3[i]==user_color:
            print("GAME FINISHED , YOU WON !!!")
            return 1
        if row_1[i]==row_2[i]==row_3[i]==row_4[i] and row_1[i]==computer_color:
            print("GAME FINISHED , YOU LOST !!!")
            return 1
        if row_2[i]==row_3[i]==row_4[i]==row_5[i] and row_3[i]==computer_color:
            print("GAME FINISHED , YOU LOST !!!")
            return 1
        if row_3[i]==row_4[i]==row_5[i]==row_6[i] and row_3[i]==computer_color:
            print("GAME FINISHED , YOU LOST !!!")
            return 1
    #termination by same row
    for j in range(2):
        if row_1[j]==row_1[j+1]==row_1[j+2]==row_1[j+3] and row_1[j]==user_color:
            print("GAME FINISHED , YOU WON !!!")
            return 1
        if row_1[j]==row_1[j+1]==row_1[j+2]==row_1[j+3] and row_1[j]==computer_color:
            print("GAME FINISHED , YOU LOST !!!")
            return 1
        if row_2[j]==row_2[j+1]==row_2[j+2]==row_2[j+3] and row_2[j]==user_color:
            print("GAME FINISHED , YOU WON !!!")
            return 1
        if row_2[j]==row_2[j+1]==row_2[j+2]==row_2[j+3] and row_2[j]==computer_color:
            print("GAME FINISHED , YOU LOST !!!")
            return 1
        if row_3[j]==row_3[j+1]==row_3[j+2]==row_3[j+3] and row_3[j]==user_color:
            print("GAME FINISHED , YOU WON !!!")
            return 1
        if row_3[j]==row_3[j+1]==row_3[j+2]==row_3[j+3] and row_3[j]==computer_color:
            print("GAME FINISHED , YOU LOST !!!")
            return 1
        if row_4[j]==row_4[j+1]==row_4[j+2]==row_4[j+3] and row_4[j]==user_color:
            print("GAME FINISHED , YOU WON !!!")
            return 1
        if row_4[j]==row_4[j+1]==row_4[j+2]==row_4[j+3] and row_4[j]==computer_color:
            print("GAME FINISHED , YOU LOST !!!")
            return 1
        if row_5[j]==row_5[j+1]==row_5[j+2]==row_5[j+3] and row_5[j]==user_color:
            print("GAME FINISHED , YOU WON !!!")
            return 1
        if row_5[j]==row_5[j+1]==row_5[j+2]==row_5[j+3] and row_5[j]==computer_color:
            print("GAME FINISHED , YOU LOST !!!")
            return 1
        if row_6[j]==row_6[j+1]==row_6[j+2]==row_6[j+3] and row_6[j]==user_color:
            print("GAME FINISHED , YOU WON !!!")
            return 1
        if row_6[j]==row_6[j+1]==row_6[j+2]==row_6[j+3] and row_6[j]==computer_color:
            print("GAME FINISHED , YOU LOST !!!")
            return 1
    #termination by being in a diagonal
    if row_1[0]==row_2[1]==row_3[2]==row_4[3] and row_1[0]==user_color:
        print("GAME FINISHED  , YOU WON !!!")
        return 1
    if row_2[0]==row_3[1]==row_4[2]==row_5[3] and row_2[0]==user_color:
        print("GAME FINISHED  , YOU WON !!!")
        return 1
    if row_3[0]==row_4[1]==row_5[2]==row_6[3] and row_3[0]==user_color:
        print("GAME FINISHED  , YOU WON !!!")
        return 1
    if row_1[1]==row_2[2]==row_3[3]==row_4[4] and row_1[1]==user_color:
        print("GAME FINISHED  , YOU WON !!!")
        return 1
    if row_2[1]==row_3[2]==row_4[3]==row_5[4] and row_2[1]==user_color:
        print("GAME FINISHED  , YOU WON !!!")
        return 1
    if row_3[1]==row_4[2]==row_5[3]==row_6[4] and row_3[1]==user_color:
        print("GAME FINISHED  , YOU WON !!!")
        return 1
    if row_1[4]==row_2[3]==row_3[2]==row_4[1] and row_1[4]==user_color:
        print("GAME FINISHED  , YOU WON !!!")
        return 1
    if row_2[4]==row_3[3]==row_3[2]==row_4[1] and row_2[4]==user_color:
        print("GAME FINISHED  , YOU WON !!!")
        return 1
    if row_3[4]==row_4[3]==row_5[2]==row_6[1] and row_3[4]==user_color:
        print("GAME FINISHED  , YOU WON !!!")
        return 1
    if row_1[3]==row_2[2]==row_3[1]==row_4[0] and row_1[3]==user_color:
        print("GAME FINISHED  , YOU WON !!!")
        return 1
    if row_2[3]==row_3[2]==row_4[1]==row_5[0] and row_2[3]==user_color:
        print("GAME FINISHED  , YOU WON !!!")
        return 1
    if row_3[3]==row_4[2]==row_5[1]==row_6[0] and row_3[3]==user_color:
        print("GAME FINISHED  , YOU WON !!!")
        return 1
    if row_1[0]==row_2[1]==row_3[2]==row_4[3] and row_1[0]==computer_color:
        print("GAME FINISHED  , YOU LOST !!!")
        return 1
    if row_2[0]==row_3[1]==row_4[2]==row_5[3] and row_2[0]==computer_color:
        print("GAME FINISHED  , YOU LOST !!!")
        return 1
    if row_3[0]==row_4[1]==row_5[2]==row_6[3] and row_3[0]==computer_color:
        print("GAME FINISHED  , YOU LOST !!!")
        return 1
    if row_1[1]==row_2[2]==row_3[3]==row_4[4] and row_1[1]==computer_color:
        print("GAME FINISHED  , YOU LOST !!!")
        return 1
    if row_2[1]==row_3[2]==row_4[3]==row_5[4] and row_2[1]==computer_color:
        print("GAME FINISHED  , YOU LOST !!!")
        return 1
    if row_3[1]==row_4[2]==row_5[3]==row_6[4] and row_3[1]==computer_color:
        print("GAME FINISHED  , YOU LOST !!!")
        return 1
    if row_1[4]==row_2[3]==row_3[2]==row_4[1] and row_1[4]==computer_color:
        print("GAME FINISHED  , YOU LOST !!!")
        return 1
    if row_2[4]==row_3[3]==row_3[2]==row_4[1] and row_2[4]==computer_color:
        print("GAME FINISHED  , YOU LOST !!!")
        return 1
    if row_3[4]==row_4[3]==row_5[2]==row_6[1] and row_3[4]==computer_color:
        print("GAME FINISHED  , YOU  LOST!!!")
        return 1
    if row_1[3]==row_2[2]==row_3[1]==row_4[0] and row_1[3]==computer_color:
        print("GAME FINISHED  , YOU LOST !!!")
        return 1
    if row_2[3]==row_3[2]==row_4[1]==row_5[0] and row_2[3]==computer_color:
        print("GAME FINISHED  , YOU LOST !!!")
        return 1
    if row_3[3]==row_4[2]==row_5[1]==row_6[0] and row_3[3]==computer_color:
        print("GAME FINISHED  , YOU LOST !!!")
        return 1  
    else:
        return 0 
def non_empty(universal_row):
    l=universal_row[len(universal_row)-1]
    if "-" not in l:
        return 1  # the row is filled entirely
    else:
        return 0
#*********************
def space_in_board(universal_row,n):
    related_space=[]
    for i in range(1,5):
        if i!=n-1:
            related_space.append(i)
    for j in range(len(universal_row)):
        l1=universal_row[j]
        for i in range(len(related_space)):
            m=related_space[i]
            if "-" in l1[m]:
                break
                return 1
    else:
        return 0


#the computer can either priortize its winning or to tie
def tie(universal_row,user_color):
    flag=0
    for i in range(5): #termination by one column.    
        if row_1[i]==row_2[i]==row_3[i] and row_1[i]==user_color:
            flag=1
            return i+1
        if row_2[i]==row_3[i]==row_4[i] and row_3[i]==user_color:
            flag=1
            return i+1
           
        if row_3[i]==row_4[i]==row_5[i] and row_3[i]==user_color:
            flag=1
            return i+1
    for i in range(6):
        l=universal_row[i]      #scan for a row
        for j in range(3):
            if l[j]==l[j+1]==l[j+2] and l[j]==user_color and i==0:
                if j==0 and l[j+3]=="-" :
                    flag=1
                    return j+4
                  
                if j==2 and l[j-1]=="-":
                    flag=1
                    return j
                    
            if l[j]==l[j+1]==l[j+2] and l[j]==user_color and i!=0:
                m=universal_row[i-1]
                if j==0 and m[j+3]!="-":
                    flag=1
                    return j+4
                 
                if j==0 and m[j+3]=="-" and space_in_board(universal_row,j+4)==0:
                    flag=1
                    return j+4
                    
                if j==2 and m[j-1]!="-":
                    flag=1
                    return j
                   
                if j==2 and m[j-1]=="-" and space_in_board(universal_row,j)==0: #check if space is
                    flag=1                                                      #available
                    return j
    if flag==0:
        return 0
                          
def winning(universal_row,computer_color):    #computer prioritizes winning              
    flag=0 
    for i in range(5): #termination by one column
        if row_1[i]==row_2[i]==row_3[i] and row_1[i]==computer_color:
            flag=1
            return i+1
        if row_2[i]==row_3[i]==row_4[i] and row_3[i]==computer_color:
            flag=1
            return i+1
        if row_3[i]==row_4[i]==row_5[i] and row_3[i]==computer_color:
            flag=1
            return i+1
    for i in range(6):
        l=universal_row[i]   #check for the columns
        for j in range(3):
            if l[j]==l[j+1]==l[j+2] and l[j]==computer_color and i==0:
                if j==0 and l[j+3]=="-" :
                    flag=1
                    return j+4
                if j==2 and l[j-1]=="-":
                    flag=1
                    return j
            if l[j]==l[j+1]==l[j+2] and l[j]==computer_color and i!=0:
                m=universal_row[i-1]
                if j==0 and m[j+3]!="-":
                    flag=1
                    return j+4
                if j==0 and m[j+3]=="-" and space_in_board(universal_row,j+4)==0:  #if space is not available
                    flag=1
                    return j+4
                if j==2 and m[j-1]!="-":
                    flag=1
                    return j
                if j==2 and m[j-1]=="-" and space_in_board(universal_row,j)==0: #check whether space is available
                    flag=1
                    return j
    if flag==0:
        return 0
def opponent_status(universal_row,user_color):
    flag=0
    for i in range(5): #termination by one column.    
        if row_1[i]==row_2[i]==row_3[i] and row_1[i]==user_color:
            flag=1
            return 1
        if row_2[i]==row_3[i]==row_4[i] and row_3[i]==user_color:
            flag=1
            return 1
           
        if row_3[i]==row_4[i]==row_5[i] and row_3[i]==user_color:
            flag=1
            return 1
    for i in range(6):
        l=universal_row[i]      #scan for a row
        for j in range(3):
            if l[j]==l[j+1]==l[j+2] and l[j]==user_color and i==0:
                if j==0 and l[j+3]=="-" :
                    flag=1
                    return 1
                  
                if j==2 and l[j-1]=="-":
                    flag=1
                    return 1
                    
            if l[j]==l[j+1]==l[j+2] and l[j]==user_color and i!=0:
                m=universal_row[i-1]
                if j==0 and m[j+3]!="-":
                    flag=1
                    return 1
                 
                if j==0 and m[j+3]=="-" and space_in_board(universal_row,j+4)==0:
                    flag=1
                    return 1
                    
                if j==2 and m[j-1]!="-":
                    flag=1
                    return 1
                   
                if j==2 and m[j-1]=="-" and space_in_board(universal_row,j)==0: #check if space is
                    flag=1                                                      #available
                    return 1
    if flag==0:
        return 0
def computer_rules(user_color,n,row_6): #it needs to scan the position of its opponent  
    if n>6:
        if opponent_status(universal_row,user_color)==0:                                            #rules defned accordingly the agent performs
            n2=winning(universal_row,computer_color)
            if n2==0:
                n2=random.randint(1,5)
            return n2
        else:
         
            n3=tie(universal_row,user_color)
            if n3==0:
                n3=random.randint(1,5)
            return n3
    if n<=6:
        n1=random.randint(1,5)
        return n1



    #in row wise the elevation also matters
#***************************

row_6=["-","-","-","-","-"]
row_5=["-","-","-","-","-"]    #THE LOWER MOST IS row_1
row_4=["-","-","-","-","-"]
row_3=["-","-","-","-","-"]
row_2=["-","-","-","-","-"]
row_1=["-","-","-","-","-"]
universal_row=[row_1,row_2,row_3,row_4,row_5,row_6]
def first_chance():
    y=input("PRESS Y IF YOU WANT TO START FIRST ELSE PRESS N ")
    if y.lower()=="y":
        return 1
    else:
        return 0

user_color=input("WHICH COLOR DO YOU WANT TO CHOOSE AMONG RED OR YELLOW :::::     ")
M=first_chance()
if  M==1:
    print("MAKE YOUR FIRST MOVE ")
else:
    print("COMPUTER  WILL MOVE FIRST")
computer_color=0
if user_color.lower()=="red":
    computer_color="yellow"
else:
    computer_color="red"
i=1
#starting move can be done by either computer or the person
if M==1 : #THE USER STARTS FIRST
    while termination_status(universal_row,user_color,computer_color)==0 :
        if i%2==1:
            n1=int(input("ENTER THE COLUMN WHERE YOU WANT TO PUT YOUR COIN  ::: "))
            if n1<=5:
                put_coin(n1,universal_row,user_color,computer_color)
            else:
                print("THE COLUMN NUMBER IS INVALID")
        if i%2==0:
            n100=computer_rules(user_color,i,row_6)
            print(n100)            
            put_coin(n100,universal_row,computer_color,user_color)

        print("*****************************************************************")
        print(row_6)
        print(row_5)
        print(row_4)
        print(row_3)
        print(row_2)
        print(row_1)
        print("******************************************************************")
        print(i)
        i=i+1

if M==0 : # THE COMPUTER STARTS FIRST
    while termination_status(universal_row,user_color,computer_color)==0:
        if i%2==1:
            n7=computer_rules(user_color,i,row_6)
            put_coin(n7,universal_row,computer_color,user_color)
        if i%2==0:
            n2=int(input("ENTER THE COLUMN WHERE YOU WANT TO PUT THE COIN :::  "))
            if n2<=5:
                put_coin(n2,universal_row,user_color,computer_color)
            else:
                print("THE COLUMN NUMBER IS INVALID")
        print("***************************************************************")
        print(row_6)
        print(row_5)
        print(row_4)
        print(row_3)
        print(row_2)
        print(row_1)
        print("***************************************************************")
        i=i+1


            
    


            
    

            
    


            
    
