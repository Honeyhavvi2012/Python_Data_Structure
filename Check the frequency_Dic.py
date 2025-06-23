test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print("Test Dictionary:", test_dict)

while True:
    val = input("Enter a number to check its frequency (or type 'exit' to stop): ")
    
    if val == 'exit':
        print("Goodbye!")
        break

    if val.isdigit():
        val = int(val)
        freq = list(test_dict.values()).count(val)
        print("Frequency of", val, "is:", freq)
    else:
        print("Please enter a number or 'exit'")
