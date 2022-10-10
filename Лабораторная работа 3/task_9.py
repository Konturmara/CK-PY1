salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен


def money_for_live(salary=5000, spend=6000, months=10, increase=0.03):
    need_money = 0  # количество денег, чтобы прожить 10 месяцев
    for _ in range(months):
        need_money += (spend - salary)
        spend *= (1 + increase)

    return(round(need_money))


print(money_for_live())
