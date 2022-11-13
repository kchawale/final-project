from ast import Delete


class menu:
    def __init__(self,food_id):
        self.food_id = food_id
        self.food_items = {}
        
    def dishes(self):
        food_id=0
        
        while food_id <5:
          
            food_id=int(input("enter food_id : "))
            if food_id==1:
                print(["pizza", 1, 300, 10, 4])
            elif food_id==2:
                print(["vegan burger", 2,100, 5 ,8])
            elif food_id==3:
                print(["Truffle cake", 2, 200, 10 , 10])
            elif food_id==4:
                print(["fries", "250", 100,10,"1"])
            elif food_id==5:
                print("we serve drinks as well")
            else:
                print("enter new dish name: ")
                print("enter quantity: ")
                print("enter price of the dish: ")
                print("dish discount: ")
                print("in stock: ")    
        print()
                
    def edit_food(self):
        food_food = int(input("Enter the new food_id: "))
        name = str(input("Name of new item to be added : ")) 
        quantity= int/float/str(input("Enter the quantity : "))
        price = int(input("enter the price: "))

        order = self.food_id

        option = int(input(f"Your added food is {food_food}  ,If want to add \n1.Yes \n.2.No \n"))
        if option == 1:
            name = input("Enter dish name : ")
            price = input("Enter dish price: ")
            added_item=str(name)+str(price)
            
            self.food_items[added_item] = [name,price]
            
            print("added Successfully!")
            print(self.order)
        else:
            print("Add next time!!!")
            
    def total_item(self):
        total_list = self.order.get(added_item,None)
        
        if total_list:
            print(f"Name : {total_list[0]} \nprice : {total_list[1]} ")
        else:
            print(f"No item to display Booked ")
            
    def deitem(self):
        de_item=Delete(food_id,None)
        if de_item:
            print("removed")
        else:
            print("no change")
