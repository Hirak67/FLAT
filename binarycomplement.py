def binary_complement(binary_string):
    result = []
    for ch in binary_string:
        if ch == "0":
            result.append("1")
        elif ch == "1":
            result.append("0")
        else:
            result.append(ch) 
    return "".join(result)

if __name__ == "__main__":
    myinput = input("Enter a binary string: ")
    output = binary_complement(myinput)
    print(f"Complement: {output}")
