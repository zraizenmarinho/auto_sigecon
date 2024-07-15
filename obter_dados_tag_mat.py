import pandas as pd
import dask.dataframe as dd

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
                unidade, modalidade, tipo_acao, '52024', mes_referencia, '2024', tipo_financiamento
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

funcoes_mat = {
    
    'matriculas': {
        'iniciacao_presencial': obter_matriculas_iniciacao_presencial_tag,
        'iniciacao_distancia': obter_matriculas_iniciacao_distancia_tag,
        'aprendizagem_presencial': obter_matriculas_aprendizagem_presencial_tag,
        'qualificacao_presencial': obter_matriculas_qualificacao_presencial_tag,
        'aprendizagem_distancia': obter_matriculas_aprendizagem_distancia_tag,
        'qualificacao_distancia': obter_matriculas_qualificacao_distancia_tag,
        'aperfeicoamento_presencial': obter_matriculas_aperfeicoamento_presencial_tag,
        'aperfeicoamento_distancia': obter_matriculas_aperfeicoamento_distancia_tag,
        'qualificacao_iti_presencial': obter_matriculas_tecnico_iti_presencial_tag,
        'aprendizagem_tec_presencial': obter_matriculas_aprendizagem_tecnica_presencial_tag,
        'tecnico_nm_presencial': obter_matriculas_tecnico_presencial_tag,
        'tecnico_nm_distancia': obter_matriculas_tecnico_distancia_tag,
        'tecnico_nm_iti_presencial': obter_matriculas_tecnico_iti_presencial_tag
    },
}

def obter_dados_por_tipo(categoria, tipo, arquivo):
    chave = f"{categoria}_{tipo}"
    return {
        'matriculas': funcoes_mat['matriculas'][chave](arquivo), 
    }

