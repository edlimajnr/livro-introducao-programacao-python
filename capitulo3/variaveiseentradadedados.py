nome = "Edvaldo"
idade = 24
grana = 79.89
print("{} tem {} anos e R${} no bolso.".format(nome, idade, grana))
print("{} tem {} anos e R${:5.2f} no bolso.".format(nome, idade, grana))
print("{:12} tem {:3} anos e R${:5.2f} no bolso.".format(nome, idade, grana))
print("{:12} tem {:03} anos e R${:5.2f} no bolso.".format(nome, idade, grana))
print("{:<12s} tem {:<3} anos e R${:5.2f} no bolso.".format(nome, idade, grana))
print(f"{nome} tem {idade} anos e R${grana} no bolso.")
print(f"{nome:12} tem {idade:3} anos e R${grana:5.2f} no bolso.")
print(f"{nome:12} tem {idade:03} anos e R${grana:5.2f} no bolso.")
print(f"{nome:<12s} tem {idade:<3} anos e R${grana:5.2f} no bolso.")
