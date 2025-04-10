import random
while True:
    computer_choice=random.randint(1,100)
    num=int(input("Enter any number betwwen 1 and 100"))
    while True:
        if(num>computer_choice):
            print("you entered high number")
            cont = input("Do you want to continue? (Y/N): ").strip().lower()
            if cont != 'y':
                break
            else:
                num=int(input("Enter Again "))
        elif (num<computer_choice):
            print("you entered too less")
            cont = input("Do you want to continue? (Y/N): ").strip().lower()
            if cont != 'y':
                break
            else:
                num=int(input("Enter Again "))
        else:
            print("congrulations!!you won")
            break
    cont = input("Do you want to continue? (Y/N): ").strip().lower()
    if cont != 'y':
        break
        
        
        
        