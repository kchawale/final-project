users={}
status=""
def status():
  status=input("are u registered: y/n? press q to quit:")
  if status=="y":
    olduser()
  else:
    register()

def olduser():
  id=input("entr id: ")
  pswd=input("enter pswd: ")
  if id==pswd:
    print("\nlogin succesful")
  else:
    print("\nuser not exists")

def register():
    name= input("enter name:")
    mobile=input("enter mobile:")
    email=input("enter email:")
    address=input("enter address: ")
print("user ceated")

if id in users:
  print("\nuser already exist") 
else:
  pass


status()


from userexecution import dashboard
class Main:
    def displaymenu(self,choice):
        if choice == 1:
            print("*******display the menu*******")
            dashboard_obj.displaymenu()
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
  option1 = int(input("option1: "))
  dashboard_obj = dashboard(option1,food_id="")
  obj = ()
  while True:
        choice = int(input("Enter \n1.displaymenu \n2.place new order \n3.order history \n4.update prifile \n0.Exit : \n"))    
        obj.execute(choice)


