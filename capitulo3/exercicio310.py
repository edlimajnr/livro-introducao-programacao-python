salário = float(input("Digite o seu salário: "))
aumento = float(input("Digite a procentagem do aumento: "))
novo_salário = salário + (salário * aumento / 100)
print(f"O seu salário era R${salário:5.2f}, mas com o reajuste de {aumento}%, o seu novo salário é R${novo_salário:5.2f}!")
