question_bank=[
    {"que":"who is current PM of India ?","ans":"Narendra Modi "},
    {"que":"which is called as silicon city ?","ans":"Bangalore "},
    {"que":"who is called as missile man ?","ans":"Abdul kalam"},
    {"que":"how many colors in our Indian flag ?","ans":"3"},
    {"que":"how many states in India ?","ans":"28"}
]


print("--"*30)
print(" !!!  Welcome to Quiz  !!!")
print("--"*30)
score=0
for question in question_bank:
    print(question["que"])
    temp=question["ans"]

    ans=input("Enter your answer : ")
    if ans.lower().strip() == temp.lower().strip():
        print("Correct")
        score+=1
    else:
        print(f"Incorrect \nCorrect answer:{temp}")

print()
print("*"*30)
print(f"Your total score : {score}/5")
print("thank you for attempting ")
print("*"*30)
    

