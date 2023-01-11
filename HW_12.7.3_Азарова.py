per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
list_per_cent = list(per_cent.values())
money = int(input('Введите сумму: '))
deposit=[]
for i in list_per_cent:
    deposit.append(int((i * money)/100))
print('Максимальная сумма, которую вы можете заработать: ' + str(max(deposit)))
