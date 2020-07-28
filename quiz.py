import random
class Country:
    def __init__(self,name1,capital1,currency1,population1,area1):
        self.name=name1
        self.capital=capital1
        self.currency=currency1
        self.population=population1
        self.area=area1
    def display(self):
        detail=self.name+" : "+self.capital+" : "+self.currency+" : "+self.population+" : "+self.area
        print(detail)
f = open("country.txt", "r")
data = f.read()
temp= (data).split("\n")
x=[]
t=[]
c1=[]
cp=[]
cc=[]
pp=[]
ar=[]
for i in range(1,len(temp)):
    t= temp[i]
    t=t.lower()
    x.append( t.split(","))    
for i in  range (0,len(x)-1): 
    c1.append(x[i][0])
    cp.append(x[i][1])
    cc.append(x[i][2])
    pp.append(x[i][3])
    ar.append(x[i][4])
print ("c1 = "+str(c1))
print ("cp = "+str(cp))
print ("cc = "+str(cc))
print ("pp = "+str(pp))
print ("ar = "+str(ar)) 

#step 4 and 5 NAME OF CAPITAL
#------------------------------------------------------------------
def option1():
    score1=0
    score2=0
    z={}
    for i in range(0,4):
        x=random.randint(0,len(c1))
        z[i]=str(c1[x])
        y=str(input("Do you  know the capital of "+str(c1[x])+ " : "))
        print (y)
        if str(y)== str(cp[x]):
            print ("correct")
            score1=score1+1
            score2=score2+1
            print ("Your score is "+str(score1)+" out of "+str(score2))
        else:
            print ("Wrong. The capital of  "+str(c1[x])+" is "+str(cp[x]))
            score2=score2+1
            print ("Your score is "+str(score1)+" out of "+str(score2))
            
# STEP  6 GIVEN THE CAPITAL, IDENTIFY THE COUNTRY
#-----------------------------------------------------------------
def option2():
    score1=0
    score2=0
    z={}
    for i in range(0,4):
        x=random.randint(0,len(cp))
        z[i]=str(cp[x])
        y=str(input(str(cp[x])+" is the capital of "+ " : "))
        if str(y)==str(c1[x]):
            print ("correct")
            score1=score1+1
            score2=score2+1
            print ("Your score is "+str(score1)+" out of "+str(score2))
        else:
            print ("Wrong. "+str(cp[x])+" is the capital of  "+str(c1[x]))
            score2=score2+1
            print ("Your score is "+str(score1)+" out of "+str(score2))

#STEP 7  DO YOU KNOW THE CURRENCY
#---------------------------------------------------------------------
def option3():
    score1=0
    score2=0
    z={}
    for i in range(0,4):
        x=random.randint(0,len(c1))
        z[i]=str(c1[x])
        y=str(input("Do you  know the currency of "+str(c1[x])+ " : "))
        if str(y)==str(cc[x]):
            print ("correct")
            score1=score1+1
            score2=score2+1
            print ("Your score is "+str(score1)+" out of "+str(score2))
        else:
            print ("Wrong. The currency of  "+str(c1[x])+" is "+str(cc[x]))
            score2=score2+1
            print ("Your score is "+str(score1)+" out of "+str(score2))

# STEP 8 WHO HAS THE LARGER THE POPULATION
#------------------------------------------------------------------------
def option4():
    score1=0
    score2=0
    z={}
    v={}
    for i in range(0,4):
        x=random.randint(0,len(c1))
        y=random.randint(0,len(c1))
        z[i]=str(c1[x])
        v[i]=str(c1[y])
        k=str(input("Which country has the larger population: "+str(c1[x])+ " or  "+str(c1[y])+' : '))
        if str(k)==str(c1[x]) and pp[x]>=pp[y]:
            print ("correct")
            score1=score1+1
            score2=score2+1
            print ("Your score is "+str(score1)+" out of "+str(score2))
        else:
            print ("Wrong. "+str(c1[y])+" has more population than "+str(c1[x]))
            score2=score2+1
            print ("Your score is "+str(score1)+" out of "+str(score2))
#STEP 9 WHICH COUNTRY IS LARGER
#-------------------------------------------------------------------------
def option5():
    score1=0
    score2=0
    z={}
    v={}
    for i in range(0,4):
        x=random.randint(0,len(c1))
        y=random.randint(0,len(c1))
        z[i]=str(c1[x])
        v[i]=str(c1[y])
        k=str(input("Which country is larger : "+str(c1[x])+ " or  "+str(c1[y])+' : '))
        if str(k)==str(c1[x]) and ar[x]>=ar[y]:
            print ("correct")
            score1=score1+1
            score2=score2+1
            print ("Your score is "+str(score1)+" out of "+str(score2))
        else:
            print ("Wrong. "+str(c1[y])+" has more population than "+str(c1[x]))
            score2=score2+1
            print ("Your score is "+str(score1)+" out of "+str(score2))
def option6():
    print ("Played Enough. Want to take a break")
#step3

def main():
    print ("Let's play a game. Choose the game you wan to play")
    print ("Option 1: Name the capital of the country")
    print ("Option 2: Given the capital, Identify the country")
    print ("Option 3: Name the currency of the country")
    print ("Option 4: Who has the larger population")
    print ("Option 5: Which country is larger")
    print ("Option 6: Played Enough. Want to take a break")
    n=int(input("What is your choice : "))
    if n==1:
        option1()
    elif n==2:
        option2()
    elif n==3:
        option3()
    elif n==4:
        option4()
    elif n==5:
        option5()
    elif n==6:
        exit()
    else:
        print ("you choice is not available")
    return n
n=0
while n!=6:
    cq=main()
    print (Sxcq)





            
