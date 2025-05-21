'''
Write a Citizen class that implements the __init__ method, taking two arguments: first_name and last_name.
    Create an object of this class, then display the citizen's first and last name.
    Add the set_nationality method to the Citizen class (and with it the nationality class field with the selected default value).
    Call this method.
    Create another class object and compare the nationality fields in both objects.
Additionally, you can try adding the total_number_of_citizens attribute which is a natural number. Increase it each time a new citizen object is created.
'''

class Citizen:
    total_number_of_citizens = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = "English"
        Citizen.total_number_of_citizens += 1

    def set_nationality(self , nationality):
        self.nationality = nationality

    def __str__(self):
        return f"\n\nFirst name : {self.first_name}\nLast name : {self.last_name}\nNationality : {self.nationality}\n\n"

citizen_1 = Citizen("Andrei" , "Necsulea")
print(citizen_1)

citizen_1.set_nationality("Romanian")
print(citizen_1)

citizen_2 = Citizen("Maria" , "Ionescust")
citizen_2.set_nationality("Bulgarian")

citizen_3 = Citizen("Jorge" , "Sunenshtein")
citizen_3.set_nationality("German")
print(f"\n\nCitizen 2 nationality is : {citizen_2.nationality}\nCitizen 3 nationality is : {citizen_3.nationality}\n\n")

print(f"\n\nTotal number of citizens is  : {Citizen.total_number_of_citizens}")