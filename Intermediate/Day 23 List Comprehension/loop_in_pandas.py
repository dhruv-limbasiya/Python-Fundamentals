student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

# looping through dictionary:

# for (key, value) in student_dict.items():
#     print(value)

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

#loop through a data frame
for (key, value) in student_data_frame.items():
    print(value)

# loop through rows of data frame
for(index, row) in student_data_frame.iterrows():
    print(row.score)