from calendar import month
from datetime import date


def get_dob():
	y = input("Enter year of birth:")
	m = input("Enter month of birth:")
	d = input("Enter day of birth:")
	return date(int(y), int(m), int(d))




def get_age(d):
    today = date.today()
    diff = today - d
    return diff.days // 365


def main():
    d = get_dob()
    age = get_age(d)
    print(f"You are {age} year(s) old!")


if __name__ == '__main__':
    main()
