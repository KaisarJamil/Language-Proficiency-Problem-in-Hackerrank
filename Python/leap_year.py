# write a function to check if the year is leap or not.


def is_leap(year):
    leap = False

    if year%4==0 and year%100 !=0:
        leap=True
    elif year%400==0 :
        leap=True
    else :
        leap=False

    return leap
