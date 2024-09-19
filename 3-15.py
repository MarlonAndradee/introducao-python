cigars_day = int(input("Quantos cigarros por dia? "))
smoker_year = int(input("Quantos anos já fumou?" ))

minute_reduction = smoker_year * 365 * cigars_day * 10

day_reduction = minute_reduction / (24 * 60)

print(f"A redução da vida em dias será de {day_reduction:.2f} dias.")