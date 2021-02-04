def days_in_year(year) :
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year%400 == 0 :
        days[1] += 1 ## Leap year
    elif year%100 != 0 and year%4 == 0 :
        days[1] += 1
    return days

if __name__ == '__main__' :
    ## 1901/01/01 is Tuesday
    ## So if the remainder of the cumulative number divided by 7 is 0, the first of the next month is Tuesday
    ## If the remainder is 5, the first of the next month is Sunday
    total_days = []
    for y in range(1901, 2001) :
        total_days += days_in_year(y)
    print([sum(total_days[:i+1])%7 for i in range(len(total_days))].count(5))
    
        