import sys

"""
DISCLAIMER

This program has been developed and tested by Aeshan Jiniwal and has entirely been written from scratch meaning that nothing from this workplace is subjected to copyright 
inculding the algorithm developed which is entirely unique. 

"""




#Converting the server's data into a 2d list
mainBoard=str(sys.argv[1])

Board=[]
Row1=[]
Row2=[]
Row3=[]

count=0
for index in range(len(mainBoard)):
    element=mainBoard[index]
    Integer=""
    if element=="0" or element=="1" or element=="2":

        if element=="0":
            Integer=0
        elif element=="1":
            Integer=1
        elif element=="2":
            Integer=2
        
        count+=1

        if count<=3:
            Row1.append(Integer)
        elif count<=6 and count>3:
            Row2.append(Integer)
        elif count<=9 and count>6:
            Row3.append(Integer)

Board.append(Row1)
Board.append(Row2)
Board.append(Row3)










#Creating the rows and column0
#0 represents no value in the matrix
#1 represents the player value in the matrix
#2 represent the computer value in the matrix
PlayerHasWon=0



"""
Computer Algorithm:

Case 1: When the user occupies a corner or edge square
- The computer should always try to occupy the centre square 
- After doing so the computer will always try to look for an empty centre row or column containing only squares occupies bu the computer

Case 2: When the computer occupies the centre square
- The computer should always try to occupy a corner square as doing so will prevent the user from winning 

Case 3: When the user forms a corner pattern as shown below - ('O' represents the computer and 'X' represents the user)

    |   |
____|___|____
    | O |  X
____|___|____
    | X |
    |   |

- The computer should always occupy the corner located in between the two user occupied squares as shows below

    |   |
____|___|____
    | O |  X
____|___|____
    | X |  O
    |   |

"""




"""
Turn System:

Everytime a move is played a 'turn' variable will be incremented by 1 which will
allow us to keep track of the turns. The player will always start first and the 
turn value will start from 0. Whenever the value is an even number it will be 
the player's turn whereas whenever the value is an odd number it will be the computer's
turn.

"""




Turn=0



"""

Update_Board Algorithm

Input: The index of the combination, the list containing all of the combinations and the index value of the empyty space
Output: Updates the main board matrix which allows the program to render the UI

Description: 

This function is designed to update the main board matrix through a list of set combinations 
    |   |
____|___|____
    |   |
____|___|____
    |   |
    |   |
"""


def Update_Board(IndexOfCombination, All_List_Combinations, IndexOfValue):

    Row1=All_List_Combinations[0]#Storing the value of Row1 to the first list in the All_List_Combinations list
    Row2=All_List_Combinations[1]#Storing the value of Row2 to the second list in the All_List_Combinations list
    Row3=All_List_Combinations[2]#Storing the value of Row3 to the third list in the All_List_Combinations list
    Column1=All_List_Combinations[3]#Storing the value of Column1 to the fourth list in the All_List_Combinations list
    Column2=All_List_Combinations[4]#Storing the value of Column2 to the fifth list in the All_List_Combinations list
    Column3=All_List_Combinations[5]#Storing the value of Column3 to the sixth list in the All_List_Combinations list
    Diagnol1=All_List_Combinations[6]#Storing the value of Diagnol1 to the seventh list in the All_List_Combinations list
    Diagnol2=All_List_Combinations[7]#Storing the value of the Diagnol2 to the eighth list in the All_List_Combinations list

    
    if All_List_Combinations[IndexOfCombination]==Row1 and IndexOfCombination==0:#Checking to see if the index of the combination's value is equal to the list in Row1 and making sure the index of the combination is 0 to avoid scanning the wrong list
     
        Board[0][IndexOfValue]=Row1[IndexOfValue]#Setting either the first, second or third square of the board to the value in Row1 which is the compputer's selected square
    
    elif All_List_Combinations[IndexOfCombination]==Row2 and IndexOfCombination==1:#Checking to see if the index of the combinations value is equal to the list in Row2 and making sure the index of the combination is 1 to avoid scanning the wrong list      
        
        Board[1][IndexOfValue]=Row2[IndexOfValue]#Setting either the fourth, fifth or sixth square of the board to the value in Row2 which is the computer's selected square
    
    elif All_List_Combinations[IndexOfCombination]==Row3 and IndexOfCombination==2:#Checking to see if the index of the combination's value is equal to the list in Row3 and making sure the index of the combination is 2 to avoid scanning the wrong list
        
        Board[2][IndexOfValue]=Row3[IndexOfValue]#Setting either the seventh, eighth or ninth square of the board to the value in Row3 which is the computer's selected square
    
    elif All_List_Combinations[IndexOfCombination]==Column1 and IndexOfCombination==3:#Checking to see if the index of the combination's value is equal to the list in Column1 and making sure the index of the combination is 3 to avoid scanning the wrong list 

        Board[IndexOfValue][0]=Column1[IndexOfValue]#Setting either the first, fourth or seventh square of the board to the value in Column1 which is the computer's selected square

    elif All_List_Combinations[IndexOfCombination]==Column2 and IndexOfCombination==4:#Checking to see if the index of the combination's value is equal to the list in Column2 and making sure that the index of the combination is 4 to avoid scanning the wroing list 

        Board[IndexOfValue][1]=Column2[IndexOfValue]#Setting the second, fifth or eighth square of the board to the value in Column2 which is the computer's selected square                  
    
    elif All_List_Combinations[IndexOfCombination]==Column3 and IndexOfCombination==5:#Checking to see if the index of the combination's value is equal to the list in Column3 and making sure that the index of the combination is 5 to avoid scanning the wrong list 

        Board[IndexOfValue][2]=Column3[IndexOfValue]#Setting the third, sixth or ninth square of the board to the value in Column3 which is the computer's selected square
    
    elif All_List_Combinations[IndexOfCombination]==Diagnol1 and IndexOfCombination==6:#Checking to see if the index of the combination's value is equal to the list in Diagnol1 and making sure that the index of the combination is 6 to avoid scanning the wrong list

        Board[IndexOfValue][IndexOfValue]=Diagnol1[IndexOfValue]#Setting the first, fifth or ninth square of the board to the value in Diagnol1 which is the computer's selected square
    
    elif All_List_Combinations[IndexOfCombination]==Diagnol2 and IndexOfCombination==7:#Checking to see if the index of the combination's value is equal to the list in Diagnol2 and making sure that the index of the combination is 7 to avoid scanning the wrong list

        if Diagnol2[0]==2:#Checking if the first value in Diagnol2 has the computer's input which is represented by '2'

            Board[2][0]=Diagnol2[0]#Setting the seventh square of Board to the first element of Diagnol2 
        
        if Diagnol2[1]==2:#Checking if the second value in Diagnol2 has the computer's input which is represented by '2'

            Board[1][1]=Diagnol2[1]#Setting the fifth square of the Board to the second element in Diagnol2
        
        if Diagnol2[2]==2:#Checking if the third value in Diagnol2 has the computer's input which is represented by '2'

            Board[0][2]=Diagnol2[2]#Setting the third square of the Board to the third element in Diagnol2

    elif IndexOfValue==8:#Checking if the combination is Corner1

        Board[0][0]=2

    elif IndexOfValue==9:#Checking if the combination is Corner2

        Board[0][2]=2
    
    elif IndexOfValue==10:#Checking if the combination is Corner3

        Board[2][0]=2
    
    elif IndexOfValue==11:#Checking if the combination is Corner4

        Board[2][2]=2
    

    print(Board)
    sys.stdout.flush()
    









"""
ComputerAlgorithm_selecting_the_right_square

Description: 

This algorithm is designed to select the winning square for the computer by scanning through all of the possible combinations and 
identifying a vacant space.


"""

def ComputerAlgorithm_selecting_the_right_square(All_List_Combinations):#Function designed select the right sqaure for the computer's victory

    global Turn#Globalising the variable 'Turn' in order to increment it

    for Combination in All_List_Combinations:#Looping through the combinations 
        
        Computer_Can_Win=True#Setting the value of Computer_Can_Win to True
        SumOfValues=sum(Combination)#Finding the sum of the values in the combination

        for Value1 in Combination:#Looping through the values in the combination
            if Value1==1:#Checking if a player has entered a value in that combination 

                Computer_Can_Win=False#Setting the value of Computer_Can_Win to False if the player has entered a value
                break#Stopping the code
        
        if SumOfValues==4 and Computer_Can_Win==True:#Checking if the total value is 4 which means that 2 values of '2'= 4 and the computer can win

            IndexOfCombination=All_List_Combinations.index(Combination)#Finding the index of the combination

            for Value in Combination:#Looping through the values in the combination
                
                if Value==0:#Checking if there is an empty space in the combination to take over

                    IndexOfValue=Combination.index(Value)#Finding the index of the Value in the Combination
                    All_List_Combinations[IndexOfCombination][IndexOfValue]=2#Setting the value of the empty space to '2' 

                    if Turn%2!=0:#Checking if the turn isn't divisible by 2 which indicates that it is the computer's turn
                        Update_Board(IndexOfCombination, All_List_Combinations, IndexOfValue)#Updating the main board
                        Turn+=1 

                        #print(Board[0])
                        #print(Board[1])
                        #print(Board[2])














"""
Block_user_from_winning

Description: 

This function is designed to block the user from winning by identifying such a situation by scanning through all of the possible combinations

"""

def Block_user_from_winning(All_List_Combinations):#Function designed to block the user from winning 

    global Turn#Globalising the variable 'Turn' in order to increment it 

    for Combination in All_List_Combinations:#Looping through all of the possible combinations

        SumOfValues=sum(Combination)#Findind the sum of all the values in the combination
        if SumOfValues==2:#Checking if the sum is 2 which could mean that there are 2 values of '1' meaning that there could be 2 values of the player 
            
            #This loop is being ran to check if there are 2 values of '1' which would mean that the computer could block the player from winning

            NumberOfPlayerValue=0#Setting the NumberOfPlayerValue to 0

            for Value in Combination:#Looping through all of the values in the combination

                if Value==1:#Checking if the value is 1 which means that there is a player value 
                    NumberOfPlayerValue=NumberOfPlayerValue+1#incrementing the NumberOfPlayerValues by 1 to see if there are 2 values of '1' in the combination
            
            if NumberOfPlayerValue==2:#Checking if there are 2 player values in the combination
               
                for Value in Combination:#Looping through the values in the combination

                    if Value==0:#Checking if the value is '0' which would mean that there is an empty space for the computer to occupy

                        IndexOfCombination=All_List_Combinations.index(Combination)#Finding the index of the combination
                        IndexOfValue=Combination.index(Value)#Finding the index of the empty value in the combination
                        All_List_Combinations[IndexOfCombination][IndexOfValue]=2#Changing the empty value to '2' which would mean that the computer has occupied the value
                        
                        if Turn%2!=0:#Checking if the turn isn't divisible by 2 which indicates that it is the computer's turn

                            Update_Board(IndexOfCombination, All_List_Combinations, IndexOfValue)#Updating the main board
                            Turn+=1#Incrementing the value of turn by 1
                            
                            #print(Board[0])
                            #print(Board[1])
                            #print(Board[2])













"""
Check_For_Winner

Description: 

This function is designed to check if whether a player or a computer has won

"""

#Checking for a winner
def Check_For_Winner(All_List_Combinations):
    global PlayerHasWon
    for Combination in All_List_Combinations:#Looping through the possible combinations

        SumOfValues=sum(Combination)#Calculating the total value of the combination

        if SumOfValues==6:#If there are 3 values of '2' then the computer has won since 3 multiplied by the value 2 = 6

            PlayerHasWon=False
            print("The computer has won!")
            print(Board)
            sys.stdout.flush()
            break
        if SumOfValues==3:#If there are 3 values of '1' then the player has won since 3 multiplied by the value 1 = 3
            UserOccupancy=0#Variable designed to count the total boxes in which the user has occupied in the combination. Used to ensure that someone has won

            for value in Combination:#For loop designed to loop through the values in the combination to ensure that all of the values are '1'

                if value==1:#Checking if the value is '1'
                    UserOccupancy+=1#Incremeneting the variable by 1
            if UserOccupancy==3:#Checking if there are three '1' values which tells us that the user has won since there are only three boxes 

                PlayerHasWon=True#Setting the variable to true indicating that the player won
                print("The player has won!")
                sys.stdout.flush()
                break


"""
Main_Computer_Algorithm

Description: 

This function is designed to select the best position for the computer using a range of algorithms 

"""


def Main_Computer_Algorithm(All_List_Combinations):#Function designed to perform the main computer algorithm which allows the computer to choose the right square

    global Turn#Globalising the 'Turn' variable in order to increment it
    global Board#Globalising the 'Board' variable in order to alter it
    if Turn%2!=0:#Checking if the turn isn't divisible by 2 which indicates that it is the computer's turn

        if Board[1][1]==0:#Checking if the 5th square(middle square) isn't occupied 

            Board[1][1]=2#Updating the board by changing the square's value to 2 which indicates that the computer has occupied the square
            Turn+=1#Incrementing the value of turn by 1
           
            print(Board)
            sys.stdout.flush()

        elif Board[1][1]==2:#Checking if the 5th square(middle square) was already occupied by the computer

            Row2=All_List_Combinations[1]#Storing the middle row 
            Column2=All_List_Combinations[4]#Storing the middle column

            Middle_Row_Sum=sum(Row2)#Storing the sum of elements which tells us if a user occupancy exists in the middle row
            Middle_Column_Sum=sum(Column2)#Storing the sum of elements which tells us if a user occupancy exists in the middle column


            #Storing the corner values in a list
            Corner1=[Board[1][0], Board[0][0], Board[0][1]]
            Corner2=[Board[0][1], Board[0][2], Board[1][2]]
            Corner3=[Board[1][0], Board[2][0], Board[2][1]]
            Corner4=[Board[2][1], Board[2][2], Board[1][2]]

            Corner1_sum=sum(Corner1)#Storing the sum of Corner1
            Corner2_sum=sum(Corner2)#Storing the sum of Corner2
            Corner3_sum=sum(Corner3)#Storing the sum of Corner3
            Corner4_sum=sum(Corner4)#Storing the sum of Corner4

            if Middle_Row_Sum==2 and 1 not in Row2:#Checking if the middle row's sum is 2, showing us that a computer occupancy exists, and verifying it by checking if there isn't a user occupancy

                Index_Of_Empty_Square=Row2.index(0)#Finding the index of the empty square in the middle row
                All_List_Combinations[1][Index_Of_Empty_Square]=2#Altering the matrix to occupy the empty square
                Update_Board(1, All_List_Combinations, Index_Of_Empty_Square)#Updating the main board 
                Turn+=1#Incrementing the Turn by 1

                #print("Empty row")
                #print(Board[0])
                #print(Board[1])
                #print(Board[2])
            
            elif Middle_Column_Sum==2 and 1 not in Column2:#Checking if the middle column's sum is 2, showing us that a computer occupancy exists, and verifying it by checking if there isn't a user occupancy

                Index_Of_Empty_Square=Column2.index(0)#Finding the index of the empty square in the middle row
                All_List_Combinations[4][Index_Of_Empty_Square]=2#Altering the matrix to occupy the empty square
                Update_Board(4, All_List_Combinations, Index_Of_Empty_Square)#Updating the main board 
                Turn+=1#Incrementing the value of Turn by 1

                #print("Empty Column")
                #print(Board[0])
                #print(Board[1])
                #print(Board[2])

            elif Corner1_sum==2 and Corner1[1]==0:#Checking is the sum is 2 and there is a vacancy
                print(Corner1_sum)
                Update_Board(8, All_List_Combinations, 8)#Updating the main board
                Turn+=1
            
            elif Corner2_sum==2 and Corner2[1]==0:#Checking is the sum is 2 and there is a vacancy
                Update_Board(8, All_List_Combinations, 9)#Updating the main board
                Turn+=1
            
            elif Corner3_sum==2 and Corner3[1]==0:#Checking is the sum is 2 and there is a vacancy
                Update_Board(8, All_List_Combinations, 10)#Updating the main board
                Turn+=1
            
            elif Corner4_sum==2 and Corner4[1]==0:#Checking is the sum is 2 and there is a vacancy
                Update_Board(8, All_List_Combinations, 11)#Updating the main board
                Turn+=1

        
        elif Board[1][1]==1:#Checking if the 5th square(middle square) has been occupied by the user

            Row1=All_List_Combinations[0]#Storing the Row1 list
            Row3=All_List_Combinations[2]#Storing the Row3 list

            if Row1[0]==0:#Checking if the first square(first corner) is vacant

                All_List_Combinations[0][0]=2#Changing the first square's value to 2 in order to occupy it for the computer
                Update_Board(0, All_List_Combinations, 0)#Updating the main board
                Turn+=1#Incrementing the value of Turn by 1
            
            elif Row1[2]==0:#Checking if the third square(second corner) is vancant

                All_List_Combinations[0][2]=2#Changing the third square's value to 2 in order to occupy it for the computer
                Update_Board(0, All_List_Combinations, 2)#Updating the main board
                Turn+=1#Incrementing the value of Turn by 1
            
            elif Row3[0]==0:#Checking if the seventh square(third corner) is vacant

                All_List_Combinations[2][0]=2#Changing the seventh square's value to 2 in order to occupy it for the computer
                Update_Board(2, All_List_Combinations, 0)#Updating the main board
                Turn+=1#Incrementing the value of Turn by 1
            
            elif Row3[2]==0:#Checking if the ninth square(fourth corner) is vacant

                All_List_Combinations[2][2]=2#Changing the ninth square's value to 2 in order to occupy it for the computer
                Update_Board(2, All_List_Combinations, 2)#Updating the main board
                Turn+=1#Incrementing the value of Turn by 1










"""
Gameplay

Description:

This is the main gameplay function which comprises of the main functions used in this program

"""




def Gameplay():

    if 0 not in Board[0] and 0 not in Board[1] and 0 not in Board[2] and PlayerHasWon==0:
        print("It's a draw!")
        sys.stdout.flush()

    global Turn#Globalising the 'Turn' variable
    Turn+=1#Indicating that it is now the computer's turn

    #Storing the row values in a list

    Row1=[Board[0][0], Board[0][1], Board[0][2]]
    Row2=[Board[1][0], Board[1][1], Board[1][2]]
    Row3=[Board[2][0], Board[2][1], Board[2][2]]

    #Storing the column values in a list
    Column1=[Board[0][0], Board[1][0], Board[2][0]]
    Column2=[Board[0][1], Board[1][1], Board[2][1]]
    Column3=[Board[0][2], Board[1][2], Board[2][2]]

    #Storing the diagnol values in a list
    Diagnol1=[Board[0][0], Board[1][1], Board[2][2]]
    Diagnol2=[Board[2][0], Board[1][1], Board[0][2]]


    All_List_Combinations=[Row1, Row2, Row3, Column1, Column2, Column3, Diagnol1, Diagnol2, [1]]#Storing all of the combination in a list. The ninth element exists as an event which is used to update a specific set of squares on the board


    ComputerAlgorithm_selecting_the_right_square(All_List_Combinations)
    Block_user_from_winning(All_List_Combinations)
    Check_For_Winner(All_List_Combinations)
    Main_Computer_Algorithm(All_List_Combinations)

    #The code below is used to occupy a random empty square in the board if a space isn't found using the algorithms above

    if Turn%2!=0:#Checking if the computer hasn't moved yet

        Index_Of_Combination=0#Initialising the combination's index value
        for Combination in All_List_Combinations:#Looping through all of the combinations

            if 0 in Combination:#Checking if there is an empty space in the combination
                
                Index_Of_Empty_Square=Combination.index(0)#Searching for the vacancy in the combination
                All_List_Combinations[Index_Of_Combination][Index_Of_Empty_Square]=2#Updating the combinations matrix
                Update_Board(Index_Of_Combination, All_List_Combinations, Index_Of_Empty_Square)#Updating the main board
                Turn+=1#Incrementing the Turn value
                break#Exit the loop

            Index_Of_Combination+=1#Incrementing the index value



Gameplay()#Calling the gameplay function