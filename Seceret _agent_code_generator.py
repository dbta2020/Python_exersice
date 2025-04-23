code1 = str(input("Enter a single word: "))
code2 = str(input("Enter a single word: "))
code3 = str(input("Enter a single word: "))
codes = [code1, code2, code3]
numA = int(input("Enter a number: "))
numB = int(input("Enter a number: "))
print("Your secret code is : " , code1, code2, code3, str(numA), str(numB))
if str(numA) in codes or str(numB) in codes:   
    print("invalid codeword")
    exit()
if numA < 1 or numB < 1:
    print("invalid numbers")
    exit()
