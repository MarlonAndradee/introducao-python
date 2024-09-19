days = int(input("Digite o dia: "))
hours = int(input("Digite o horário: "))
minutes = int(input("Digite os minutos: "))
seconds = int(input("Digite os segundos: "))

total_seconds = days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds

print(f"Total de {total_seconds} segundos")