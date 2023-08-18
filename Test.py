import sys
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

#sys.stdout.flush()

