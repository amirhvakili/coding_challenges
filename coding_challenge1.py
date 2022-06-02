# Accept a list of 5 float numbers as an input
# from the user

numbers = []

for i in range(1, 6):
    while True:
        try:
            num = float(input(f"Please insert input number {i}: "))
            num_refined = "{:.1f}".format(num)
            numbers.append(num_refined)

        except:
            print("Please only insert numbers")
            continue
        break


print(numbers)
