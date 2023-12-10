import random
from matplotlib import pyplot as plt
class Question: 
    def __init__(self,text,options,correct_answer):
        self.text=text
        self.options=options
        self.correct_answer=correct_answer
    def display(self,k):
        print(f"Question {k+1} {self.text}")
        ascii=65
        for i in self.options:
            print("Option",chr(ascii),":",i,end="   ")
            ascii+=1
        print()
    def lifeline_50_50(self):
        l=[]
        for j in range(len(self.options)):
            if j!=self.correct_answer:
                l.append(j)
        m=random.choice(l)
        l=[]
        for i in range(len(self.options)):
            if i==m or i==self.correct_answer:
                l.append(self.options[i])
        new_correct=l.index(self.options[self.correct_answer])
        self.options=l
        self.correct_answer = new_correct
        
    def double_dip(self,val,i):
        l=[]
        for i in range(len(self.options)):
            if i!=val:
                l.append(self.options[i])
        new_correct=l.index(self.options[self.correct_answer])
        self.options=l
        self.correct_answer = new_correct

def audience_poll(k,obj):
    l=len(obj)
    c=random.randint(50,70)
    sum_of_poll=0
    y=[]
    for i in range (l):
        w=random.randint(10,25)
        y.append(w)
        if i==k:
            y[i]=c
        sum_of_poll = sum_of_poll + y[i]
    
    for i in range (l):
        y[i] = round((100*y[i])/sum_of_poll)
    
    x=[]
    for j in range(l):
        x.append(f"{obj[j]}\n {str(y[j])}%")
        
    plt.ylim(0,100)
    plt.title("Result")
    plt.bar(x,y)
    return plt.show()



    
def show_remaining_lifelines(lifeline):
    print("Remaining lifelines:", end=" ")
    ctr=0
    for j in lifeline.items():
        if j[1]==0:
            ctr+=1
            print(j[0],end="  ")
    print()
    return ctr

list=[["Which country is not included in G20?",["Mexico","South Korea","France","North Korea"],3],
      ["Which Indian has won the 2023 Ramon Magsaysay award?",["Ravi Kannan","Gautam Adani","Ghazal Alagh","Kailash Vidyarthi"],0],
      ["Who becomes the first cricketer who has hit the six sixes in an over in One Day International Cricket",["Kieron Pollard","Yuvraj Singh","Herschelle Gibs","Viv Richards"],2],
      ["Which state launched 'Gruha Lakshmi scheme'?",["Kerala","Karnataka","Andhra Pradesh","Odisha"],1],
      ["Who among the following has been appointed as the first woman CEO and chairperson of the Railway Board?",["Jaya Verma Sinha","Leena Nair","Falguni Nayar","Roshni Nadar"],0]
    ]

questionsList=[]
text=[]
options=[]
correct_answer=[]
lifeline={
    "Audience Poll" : 0,
    "Double Dip" : 0,
    "50-50" : 0
}
milestone=[1,3]
assured_amt = 0
curr_amt=0
amt_list=[10000,20000,40000,80000,160000]
playing = True
for i in range(len(list)):
    text.append(list[i][0])
    options.append(list[i][1])
    correct_answer.append(list[i][2])
    questionsList.append(Question(text[i],options[i],correct_answer[i]))

print("Welcome to KBC")
lifelines_left = show_remaining_lifelines(lifeline)
i=0
ms_count=0
while i < len(list):
    print("This Question is of worth:",amt_list[i])
    (questionsList[i].display(i))
    inp = input("Press L for LifeLine or Q to quit or play by pressing preferred option: ")
    corr_opt=questionsList[i].correct_answer
    if lifelines_left == 0:
        print("No Lifelines Left!!")
    elif inp.lower() == 'l':
        str1="Enter:"
        ctr=1
        for key,value in lifeline.items():
            if value == 0:
                str1 += f'\n{ctr} for {key}' 
            ctr+=1
        print(str1)
        inp1=int(input("Choose Lifeline:"))
        if lifeline.get([*lifeline][inp1-1]) == 0:
            if inp1==1:
                print(audience_poll(corr_opt,questionsList[i].options))
                
            elif inp1==2:
                inp2= input("Enter your first attempt answer: ")
                if ord(inp2.lower())-97 != corr_opt:
                    print("Wrong Answer!! Time For Second Attempt")
                    questionsList[i].double_dip(ord(inp2.lower())-97,i)
                    print("Make your Second attempt:\n")
                else:
                    i+=1
            elif inp1==3:
                questionsList[i].lifeline_50_50()
            else:
                print("Invalid Lifeline")
            lifeline[[*lifeline][inp1-1]] = 1 
        else :
            print("Lifeline is already used") 
        i=i-1             

    elif inp.lower() == 'q':
        print(f"You have opted to quit. Thanks for playing with us. You have won Rs.{curr_amt}")
        break
    elif inp.lower() in {'a','b','c','d'} :
        if ord(inp.lower())-97 == corr_opt:
            curr_amt=amt_list[i]
            print(f"\n Correct Answer!!!\nYou have won Rs.{curr_amt}!!")
            if i==milestone[ms_count]:
                assured_amt=curr_amt
                ms_count+=1
        else:
            print(f"This is the Wrong Answer!!\nThe Correct Answer is Option {chr(65+corr_opt)}: {questionsList[i].options[corr_opt]}")
            print(f"You have won {assured_amt}")
            break
    else:
        print("Invalid input")
    lifelines_left = show_remaining_lifelines(lifeline)
    i+=1