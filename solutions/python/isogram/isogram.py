def is_isogram(string):
    alpha_string = ''.join(filter(str.isalpha, string))
    return len(set(alpha_string.lower())) == len(alpha_string)
