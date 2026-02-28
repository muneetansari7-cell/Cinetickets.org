import os
import datetime

money=0
ticket=0
default_movie = ""
print("CINETICKETS.org")

cus_name = input("enter your name :")
cus_age = int(input("enter your age :"))
while True:
    
    cus_gen = input("enter your gendre: M | F :")
    if cus_gen=="male" or cus_gen=="female" or cus_gen=="m" or cus_gen=="f":
        pass
        break
    else:
        print("Invailid Choice")
        
store=open("ppt.txt", "a")
store.write(f"{cus_name}:{cus_age}:{cus_gen}\n")
store.close()
print("Movies List :\n 1-Avengers: Doomsday = 550rs | 13+ \n 2-Spider-man: Brand New day = 550rs | 13+ \n 3-Outcome = 400rs | 17+ \n 4-Mortal KOmbat || = 400rs | 17+\n 5-Scream 7 = 400rs | 18+\n 6-The Hunger Games =400rs | 10+")

while True:
    movie = input("enter movie name that you want to watch or enter number of movie name in list :")
    if movie=="1" or movie=="avengers: doomsday":
        ticket = int(input("how many tickets you want? :"))
        money = ticket*550
        default_movie = "Avengers :Doomsday"
        break
    elif movie=="2" or movie=="spider-man: brand new day":
        ticket = int(input("how many tickets you want? :"))
        money = ticket*550
        default_movie = "Spider-man Brand New Day"
        break
    elif movie=="3" or movie== "outcome":
        ticket = int(input("how many tickets you want? :"))
        money = ticket*400
        default_movie = "Outcome"
        break
    elif movie=="4" or movie=="mortal kombat":
        ticket = int(input("how many tickets you want? :"))
        money = ticket*400
        default_movie = "Mortal Kombat"
        break
    elif movie=="5" or movie=="scream 7":
        ticket = int(input("how many tickets you want? :"))
        money = ticket*400
        default_movie = "Scream 7"
        break
    elif movie=="6" or movie=="the hunger games":
        ticket = int(input("how many tickets you want? :"))
        money = ticket*400
        default_movie = "The Hunger Games"
        break
    else:
        print("choose vailid movie")

while True:
    payment = input(f"which payment method do you want cash or upi? your total is {money} : ").strip().lower()
    if payment == "upi":
        import qrcode
        img = qrcode.make(f"upi://pay?pa=9927972990@ptsbi&pn=MOHD%20MUNEER&am={money}&tn=Payment")
        img.save(f"{cus_name}.png")
        print("QR code generated")
        break
    elif payment == "cash":
        print("ok sir")
        break
    else:
        print("pls choose valid option")

if cus_gen=="male" or cus_gen=="m" or cus_gen=="female" or cus_gen=="f":
    print(f"Hello! Mr. {cus_name} Here's your Invoice")

print("---------------------CINETICKETS.org----------------------")
print("-------------------------INVOICE--------------------------")
print(" MOVIE                                       TICKET QTY")
print("="*59)
print(f"{default_movie}               :                 {ticket}")
print("="*59)
print(f"Total Price-{money}")
print("*"*59)
print(f"Payment Recieved By {payment}")
print("*"*59)
print("\t\t   Thankyou for your Time")
print("="*59)
print(datetime.datetime.now())
