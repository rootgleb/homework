def check_palindrom(text):
    for i in range(len(text) // 2):
        if text[i] != text[-i - 1]:
            return False
    return True


print(check_palindrom(input()))
