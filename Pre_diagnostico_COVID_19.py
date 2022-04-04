# ESTE PROGRAMA AJUDA NA POSSÍVEL DETECÇÃO DE SINTOMAS DE COVID-19
# PROJETO INTEGRADOR 1-A
# CURSO: BIG DATA E INTELIGÊNCIA ARTIFICIAL
# ALUNOS:
#         BRUNO MATHIAS ALVES
#         FELIPE MARTINS YOSHIMOTO
#         GUILHERME COLHERINHAS DE OLIVEIRA

# DECLARAÇÃO DE VARIÁVEIS GLOBAIS:

registro_paciente = []  # MATRIZ PARA ARMAZENAMENTO DOS PACIENTES
registro_idade = []  # MATRIZ PARA ARMAZENAMENTO DA IDADE
registro_doenca = []  # MATRIZ PARA ARMAZENAMENTO DO DIAGNÓSTICO
menu = str('a')  # VARIÁVEL PARA MENU

# FUNÇÃO QUE DEFINE O MENU INICIAL DO PROGRAMA


def menu_inicial():  # FUNÇÃO QUE CRIA O MENU DE ESCOLHA PARA O QUE FAZER NO PROGRAMA
    global menu  # UTILIZA A VARIÁVEL GLOBAL PARA ACESSO NAS OPÇÕES DO MENU
    print('-=' * 40)  # APENAS CRIA UMA LINHA PARA FORMATAÇÃO - APARECE MAIS VEZES NO PROGRAMA
    print('                 V.0.1 - PRÉ-DIAGNÓSTICO DE DOENÇAS RESPIRATÓRIAS')
    print('-=' * 40)  # APENAS CRIA UMA LINHA PARA FORMATAÇÃO - APARECE MAIS VEZES NO PROGRAMA
    print('      DIGITE A OPÇÃO DESEJADA:')  # INÍCIO DO MENU
    print('           [1] - CADASTRAR NOVO PACIENTE')  # OPÇÃO DO MENU
    print('           [2] - SINTOMAS E DIAGNÓSTICO')  # OPÇÃO DO MENU
    print('           [3] - IMPRIMIR RELATÓRIO')  # OPÇÃO DO MENU
    print('           [4] - SAIR DO PROGRAMA')  # OPÇÃO DO MENU
    print('-=' * 40)
    menu = str(input('OPÇÃO: '))  # REGISTRA A OPÇÃO QUE DESEJA EXECUTAR
    while menu != '1' and menu != '2' and menu != '3' and menu != '4':  # CONTROLE DE ERROS: REGISTRA APENAS 1, 2, 3 E 4.
        menu = str(input('OPÇÃO INVÁLIDA. DIGITE NOVAMENTE: '))  # QUALQUER ENTRADA DIFERENTE DAS OPÇÕES DO MENU SOLICITA-SE DIGITAR NOVAMENTE

# FUNÇÃO QUE FAZ O CADASTRO DO PACIENTE


def cadastro_paciente():  # FUNÇÃO QUE FAZ O CADASTRO DO PACIENTE
    print('-=' * 40)
    print('                            CADASTRO DO PACIENTE')
    print('-=' * 40)
    nome = str(input('  NOME DO PACIENTE: '))  # REGISTRA O NOME DO PACIENTE
    idade = input('  IDADE DO PACIENTE: ')  # REGISTRA A IDADE DO PACIENTE; PODE REGISTRAR UMA STR (SI - SEM INFORMAÇÃO, POR EXEMPLO)
    registro_paciente.append(nome)  # ARMAZENA O NOME NA MATRIZ REGISTRO_PACIENTE PARA SER USADA DEPOIS EM UM RELATÓRIO
    registro_idade.append(idade)  # ARMAZENA A IDADE NA MATRIZ REGISTRO_IDADE PARA SER USADA DEPOIS EM UM RELATÓRIO
    print(' ')
    print('  ==> PACIENTE CADASTRADO COM SUCESSO!')
    print('  ==> FAÇA O CADASTRO DOS SINTOMAS DO PACIENTE.')
    print(' ')

# FUNÇÃO QUE VERIFICA OS SINTOMAS


def verificar_sintomas():  # CRIA A FUNÇÃO EXECUTA AS PERGUNTAS SOBRE OS SINTOMAS DO PACIENTE
    print('-=' * 40)
    print('                            SINTOMAS E DIAGNÓSTICO')
    print('-=' * 40)
    pergunta1 = str(input('O PACIENTE APRESENTA FEBRE OU MAL ESTAR? [S/N]: ')).upper()  # UMA PERGUNTA PARA CADA SINTOMA, COM REGISTRO SIM OU NÃO
    while pergunta1 != 'S' and pergunta1 != 'N':   # SE RESPONDER ALGO DIFERENTE DE `S` OU `N` O PROGRAMA PEDE PARA RESPONDER NOVAMENTE
        pergunta1 = str(input('    RESPONDA NOVAMENTE [S - SIM / N - NÃO]: ')).upper()  # SOLICITAÇÃO EM CASO DE RESPOSTA DIFERENTE DE `S` OU `N`
    pergunta2 = str(input('O PACIENTE APRESENTA TOSSE SECA? [S/N]: ')).upper()  # MESMA ESTRUTURA DA PERGUNTA ACIMA MAS PARA OUTRO SINTOMA
    while pergunta2 != 'S' and pergunta2 != 'N':
        pergunta2 = str(input('    RESPONDA NOVAMENTE [S - SIM / N - NÃO]: ')).upper()
    pergunta3 = str(input('O PACIENTE APRESENTA TOSSE COM CATARRO? [S/N]: ')).upper()
    while pergunta3 != 'S' and pergunta3 != 'N':
        pergunta3 = str(input('    RESPONDA NOVAMENTE [S - SIM / N - NÃO]: ')).upper()
    pergunta4 = str(input('O PACIENTE APRESENTA CANSAÇO? [S/N]: ')).upper()
    while pergunta4 != 'S' and pergunta4 != 'N':
        pergunta4 = str(input('    RESPONDA NOVAMENTE [S - SIM / N - NÃO]: ')).upper()
    pergunta5 = str(input('O PACIENTE APRESENTA DORES NO CORPO? [S/N]: ')).upper()
    while pergunta5 != 'S' and pergunta5 != 'N':
        pergunta5 = str(input('    RESPONDA NOVAMENTE [S - SIM / N - NÃO]: ')).upper()
    pergunta6 = str(input('O PACIENTE APRESENTA IRRITAÇÃO NA GARGANTA? [S/N]: ')).upper()
    while pergunta6 != 'S' and pergunta6 != 'N':
        pergunta6 = str(input('    RESPONDA NOVAMENTE [S - SIM / N - NÃO]: ')).upper()
    pergunta7 = str(input('O PACIENTE APRESENTA NÁUSEAS OU VÔMITO? [S/N]: ')).upper()
    while pergunta7 != 'S' and pergunta7 != 'N':
        pergunta7 = str(input('    RESPONDA NOVAMENTE [S - SIM / N - NÃO]: ')).upper()
    pergunta8 = str(input('O PACIENTE APRESENTA DIARRÉIA? [S/N]: ')).upper()
    while pergunta8 != 'S' and pergunta8 != 'N':
        pergunta8 = str(input('    RESPONDA NOVAMENTE [S - SIM / N - NÃO]: ')).upper()
    pergunta9 = str(input('O PACIENTE APRESENTA DORES DE CABEÇA? [S/N]: ')).upper()
    while pergunta9 != 'S' and pergunta9 != 'N':
        pergunta9 = str(input('    RESPONDA NOVAMENTE [S - SIM / N - NÃO]: ')).upper()
    pergunta10 = str(input('O PACIENTE APRESENTA PERDA DE PALADAR OU OLFATO? [S/N]: ')).upper()
    while pergunta10 != 'S' and pergunta10 != 'N':
        pergunta10 = str(input('    RESPONDA NOVAMENTE [S - SIM / N - NÃO]: ')).upper()
    pergunta11 = str(input('O PACIENTE APRESENTA FALTA DE AR OU DORES NO PEITO? [S/N]: ')).upper()
    while pergunta11 != 'S' and pergunta11 != 'N':
        pergunta11 = str(input('    RESPONDA NOVAMENTE [S - SIM / N - NÃO]: ')).upper()
    pergunta12 = str(input('O PACIENTE APRESENTA PERDA DA FALA OU MOVIMENTOS? [S/N]: ')).upper()
    while pergunta12 != 'S' and pergunta12 != 'N':
        pergunta12 = str(input('    RESPONDA NOVAMENTE [S - SIM / N - NÃO]: ')).upper()
    contador_covid = 0  # CRIAR UM CONTADOR ZERADO PARA QUANTOS SINTOMAS DO PACIENTE ESTÁ RELACIONADO COM A COVID
    contador_h1n1 = 0  # CRIAR UM CONTADOR ZERADO PARA QUANTOS SINTOMAS DO PACIENTE ESTÁ RELACIONADO COM A H1N1
    contador_malaria = 0  # CRIAR UM CONTADOR ZERADO PARA QUANTOS SINTOMAS DO PACIENTE ESTÁ RELACIONADO COM A MALÁRIA
    if pergunta1 == 'S':  # PARA CADA PERGUNTA CONTAMOS SE O REGISTRO FOI  `S` E ADICIONA UM NO CONTADOR DE ACORDO COM A TABELA DE SINTOMAS
        contador_covid += 1  # PERGUNTA 1 (FEBRE OU MAL ESTAR) É SINTOMA DE COVID
        contador_h1n1 += 1  # PERGUNTA 1 (FEBRE OU MAL ESTAR) É SINTOMA DE H1N1
        contador_malaria += 1  # PERGUNTA 1 (FEBRE OU MAL ESTAR) É SINTOMA DE MALÁRIA
    if pergunta2 == 'S':  # PERGUNTA 2 (TOSSE SECA) SÓ É SINTOMA DE COVID (SOMA 1 NO CONTADOR DA COVID)
        contador_covid += 1
    if pergunta3 == 'S':  # PERGUNTA 3 (TOSSE COM CATARRO) SÓ É SINTOMA DE H1N1 (SOMA 1 NO CONTADOR DA H1N1)
        contador_h1n1 += 1
    if pergunta4 == 'S':  # PERGUNTA 4 (CANSAÇO) É SINTOMA DE COVID E MALÁRIA (SOMA 1 NOS DOIS CONTADORES)
        contador_covid += 1
        contador_malaria += 1
    if pergunta5 == 'S':  # PERGUNTA 5 (DORES NO CORPO) É SINTOMA DE TODAS (SOMA 1 EM TODOS OS CONTADORES)
        contador_covid += 1
        contador_h1n1 += 1
        contador_malaria += 1
    if pergunta6 == 'S':  # PERGUNTA 6 (IRRITAÇÃO NA GARGANTA) É SINTOMA DE COVID
        contador_covid += 1
    if pergunta7 == 'S':  # PERGUNTA 7 (NÁUSEAS OU VÔMITO) É SINTOMA DE MALÁRIA
        contador_malaria += 1
    if pergunta8 == 'S':  # PERGUNTA 8 (DIARRÉIA) É SINTOMA DE COVID E MALÁRIA
        contador_covid += 1
        contador_malaria += 1
    if pergunta9 == 'S':  # PERGUNTA 9 (DORES DE CABEÇA) É SINTOMA DE TODAS
        contador_covid += 1
        contador_h1n1 += 1
        contador_malaria += 1
    if pergunta10 == 'S':  # PERGUNTA 10 (PERDA DE PALADAR OU OLFATO) É SINTOMA DE COVID
        contador_covid += 1
    if pergunta11 == 'S':  # PERGUNTA 11 (FALTA DE AR OU DORES NO PEITO) É SINTOMA DE COVID
        contador_covid += 1
    if pergunta12 == 'S':  # PERGUNTA 12 (PERDA DA FALA OU MOVIMENTOS) É SINTOMA DE COVID
        contador_covid += 1
    percentual_covid = contador_covid/10 * 100  # OBTEM O PERCENTUAL DE SINTOMAS POSITIVOS PARA COVID
    percentual_h1n1 = contador_h1n1/4 * 100  # OBTEM O PERCENTUAL DE SINTOMAS POSITIVOS PARA H1N1
    percentual_malaria = contador_malaria/6 * 100  # OBTEM O PERCENTUAL DE SINTOMAS POSITIVOS PARA MALÁRIA
    if percentual_covid >= 50 and pergunta10 == 'S' and pergunta11 == 'S' and pergunta12 == 'S':  # SE O PERCENTUAL FOR MAIOR QUE 50% E ALGUNS SINTOMAS EXCLUSIVOS DE COVID
        registro_doenca.append('POSSÍVEL COVID')  # REGISTRA POSSÍVEL COVID PARA O PACIENTE
        print('-=' * 40)
        print(' ')
        print('      ==> RESULTADO: POSSÍVEL DIAGNÓSTICO DE COVID')  # IMPRIME NA TELA O DIAGNÓSTICO DO PACIENTE
        print(' ')
    elif percentual_h1n1 >= 50 and pergunta3 == 'S':  # SE O PERCENTUAL FOR > 50% E SIM PARA A PERGUNTA 3 (EXCLUSIVO DE H1N1) REGISTRA H1N1
        registro_doenca.append('POSSÍVEL H1N1')  # REGISTRO DE H1N1 PARA O PACIENTE
        print('-=' * 40)
        print(' ')
        print('      ==> RESULTADO: POSSÍVEL DIAGNÓSTICO DE H1N1')  # IMPRIME NA TELA O DIAGNÓSTICO DO PACIENTE
        print(' ')
    elif percentual_malaria >= 50 and pergunta7 == 'S' and pergunta8 == 'S':  # MAIOR QUE 50% E PERGUNTA 7 E 8 = SIM, MALÁRIA
        registro_doenca.append('POSSÍVEL MALÁRIA')  # REGISTRO DE MALÁRIA PARA O PACIENTE
        print('-=' * 40)
        print(' ')
        print('      ==> RESULTADO: POSSÍVEL DIAGNÓSTICO DE MALÁRIA')  # IMPRIME NA TELA O DIAGNÓSTICO DO PACIENTE
        print(' ')
    else:
        registro_doenca.append('EXAME NECESSÁRIO')  # QUALQUER OUTRA COMBINAÇÃO ELE ACUSA DIAGNÓSTICO IMPOSSÍVEL - INDICA EXAME
        print('-=' * 40)
        print(' ')
        print('      ==> RESULTADO: DIAGNÓSTICO IMPOSSÍVEL - EXAME NECESSÁRIO') # IMPRIME NA TELA O DIAGNÓSTICO DO PACIENTE
        print(' ')


# FUNÇÃO PARA IMPRIMIR O RELATÓRIO
def imprimir_relatorio(): # UMA FUNÇÃO QUE IMPRIME UM RELATÓRIO APOS REGISTRO DE PACIENTE E SINTOMAS
    print('-=' * 40)
    print('                                    RELATÓRIO')
    print('-=' * 40)
    print(' ')
    if len(registro_paciente) != len(registro_doenca):  # CONTROLE DE ERROS, O VETOR PACIENTES DEVE TER O MESMO TAMANHO DO VETOR DE REGISTRO DA DOENÇA
        print('Registro Incompleto') # SOLICITA QUE O USUÁRIO COMPLETE O REGISTRO (PACIENTE+IDADE OU DOENÇA)
    else:
        for i in range(len(registro_paciente)):  # PARA TODOS OS REGISTROS DE PACIENTES IMPRIME O NOME, IDADE, DIAGNÓSTICO, NA SEQUÊNCIA QUE FOI REGISTRADO (ATENDIDO)
            print(' ==> PACIENTE', i+1, ':', registro_paciente[i], '- IDADE:', registro_idade[i], '- DIAGNÓSTICO:', registro_doenca[i])
    print(' ')

# FUNÇÃO PARA SAIR DO PROGRAMA


def fim_programa():
    print('-=' * 40)


print('-=' * 40)  # PROGRAMA PRINCIPAL
print('                                   BEM VINDO')
menu_inicial()  # CHAMA O MENU INICIAL
while menu != '4':  # RODA O MENU INICIAL INFINITAMENTE ATÉ A ESCOLHA FOR `4` PARA ENCERRAR O PROGRAMA
    if menu == '1':  # SE FOR 1 ENTRA NO CADASTRO DE PACIENTES (FUNÇÃO CADASTRO) E DEPOIS VOLTA PARA O MENU INICIAL (FUNÇÃO MENU_INICIAL)
        cadastro_paciente()
        menu_inicial()
    if menu == '2':  # SE FOR 2 ENTRA NO REGISTRO DE SINTOMAS (FUNÇÃO VERIFICAR_SINTOMAS) E VOLTA PARA MENU INICIAL (FUNÇÃO MENU_INICIAL)
        verificar_sintomas()
        menu_inicial()
    if menu == '3':  # SE FOR 3 IMPRIME O RELATÓRIO (FUNÇÃO IMPRIMIR_RELATÓRIO) E VOLTA PARA O MENU INICIAL (FUNÇAÕ MENU_INICIAL)
        imprimir_relatorio()
        menu_inicial()
fim_programa()


