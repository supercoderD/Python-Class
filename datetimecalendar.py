from datetime import date, time, datetime
today=date.today()
now=datetime.now()
print("Today's date is ", today)
print("\nCurrent Date and time is", now)

print("\nDate components", today.year, today.month, today.day)




from datetime import date

birthyear=int(input("Enter the birth year: "))
birthmonth=int(input("Enter the birth month: "))
birthday=int(input("Enter the birth day: "))

birthdate=date(birthyear, birthmonth, birthday)
today=date.today()
age=today.year-birthdate.year
if (today.month, today.day)<(birthdate.month, birthdate.day):
    age-=1
if (today.month, today.day)>(birthdate.month, birthdate.day):
    print("The values is invalid.")



print("The age is", age)


def hotelcost(night):
    return 140*night
def planeridecost(city):
    if "Paris"==city:
        return 109
    elif "Mumbai"==city:
        return 1900
    elif "NYC"==city:
        return 50
    elif"Moscow"==city:
        return 1750
def rentalcarcost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days
def tripcost(city,days,spendingmoney):
    return rentalcarcost(days) + hotelcost(days) + planeridecost(city) + spendingmoney

print("Cost of car rental: ", rentalcarcost(5))
print("Cost of plane ride:", planeridecost("NYC"))
print("cost of hotel room",hotelcost(7))
print("Total cost of the trip:",tripcost("NYC", 7,500))


    





