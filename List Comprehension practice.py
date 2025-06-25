num = int(input("Enter a number: "))

odd_list = [i for i in range(num) if i % 2 != 0]

odd_squares = [i**2 for i in range(num) if i % 2 != 0]

print("Odd numbers:", odd_list)
print("Squares of odd numbers:", odd_squares)


fruits = ['apple', 'banana', 'mango', 'grape', 'orange']

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Updated list:", capitalized_fruits)
