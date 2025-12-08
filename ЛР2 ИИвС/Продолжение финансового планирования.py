salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

current_spend = spend
total_deficit = 0

for i in range(1, months + 1):

    current_spend_i = spend * ((1 + increase) ** (i - 1))

    deficit = current_spend_i - salary

    if deficit > 0:
        total_deficit += deficit

money_capital = round(total_deficit)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
