
from mat_tag import tag_iniciacao_presencial

from obter_dados_tag_mat import obter_matriculas_aperfeicoamento_distancia_tag
mat = obter_matriculas_aperfeicoamento_distancia_tag('si_jan.xlsx')


#Matricula Janeiro
#print(tag_iniciacao_presencial)
{'jan_mat_regi': 598, 'jan_mat_bolsa': 0, 'jan_mat_convenio': 0, 'jan_mat_n_gratuita': 3}


#Matricula Fevereiro
print(mat)

{

'fev_aperfei_distan_mat_1 Gratuidade Regimental': 0, 'fev_aperfei_distan_mat_2 Gratuidade Não Regimental': 0, 'fev_aperfei_distan_mat_3 Convênio': 0, 
'fev_aperfei_distan_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 

}
 
 