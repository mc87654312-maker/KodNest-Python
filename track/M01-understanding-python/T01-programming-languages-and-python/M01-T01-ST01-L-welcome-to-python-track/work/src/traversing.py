# Nested list

marks = [[45, 75], [48, 78]]

print(marks[1][1])

# Update value
marks[1][1] = 90

print(marks)

#List inside dictionary 
stu_info = {
    "name": "Ravi",
    "marks": [48, 78]
}

print(stu_info["marks"][1])

# Nested Dictionary

stu_info = {
    "name": "Asha",
    "marks": {
        "cs": 48,
        "py": 90
    }
}

print(stu_info["marks"]["py"])


# Updated Nested Dictionary
stu_info["marks"]["py"] = 95

print(stu_info)

## Nested dictionary one or example
stu_info = {
    "asha": {
        "cs": 48,
        "py": 78
    },
    "ravi": {
        "cs": 48,
        "py": 90
    }
}

#Create a list
trainers = ["Divya", "Gamana", "Salman", "Gamana", "Salman", "Gamana"]

#print(trainers)

trainer_count = {}

for t in trainers:
    if t in trainer_count:
        trainer_count[t] += 1
    else:
        trainer_count[t] = 1

print(trainer_count)

##
from collections import Counter

trainers = ["Divya", "Gamana", "Salman", "Gamana", "Salman", "Gamana"]

trainer_count = Counter(trainers)

print(trainer_count.most_common(1)) # print one  highest trainers

print(trainer_count.most_common())
