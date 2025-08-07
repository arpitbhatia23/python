leap_year=int(input("enter and year:"))

calculate_leap=leap_year%400==0 or leap_year%4==0 and  leap_year%100!=0


if calculate_leap:
    print(f"{leap_year} is a leap year")
else:
    print(f"{leap_year} is not a leap year")