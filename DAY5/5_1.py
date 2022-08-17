# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

count=0
total=0
for student in student_heights:
    total=total + student
    count+=1
print(round(total/count))


