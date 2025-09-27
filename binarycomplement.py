def binary_complement(binary_string: str) -> str:
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
    user_input = input("Enter a binary string: ")
    output = binary_complement(user_input)
    print(f"Complement: {output}")
