from Python_users_class import user
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