# Weighted Exam Score Average

# Entering how many exams you have completed
number_of_exams = int(input("Enter number of exams: "))

# Enter how many total credits these exams cover
total_credits = int(input("Enter how many credits these exams cover: "))

Avg_credits_per_exam = total_credits/number_of_exams

print("Number of exams =",number_of_exams, "; Total credits =", total_credits)
print("Average credits/exam =", Avg_credits_per_exam)

# Begin with average of 0 and then add up percentages for each exam
Weighted_Average = 0
for exam in range(number_of_exams):
    score = int(input("Enter exam score: "))
    exam_credits = int(input("Enter how many credits this exam was worth: "))
    Weighted_Average = Weighted_Average + score*exam_credits/total_credits
print("Your weighted average is: ",round(Weighted_Average,2))


