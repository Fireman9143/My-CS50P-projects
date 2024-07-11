import inflect
import datetime
import sys

p = inflect.engine()

def main():
    try:
        answer=(convert_time(birthday(input("What's your birthday?: "))))
        print(p.number_to_words(answer, andword=""))
    except ValueError:
        sys.exit("Invalid format")
    

def birthday(date):
    birth_year, birth_month, birth_day = date.split("-")
    birth_year=int(birth_year)
    birth_month=int(birth_month)
    birth_day=int(birth_day)
    return datetime.date(birth_year, birth_month, birth_day) 
    

def convert_time(birth):
    today = datetime.date.today()
    #today = datetime.date(2000, 1, 1)
    age_days = today - birth
    return age_days.days*24*60
    

if __name__ == "__main__":
    main()

"""Type a date one year ago from today, in the specified format. 
Your program should sing print Five hundred twenty-five thousand, six hundred minutes.
Type a date two years ago from today, in the specified format. 
Your program should print One million, fifty-one thousand, two hundred minutes.
Type a date of your choice, but this time use an invalid format. 
Press Enter and your program should exit using sys.exit without raising an Exception."""