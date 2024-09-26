import math

def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b != 0:
        return a / b
    else:
        return "Lỗi: Không thể chia cho 0"
    
def sqrt(a):
    if a >= 0:
        return math.sqrt(a)
    else: return
