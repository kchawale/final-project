import random
class Login:
    error = None
    def __init__(self, uid, passw):
        self.uid = "admin"
        self.passw = "admin"
        Login.error = "Enter a valid user id and password"

    def authenticate(self):
        if (self.uid == logid and self.passw == logpass):
            print ("Login successful")
        else:
            print (Login.error)
log = Login("", "")
logid = input("Enter your user ID: ")
logpass = input("Enter your password: ")


log.authenticate()

from adminexecution import menu
class Main:
    def execute(self,choice):
        if choice == 1:
            print("*******Show the foodlist*******")
            menu_obj.dishes()
        if choice == 2:
            print("*******edit food list*******")
            menu_obj.edit_food()
        if choice == 3:
            
            print("*******foodlist with new items*******")
            menu_obj.total_item()
        if choice == 4:
            
            print("*******delete item*******")
            menu_obj.deitem()
        if choice == 0:
            pass
            print("*******Thank You*******")
            exit()


if __name__ == "__main__":
    food_id = int(input("enter food_id: "))
    menu_obj = menu(food_id)
    obj = Main()
    while True:
        choice = int(input("Enter \n1.show the food list \n2.edit food list \n3.new food list \n4.remove items\n0.Exit : \n"))    
        obj.execute(choice)