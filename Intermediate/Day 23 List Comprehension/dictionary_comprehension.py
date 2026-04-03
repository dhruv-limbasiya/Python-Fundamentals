# simplest form of Dictionary comprehesion
# new_dict = {new_key: new_value for item in list}

# create a new dictionary based on value in an existing dictionary
# new_dict = {new_key : new_value for (key,value) in dict.items()}

# conditional dictionary comprehension
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

import random
# simplest form Ex:
names = ["Alex", "Beth", "Carolina", "Dave", "Elenor", "Fraddie"]
student_scores = {name : random.randint(1, 100) for name in names}
# in this dict. comprehension first python interpreter go in for loop and ietrate in given list and than
# assign that name as key and it value is random number

# create a new dictionary based on value in an existing dictionay win conditionEx:
passed_student ={student : student_scores[student] for student in student_scores if student_scores[student] >= 60}
# second way to create dict. comprehension
passedd_student = {student : score for(student, score) in student_scores.items() if score >= 60}
print(passed_student)
print(passedd_student)