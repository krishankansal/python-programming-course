students = {
    "Laveneesh": 90,
    "Rohit": 65,    
    "Amit": 75,
    "Suresh": 80,
    "nilesh": 55
}

# print(students["amit"])
print(students.get("amit"))
print(students.get("amit", "Not Found"))