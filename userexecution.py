class dashboard:
    def __init__(self,option,food_id):
        self.option = option
        self.food_id = food_id
        self.user_profile = {}
        
    
    def option1(self):
        
        food_id=0
        
        while food_id <3:
          
            food_id=int(input("pick an option: "))
            if food_id==1:
                print("Tandoori Chicken" ,"4 pieces", "INR 240")
            elif food_id==2:
                print("Vegan Burger", "1 Piece", "INR 320")
            elif food_id==3:
                print("Truffle Cake", "500g" ,"INR 900")
           
            else:
                print("enter new dish to order: ")
                print("enter quantity: ")
                
    def displaymenu(self):
        self.displaymenu
        print("Tandoori Chicken ,4 pieces, INR 240", "\nVegan Burger, 1 Piece, INR 320" , "\nTruffle Cake", "500g" ,"INR 900") 
              
                  
        print()
