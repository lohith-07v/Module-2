n = int(input("Enter a number: "))
temp = n
rev = 0

while temp > 0:
    rev = (10 * rev) + temp % 10
    temp = temp // 10

if rev == n:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")