flag = True
while flag:
    wanna = input("If you want to use the program enter y or n to quit") 
    wanna = wanna.lower()  
    if wanna == "y" :
        current = input("Please input the money in <150-type> form ")
        current = current.upper()
        my_list = current.split("-")
        my_num = int(my_list[0])
        my_type = my_list[1]
        result ="Not found"
        if my_type == "SAR":
            result = my_num*4.25
        elif my_type == "USD":
            result = my_num*15.7 
        elif my_type == "GBP":
            result = my_num*21.4
        elif my_type == "ERU":
            result = my_num*17.8    

        print (f"The money in L.E is {result}")
    else:
        print("Bye!!")   
        break; 