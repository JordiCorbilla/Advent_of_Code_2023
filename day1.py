def convert_spelled_numbers(text):
    result = []
    current_word = ''

    for char in text:
        if char.isalpha():
            current_word += char
            if current_word.__contains__('one') or current_word.__contains__('two') or \
                    current_word.__contains__('three') or current_word.__contains__('four') or \
                    current_word.__contains__('five') or current_word.__contains__('six') or \
                    current_word.__contains__('seven') or current_word.__contains__('eight') or \
                    current_word.__contains__('nine'):
                result.append(str(convert_to_number(current_word)))
                current_word = ''
        else:
            if current_word:
                result.append(str(convert_to_number(current_word)))
                current_word = ''
            result.append(char)

    # Handle the case where the last part of the string is a spelled-out number
    if current_word:
        result.append(str(convert_to_number(current_word)))

    return ''.join(result)


def convert_to_number(value):
    # Convert spelled-out numbers to their corresponding digits
    number_mapping = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
        'nine': 9
    }

    num = value.replace('one', '1')
    num = num.replace('two', '2')
    num = num.replace('three', '3')
    num = num.replace('four', '4')
    num = num.replace('five', '5')
    num = num.replace('six', '6')
    num = num.replace('seven', '7')
    num = num.replace('eight', '8')
    num = num.replace('nine', '9')

    return num


# Example usage:
input_text = "knmzhbvhzfvrbkvsmnl7sixseven"  # "eightwone"
output_text = convert_spelled_numbers(input_text)
print(output_text)  # Output: "8w1"
