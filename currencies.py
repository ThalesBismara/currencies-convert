import requests

resposta = requests.get("https://api.exchangerate-api.com/v4/latest/USD")

dados = resposta.json()

cotacao = dados["rates"]["BRL"]
cotacao1 = dados["rates"]["EUR"]
cotacao2 = dados["rates"]["JPY"]
cotacao3 = dados["rates"]["GBP"]

print(cotacao)

moeda = input("Digite qual moeda voce quer converter seus reais, utilize SOMENTE os cifrões, $,€,¥,£: ")


if moeda == "$":
    qnt = float(input(" Quantos reais voce quer converter para dólares? "))
    novo_valor = qnt / cotacao
    print("O valor de", qnt,"reais ", "em dólares é de",  novo_valor)

elif moeda == "€":
    qnt = float(input(" Quantos reais voce quer converter para euros? "))
    novo_valor = qnt * cotacao
    valor_euro = novo_valor / cotacao1
    print("O valor de", qnt,"reais ", "em euros é de",  valor_euro)

elif moeda == "¥":
    qnt = float(input(" Quantos reais voce quer converter para Yenes? "))
    novo_valor = qnt / cotacao
    valor_yene = novo_valor * cotacao2
    print("O valor de", qnt,"reais ", "em yenes é de", valor_yene)

else:
    qnt = float(input(" Quantos reais voce quer converter para Libras? "))
    novo_valor = qnt * cotacao
    valor_libra = novo_valor / cotacao3
    print("O valor de", qnt,"reais ", "em Libras é de",  valor_libra)