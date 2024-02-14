from datetime import datetime, date
import sys
import inflect

p = inflect.engine()

def main():
    user_date = input("Date of Birth: ")
    if check_date(user_date) is True:
        print(calculate_mins(user_date))

def check_date(n):
    if len(n.split("-")) == 3:
        year, month, day = n.split("-")
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            if year.isnumeric() and len(year) == 4 and month.isnumeric() and len(month) == 2 or 1 and day.isnumeric() and len(day) == 2 or 1:
                return True
            else:
                sys.exit("Not valid date")
        else:
            sys.exit("Not valid date")
    else:
        sys.exit("Not valid date")

def calculate_mins(raw_date):
    format_date = datetime.strptime(raw_date, "%Y-%m-%d").date()
    today = date.today()
    days = (today - format_date).days
    minutes = days*24*60
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()
