prefixes = [616,454,659]
def is_valid_code(code):
    if len(code) == 8:
        code = "00" + code
    elif len(code) == 9:
        code = "0" + code
    elif len(code) == 10:
        x = [int(code[i]) * (10 - i) for i in range(9)]
        end = sum(x) % 11
        if end == int(code[9]) or (11 - end) % 11 == int(code[9]):
            return True
        else:
            return False
    else:
        return False

def generate_valid_codes(prefixes, num_codes):
    valid_codes = []
    for prefix in prefixes:
        for i in range(10000000):
            code = str(prefix) + '{:07}'.format(i)
            if is_valid_code(code):
                valid_codes.append(code)
                if len(valid_codes) == num_codes:
                    return valid_codes
    return valid_codes

user_input = input("Enter 'all' to generate all valid codes or enter the number of codes to generate: ")
if user_input.isdigit():
    num_codes = int(user_input)
    codes = generate_valid_codes(prefixes, num_codes)
    print("Generated codes:")
    for code in codes:
        print(code)
elif user_input.lower() == 'all':
    codes = generate_valid_codes(prefixes, float('inf'))
    # Writing all valid codes to a text file
    with open("all_valid_codes.txt", "w") as file:
        for code in codes:
            file.write(code + "\n")
    print("All valid codes written to all_valid_codes.txt")
else:
    print("Invalid input. Please enter 'all' or a number.")
