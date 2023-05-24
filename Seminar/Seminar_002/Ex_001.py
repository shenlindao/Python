count = 0 
max = 0

n = int(input("Input a quantity of days: "))

for dayCount in range(n) :
    day = int(input("Input a temperature of days: "))
    if day > 0 :
        count += 1
    else :
        if count >= max :
            max = count
            count = 0

if count > max :
    max = count

print("Max quantity of warm days is ", max)