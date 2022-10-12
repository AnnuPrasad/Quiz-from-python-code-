# Quiz

print("Here the quiz start")
print("1. when python was developed ?")
a=input("enter the answer")
score=0
#1 question
if  a=="1991":
    print("your answer is correct")
    score+=1
else :
    print("your answer is incorrect")
    score-=0.5
#2question
print("2. who is the father of python ?")
b=input("enter the answer")
if  b=="guido van rossum":
    print("your answer is correct")
    score+=1
else :
    print("your answer is incorrect")
    score-=0.5
#3question
print("3. who is the ceo of microsoft?")
c=input("enter the answer")
if  c=="satya nadella":
    print("your answer is correct")
    score+=1
else :
    print("your answer is incorrect")
    score-=0.5
#4question
print("4. Python is interpreter or compiler based language ?")
d=input("enter the answer")
if  d=="interpreter":
    print("your answer is correct")
    score+=1
else :
    print("your answer is incorrect")
    score-=0.5
#5question
print("5. who is the ceo of google?")
e=input("enter the answer")
if  e=="sundar pichai":
    print("your answer is correct")
    score+=1
else :
    print("your answer is incorrect")
    score-=0.5
#6question
print("6. What is part of a database that holds only one type of information?")
a=input("enter the answer")
score=0

if  a=="field":
    print("your answer is correct")
    score+=1
else :
    print("your answer is incorrect")
    score-=0.5
#7question
print("7. '.INI' extension refers usually to what kind of file?")
b=input("enter the answer")
if  b=="System file" :
    print("your answer is correct")
    score+=1
else :
    print("your answer is incorrect")
    score-=0.5
#8question
print("8. Which company created the most used networking software in the 1980's")
c=input("enter the answer")
if  c=="Sun":
    print("your answer is correct")
    score+=1
else :
    print("your answer is incorrect")
    score-=0.5
#9question
print("9. Which of the following operating systems is produced by IBM?")
d=input("enter the answer")
if  d=="OS-2":
    print("your answer is correct")
    score+=1
else :
    print("your answer is incorrect")
    score-=0.5
#10question
print("10. In which decade was the Internet first implemented?")
e=input("enter the answer ")
if  e=="1960":
    print("your answer is correct")
    score+=1
else :
    print("your answer is incorrect")
    score-=0.5
print("your total score is " ,score)