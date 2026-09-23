import requests

moedas = {
    "$": "USD",
    "€": "EUR",
    "¥": "JPY",
    "£": "GBP"
}

resposta = requests.get("https://api.exchangerate-api.com/v4/latest/USD")

dados = resposta.json()

cotacao_brl = dados["rates"]["BRL"]

try:
 moeda = input("Digite qual moeda voce quer converter seus reais, utilize SOMENTE os cifrões, $,€,¥,£: ")


 if moeda == "$":
    qnt = float(input(" Quantos reais voce quer converter para dólares? "))
    novo_valor = cotacao_brl / dados["rates"][moedas[moeda]]
    convert = qnt / novo_valor
    print(convert)

 elif moeda == "€":
    qnt = float(input(" Quantos reais voce quer converter para euros? "))
    novo_valor = qnt / cotacao_brl
    convert = novo_valor * dados["rates"][moedas[moeda]]
    print(convert)

 elif moeda == "¥":
    qnt = float(input(" Quantos reais voce quer converter para Yenes? "))
    novo_valor = qnt / cotacao_brl
    convert = novo_valor * dados["rates"][moedas[moeda]]
    print(convert)

 elif moeda =="£":
    qnt = float(input(" Quantos reais voce quer converter para Libras? "))
    novo_valor = qnt / cotacao_brl
    convert = novo_valor * dados["rates"][moedas[moeda]]
    print(convert)
 else:
    print("Verifique os dados inseridos")

except ValueError:
   print("Digite uma moeda válida")


