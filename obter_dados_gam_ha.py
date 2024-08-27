import pandas as pd
import dask.dataframe as dd

def obter_horas(file_path, unidade, modalidade, tipo_acao, chave_prefixo):
    class HorasPorTipoFinanciamento:
        def __init__(self, file_path):
            pandas_df = pd.read_excel(file_path)
            self.data = dd.from_pandas(pandas_df, npartitions=1)
        
        def somar_horas(self, unidade, modalidade, tipo_acao, mes_rela, tipo_financiamento):
            filtros = (
                (self.data['UNIDADE_ATENDIMENTO'] == unidade) &
                (self.data['MODALIDADE'] == modalidade) &
                (self.data['TIPO_ACAO'] == tipo_acao) &
                (self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])) &
                (self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento)
            )

            base_filtrada = self.data[filtros].compute()

            soma_hora_aluno = base_filtrada['HORA_ALUNO'].sum()
            soma_hora_aluno_ead = base_filtrada['HORA_ALUNO_EAD'].sum()

            return soma_hora_aluno + soma_hora_aluno_ead
    
    hora_por_tipo = HorasPorTipoFinanciamento(file_path)

    meses = {
        'jan': '12024',
        'fev': '22024',
        'mar': '32024',
        'abr': '42024',
        'mai': '52024',
        'jun': '62024',
        'jul': '72024',
        'ago': '82024',
        'set': '92024',
        'out': '102024',
        'nov': '112024',
        'dez': '122024'
    }

    resultados_ha = {}

    # Coleta as horas para cada combinação de mês e tipo de financiamento
    for mes_atual, mes_rela in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_{chave_prefixo}_ha_{tipo_financiamento}"
            resultados_ha[chave_resultado] = hora_por_tipo.somar_horas(
                unidade, modalidade, tipo_acao, mes_rela, tipo_financiamento)

    # Ajusta as horas subtraindo as horas dos meses anteriores
    for idx, (mes_atual, mes_rela) in enumerate(meses.items()):
        if idx == 0:
            continue

        mes_anterior_str = str(int(mes_rela) - 1).zfill(5)
        mes_anterior = mes_anterior_str

        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado_atual = f"{mes_atual}_{chave_prefixo}_ha_{tipo_financiamento}"
            
            if chave_resultado_atual in resultados_ha:
                total_anterior = sum(
                    resultados_ha.get(f"{list(meses.keys())[i]}_{chave_prefixo}_ha_{tipo_financiamento}", 0)
                    for i in range(idx)
                )
                resultados_ha[chave_resultado_atual] -= total_anterior

                if resultados_ha[chave_resultado_atual] < 0:
                    resultados_ha[chave_resultado_atual] = 0
            else:
                print(f"A chave {chave_resultado_atual} não foi encontrada em resultados_ha")

    return resultados_ha


def obter_hora_iniciacao_presencial_tag(file_path):
    return obter_horas(file_path, '1117374 SENAI Gama', '5 Iniciação Profissional', '1 Presencial', 'inicia_presen')

def obter_hora_iniciacao_distancia_tag(file_path):
    return obter_horas(file_path, '1117374 SENAI Gama', '5 Iniciação Profissional', '2 A distância', 'inicia_distan')

def obter_hora_aprendizagem_presencial_tag(file_path):
    return obter_horas(file_path, '1117374 SENAI Gama', '11 Aprendizagem Industrial básica', '1 Presencial', 'aprendi_presen')

def obter_hora_qualificacao_presencial_tag(file_path):
    return obter_horas(file_path, '1117374 SENAI Gama', '21 Qualificação Profissional', '1 Presencial', 'qualifi_presen')

def obter_hora_aprendizagem_distancia_tag(file_path):
    return obter_horas(file_path, '1117374 SENAI Gama', '11 Aprendizagem Industrial básica', '2 A distância', 'aprendi_distan')

def obter_hora_qualificacao_distancia_tag(file_path):
    return obter_horas(file_path, '1117374 SENAI Gama', '21 Qualificação Profissional', '2 A distância', 'qualifi_distan')

def obter_hora_aperfeicoamento_presencial_tag(file_path):
    return obter_horas(file_path, '1117374 SENAI Gama', '58 Aperfeiçoamento/Especialização Profissional', '1 Presencial', 'aperfei_presen')

def obter_hora_aperfeicoamento_distancia_tag(file_path):
    return obter_horas(file_path, '1117374 SENAI Gama', '58 Aperfeiçoamento/Especialização Profissional', '2 A distância', 'aperfei_distan')

def obter_hora_qualificacao_iti_presencial_tag(file_path):
    return obter_horas(file_path, '1117374 SENAI Gama', '22 Qualificação Profissional - Itinerário V Ensino Médio', '1 Presencial', 'qualifi_iti_presen')

def obter_hora_aprendizagem_tec_presencial_tag(file_path):
    return obter_horas(file_path, '1117374 SENAI Gama', '15 Aprendizagem Industrial Técnica de Nível Médio', '1 Presencial', 'aprendi_tec_presen')

def obter_hora_tecnico_presencial_tag(file_path):
    return obter_horas(file_path, '1117374 SENAI Gama', '31 Técnico de Nível Médio', '1 Presencial', 'tecni_presen')

def obter_hora_tecnico_distancia_tag(file_path):
    return obter_horas(file_path, '1117374 SENAI Gama', '31 Técnico de Nível Médio', '2 A distância', 'tecni_distan')

def obter_hora_tecnico_iti_presencial_tag(file_path):
    return obter_horas(file_path, '1117374 SENAI Gama', '32 Técnico de Nível Médio - Itinerário V Ensino Médio', '1 Presencial', 'tecni_iti_presen')

funcoes_ha = {

    'horas': {
        'iniciacao_presencial': obter_hora_iniciacao_presencial_tag,
        'iniciacao_distancia': obter_hora_iniciacao_distancia_tag,
        'aprendizagem_presencial': obter_hora_aprendizagem_presencial_tag,
        'qualificacao_presencial': obter_hora_qualificacao_presencial_tag,
        'aprendizagem_distancia': obter_hora_aprendizagem_distancia_tag,
        'qualificacao_distancia': obter_hora_qualificacao_distancia_tag,
        'aperfeicoamento_presencial': obter_hora_aperfeicoamento_presencial_tag,
        'aperfeicoamento_distancia': obter_hora_aperfeicoamento_distancia_tag,
        'qualificacao_iti_presencial': obter_hora_qualificacao_iti_presencial_tag,
        'aprendizagem_tec_presencial': obter_hora_aprendizagem_tec_presencial_tag,
        'tecnico_nm_presencial': obter_hora_tecnico_presencial_tag,
        'tecnico_nm_distancia': obter_hora_tecnico_distancia_tag,
        'tecnico_nm_iti_presencial': obter_hora_tecnico_iti_presencial_tag
    },
}

def obter_dados_por_tipo(categoria, tipo, arquivo):
    chave = f"{categoria}_{tipo}"
    return {
        'horas': funcoes_ha['horas'].get(chave, lambda x: 0)(arquivo), 
    }
