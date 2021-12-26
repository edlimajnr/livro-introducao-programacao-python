dias = int(input("Digite os dias: "))
dias_conv = dias * 86400
horas = int(input("Digite as horas: "))
horas_conv = horas * 3600
minutos = int(input("Digite os minutos: "))
minutos_conv = minutos * 60
segundos = int(input("Digite os segundos: "))
conversão = dias_conv + horas_conv + minutos_conv + segundos
print(f"Você informou {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos\nConvertido em segundos são {conversão}")
