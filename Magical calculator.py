import re
print ("Our magical calculator")
print ("Type 'quit' to exit\n")

previous=0
run=True

def performMath():
    global run
    global previous
    equation = ""
    if previous==0:
        equation =input("Enter Equation :")
    else:
        equation=input(str(previous))
        
    if equation =='quit':
        print("Good Bye, Insaan")
        run=False
    else:
        equation=re.sub('[a-zA-Z,.():" "]','',equation)
        if previous==0:
            previous=eval(equation)
        else:
            previous=eval(str(previous) + equation)
        
while run:
    performMath()
