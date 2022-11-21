#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2M²
#AREA = BASE X ALTURA

b = float(input ('Base: '))
h = float(input ('Altura: '))

a = b*h

print ('A area da parede mede {}m2.\nSera necessario {} litros de tinta para pinta-la completamente' .format (a, a/2))

