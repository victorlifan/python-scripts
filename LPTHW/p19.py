def income_oct(invest, transfer, clothing, grocery):
    total = invest + transfer + clothing + grocery
    print(f"total income of Oct is {total}.")
    print(f"{invest} from investment.")
    print(f"{transfer} from bank transfer.")
    print(f"{clothing} from cloth refund.")
    print(f"and {grocery} from grocery refund.\n")

print("1st way run it")
income_oct(10195.95, 6000, 793.55, 212)


print("2nd way run it")
investment= 10000+195.95
clothes = 700 + 93.55
income_oct(investment, 6000, clothes, 212)


print("3rd way run it")
income_oct(10000+195.95, 6000, 700+93.55,212)

print("4th way to run it")
half_tranfer = 3000
half_clothing = 106
income_oct(investment,half_tranfer+3000,clothes,half_clothing+106)

print("5th way to run it")
print("how much did you get from investment?")
prompt = "|"
input_investment = input(prompt)
print("how much did you get from transfer?")
input_tranfer = input(prompt)
print("how about clothing?")
input_clothing = input(prompt)
print("and grocery?")
inpuit_grocery = input(prompt)
income_oct(input_investment,input_tranfer,input_clothing,inpuit_grocery)

print("6th")
x = income_oct
x (10195.95,6000,793.55,212)

print("7th")
