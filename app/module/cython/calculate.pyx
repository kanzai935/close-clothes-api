c = 0
def add(a, b):
    global c
    c = a + b
    return c

def print_result():
    print(c)
