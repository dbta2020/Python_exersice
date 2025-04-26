#Numbers Divisible by 3
start_num = int(input("Enter a start number: "))
end_num = int(input("Enter an end number: "))
#Since they want to count the numbers divisible by 3:
counter_divisible = 0
for start_num in range (end_num):
    if start_num % 3 == 0:
        print(start_num, "is divisible by 3")
        counter_divisible += 1
print("The total numbers divisible by 3 are: ", counter_divisible)
