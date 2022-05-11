# # class BasePasswordManager
# #     members
# #         old_passwords: is a list that holds all of the user's past
# #                            passwords.
# #                            The last item of the list is the user's current password.
# #     methods
# #         get_password method that returns the current password as a string.
# #         is_correct method that receives a string and returns a boolean
# #              True or False depending on whether the string is equal to
# #              the current password or not.

# # class PasswordManager
# #     This class inherits from BasePasswordManager
# #         methods
# #         set_password method that sets the user's password.
# #              Password change is successful only if:
# #                     - Security level of the new password is greater.
# #                     - Length of new password is minimum 6

# #              However, if the old password already has the highest security level,
# #              new password must be of the highest security level for a successful password change.

# #         get_level method that returns the security level of the current password.
# #              It can also check and return the security level of a new password passed as a string.

# # Security levels:
# #          level 0 - password consists of alphabets or numbers only.
# #          level 1 - Alphanumeric passwords.
# #          level 2 - Alphanumeric passwords with special characters.


import re
import msvcrt


class BasePasswordManager:
    old_passwords = ['abcd', 'abc!123']

    def get_password(self):
        try:
            self.old_passwords[-1]
            return self.old_passwords[-1]
        except IndexError:
            print("Error")
            return -1

    def is_correct(self, password):
        return password == self.get_password()


class PasswordManager(BasePasswordManager):
    def set_password(self, new_password):
        oldPass = BasePasswordManager.get_password(self)
        oldLevel = self.get_Level(oldPass)
        newLevel = self.get_Level(new_password)

        if len(new_password) >= 6 and newLevel == 2:
            if (new_password is not self.old_passwords[-1]):
                self.old_passwords.append(new_password)
                print("Password Set Successfully.")
            else:
                print("Cannot use previous password.")

        elif newLevel > oldLevel and len(new_password) >= 6:
            print('Password Set Successfully')
        else:
            print(
                "Security Level of new password is lower than pervious password or length is less than 6")

    def get_Level(self, new_password):
        level = 0
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        regex1 = re.compile("[a-zA-Z]")
        if new_password.isnumeric() or new_password.isalpha():
            level = 0
        elif new_password.isalnum():
            level = 1
        elif re.search(r'\d', new_password) != None and regex.search(new_password) != None and regex1.search(new_password) != None:
            level = 2
        elif regex.search(new_password) != None and regex1.search(new_password) != None:
            level = 1
        elif regex.search(new_password) != None and re.search(r'\d', new_password) != None:
            level = 1
        return level


pm = PasswordManager()

password = ''
password = input("Enter the password: ")
flag = True
flag = pm.is_correct(password)
if flag == True:
    print("Entered password is correct.")
else:
    print("Entered password is wrong. Exiting....")
    exit()

setNewPass = ''
passwordCheck = ''
toExit = ''
print("Want to change password press 'Y' for yes or 'N' for no. ")
setNewPass = input("Y/N ?: ")
if setNewPass == 'Y':
    new_pass = ''
    new_pass = input("Enter new password: ")
    pm.set_password(new_pass)

    print("Want to check password security level press 'Y' for yes or 'N' or no. ")
    passwordCheck = input("Y/N ?: ")
    if passwordCheck == 'Y':
        print("Level : ", pm.get_Level(pm.get_password()))

    print("Press any key to EXIT.")
    msvcrt.getch()
    exit()

elif setNewPass == 'N':
    print("Want to check password security level press 'Y' for yes or 'N' or no. ")
    passwordCheck = input("Y/N ?: ")
    if passwordCheck == 'Y':
        print("Level : ", pm.get_Level(pm.get_password()))

    print("Press any key to EXIT.")
    msvcrt.getch()
    exit()
