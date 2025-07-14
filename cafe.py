import pyttsx3
engine = pyttsx3.init()
engine.say("heyyy! WElcome to my cafe!    What do you want to order? ") 
engine.runAndWait()


print("\n      What do you want to order?😊🥤🧁")
menu={
    "Tea":10,
    "Coffee":50,
    "Cake":20,
    "Water":10,
    "Juice":20
}
for i,p in menu.items():
    print(f"{i.title()} - Rs.{p}")
 #print(f"{i}--------{menu[i]}")
print("\nEnter your order by name and Write---'Done'---- for total bill\n")

total=0
orders={}
while True:
    a = input("Enter order: ").strip().title()
    if a in menu:
        qty = int(input(f"How many {a}s do you want? "))
        total += menu.get(a) * qty 
        orders[a] = orders.get(a, 0) + qty
    elif(a=="Done".title()):
        break
    else:
        print("You enter something wrong!\n Order from Menu😊")

print("\n🧾 Your Receipt:")
for item, q in orders.items():
    print(f"{item} x {q} = Rs.{menu[item]*q}")
print(f"\nTotal Bill: ${total}🙏")



    
