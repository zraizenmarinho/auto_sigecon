import pandas as pd
import dask.dataframe as dd

arquivo = 'si_jan.xlsx'

class MatriculasPorTipoFinanciamentoJan:
    def __init__(self, file_path):
        pandas_df = pd.read_excel(file_path)
        self.data = dd.from_pandas(pandas_df, npartitions=1)
    
    def contar_matriculas_jan(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento):
        filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
        filtro_mod = self.data['MODALIDADE'] == modalidade
        filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
        filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])
        filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin(mes_referencia)
        filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin(anos_referencia)
        filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento
        
        base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan].compute()

        return len(base_filtrada)

def obter_matriculas_por_tipo_jan(file_path, unidade ,modalidade, tipo_acao):
    matriculas_por_tipo = MatriculasPorTipoFinanciamentoJan(file_path)

    mes_rela = '12024'
    mes_referencia = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    anos_referencia = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
    
    jan_mat_regi = matriculas_por_tipo.contar_matriculas_jan(unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, '1 Gratuidade Regimental')
    jan_mat_bolsa = matriculas_por_tipo.contar_matriculas_jan(unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, '2 Gratuidade Não Regimental')
    jan_mat_convenio = matriculas_por_tipo.contar_matriculas_jan(unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, '3 Convênio')
    jan_mat_n_gratuita = matriculas_por_tipo.contar_matriculas_jan(unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, '9 Pago por Pessoa Fisica ou Empresa')

    return {
        "jan_mat_regi": jan_mat_regi,
        "jan_mat_bolsa": jan_mat_bolsa,
        "jan_mat_convenio": jan_mat_convenio,
        "jan_mat_n_gratuita": jan_mat_n_gratuita
    }


tag_iniciacao_presencial = obter_matriculas_por_tipo_jan('si_jan.xlsx', '1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial')
tag_iniciacao_distancia = obter_matriculas_por_tipo_jan('si_jan.xlsx','1117376 SENAI Taguatinga','5 Iniciação Profissional', '2 A distância')
tag_aprendizagem_presencial = obter_matriculas_por_tipo_jan('si_jan.xlsx','1117376 SENAI Taguatinga','11 Aprendizagem Industrial básica', '1 Presencial')
tag_qualificacao_presencial = obter_matriculas_por_tipo_jan('si_jan.xlsx','1117376 SENAI Taguatinga','21 Qualificação Profissional', '1 Presencial')
tag_aprendizagem_distancia = obter_matriculas_por_tipo_jan('si_jan.xlsx','1117376 SENAI Taguatinga','11 Aprendizagem Industrial básica', '2 A distância')
tag_qualificacao_distancia = obter_matriculas_por_tipo_jan('si_jan.xlsx','1117376 SENAI Taguatinga','21 Qualificação Profissional', '2 A distância')
tag_aperfeicoamento_presencial = obter_matriculas_por_tipo_jan('si_jan.xlsx','1117376 SENAI Taguatinga','58 Aperfeiçoamento/Especialização Profissional', '1 Presencial')
tag_aperfeicoamento_distancia = obter_matriculas_por_tipo_jan('si_jan.xlsx','1117376 SENAI Taguatinga','58 Aperfeiçoamento/Especialização Profissional', '2 A distância')
tag_qualificacao_iti_presencial = obter_matriculas_por_tipo_jan('si_jan.xlsx','1117376 SENAI Taguatinga','22 Qualificação Profissional - Itinerário V Ensino Médio', '1 Presencial')
tag_aprendizagem_tec = obter_matriculas_por_tipo_jan('si_jan.xlsx','1117376 SENAI Taguatinga','15 Aprendizagem Industrial Técnica de Nível Médio', '1 Presencial')
tag_tecnico_presencial = obter_matriculas_por_tipo_jan('si_jan.xlsx','1117376 SENAI Taguatinga','31 Técnico de Nível Médio', '1 Presencial')
tag_tecnico_distancia = obter_matriculas_por_tipo_jan('si_jan.xlsx','1117376 SENAI Taguatinga','31 Técnico de Nível Médio', '2 A distância')
tag_tecnico_iti_presencial = obter_matriculas_por_tipo_jan('si_jan.xlsx','1117376 SENAI Taguatinga','32 Técnico de Nível Médio - Itinerário V Ensino Médio', '1 Presencial')

