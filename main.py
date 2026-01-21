# ==============================
# FUNÇÃO DE VALIDAÇÃO DE ENTRADA
# ==============================

def quantidade_validacao(text):
    """
    Solicita ao usuário um número inteiro positivo.
    Continua pedindo enquanto o valor for menor ou igual a zero.
    Retorna a quantidade válida.
    """
    valor = int(input(text))

    while valor <= 0:
        print('Insira um valor válido!')
        valor = int(input(text))

    return valor


# ==============================
# FUNÇÃO UTILITÁRIA
# ==============================

def formatar_temperatura(temp):
    """
    Converte a temperatura digitada pelo usuário para float.
    Substitui vírgula por ponto para aceitar formato brasileiro.
    Exemplo: "7,5" -> 7.5
    """
    temp = temp.replace(',', '.')
    return float(temp)


# ==============================
# FUNÇÃO DE ENTRADA DE DADOS
# ==============================

def inserir_temperaturas(qtd):
    """
    Recebe a quantidade de temperaturas a serem cadastradas.
    Solicita os valores ao usuário, valida o intervalo permitido
    (-30°C a 60°C) e retorna a lista final.
    """
    temperaturas = []

    for i in range(qtd):
        temp = formatar_temperatura(input(f'Insira a {i + 1}ª temperatura: '))

        # Validação de faixa de temperatura
        while temp < -30 or temp > 60:
            print('Insira uma temperatura válida!')
            temp = formatar_temperatura(input(f'Insira a {i + 1}ª temperatura: '))

        temperaturas.append(temp)

    return temperaturas


# ==============================
# FUNÇÃO DE PROCESSAMENTO
# ==============================

def maior_menor_posicao(lista):
    """
    Identifica a maior e a menor temperatura da lista.
    Retorna também a posição (índice humano) desses valores.
    """
    maior_temp = lista[0]
    menor_temp = lista[0]
    pos_maior = 1
    pos_menor = 1

    for i, temp in enumerate(lista):
        if temp > maior_temp:
            maior_temp = temp
            pos_maior = i + 1

        if temp < menor_temp:
            menor_temp = temp
            pos_menor = i + 1

    return maior_temp, menor_temp, pos_maior, pos_menor


# ==============================
# FUNÇÃO DE CÁLCULO
# ==============================

def media_temperatura(lista):
    """
    Calcula e retorna a média aritmética das temperaturas.
    """
    media = sum(lista) / len(lista)
    return media


# ==============================
# FUNÇÃO DE CONTAGEM
# ==============================

def contar_acima_abaixo_igual(lista, media):
    """
    Conta quantas temperaturas estão:
    - acima da média
    - abaixo da média
    - iguais à média
    """
    acima = 0
    abaixo = 0
    igual = 0

    for temp in lista:
        if temp > media:
            acima += 1
        elif temp < media:
            abaixo += 1
        else:
            igual += 1

    return acima, abaixo, igual


# ==============================
# FUNÇÃO DE CÁLCULO EXTRA
# ==============================

def diferencaMaiorMenor(maiorTemperatura, menorTemperatura):
    """
    Calcula a diferença entre a maior e a menor temperatura registrada.
    """
    diferenca = maiorTemperatura - menorTemperatura
    return diferenca


# ==============================
# FUNÇÃO DE ANÁLISE EXTRA
# ==============================

def temperatura_negativa(lista):
    """
    Identifica temperaturas negativas.
    Retorna a quantidade e uma lista contendo esses valores.
    """
    quant_negativa = 0
    temp_negativas = []

    for temp in lista:
        if temp < 0:
            quant_negativa += 1
            temp_negativas.append(temp)

    return quant_negativa, temp_negativas


# ==============================
# FUNÇÃO DE SAÍDA (RELATÓRIO)
# ==============================

def mostrar_relatorio(lista, media, maiorTemperatura, menorTemperatura,
                      posMaiorT, posMenorT, acimaTemp, abaixoTemp,
                      igualTemp, quantidadeT, listaN, diferenca):
    """
    Exibe no terminal o relatório final com todas as informações
    processadas pelo sistema.
    """
    print(f'\nTemperaturas registradas: {lista}')
    print('=' * 30)

    print(f'Temperatura média: {media:.2f}°')
    print('=' * 30)

    print(f'Maior temperatura registrada: {maiorTemperatura}° (posição: {posMaiorT})')
    print(f'Menor temperatura registrada: {menorTemperatura}° (posição: {posMenorT})')
    print('=' * 30)

    print(f'Acima da média: {acimaTemp}')
    print(f'Abaixo da média: {abaixoTemp}')
    print(f'Igual à média: {igualTemp}')
    print('=' * 30)

    print(f'Temperaturas negativas: {quantidadeT} -> {listaN}')
    print(f'Variação entre maior e menor temperatura: {diferenca}°')


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

quant = quantidade_validacao('Insira a quantidade de temperaturas para serem cadastradas: ')

temperaturas_inseridas = inserir_temperaturas(quant)

maiorTemp, menorTemp, posMaior, posMenor = maior_menor_posicao(temperaturas_inseridas)

mediaTemp = media_temperatura(temperaturas_inseridas)

tempAcima, tempAbaixo, tempIgual = contar_acima_abaixo_igual(temperaturas_inseridas, mediaTemp)

diferencaTemp = diferencaMaiorMenor(maiorTemp, menorTemp)

quantidadeNegativas, listaNegativas = temperatura_negativa(temperaturas_inseridas)

mostrar_relatorio(
    temperaturas_inseridas,
    mediaTemp,
    maiorTemp,
    menorTemp,
    posMaior,
    posMenor,
    tempAcima,
    tempAbaixo,
    tempIgual,
    quantidadeNegativas,
    listaNegativas,
    diferencaTemp
)
