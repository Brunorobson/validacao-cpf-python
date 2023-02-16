def numerar_cpf():
    for a in cpf:
        a = int(a)
        cpf_numerado.append(a)

def quantidade():
    if len(cpf) < 11 or len(cpf) > 11:
        return False
    else:
        return True

def primeiro_digito():
    acumulador = 0
    resultado = 0
    controlador = 10
    for numeros in cpf_numerado[0:9]:
        resultado = numeros * controlador
        acumulador += resultado
        controlador = controlador - 1
    acumulador = acumulador *10 % 11
    if acumulador == 10:
        acumulador = 0
    if acumulador == cpf_numerado[9]:
        return True
    else:
        return False

def segundo_digito():
    acumulador = 0
    resultado = 0
    controlador = 11
    for numeros in cpf_numerado[0:10]:
        resultado = numeros * controlador
        acumulador += resultado
        controlador = controlador - 1
    acumulador = acumulador *10 % 11
    if acumulador == 10:
        acumulador = 0
    if acumulador == cpf_numerado[9]:
        return True
    else:
        return False


cpf_numerado = []
cpf = str(input("Qual o seu CPF")).replace('.','').replace('-','')

numerar_cpf()
quantidade()
primeiro_digito()
segundo_digito()

if quantidade() == True and primeiro_digito() == True and segundo_digito() == True:
    print("O CPF é valido!")
else:
    print("O CPF é invalido!")