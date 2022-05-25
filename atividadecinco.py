#1) Faça um algoritmo que ajude uma empresa de limpeza. Para isso o programa deve ler a largura e o 
#comprimento de um cômodo e calcular e mostrar a área a ser limpa e a 
#quantidade de produto necessária para o serviço,sabendo que cada litro de produto limpa 
#uma área de 2 metros quadrados.

c = float(input('Digite o comprimento do comodo (m²): '))
l = float(input('Digite a largura do comodo (m²): '))

area = c*l
p = area/2

print(f'O comodo total é de {area}, e a quantidade de produto a ser usado em uma area de 2m² é {p}')
