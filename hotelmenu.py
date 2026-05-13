#define menu of restaurant
menu={"Pizza":180,
      "Coffee":40,
      "Masala Dosa":60,
      "Faluda":80,
      "Tea":20,
      "Burger":50,
      }
print(menu)
print("Welcome to Menu Restaurant")
print("Pizza: Rs180\nCoffee: Rs40\nMasala Dosa: Rs60\nFaluda: Rs80\nTea: Rs20\nBurger: Rs50")
order_total=0
item_1=input("Enter the name of item you want = ")
if item_1 in menu:
    order_total +=menu[item_1]
    print("your item ",{item_1}," has been added to your order")
else:
    print("Ordered item", {item_1} ,"is not available yet!")

another_order=input("Do you want to order something else? (Yes/No) ")
if another_order=="Yes":
    item_2 =input("Enter the name of second item =")
    if item_2 in menu:
        order_total+=menu[item_2]
        print("Item", {item_2} ,"is added to your order")
    else:
        print("Ordered item", {item_2}," is not available! you can order something else from menu")
print("the total amount of items is ",{order_total}) 
print("hope you enjoy it,Have a good day!")      
