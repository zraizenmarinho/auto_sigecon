
#Matricula

#from obter_dados_tag_ha import obter_hora_iniciacao_presencial_tag
#import pandas as pd

#x = obter_hora_iniciacao_presencial_tag()

#dados_processados = []
#for key, value in x.items():
#    if value > 0:  
#        partes = key.split("_")
#        mes = partes[0]  #
#        tipo_matricula = " ".join(partes[1:])  
#        dados_processados.append([mes, tipo_matricula, value])

#df = pd.DataFrame(dados_processados, columns=["Mês", "Tipo de Matrícula", "Quantidade"])

#print(df)

######Hora Aluno

from obter_dados_tag_ha import obter_hora_iniciacao_distancia_tag
import pandas as pd

dados = obter_hora_iniciacao_distancia_tag()

dados_transformados = []
for chave, valor in dados.items():
    if valor > 0:
        partes = chave.split()
        mes = partes[0]  
        tipo_gratuidade = ' '.join(partes[1:])  
    
        dados_transformados.append((mes, tipo_gratuidade, valor))

df = pd.DataFrame(dados_transformados, columns=['Mês', 'Tipo de Gratuidade', 'Valor'])

print(df)
