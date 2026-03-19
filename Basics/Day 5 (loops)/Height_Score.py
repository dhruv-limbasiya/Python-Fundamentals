Student_Score = [99, 45, 56, 100, 350, 257, 423, 123, 132]

total_Score = 0

for i in Student_Score:
    total_Score += i

# with function
total_Score2 = sum(Student_Score)

print(total_Score)
print(total_Score2)

# max in list

maxx = Student_Score[0]

for i in Student_Score:
    if i > maxx:
        maxx = i

#with funcntion
print(max(Student_Score))

print(maxx)