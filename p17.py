# one_thr_twnty = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'\
# 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', \
# 'twenty']
# tens = ['thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
# hun = 'hundred'
# thou = 'thousand'

# letters = 0

# for i in range(0, len(one_thr_twnty)):
# 	letters = letters + len(one_thr_twnty[i])
# 	print(one_thr_twnty[i])
# 	print(letters)
	
# for i in range(0, len(tens)):
# 	for j in range(0, 8):
# 		if j == 0:
# 			letters = letters + len(tens[i])
# 			print(tens[i])
# 			print(letters)
# 		letters = letters + len(tens[i]) + len(one_thr_twnty[j])
# 		print(tens[i] + " " + one_thr_twnty[j])
# 		print(letters)

# nums = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, \
# 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, \
# 'fourteen':14,'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, \
# 'nineteen':19, 'twenty':20}

s = 0

one_thr_twnty = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', \
'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', \
'seventeen', 'eighteen', 'nineteen', 'twenty']

teens = ['thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

for i in range(0, len(one_thr_twnty)):
	s = s + len(one_thr_twnty[i])
	print(one_thr_twnty[i], s)


for j in range(0, len(teens)):
	for i in range(0, 9):
		s = s + len(teens[j]) + len(one_thr_twnty[i])
		print(teens[j] + ' ' + one_thr_twnty[i], s)

n = s + (100*13+s) + (100*13+s) + (100*15+s)+(100*14+s)+(100*14+s)+(100*13+s)+(100*15+s)+(100*15+s)+(100*14+s) + 3 + 8
print(n)