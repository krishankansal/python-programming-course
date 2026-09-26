# in the given dictionary print the name of students who
# got marks greater than 70

students = {
    "Laveneesh": 90,
    "Rohit": 65,    
    "Amit": 75,
    "Suresh": 80,
    "nilesh": 55
}

for name, marks in students.items():    
    if marks > 70:
        print(name)  
