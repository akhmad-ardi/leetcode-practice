def romanToInt(s: str):
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    input = list(s)
    result = 0

    for i in range(len(input)):
        if i + 1 < len(input) and symbols[input[i]] < symbols[input[i + 1]]:
            result -= symbols[input[i]]
        else:
            result += symbols[input[i]]
    
    return result

print(romanToInt("III")) # 3
print(romanToInt("LVIII")) # 58
print(romanToInt("MCMXCIV")) # 3