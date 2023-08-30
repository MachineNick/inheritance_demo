class User:
    def login(self):
        print("login")
    def register(self):
        print("register")
class Student(User):
    def enroll(self):
        print("enroll")
    def review(self):
        print("review")
        
        
#parent class can access child class
stu1 = Student()
stu1.enroll()
stu1.review()
stu1.login()
stu1.register()
#but child class can't acces to parent class
u =User()
u.enroll()
u.review()
u.login()
u.register()
