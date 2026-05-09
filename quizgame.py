name = input("Enter your name:")
print("Welcome", name)
print("Lets play quiz game!!", name)

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer  
        
print("Total questions: 3")

question1 = Question("\n1)What is the capital of india? \n 1.Delhi \n 2.Mumbai", "1")

question2 = Question("\n2)2+2=? \n 1.5 \n 2.4", "2")

question3 = Question("\n3)Python is ? \n 1.language \n 2.human", "1")


list = [question1, question2, question3]

answers = []

for each in list:
   
   userInput = input(each.question)
   
   if each.answer == userInput:
      
     answers.append(1) 
      
     print("\n correct")
   else:
     print("\n wrong")
   
print("\n Your score is: ", len(answers))

if len(answers) == 3:
    print("\n Excellent")
elif len(answers) ==2:
    print("\n Good")
else:
    print("\n Keep practicing")

percentage = (len(answers)/3)*100
print("\n Your percentage:", percentage)
      