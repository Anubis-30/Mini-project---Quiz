import random
import json

Questions=[]
Answers=[]
f=open('Questions.json')
data=json.load(f)
for i in data.keys():
    Questions.append(data[i])

f=open('Answers.json')
data1=json.load(f)
for i in data1.keys():
    Answers.append(data1[i])

ans=dict(zip(Questions,Answers))
l=[x for x in range(0,len(Questions)-1)]
x=random.sample(l,5)
score=0
for i in range(len(x)):
    y=Questions[i]
    print(y)
    your_answer=input('Answer: ')
    if your_answer==ans[y]:
        print('Correct')
        score+=1
    else:
        print('Incorrect')

print("Your Final Score is ", score)
