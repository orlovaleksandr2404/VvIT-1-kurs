class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self,new_password):
        self.__password = new_password
    def check_password(self, password):
        return self.__password == password


useraccount1 = UserAccount('user123','user123@inbox.ru','a')
useraccount1.set_password('password')
print(useraccount1.check_password('password'))