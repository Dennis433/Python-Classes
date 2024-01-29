#Users: Make a class called User. Create two attributes called first_name
#and last_name, and then create several other attributes that are typically stored
#in a user profile. Make a method called describe_user() that prints a summary
#of the user’s information. Make another method called greet_user() that prints
#a personalized greeting to the user.
#Create several instances representing different users, and call both methodsfor each user.
class user:
    def __init__(self, full_name, age, gender, height, email, country):
        self.full_name = full_name
        self.age = age
        self.gender = gender
        self.height = height
        self.email = email
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f'Full name: {self.full_name}\nAge: {self.age} \nGender: {self.gender} \nHeight:\
 {self.height} \nEmail:  {self.email}  \nCountry: {self.country}')

    def greet_user(self):
        print(f'Hello {self.full_name}')

    def incremtnt_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privilage:
    def __init__(self):
        self.privilages = ["can add post", "can delete post", "can ban user"]

    def show_privilages(self):
        print('The list of privi  leges include: ')
        for i in self.privilages:
            print(i)

class Admin(user):
    def __init__(self, full_name, age, gender, height, email, country):
        super().__init__(full_name, age, gender, height, email, country)
        self.privilages = Privilage()

    def show_privilages(self):
        self.privilages.show_privilages()


#user2 = Admin('Nate Furry', 31, 'Male', 6.9, 'natefurry21@gmail.com', 'United Kingdom')
#print(user2.privilages.show_privilages())




user_1 = Admin('Nate Furry', 31, 'Male', 6.9, 'natefurry21@gmail.com', 'United Kingdom')
#print(user_1.show_privilages())
#user_1.describe_user()
#user_1.greet_user()
#user_1.incremtnt_login_attempts()
#user_1.reset_login_attempts()
#print(user_1.login_attempts)
