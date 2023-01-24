qte_tickets = int(input("Укажите количество билетов: "))
total_cost = 0 #заводим счетчик
for qte in range(qte_tickets): #задаем переменную для отображения порядкового номера посетителя.
#цикл будет продолжаться в пределах указанного количества билетов
    age_visitors = int(input(f"Укажите возраст {qte+1} посетителя: "))
    if 18 < age_visitors:
        total_cost = total_cost
    if 18 <= age_visitors < 25:
        total_cost += 990
    if age_visitors >= 25:
        total_cost += 1390
if qte_tickets > 3:
    total_cost -= (total_cost / 100) * 10
print("Сумма к оплате: " + str(total_cost))



