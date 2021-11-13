def fcn(Num):
    n=0
    count=1
    
    while(n**2>Num or Num>=count**2):
        n=n+1
        count=count+1
        
    q=n**2
    
    print("Quotient is:", n)
    print("Quotient squared is:", q)
    
fcn(30)