print("Welcome To Quiz Game")
point=0
#Question1.
print("Question1 : What is the formula of (a+b)^3 ?")
print("(A).a^3+3a^2b+3ab^2+b^3\n" 
      "(B).a^3+3a^2b+4ab^2+b^4\n" 
      "(C).a^3+3ab^3+3ab^2+b^3\n" 
      "(D).None of these\n")
answer=input("Choose the correct option (A-D): ")
if answer=="A":
    print("Correct")
    point+=1
else:
    print("Incorrect The answer is Option A")    
print(point)
#Question2.
print("Question1 : Who is the CEO of google ?")
print("(A)Mark Zuckerberg\n" 
      "(B).Tim Cook\n"
      "(C).Sundar Pichai\n"
      "(D).None of these\n")
answer=input("Choose the correct option (A-D): ")
if answer=="C":
    print("Correct")
    point+=1
else:
    print("Incorrect The answer is Option A")    
print(point)
#Question3.
print("Question1 :CBI Stands for  ?")
print("(A).Central Bank of India\n"
      "(B).Central Bureau of Investigation\n"
      "(C).Both A and B\n"
      "(D).None of these\n")
answer=input("Choose the correct option (A-D): ")
if answer=="A"or"B"or"C":
    print("Correct")
    point+=1
else:
    print("Incorrect The answer is Option A") 
print(point) 
#Question4. 
print("Question4 : UPSC Stands for ?")
print("(A).Union publics commission\n"
     "(B).Union public service commission\n"
     "(C).Under police service comission\n"
     "(D).None of these\n")
answer=input("Choose the correct option (A-D): ")
if answer=="B":
    print("Correct")
    point+=1
else:
    print("Incorrect The answer is Option A")    
print(point)
#Question5.
print("Question5 : Formula of water ?")
print("(A).HO2\n"
      "(B).H3O\n"
      "(C).H2O\n"
      "(D).None of these\n")
answer=input("Choose the correct option (A-D): ")
if answer=="C":
    print("Correct")
    point+=1
else:
    print("Incorrect The answer is Option A")    
print(point)     
print(f'Your final score is {point}')
#Final Point
if point==5:
    print('Amazing Performance')
elif point==4:
    print('Good Performance') 
elif point==3:
    print('Average Perfromance')   
else:
    print('Not Good')    