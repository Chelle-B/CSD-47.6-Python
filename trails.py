# Create a function for school admission system. 
# A student can apply for admission by providing their name, age, email, grade
# The function should check if the student is eligible for admission based 
# on grade
# If the student is eligible, 
# the function should return a message saying "Congratulations {name}, 
# you have been admitted to our school"
# If the student is not eligible, the function should return a message saying
#  "Sorry {name}, you are not eligible for admission"
# If the student is eligible, the function should also return the student's 
# profile which includes their name, age, email, and grade.
# If the student is not eligible, the function should not return the profile.
# The function should also store the student's profile in a local storage
# (a dictionary) if they are eligible for admission.


def school_admission(name,age,email,grade):
    eligible_grades = ['A','B','B+','C','C+']
    
    local_storage = {}
    if grade in eligible_grades:
        student_profile = {
        "name" : name,
        "age"  :  age,
        "email" : email,
        "grade" : grade
    }
        local_storage[email] = student_profile
        
        return(f"Congratulations {name},  you have been admitted to our school",
               local_storage
               )
    else:
        return f"Sorry {name}, you are not eligible for admission"
name = input("Enter student name:")
age = int(input("Enter student age:"))
email = input("Enter student email:")
grade = input("Enter student grade:").upper()

ama_admission_se23 = school_admission(name,age,email,grade)
print(ama_admission_se23)

           