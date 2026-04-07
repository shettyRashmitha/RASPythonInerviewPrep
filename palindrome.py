'''
check number is palindrome, if yes stop
if not add the original and reversed check result is palindrme continue till 10 iteration
then return-1
'''
def check_palindrome(given_number):
    is_palindrome=False
    for i in range(10):
        reversed_number=given_number[::-1]
        if given_number == reversed_number:
            print("The number entered is palindrome:" ,given_number)
            is_palindrome=True
            break
        else:
           given_number= str(int(given_number)+int(reversed_number))
    return is_palindrome   


given_number=input("Enter a number: ")
is_palindrome=check_palindrome(given_number)
if is_palindrome == False:
    print("-1")