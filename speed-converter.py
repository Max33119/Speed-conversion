print("This program will translate kilometers to miles and vice versa\n")
loop = True
while loop == True:
    MorKM = input("Please select either miles or kilometers to convert from (type done to end program): ").lower()

    # finds out if the variable works 
    if MorKM == "miles" or MorKM == "kilometers":
        amount = int(input("please type out the distance: "))

    #does calculations or ends program
    if MorKM == "miles":
        result = amount / 0.621371
        print(result)
    elif MorKM == "kilometers":
        result = amount * 0.621371
        print(result) 
        
    elif MorKM == "done":
        print("Done")
        loop = False
    else:
        print("please input a valid response")
