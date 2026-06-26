students_list = [
    {"name": "Shaikat", "score": 85},
    {"name": "Sagor", "score": 42},
    {"name": "Akhi", "score": 73},
    {"name": "Rohan", "score": 91},
    {"name": "Rahul", "score": 85},
    {"name": "Sajid", "score": 65},
    {"name": "Anika", "score": 45}
]

# নম্বর অনুযায়ী গ্রেড হিসাব করার ফাংশন
def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# লুপ ব্যবহার করে প্রত্যেক শিক্ষার্থীর গ্রেড প্রিন্ট করা
print("--- শিক্ষার্থীদের গ্রেড তালিকা ---")
for student in students_list:
    name = student["name"]
    score = student["score"]
    grade = calculate_grade(score) # ফাংশন কল করা হচ্ছে
    
    print(f"{name}-total score : {score}, grade: {grade}")