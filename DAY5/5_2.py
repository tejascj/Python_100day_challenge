# https://replit.com/@tejascj/day-5-2-exercise#README.md

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
large=student_scores[0]
for student in student_scores:
  if student>large:
    large=student
print(f"The highest score in the class is: {large}")



