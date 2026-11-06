# Эта функция переворачивает переданную строку
def reverse(string):
    return string[::-1]

def reverse_from_file(filename):
    with open(filename, "r") as f:
        content = f.read()
    return reverse(content)

def reverse_to_file(string, filename):
    reversed_string = reverse(string)
    with open(filename, "w") as f:
        f.write(reversed_string)