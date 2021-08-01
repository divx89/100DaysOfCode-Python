student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

numStudents = 0
totalHeight = 0

for height in student_heights:
    numStudents += 1
    totalHeight += height

average_height = round(totalHeight/numStudents)
print(average_height)
