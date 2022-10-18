salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
all_spends = 6000 # затраты на первый месяц
count_month = 1
while count_month != 10: # цикл для расчета всех затрат
    spend = spend + spend * increase
    all_spends += spend
    count_month += 1
need_money = all_spends - salary * months # нужная сумма денег за вычетом зарплаты
print(round(need_money))
