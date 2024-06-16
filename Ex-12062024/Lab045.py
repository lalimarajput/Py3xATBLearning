#WAP to calculate and display grades A,B,C,D,F based on following scores:
#A=90-100
#B=80-89
#C=70-79
#D=60-69
#F=0-59 (Fail)

#Step 1 (Logic building):
#input->score->int
#output->grade->str
score=int(input("Enter your score:"))

#Step2 (rough logic):
#score>=90 and score<=100---->A
#score>=80 and score<=89---->A
#score>=70 and score<=79---->A
#score>=60 and score<=69---->A
#score>=0 and score<=59---->A

#Step3 (Real logic):
if score>=90 and score<=100:
    print("Grade is A")
elif score>=80 and score<=89:
    print("Grade is B")
elif score>=70 and score<=79:
    print("Grade is C")
elif score>=60 and score<=69:
    print("Grade is D")
elif score >=0 and score <= 59:
    print("Grade is C")
else:
    print("Invalid score")
