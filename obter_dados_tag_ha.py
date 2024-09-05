import pandas as pd
from supabase import create_client, Client

url = "https://rrlcjzoliigmswfbnzgz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJybGNqem9saWlnbXN3ZmJuemd6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjUzNzEwODQsImV4cCI6MjA0MDk0NzA4NH0.O9QG-fope78SqhveVEwDzwU37ZZjOMTf__m7zbsAY3w"

supabase: Client = create_client(url, key)

def obter_horas(unidade, modalidade, tipo_acao, chave_prefixo):
    class HorasPorTipoFinanciamento:
        def __init__(self, supabase_client):
            self.supabase = supabase_client
        
        def somar_horas(self, unidade, modalidade, tipo_acao, mes_rela, tipo_financiamento):
            response = self.supabase.table("si_ep").select("*") \
                .eq("UNIDADE_ATENDIMENTO", unidade) \
                .eq("MODALIDADE", modalidade) \
                .eq("TIPO_ACAO", tipo_acao) \
                .eq("MES_REFERENCIA", mes_rela) \
                .eq("TIPO_FINANCIAMENTO", tipo_financiamento) \
                .execute()

            data = response.data
            #converter a lista de dicionários para DataFrame
            df = pd.DataFrame(data)

            #verificar se as colunas existem e somar as horas
            if 'HORA_ALUNO' in df.columns:
                soma_hora_aluno = df['HORA_ALUNO'].sum()
            else:
                soma_hora_aluno = 0
            
            if 'HORA_ALUNO_EAD' in df.columns:
                soma_hora_aluno_ead = df['HORA_ALUNO_EAD'].sum()
            else:
                soma_hora_aluno_ead = 0

            return soma_hora_aluno + soma_hora_aluno_ead
    
    hora_por_tipo = HorasPorTipoFinanciamento(supabase)

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

    #coleta as horas para cada mês e tipo de financiamento
    for mes_atual, mes_rela in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_{chave_prefixo}_ha_{tipo_financiamento}"
            resultados_ha[chave_resultado] = hora_por_tipo.somar_horas(
                unidade, modalidade, tipo_acao, mes_rela, tipo_financiamento)

    #ajusta as horas subtraindo as horas dos meses anteriores e gravando na variavel
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


def obter_hora_iniciacao_presencial_tag():
    return obter_horas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', 'inicia_presen')

def obter_hora_iniciacao_distancia_tag():
    return obter_horas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '2 A distância', 'inicia_distan')

def obter_hora_aprendizagem_presencial_tag():
    return obter_horas('1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '1 Presencial', 'aprendi_presen')

def obter_hora_qualificacao_presencial_tag():
    return obter_horas('1117376 SENAI Taguatinga', '21 Qualificação Profissional', '1 Presencial', 'qualifi_presen')

def obter_hora_aprendizagem_distancia_tag():
    return obter_horas('1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '2 A distância', 'aprendi_distan')

def obter_hora_qualificacao_distancia_tag():
    return obter_horas('1117376 SENAI Taguatinga', '21 Qualificação Profissional', '2 A distância', 'qualifi_distan')

def obter_hora_aperfeicoamento_presencial_tag():
    return obter_horas('1117376 SENAI Taguatinga', '58 Aperfeiçoamento/Especialização Profissional', '1 Presencial', 'aperfei_presen')

def obter_hora_aperfeicoamento_distancia_tag():
    return obter_horas('1117376 SENAI Taguatinga', '58 Aperfeiçoamento/Especialização Profissional', '2 A distância', 'aperfei_distan')

def obter_hora_qualificacao_iti_presencial_tag():
    return obter_horas('1117376 SENAI Taguatinga', '22 Qualificação Profissional - Itinerário V Ensino Médio', '1 Presencial', 'qualifi_iti_presen')

def obter_hora_aprendizagem_tec_presencial_tag():
    return obter_horas('1117376 SENAI Taguatinga', '15 Aprendizagem Industrial Técnica de Nível Médio', '1 Presencial', 'aprendi_tec_presen')

def obter_hora_tecnico_presencial_tag():
    return obter_horas('1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '1 Presencial', 'tecni_presen')

def obter_hora_tecnico_distancia_tag():
    return obter_horas('1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '2 A distância', 'tecni_distan')

def obter_hora_tecnico_iti_presencial_tag():
    return obter_horas('1117376 SENAI Taguatinga', '32 Técnico de Nível Médio - Itinerário V Ensino Médio', '1 Presencial', 'tecni_iti_presen')


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

def obter_dados_por_tipo(categoria, tipo):
    chave = f"{categoria}_{tipo}"
    return {
        'horas': funcoes_ha['horas'].get(chave, lambda x: 0)(), 
    }
