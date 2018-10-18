def mutate_string(string, position, character):
    for i in range(0, len(string)):
        if i == position:
            string[i] = character
    return string

s = input()
position = int(input())
character = input()
mutate_string(s, position, character)