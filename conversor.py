def conversor():
  vlr= float(input("Digite um valor em centímetros para a conversão: "))
  VlrPolegadas = vlr / 2.54
  cvrs = open("conversão.txt", 'w+')
  cvrs.write (f'{vlr} o centímetro é %.2f em polegadas.\n'%(VlrPolegadas)) 