import random

num = random.randrange(0,30)
stevilo_poskusov = 0 

while stevilo_poskusov < 5: 
    poskus = input("vnesi stevilo:")
    poskus = int(poskus)
    if num == poskus:
        print("Zmaga")
        break
    elif poskus< num:
        print("Premajhno število")
    else:
        print("Preveliko število")
    stevilo_poskusov= stevilo_poskusov+1
    
