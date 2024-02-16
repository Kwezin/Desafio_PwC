import re

endereco = input('Endereço: ')
achar_virgula = re.findall(r',', endereco) # Procurando alguma vígula e guardando em uma lista

if achar_virgula:
  endereco = re.sub(r',', '', endereco) # Caso seja encontrada alguma vírgula, ela será substituída por "nada"
   
achar_num = re.findall(r'\d+\w*', endereco) # Procurando o número no endereço e guardando em uma lista

if len(achar_num) == 1: # Caso tenha apenas um número no endereço
  index_num = re.search(achar_num[0], endereco) # Retorna o índice da primeira ocorrência do número

  if index_num:
    primeiro_index = index_num.start()
    
    if primeiro_index != 0: # Caso o número não esteja no começo do endereço
      nome = endereco[0:primeiro_index].strip() # Será atribuído desde o índice 0 até primeiro índice do número - 1
      numero = endereco[primeiro_index:].strip()

    else:
      nome = re.sub(achar_num[0], '', endereco).strip() #Substituirá o número por nada
      numero = achar_num[0].strip()
      
    print(f'\n"{nome}", "{numero}"')

elif len(achar_num) > 1: # Caso tenha mais de um número no endereço
  index_num = re.search(achar_num[0], endereco)

  if index_num:   
    ultimo_index = index_num.end() + 1
    nome = endereco[0:ultimo_index].strip() # Será atribuído desde o índice 0 até último índice do número - 1
    numero = endereco[ultimo_index:].strip() # Será atribuído desde o último índice até o final
    print(f'\n"{nome}", "{numero}"')