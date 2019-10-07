class User:
    def __init__(self, username, password, credit=0):
        self.username = username
        self.password = password
        self.credit = int(credit)

    def __str__(self):
        return "{} {} {}".format(self.username, self.password, self.credit)

    def __repr__(self):
        return str(self)


class Database:
    def __init__(self):
        self.users = self.read()
        self.admin_password = "1234"

    def save(self):
        new_list = [str(user) for user in self.users]
        text = '\n'.join(new_list)
        with open("accounts.ck", "w+") as f:
            f.write(text)

    def read(self):
        with open("accounts.ck", "r") as f:
            text = f.read()
        lines = text.splitlines()
        return list([User(*line.split()) for line in lines])

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return True
        return None

    def print_all(self, password):
        # check for admin password
        if self.admin_password == password:
            print(self.users)
        pass

    def get_number_of_users(self, password):
        # check for admin password
        if self.admin_password == password:
            print(len(self.users))
        pass

    def get_total_amount_of_credits(self, password):
        # 1. check for admin password
        # 2. define sum = 0
        # 3. loop on all of self.users
        summ = 0
        if self.admin_password == password:
            for user in self.users:
                summ = user.credit + summ
            print(summ)

        pass

    def user_exists(self, username):

            if self.find_user(username) == True:
                return True
            else:
                return False
    pass

    def username_matches_password(self, username, password):
        for user in self.users:
            # find the user with that username
            # check username == password

            if user.username == username:
                if user.password == password:
                    return True
                else:
                    return False
    pass

    def show_credit_of_user(self, username, password):
        # 1. check user exists
        # 2. check username and password match
        # 3. find the user and show credit
        for user in self.users:
            if user.username == username:
                if user.password == password:
                    print(user.credit)
                else:
                    return False
    pass

    def add_user(self, username, password):
        # 1. check user does not exist
        # 2. create a new User(username, password)
        # 3. append the new user to self.users
        # 4. don't forget to save() !
        #if self.user_exists(username) == False:

            if self.user_exists(username) == False:


                new = User(username, password)
                self.users.append(new)
                self.save()
                print("user add successfully")




            pass

    def add_credit_to_user(self, money, username, password):
        # 1. check user exist
        # 2. search for the user
        # 3. add money to user.credit
        # 4. print new credit
        # 5. don't forget to save() !

        for user in self.users:
            if user.username == username:
                if user.password == password:
                    user.credit = money + user.credit
                    print("your credit is: ",user.credit)
                    self.save()
                else:
                    print("False")
                    return False

    pass

    def send_credit_from_user_to_user(self, money, username1, password1, username2):
        # 1. check user1 exists
        # 2. check user2 exists
        # 3. check username1 and password1 match
        # 4. check user1 has enough credit
        # 5. find user1 and user2
        # 6. send money from user1 to user2
        # 7. show user1 credit
        # 8. don't forget to save() !
        for user in self.users:
            for user2 in self.users:
                if user.username == username1:
                    if user.password == password1:
                        if user2.username == username2:
                            if (user.credit - money) > 0:
                                user.credit = user.credit - money
                                user2.credit = user2.credit + money
                                print("your money send successfully")
                                print("your credit is: ", user.credit)
                                self.save()
                                return True




        pass
