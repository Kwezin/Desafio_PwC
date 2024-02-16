import re

endereco = input('Endereço: ')
   
achar_num = re.findall(r'\d+\w*', endereco) # Procurando o número no endereço e guardando em uma lista

index_num = re.search(achar_num[0], endereco) # Retorna o índice da primeira ocorrência do número

if index_num:
  primeiro_index = index_num.start()
  rua = endereco[0:primeiro_index].strip()
  numero = endereco[primeiro_index:].strip()
      
  print(f'"{rua}", "{numero}"')


  
  