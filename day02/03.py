money = 5,000,000
print(money)
print(type(money)) #tuple
money=5_000_000
print(money)
print(type(money)) #int
print()

base_num = int(input('Enter base number: '))
expoent_num = int(input('Enter expoent number: '))
print(f'result : {base_num ** expoent_num}')
print("result : {}".format(base_num ** expoent_num))
print("result : %d " % (base_num ** expoent_num))

print(divmod(9, 5))
print(ord('a'))

def temperature(temp):
    result = (temp - 32) * 5 / 9
    return result
print("{:.4f}".format(temperature(100))) #화씨 -> 섮씨
print(f'{temperature(100):.4f}')
