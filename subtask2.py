Num = input("Enter number:")
Num = int(Num)
Count = 0
Min = Num
Sum = 0
while(Num != -1):
    Count=Count+1
    if (Num <= Min):
        Min = Num
    Sum = Sum + Num
    Num = input("Enter another number:")
    Num = int(Num)
if (Count == 0):
    print ("Min = -1" + "\nAvg = -1")    
else:
    print ("Count = " + str(Count) + "\nMin = " + str(Min) + "\nSum = " + str(Sum) + "\nAvg = " + str(Sum/Count))