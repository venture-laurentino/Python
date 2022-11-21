#MAKE A SCRIPT TO READ SOMETHING ON THE KEYBOARD AND SHOW YOUR PRIMITIVE TYPE AND ALL INFORMATION ABOUT IT ON THE SCREEN

d = int (input ('Digite qualquer coisa: '))
print('Qual é o tipo? ',type(d))
print ('É alphanumérico? ',d.isalnum())
print ('É numérico? ',d.isnumeric())
print ('É alpha? ',d.isalpha())
print ('É maiúsculo? ',d.isupper())
print ('É minúsculo? ',d.islower())