import pandas as pd
import openpyxl
import numpy as np
import si_janeiro
import pandas as pd

# SENAI TAGUATINGA INICIAÇÃO PROFISSIONAL PRESENCIAl #################################################################


def obter_hora_por_tipo(file_path):
    class HorasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)

        def somar_hora(self, unidade, modalidade, tipo_acao, mes_referencia, tipo_financiamento):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_ref = self.data['MES_REFERENCIA'].astype(str).isin(mes_referencia)
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_ref & filtro_finan]

            soma_hora_aluno = base_filtrada['HORA_ALUNO'].sum()
            soma_hora_aluno_ead = base_filtrada['HORA_ALUNO_EAD'].sum()

            return soma_hora_aluno + soma_hora_aluno_ead

    hora_aluno_por_tipo = HorasPorTipoFinanciamento(file_path)


    meses = {
        'jan': ['12024'],
        'fev': ['22024'],
        'mar': ['32024'],
        'abr': ['42024'],
        'mai': ['52024'],
        'jun': ['62024'],
        'jul': ['72024'],
        'ago': ['82024'],
        'set': ['92024'],
        'out': ['102024'],
        'nov': ['112024'],
        'dez': ['122024']
    }

    resultados_ha = {}

    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_ip_ha_{tipo_financiamento}"
            resultados_ha[chave_resultado] = hora_aluno_por_tipo.somar_hora('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', mes_referencia, tipo_financiamento)

    for idx, (mes_atual, mes_referencia) in enumerate(meses.items()):
        if idx == 0:
            continue

        mes_anterior_str = str(int(mes_referencia[0]) - 1).zfill(2)
        mes_anterior = [mes_anterior_str]

        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado_atual = f"{mes_atual}_ip_ha_{tipo_financiamento}"
            chave_resultado_anterior = f"{list(meses.keys())[idx-1]}_ip_ha_{tipo_financiamento}"
            
            resultado_atual = resultados_ha[chave_resultado_atual]
            soma_meses_anteriores = sum(resultados_ha[f"{list(meses.keys())[i]}_ip_ha_{tipo_financiamento}"] for i in range(idx))
            resultados_ha[chave_resultado_atual] -= soma_meses_anteriores

            if resultados_ha[chave_resultado_atual] < 0:
                resultados_ha[chave_resultado_atual] = 0


    return resultados_ha


# SENAI TAGUATINGA INICIAÇÃO PROFISSIONAL DISTANCIA #####################################################################

def obter_hora_IPD_TAG(file_path):
    class HorasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)

        def somar_hora(self, unidade, modalidade, tipo_acao, mes_referencia, tipo_financiamento):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_ref = self.data['MES_REFERENCIA'].astype(str).isin(mes_referencia)
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_ref & filtro_finan]

            soma_hora_aluno = base_filtrada['HORA_ALUNO'].sum()
            soma_hora_aluno_ead = base_filtrada['HORA_ALUNO_EAD'].sum()

            return soma_hora_aluno + soma_hora_aluno_ead

    hora_aluno_por_tipo = HorasPorTipoFinanciamento(file_path)


    meses = {
        'jan': ['12024'],
        'fev': ['22024'],
        'mar': ['32024'],
        'abr': ['42024'],
        'mai': ['52024'],
        'jun': ['62024'],
        'jul': ['72024'],
        'ago': ['82024'],
        'set': ['92024'],
        'out': ['102024'],
        'nov': ['112024'],
        'dez': ['122024']
    }

    resultados_ha = {}

    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_ipd_ha_{tipo_financiamento}"
            resultados_ha[chave_resultado] = hora_aluno_por_tipo.somar_hora('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '2 A distância', mes_referencia, tipo_financiamento)

    for idx, (mes_atual, mes_referencia) in enumerate(meses.items()):
        if idx == 0:
            continue

        mes_anterior_str = str(int(mes_referencia[0]) - 1).zfill(2)
        mes_anterior = [mes_anterior_str]

        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado_atual = f"{mes_atual}_ipd_ha_{tipo_financiamento}"
            chave_resultado_anterior = f"{list(meses.keys())[idx-1]}_ipd_ha_{tipo_financiamento}"
            
            resultado_atual = resultados_ha[chave_resultado_atual]
            soma_meses_anteriores = sum(resultados_ha[f"{list(meses.keys())[i]}_ipd_ha_{tipo_financiamento}"] for i in range(idx))
            resultados_ha[chave_resultado_atual] -= soma_meses_anteriores

            if resultados_ha[chave_resultado_atual] < 0:
                resultados_ha[chave_resultado_atual] = 0


    return resultados_ha