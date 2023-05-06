# Update the Student Class to include these attributes - first_name, last_name, age, country
#      - Add these methods to the Student class
#              - show_full_name
#              - year_of_birth
#              - show_initials

class Student:
    def __init__(self,first_name,last_name,age,country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def full_name(self):
        return f"Hey there I am {self.first_name},{self.last_name} and I am happy to be here"
    
    def year_of_birth(self):
        current_year = 2023
        return current_year - self.age
    
    def show_initials(self):
        return f"{self.first_name[0],self.last_name[0]}"