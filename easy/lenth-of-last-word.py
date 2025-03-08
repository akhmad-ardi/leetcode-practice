def length_of_last_word(s: str) -> int:
    new_s = [] 
    s = s.split(" ")
    
    for word in s:
        if word: 
            new_s.append(word)

    return len(new_s[len(new_s) - 1])

case1 = "Hello World"
case2 = "   fly me   to   the moon  "
case3 = "luffy is still joyboy"

print(length_of_last_word(case1))
print(length_of_last_word(case2))
print(length_of_last_word(case3))