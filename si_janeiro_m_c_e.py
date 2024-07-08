import pandas as pd
import dask.dataframe as dd

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


def obter_matriculas(file_path, unidade, modalidade, tipo_acao, chave_prefixo):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            pandas_df = pd.read_excel(file_path)
            self.data = dd.from_pandas(pandas_df, npartitions=1)
        
        def contar_matriculas(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento):
            filtros = (
                (self.data['UNIDADE_ATENDIMENTO'] == unidade) &
                (self.data['MODALIDADE'] == modalidade) &
                (self.data['TIPO_ACAO'] == tipo_acao) &
                (self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])) &
                (self.data['DT_ENTRADA_MÊS'].astype(str).isin([mes_referencia])) &
                (self.data['DT_ENTRADA_ANO'].astype(str).isin([anos_referencia])) &
                (self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento)
            )

            base_filtrada = self.data[filtros].compute()
            return len(base_filtrada)
        
    matriculas_por_tipo = MatriculasPorTipoFinanciamento(file_path)

    meses = {
        'fev': '2',
        'mar': '3',
        'abr': '4',
        'mai': '5',
        'jun': '6',
        'jul': '7',
        'ago': '8',
        'set': '9',
        'out': '10',
        'nov': '11',
        'dez': '12'
    }
    
    resultados_mat = {}
    
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_{chave_prefixo}_{tipo_financiamento}"
            resultados_mat[chave_resultado] = matriculas_por_tipo.contar_matriculas(
                unidade, modalidade, tipo_acao, '32024', mes_referencia, '2024', tipo_financiamento
            )
    
    return resultados_mat

def obter_matriculas_iniciacao_presencial_tag(file_path):
    return obter_matriculas(file_path, '1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', 'inicia_presen_mat')

def obter_matriculas_iniciacao_distancia_tag(file_path):
    return obter_matriculas(file_path, '1117376 SENAI Taguatinga', '5 Iniciação Profissional', '2 A distância', 'inicia_distan_mat')

def obter_matriculas_aprendizagem_presencial_tag(file_path):
    return obter_matriculas(file_path, '1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '1 Presencial', 'aprendi_presen_mat')

def obter_matriculas_qualificacao_presencial_tag(file_path):
    return obter_matriculas(file_path, '1117376 SENAI Taguatinga', '21 Qualificação Profissional', '1 Presencial', 'qualifi_presen_mat')

def obter_matriculas_aprendizagem_distancia_tag(file_path):
    return obter_matriculas(file_path, '1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '2 A distância', 'aprendi_distan_mat')

def obter_matriculas_qualificacao_distancia_tag(file_path):
    return obter_matriculas(file_path, '1117376 SENAI Taguatinga', '21 Qualificação Profissional', '2 A distância', 'qualifi_distan_mat')

def obter_matriculas_aperfeicoamento_presencial_tag(file_path):
    return obter_matriculas(file_path, '1117376 SENAI Taguatinga', '58 Aperfeiçoamento/Especialização Profissional', '1 Presencial', 'aperfei_presen_mat')

def obter_matriculas_aperfeicoamento_distancia_tag(file_path):
    return obter_matriculas(file_path, '1117376 SENAI Taguatinga', '58 Aperfeiçoamento/Especialização Profissional', '2 A distância', 'aperfei_distan_mat')

def obter_matriculas_qualificacao_itine_presencial_tag(file_path):
    return obter_matriculas(file_path, '1117376 SENAI Taguatinga', '22 Qualificação Profissional - Itinerário V Ensino Médio', '1 Presencial', 'qualifi_iti_presen_mat')

def obter_matriculas_aprendizagem_tecnica_presencial_tag(file_path):
    return obter_matriculas(file_path, '1117376 SENAI Taguatinga', '15 Aprendizagem Industrial Técnica de Nível Médio', '1 Presencial', 'aprendi_tec_presen_mat')

def obter_matriculas_tecnico_presencial_tag(file_path):
    return obter_matriculas(file_path, '1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '1 Presencial', 'tecni_presen_mat')

def obter_matriculas_tecnico_distancia_tag(file_path):
    return obter_matriculas(file_path, '1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '2 A distância', 'tecni_distan_mat')

def obter_matriculas_tecnico_iti_presencial_tag(file_path):
    return obter_matriculas(file_path, '1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '1 Presencial', 'tecni_iti_presen_mat')



def obter_concluintes(file_path, unidade, modalidade, tipo_acao, chave_prefixo):
    class ConcluintesPorTipoFinanciamento:
        def __init__(self, file_path):
            pandas_df = pd.read_excel(file_path)
            self.data = dd.from_pandas(pandas_df, npartitions=1)
        
        def contar_concluintes(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento,tipo_situacao):
            filtros = (
                (self.data['UNIDADE_ATENDIMENTO'] == unidade) &
                (self.data['MODALIDADE'] == modalidade) &
                (self.data['TIPO_ACAO'] == tipo_acao) &
                (self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])) &
                (self.data['DT_ENTRADA_MÊS'].astype(str).isin([mes_referencia])) &
                (self.data['DT_ENTRADA_ANO'].astype(str).isin([anos_referencia])) &
                (self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento) &
                (self.data['SITUACAO_MATRICULA'] == tipo_situacao)
            )

            base_filtrada = self.data[filtros].compute()
            return len(base_filtrada)
        
    concluintes_por_tipo = ConcluintesPorTipoFinanciamento(file_path)

    meses = {
        'jan': '1',
        'fev': '2',
        'mar': '3',
        'abr': '4',
        'mai': '5',
        'jun': '6',
        'jul': '7',
        'ago': '8',
        'set': '9',
        'out': '10',
        'nov': '11',
        'dez': '12'
    }
    
    resultados_con = {}
    
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_{chave_prefixo}_{tipo_financiamento}"
            resultados_con[chave_resultado] = concluintes_por_tipo.contar_concluintes(
                unidade, modalidade, tipo_acao, '32024', mes_referencia, '2024', tipo_financiamento, '2 Concluída'
            )
    
    return resultados_con

def obter_concluintes_iniciacao_presencial_tag(file_path):
    return obter_concluintes(file_path, '1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', 'inicia_presen_con')

def obter_concluintes_iniciacao_distancia_tag(file_path):
    return obter_concluintes(file_path, '1117376 SENAI Taguatinga', '5 Iniciação Profissional', '2 A distância', 'inicia_distan_con')

def obter_concluintes_aprendizagem_presencial_tag(file_path):
    return obter_concluintes(file_path, '1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '1 Presencial', 'aprendi_presen_con')

def obter_concluintes_qualificacao_presencial_tag(file_path):
    return obter_concluintes(file_path, '1117376 SENAI Taguatinga', '21 Qualificação Profissional', '1 Presencial', 'qualifi_presen_con')

def obter_concluintes_aprendizagem_distancia_tag(file_path):
    return obter_concluintes(file_path, '1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '2 A distância', 'aprendi_distan_con')

def obter_concluintes_qualificacao_distancia_tag(file_path):
    return obter_concluintes(file_path, '1117376 SENAI Taguatinga', '21 Qualificação Profissional', '2 A distância', 'qualifi_distan_con')

def obter_concluintes_aperfeicoamento_presencial_tag(file_path):
    return obter_concluintes(file_path, '1117376 SENAI Taguatinga', '58 Aperfeiçoamento/Especialização Profissional', '1 Presencial', 'aperfei_presen_con')

def obter_concluintes_aperfeicoamento_distancia_tag(file_path):
    return obter_concluintes(file_path, '1117376 SENAI Taguatinga', '58 Aperfeiçoamento/Especialização Profissional', '2 A distância', 'aperfei_distan_con')

def obter_concluintes_qualificacao_itine_presencial_tag(file_path):
    return obter_concluintes(file_path, '1117376 SENAI Taguatinga', '22 Qualificação Profissional - Itinerário V Ensino Médio', '1 Presencial', 'qualifi_iti_presen_con')

def obter_concluintes_aprendizagem_tecnica_presencial_tag(file_path):
    return obter_concluintes(file_path, '1117376 SENAI Taguatinga', '15 Aprendizagem Industrial Técnica de Nível Médio', '1 Presencial', 'aprendi_tec_presen_con')

def obter_concluintes_tecnico_presencial_tag(file_path):
    return obter_concluintes(file_path, '1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '1 Presencial', 'tecni_presen_con')

def obter_concluintes_tecnico_distancia_tag(file_path):
    return obter_concluintes(file_path, '1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '2 A distância', 'tecni_distan_con')

def obter_concluintes_tecnico_iti_presencial_tag(file_path):
    return obter_concluintes(file_path, '1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '1 Presencial', 'tecni_iti_presen_con')



def obter_evadidos(file_path, unidade, modalidade, tipo_acao, chave_prefixo):
    class EvadidosPorTipoFinanciamento:
        def __init__(self, file_path):
            pandas_df = pd.read_excel(file_path)
            self.data = dd.from_pandas(pandas_df, npartitions=1)
        
        def contar_evadidos(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento,tipo_situacao):
            filtros = (
                (self.data['UNIDADE_ATENDIMENTO'] == unidade) &
                (self.data['MODALIDADE'] == modalidade) &
                (self.data['TIPO_ACAO'] == tipo_acao) &
                (self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])) &
                (self.data['DT_ENTRADA_MÊS'].astype(str).isin([mes_referencia])) &
                (self.data['DT_ENTRADA_ANO'].astype(str).isin([anos_referencia])) &
                (self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento) &
                (self.data['SITUACAO_MATRICULA'] == tipo_situacao)
            )

            base_filtrada = self.data[filtros].compute()
            return len(base_filtrada)
        
    evadidos_por_tipo = EvadidosPorTipoFinanciamento(file_path)

    meses = {
        'jan': '1',
        'fev': '2',
        'mar': '3',
        'abr': '4',
        'mai': '5',
        'jun': '6',
        'jul': '7',
        'ago': '8',
        'set': '9',
        'out': '10',
        'nov': '11',
        'dez': '12'
    }
    
    resultados_eva = {}
    
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_{chave_prefixo}_{tipo_financiamento}"
            resultados_eva[chave_resultado] = evadidos_por_tipo.contar_evadidos(
                unidade, modalidade, tipo_acao, '32024', mes_referencia, '2024', tipo_financiamento, '4 Evadida'
            )
    
    return resultados_eva

def obter_evadidos_iniciacao_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', 'inicia_presen_eva')

def obter_evadidos_iniciacao_distancia_tag(file_path):
    return obter_evadidos(file_path, '1117376 SENAI Taguatinga', '5 Iniciação Profissional', '2 A distância', 'inicia_distan_eva')

def obter_evadidos_aprendizagem_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '1 Presencial', 'aprendi_presen_eva')

def obter_evadidos_qualificacao_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117376 SENAI Taguatinga', '21 Qualificação Profissional', '1 Presencial', 'qualifi_presen_eva')

def obter_evadidos_aprendizagem_distancia_tag(file_path):
    return obter_evadidos(file_path, '1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '2 A distância', 'aprendi_distan_eva')

def obter_evadidos_qualificacao_distancia_tag(file_path):
    return obter_evadidos(file_path, '1117376 SENAI Taguatinga', '21 Qualificação Profissional', '2 A distância', 'qualifi_distan_eva')

def obter_evadidos_aperfeicoamento_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117376 SENAI Taguatinga', '58 Aperfeiçoamento/Especialização Profissional', '1 Presencial', 'aperfei_presen_eva')

def obter_evadidos_aperfeicoamento_distancia_tag(file_path):
    return obter_evadidos(file_path, '1117376 SENAI Taguatinga', '58 Aperfeiçoamento/Especialização Profissional', '2 A distância', 'aperfei_distan_eva')

def obter_evadidos_qualificacao_itine_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117376 SENAI Taguatinga', '22 Qualificação Profissional - Itinerário V Ensino Médio', '1 Presencial', 'qualifi_iti_presen_eva')

def obter_evadidos_aprendizagem_tecnica_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117376 SENAI Taguatinga', '15 Aprendizagem Industrial Técnica de Nível Médio', '1 Presencial', 'aprendi_tec_presen_eva')

def obter_evadidos_tecnico_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '1 Presencial', 'tecni_presen_eva')

def obter_evadidos_tecnico_distancia_tag(file_path):
    return obter_evadidos(file_path, '1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '2 A distância', 'tecni_distan_eva')

def obter_evadidos_tecnico_iti_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '1 Presencial', 'tecni_iti_presen_eva')