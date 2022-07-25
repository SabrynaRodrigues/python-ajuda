# programa - sistema interativo em python
def info(x):
    help(x)


    

# programa principal
print('\033[1;44m-\033[m' * 40)
print('\033[1;44m* BEM-VINDO AO SISTEMA DE AJUDA PYTHON *\033[m')
print('\033[1;44m-\033[m' * 40)
while True:
    res = str(input('Biblioteca ou Função:'))
    info(res)
    ques = str(input('\033[1;44mDeseja continuar: S/N\033[m'))
    if ques not in 'S':
        break
print('\033[1;91m*--PROGRAMA ENCERRADO!--*\033[m')