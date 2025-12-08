money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

current_spend = spend
months = 0

while current_spend <= salary + money_capital:
    months += 1

    deficit = current_spend - salary

    if deficit > 0:
        money_capital -= deficit

    current_spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)
