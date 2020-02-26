def x(a,b,c,d):
    return a + b + c + d

print("type in a, b, c, d")
a_type = float(input())
b_type = float(input())
c_type = float(input())
d_type = float(input())
total_income= x(a_type, b_type, c_type, d_type)
print("total income is", int(total_income))

def y(e,f):
    return e - f

print("total expense is")
f_type = float(input())
balance = y(total_income, f_type)
print("so balance will be")
print(f"{total_income} - {f_type} = {balance}")

def multiply(g,h):
    return g * h
print(multiply(18,35))
