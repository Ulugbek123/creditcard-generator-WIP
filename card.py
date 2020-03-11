from random import randint


def single_num(prompt):
    num = ""
    while True:
        num = input(prompt)

        if len(num) == 16:
            try:
                return int(num)
            except ValueError:
                print()
        else:
            print("Credit card digit number is not valid, Please re-enter 16 digits")


def Vendor(Verifer):
    # Calls the define as Vendor
    num = '2221-2720'  # Mastercard
    num2 = '6150-6500'  # Visa Credit
    num3 = '5000-5500'  # Discovery
    num4 = '1500-1700'  # American Express


def Checksum(Verifer):
    # Calls the define as Checksum
    CheckNum = '0,1,2,3,4,5,6,7,8,9'


from random import randint


def Generate(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


print(Generate(16))

somecard = input('Choose 1 to Verify, 2 to Vendor, 3 to Checksum, 4 to Generate: ')
if somecard == '1':
    string = (input('Enter Credit Card Number to see if its valid: '))
    single_num(int)
    # Take a credit card number as input and output if it is a valid or invalid credit card number.

if somecard == '2':
    string = (input('Enter Credit Card Number to see its issuing vendor: '))
    Vendor(int)
    # Again take a credit card number as input and output the issuing vendor

if somecard == '3':
    string = (input('Enter the first 4 digit of your Credit card to calculate the checksum: '))
    Checksum(int)
    # (Calculate last four digits

if somecard == '4':
    string = (input('Select the vendor to generate random valid Credit card: '))
    Generate(int)
    # Select the issuing vendor from a list, then generate a random valid credit card for that vendor.

print(somecard)
