import pandas as pd
import dask.dataframe as dd

def inicializar_horas_por_tipo(file_path):
    pandas_df = pd.read_excel(file_path)
    data = dd.from_pandas(pandas_df, npartitions=1)
    return data

def somar_horas(hora_aluno_por_tipo, unidade, modalidade, tipo_acao, mes_referencia, tipo_financiamento):
    filtro_uni = hora_aluno_por_tipo['UNIDADE_ATENDIMENTO'] == unidade
    filtro_mod = hora_aluno_por_tipo['MODALIDADE'] == modalidade
    filtro_tipo = hora_aluno_por_tipo['TIPO_ACAO'] == tipo_acao
    filtro_mes_ref = hora_aluno_por_tipo['MES_REFERENCIA'].astype(str).isin(mes_referencia)
    filtro_finan = hora_aluno_por_tipo['TIPO_FINANCIAMENTO'] == tipo_financiamento

    base_filtrada = hora_aluno_por_tipo[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_ref & filtro_finan].compute()

    soma_hora_aluno = base_filtrada['HORA_ALUNO'].sum()
    soma_hora_aluno_ead = base_filtrada['HORA_ALUNO_EAD'].sum()

    return soma_hora_aluno + soma_hora_aluno_ead

def calcular_resultados(meses, hora_aluno_por_tipo, unidade, modalidade, tipo_acao):
    resultados_ha = {}

    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_{modalidade}_{tipo_acao}_ha_{tipo_financiamento}"
            resultados_ha[chave_resultado] = somar_horas(hora_aluno_por_tipo, unidade, modalidade, tipo_acao, mes_referencia, tipo_financiamento)

    for idx, (mes_atual, mes_referencia) in enumerate(meses.items()):
        if idx == 0:
            continue

        mes_anterior_str = str(int(mes_referencia[0]) - 1).zfill(2)
        mes_anterior = [mes_anterior_str]

        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado_atual = f"{mes_atual}_{modalidade}_{tipo_acao}_ha_{tipo_financiamento}"
            chave_resultado_anterior = f"{list(meses.keys())[idx-1]}_{modalidade}_ha_{tipo_financiamento}"
            
            resultados_ha[chave_resultado_atual] -= sum(resultados_ha[f"{list(meses.keys())[i]}_{modalidade}_{tipo_acao}_ha_{tipo_financiamento}"] for i in range(idx))

            if resultados_ha[chave_resultado_atual] < 0:
                resultados_ha[chave_resultado_atual] = 0

    return resultados_ha

def obter_hora_iniciacao_presencial_tag(file_path):
    hora_aluno_por_tipo = inicializar_horas_por_tipo(file_path)

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

    resultados_ha = calcular_resultados(meses, hora_aluno_por_tipo, '1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial')

    return resultados_ha

def obter_hora_iniciacao_distancia_tag(file_path):
    hora_aluno_por_tipo = inicializar_horas_por_tipo(file_path)

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

    resultados_ha = calcular_resultados(meses, hora_aluno_por_tipo, '1117376 SENAI Taguatinga', '5 Iniciação Profissional', '2 A distância')

    return resultados_ha

def obter_hora_aprendizagem_presencial_tag(file_path):
    hora_aluno_por_tipo = inicializar_horas_por_tipo(file_path)

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

    resultados_ha = calcular_resultados(meses, hora_aluno_por_tipo, '1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '1 Presencial')

    return resultados_ha

def obter_hora_qualificacao_presencial_tag(file_path):
    hora_aluno_por_tipo = inicializar_horas_por_tipo(file_path)

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

    resultados_ha = calcular_resultados(meses, hora_aluno_por_tipo, '1117376 SENAI Taguatinga', '21 Qualificação Profissional', '1 Presencial')

    return resultados_ha

def obter_hora_aprendizagem_distancia_tag(file_path):
    hora_aluno_por_tipo = inicializar_horas_por_tipo(file_path)

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

    resultados_ha = calcular_resultados(meses, hora_aluno_por_tipo, '1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '2 A distância')

    return resultados_ha

def obter_hora_qualificacao_distancia_tag(file_path):
    hora_aluno_por_tipo = inicializar_horas_por_tipo(file_path)

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

    resultados_ha = calcular_resultados(meses, hora_aluno_por_tipo, '1117376 SENAI Taguatinga', '21 Qualificação Profissional', '2 A distância')

    return resultados_ha

def obter_hora_aperfeicoamento_presencial_tag(file_path):
    hora_aluno_por_tipo = inicializar_horas_por_tipo(file_path)

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

    resultados_ha = calcular_resultados(meses, hora_aluno_por_tipo, '1117376 SENAI Taguatinga', '58 Aperfeiçoamento/Especialização Profissional', '1 Presencial')

    return resultados_ha

def obter_hora_aperfeicoamento_distancia_tag(file_path):
    hora_aluno_por_tipo = inicializar_horas_por_tipo(file_path)

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

    resultados_ha = calcular_resultados(meses, hora_aluno_por_tipo, '1117376 SENAI Taguatinga', '58 Aperfeiçoamento/Especialização Profissional', '2 A distância')

    return resultados_ha

def obter_hora_qualificacao_iti_presencial_tag(file_path):
    hora_aluno_por_tipo = inicializar_horas_por_tipo(file_path)

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

    resultados_ha = calcular_resultados(meses, hora_aluno_por_tipo, '1117376 SENAI Taguatinga', '22 Qualificação Profissional - Itinerário V Ensino Médio', '1 Presencial')

    return resultados_ha

def obter_hora_aprendizagem_tec_presencial_tag(file_path):
    hora_aluno_por_tipo = inicializar_horas_por_tipo(file_path)

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

    resultados_ha = calcular_resultados(meses, hora_aluno_por_tipo, '1117376 SENAI Taguatinga', '15 Aprendizagem Industrial Técnica de Nível Médio', '1 Presencial')

    return resultados_ha

def obter_hora_tecnico_presencial_tag(file_path):
    hora_aluno_por_tipo = inicializar_horas_por_tipo(file_path)

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

    resultados_ha = calcular_resultados(meses, hora_aluno_por_tipo, '1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '1 Presencial')

    return resultados_ha

def obter_hora_tecnico_distancia_tag(file_path):
    hora_aluno_por_tipo = inicializar_horas_por_tipo(file_path)

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

    resultados_ha = calcular_resultados(meses, hora_aluno_por_tipo, '1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '2 A distância')

    return resultados_ha

def obter_hora_tecnico_iti_presencial_tag(file_path):
    hora_aluno_por_tipo = inicializar_horas_por_tipo(file_path)

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

    resultados_ha = calcular_resultados(meses, hora_aluno_por_tipo, '1117376 SENAI Taguatinga', '32 Técnico de Nível Médio - Itinerário V Ensino Médio', '1 Presencial')

    return resultados_ha


