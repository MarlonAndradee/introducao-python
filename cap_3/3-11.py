product_value = int(input("Digite o valor do produto: "))
product_discount = int(input("Digite o percentual de desconto: "))

total_discount = product_discount / 100 * product_value
total_pay = product_value - total_discount

print(f"O valor do desconto é de R$ {total_discount:.2f} reais.")
print(f"Portanto, o preço total a pagar é R$ {total_pay:.2f} reais.")