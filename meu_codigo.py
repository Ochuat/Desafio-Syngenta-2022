def get_cheapest_hotel(number):   #DO NOT change the function's name

    #Definindo constantes e configurando aplicação
    CATEGORIA = 0
    TAXA_DIA_SEMANA_NORMAL = 1
    TAXA_DIA_SEMANA_FIDELIDADE = 2
    TAXA_FIM_SEMANA_NORMAL = 3
    TAXA_FIM_SEMANA_FIDELIDADE = 4
    NOME_HOTEL_1 = "Lakewood"
    PRECOS_HOTEL_1 = [3, 110, 80, 90, 80]
    NOME_HOTEL_2 = "Bridgewood"
    PRECOS_HOTEL_2 = [4, 160, 110, 60, 50]
    NOME_HOTEL_3 = "Ridgewood"
    PRECOS_HOTEL_3 = [5, 220, 100, 150, 40]
    STATUS_CLIENTE_NORMAL = "Regular"
    MENSAGEM_ERRO = "Erro ao escolher o hotel"

    #Inicializando as variáveis
    precos = [0, 0, 0]
    menor_preco = 0
    indice_menor_preco = 0
    qtdade_dias_semana = 0
    qtdade_fim_semana = 0

    #Tratando o dado de entrada para virar informação útil e organizada
    entrada = str(number)
    tipo = entrada.split(":")
    categoria_cliente = tipo[CATEGORIA]
    dias = tipo[1].split(",")

    #Calculando o número de diárias em dias de semana e o número de diárias no fim de semana
    for dia in dias:
        if "sat" in dia or "sun" in dia:
            qtdade_fim_semana += 1
        else:
            qtdade_dias_semana += 1

    #Tabelando os preços de cada hotel em um dicionário de listas
    tabela_precos = {NOME_HOTEL_1: PRECOS_HOTEL_1, NOME_HOTEL_2: PRECOS_HOTEL_2,
                     NOME_HOTEL_3: PRECOS_HOTEL_3}

    #Calculando o valor a se pagar, considerando o tipo de cliente e o tipo de diária (dia da semana vs fim de semana)
    for indice, hotel in enumerate (tabela_precos):
        #preço para clientes normais
        if categoria_cliente == STATUS_CLIENTE_NORMAL:
            precos[indice] = (qtdade_dias_semana * tabela_precos[hotel][TAXA_DIA_SEMANA_NORMAL])\
                             + (qtdade_fim_semana * tabela_precos[hotel][TAXA_FIM_SEMANA_NORMAL])
        else:#preço para clientes fidelizados
            precos[indice] = (qtdade_dias_semana * tabela_precos[hotel][TAXA_DIA_SEMANA_FIDELIDADE])\
                             + (qtdade_fim_semana * tabela_precos[hotel][TAXA_FIM_SEMANA_FIDELIDADE])

    #Procurando o hotel mais barato e, se houver empate, o mais confortável
    for indice, preco in enumerate (precos):
        if indice == 0 or menor_preco >= preco:
            menor_preco = preco
            indice_menor_preco = indice

    #Configurando a saída com o nome do hotel mais barato ou confortável
    if indice_menor_preco == 0:
        cheapest_hotel = NOME_HOTEL_1
    elif indice_menor_preco == 1:
        cheapest_hotel = NOME_HOTEL_2
    elif indice_menor_preco == 2:
        cheapest_hotel = NOME_HOTEL_3
    else:
        cheapest_hotel = MENSAGEM_ERRO

    return cheapest_hotel
