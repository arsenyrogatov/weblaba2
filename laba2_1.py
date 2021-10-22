def palindrome(num):
	isNeg = num < 0
	if isNeg:
		num *= -1
	n = num
	rev = 0
	while num > 0:
		dig = num % 10
		rev = rev * 10 + dig
		num =  num // 10
	return rev == n

print (palindrome(int(input("Введите число: "))))