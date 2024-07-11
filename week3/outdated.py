def main():
    while True:
        try:
            date = input("Date: ")
            if convert(date):
                print(convert(date))            
                break
            else:
                raise ValueError
        except ValueError:
            pass


def convert(text):
    months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    if "/" in text:
        month, day, year = text.split("/")
    elif " " in text:
        month, day, year = text.split(" ")
        day = day.rstrip(",")
    try:
        if month.title() in months:
            month = months.index(month) +1
        else:
            month = int(month)
    except ValueError:
        return False
    day = int(day)
    year = int(year)
    if month in range(1,13) and day in range(1,32):
        return f"{year}-{month:02}-{day:02}"
    else:
        return False
    

if __name__ == "__main__":
    main()  

"""Run your program with python outdated.py. Type 9/8/1636 and press Enter. Your program should output:
1636-09-08
Run your program with python outdated.py. Type September 8, 1636 and press Enter. Your program should output:
1636-09-08
Run your program with python outdated.py. Type 23/6/1912 and press Enter. Your program should reprompt the user.
Run your program with python outdated.py. Type December 80, 1980 and press Enter. Your program should reprompt the user."""