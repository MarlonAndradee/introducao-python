distance_traveled = int(input("Quantos kilometros foram percorridos? "))
rent_days = int(input("Por quantos dias o carro foi alugado? "))

price_rent = 60
price_km = 0.15

price_pay = price_km * distance_traveled + price_rent * rent_days

print(f"Você deverá pagar R${price_pay:.2f} reais")