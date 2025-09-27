digit_to_word = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}
def digit_to_word_fst(input_string):
    output = []
    for ch in input_string:
        if ch in digit_to_word:      
            output.append(digit_to_word[ch])
        else:                         
            output.append(ch)
    
    return " ".join(output)

if __name__ == "__main__":
    user_input = input("Enter a number or a string with digits: ")
    print("Output:", digit_to_word_fst(user_input))
