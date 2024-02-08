
dict = {}
while True:
    try:
        user_input = input("")
        if user_input not in dict:
            dict[user_input] = 1
        else:
            dict[user_input] = dict[user_input] + 1
    except EOFError:        
    alpha = sorted(dict.keys())
    for key in alpha:
        value = dict[key]        
        print(value, key.upper())
    break
