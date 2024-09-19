salary = int(input("Digite o seu salário: "))
increase = int(input("Digite a porcentagem de aumento desejada: "))

total_increase = salary + (salary * increase / 100)

print(f"O salário junto com o aumento será de R$ {total_increase}")