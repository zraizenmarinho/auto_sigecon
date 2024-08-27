import pandas as pd
import dask.dataframe as dd

arquivo = 'si_jan.xlsx'

def obter_evadidos(file_path, unidade, modalidade, tipo_acao, chave_prefixo):
    class EvadidosPorTipoFinanciamento:
        def __init__(self, file_path):
            pandas_df = pd.read_excel(file_path)
            self.data = dd.from_pandas(pandas_df, npartitions=1)
        
        def contar_evadidos(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento, tipo_situacao):
            filtros = (
                (self.data['UNIDADE_ATENDIMENTO'] == unidade) &
                (self.data['MODALIDADE'] == modalidade) &
                (self.data['TIPO_ACAO'] == tipo_acao) &
                (self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])) &
                (self.data['DT_SAIDA_MÊS'].astype(str).isin([mes_referencia])) &
                (self.data['DT_SAIDA_ANO'].astype(str).isin([anos_referencia])) &
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
                unidade, modalidade, tipo_acao, '72024', mes_referencia, '2024', tipo_financiamento,'4 Evadida'
            )
    
    return resultados_eva

def obter_evadidos_iniciacao_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117374 SENAI Gama', '5 Iniciação Profissional', '1 Presencial', 'inicia_presen_eva')

def obter_evadidos_iniciacao_distancia_tag(file_path):
    return obter_evadidos(file_path, '1117374 SENAI Gama', '5 Iniciação Profissional', '2 A distância', 'inicia_distan_eva')

def obter_evadidos_aprendizagem_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117374 SENAI Gama', '11 Aprendizagem Industrial básica', '1 Presencial', 'aprendi_presen_eva')

def obter_evadidos_qualificacao_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117374 SENAI Gama', '21 Qualificação Profissional', '1 Presencial', 'qualifi_presen_eva')

def obter_evadidos_aprendizagem_distancia_tag(file_path):
    return obter_evadidos(file_path, '1117374 SENAI Gama', '11 Aprendizagem Industrial básica', '2 A distância', 'aprendi_distan_eva')

def obter_evadidos_qualificacao_distancia_tag(file_path):
    return obter_evadidos(file_path, '1117374 SENAI Gama', '21 Qualificação Profissional', '2 A distância', 'qualifi_distan_eva')

def obter_evadidos_aperfeicoamento_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117374 SENAI Gama', '58 Aperfeiçoamento/Especialização Profissional', '1 Presencial', 'aperfei_presen_eva')

def obter_evadidos_aperfeicoamento_distancia_tag(file_path):
    return obter_evadidos(file_path, '1117374 SENAI Gama', '58 Aperfeiçoamento/Especialização Profissional', '2 A distância', 'aperfei_distan_eva')

def obter_evadidos_qualificacao_itine_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117374 SENAI Gama', '22 Qualificação Profissional - Itinerário V Ensino Médio', '1 Presencial', 'qualifi_iti_presen_eva')

def obter_evadidos_aprendizagem_tecnica_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117374 SENAI Gama', '15 Aprendizagem Industrial Técnica de Nível Médio', '1 Presencial', 'aprendi_tec_presen_eva')

def obter_evadidos_tecnico_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117374 SENAI Gama', '31 Técnico de Nível Médio', '1 Presencial', 'tecni_presen_eva')

def obter_evadidos_tecnico_distancia_tag(file_path):
    return obter_evadidos(file_path, '1117374 SENAI Gama', '31 Técnico de Nível Médio', '2 A distância', 'tecni_distan_eva')

def obter_evadidos_tecnico_iti_presencial_tag(file_path):
    return obter_evadidos(file_path, '1117374 SENAI Gama', '32 Técnico de Nível Médio - Itinerário V Ensino Médio', '1 Presencial', 'tecni_iti_presen_eva')

funcoes_eva = {
    
    'evadidos': {
        'iniciacao_presencial': obter_evadidos_iniciacao_presencial_tag,
        'iniciacao_distancia': obter_evadidos_iniciacao_distancia_tag,
        'aprendizagem_presencial': obter_evadidos_aprendizagem_presencial_tag,
        'qualificacao_presencial': obter_evadidos_qualificacao_presencial_tag,
        'aprendizagem_distancia': obter_evadidos_aprendizagem_distancia_tag,
        'qualificacao_distancia': obter_evadidos_qualificacao_distancia_tag,
        'aperfeicoamento_presencial': obter_evadidos_aperfeicoamento_presencial_tag,
        'aperfeicoamento_distancia': obter_evadidos_aperfeicoamento_distancia_tag,
        'qualificacao_iti_presencial': obter_evadidos_tecnico_iti_presencial_tag,
        'aprendizagem_tec_presencial': obter_evadidos_aprendizagem_tecnica_presencial_tag,
        'tecnico_nm_presencial': obter_evadidos_tecnico_presencial_tag,
        'tecnico_nm_distancia': obter_evadidos_tecnico_distancia_tag,
        'tecnico_nm_iti_presencial': obter_evadidos_tecnico_iti_presencial_tag
    },
}

def obter_dados_por_tipo(categoria, tipo, arquivo):
    chave = f"{categoria}_{tipo}"
    return {
        'evadidos': funcoes_eva['evadidos'][chave](arquivo), 
    }
