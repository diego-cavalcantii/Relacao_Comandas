'''
•	O gerente de um bar precisa fazer um levantamento do movimento no final do expediente. Basicamente, o bar oferece um menu (tabela abaixo) onde cada item tem um código associado. Considerando que ele tem uma relação das comandas com as quantidades consumidas por mesa, escreva um programa em Python faça a leitura do código e da quantidade de cada item até que o usuário digite 0 (1-continuar e 0-parar). Calcule o total para cada comanda baseado nas quantidades de porções e cervejas consumidas e o valor total geral do dia. Para tanto, utilize a estrutura de repetição “while”.

01	Porção de fritas	R$ 35,00
02	Porção de pastéis	R$ 25,00
03	Tábua de frios	R$ 40,00
04	Porção de peixes	R$ 55,00
05	Cerveja	R$ 18,00
'''

lista_comada = []
lista_valor_tot = []
resp = 1
valor_tot = 0

print("\n01	Porção de fritas	R$ 35,00 "
      "\n02	Porção de pastéis	R$ 25,00"
      "\n03	Tábua de frios	    R$ 40,00"
      "\n04	Porção de peixes	R$ 55,00"
      "\n05	Cerveja	            R$ 18,00")

while (resp != 0):
    lista_comada.append(int(input("\nDigite o número da comanda : ")))
    while (resp != 0):
        cod_item = int(input("Digite o código do item : "))
        qtde_item = int(input("Digite a quantidade do item : "))
        match cod_item:
            case 1:
                valor_prod = 35 * qtde_item
            case 2:
                valor_prod = 25 * qtde_item
            case 3:
                valor_prod = 40 * qtde_item
            case 4:
                valor_prod = 55 * qtde_item
            case 5:
                valor_prod = 18 * qtde_item
        valor_tot += + valor_prod
        lista_valor_tot.append(valor_tot)
        resp = int(input("(1-continuar e 0-parar) : "))
    resp = int(input("Inserir outra comanda (1-continuar e 0-parar) : "))

tot_comandas = len(lista_comada)
tot_dia = sum(lista_valor_tot)
print(f"\nSendo usadas {tot_comandas} comandas o valor total do dia foi R${tot_dia:.2f}")


