def check_leap(n):
        # n is an int representing the year
	if n%4 == 0:
		if n%100 == 0 and n%400 != 0:
			return False
		return True
	else:
		return False

def check_num_days(date):
	# check num of days in month where n is list of date
	if date[1] == 1 or date[1] == 3 or date[1] == 5 or date[1] == 7 or date[1] == 8 or date[1] == 10 or date[1] == 12:
		days = 31
	elif date[1] == 4 or date[1] == 6 or date[1] == 9 or date[1] == 11:
		days = 30
	elif date[1] == 2 and check_leap(date[2]) == False:
		days = 28
	elif date[1] == 2 and check_leap(date[2]) == True:
		days = 29
	return days


def inc_day(date):
	num_days = check_num_days(date)
	if date[0] == num_days:
		date[0] = 1
		inc_mon(date)
	else:
		date[0] = date[0] + 1
	return date

def inc_mon(date):
	if date[1] == 12:
		date[1] = 1
		inc_year(date)
	else:
		date[1] = date[1] + 1
	return date

def inc_year(date):
	date[2] = date[2] + 1
	return date

def count_days(start, end):
	count = 1
	while start != end:
		inc_day(start)
		count = count + 1
	return count

def inc_dow(start):
	if start == 'sun':
		return 'mon'
	elif start == 'mon':
		return 'tue'
	elif start == 'tue':
		return 'wed'
	elif start == 'wed':
		return 'thr'
	elif start == 'thr':
		return 'fri'
	elif start == 'fri':
		return 'sat'
	elif start == 'sat':
		return 'sun'

date = [1, 1, 1901]
dow = 'tue'
suns = 0

tot_days = count_days([1, 1, 1901], [31, 12, 2000])

for i in range(0, tot_days):
	# print(date, dow)
	if date[0] == 1 and dow == 'sun':
		suns = suns + 1
	inc_day(date)
	dow = inc_dow(dow)

print(suns)