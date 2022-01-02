preco_mercadoria = float(input("Digite o preço da mercadoria: R$"))
percentual_desconto = float(input("Digite o percentual de desconto: "))
preco_a_pagar = preco_mercadoria - (preco_mercadoria * percentual_desconto / 100)
desconto = preco_mercadoria - preco_a_pagar
print(f"O preço da mercadoria é R${preco_mercadoria:5.2f}, o percentual de desconto é {percentual_desconto:.0f}%, o desconto é de R${desconto:5.2f}, o novo valor da mercadoria é R${preco_a_pagar:5.2f}!")
