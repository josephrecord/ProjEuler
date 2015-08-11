one_thr_twnty = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'\
'ten', 'eleven', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', \
'twenty']
tens = ['thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hun = 'hundred'
thou = 'thousand'

letters = 0

for i in range(0, len(one_thr_twnty)):
	letters = letters + len(one_thr_twnty[i])
	print(one_thr_twnty[i])
	print(letters)
	
for i in range(0, len(tens)):
	for j in range(0, 8):
		if j == 0:
			letters = letters + len(tens[i])
			print(tens[i])
			print(letters)
		letters = letters + len(tens[i]) + len(one_thr_twnty[j])
		print(tens[i] + " " + one_thr_twnty[j])
		print(letters)