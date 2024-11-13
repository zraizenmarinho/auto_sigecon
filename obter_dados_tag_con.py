from supabase import create_client, Client

url = "https://rrlcjzoliigmswfbnzgz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJybGNqem9saWlnbXN3ZmJuemd6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjUzNzEwODQsImV4cCI6MjA0MDk0NzA4NH0.O9QG-fope78SqhveVEwDzwU37ZZjOMTf__m7zbsAY3w"

supabase: Client = create_client(url, key)

def obter_concluintes(unidade, modalidade, tipo_acao, chave_prefixo):
    class ConcluintesPorTipoFinanciamento:
        def __init__(self, supabase_client):
            self.supabase = supabase_client
        
        def contar_concluintes(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento,tipo_situacao):
            response = self.supabase.table("si_ep").select("*") \
                .eq("UNIDADE_ATENDIMENTO", unidade) \
                .eq("MODALIDADE", modalidade) \
                .eq("TIPO_ACAO", tipo_acao) \
                .eq("MES_REFERENCIA", mes_rela) \
                .eq("DT_SAIDA_MÊS", mes_referencia) \
                .eq("DT_SAIDA_ANO", anos_referencia) \
                .eq("TIPO_FINANCIAMENTO", tipo_financiamento) \
                .eq("SITUACAO_MATRICULA", tipo_situacao) \
                .execute()
            data = response.data
            return len(data)
        
    conriculas_por_tipo = ConcluintesPorTipoFinanciamento(supabase)

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
            resultados_con[chave_resultado] = conriculas_por_tipo.contar_concluintes(
                unidade, modalidade, tipo_acao, '92024', mes_referencia, '2024', tipo_financiamento, '2 Concluída'
            )
    
    return resultados_con


def obter_concluintes_iniciacao_presencial_tag():
    return obter_concluintes('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', 'inicia_presen_con')

def obter_concluintes_iniciacao_distancia_tag():
    return obter_concluintes('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '2 A distância', 'inicia_distan_con')

def obter_concluintes_aprendizagem_presencial_tag():
    return obter_concluintes('1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '1 Presencial', 'aprendi_presen_con')

def obter_concluintes_qualificacao_presencial_tag():
    return obter_concluintes('1117376 SENAI Taguatinga', '21 Qualificação Profissional', '1 Presencial', 'qualifi_presen_con')

def obter_concluintes_aprendizagem_distancia_tag():
    return obter_concluintes('1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '2 A distância', 'aprendi_distan_con')

def obter_concluintes_qualificacao_distancia_tag():
    return obter_concluintes('1117376 SENAI Taguatinga', '21 Qualificação Profissional', '2 A distância', 'qualifi_distan_con')

def obter_concluintes_aperfeicoamento_presencial_tag():
    return obter_concluintes('1117376 SENAI Taguatinga', '58 Aperfeiçoamento/Especialização Profissional', '1 Presencial', 'aperfei_presen_con')

def obter_concluintes_aperfeicoamento_distancia_tag():
    return obter_concluintes('1117376 SENAI Taguatinga', '58 Aperfeiçoamento/Especialização Profissional', '2 A distância', 'aperfei_distan_con')

def obter_concluintes_qualificacao_itine_presencial_tag():
    return obter_concluintes('1117376 SENAI Taguatinga', '22 Qualificação Profissional - Itinerário V Ensino Médio', '1 Presencial', 'qualifi_iti_presen_con')

def obter_concluintes_aprendizagem_tecnica_presencial_tag():
    return obter_concluintes('1117376 SENAI Taguatinga', '15 Aprendizagem Industrial Técnica de Nível Médio', '1 Presencial', 'aprendi_tec_presen_con')

def obter_concluintes_tecnico_presencial_tag():
    return obter_concluintes('1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '1 Presencial', 'tecni_presen_con')

def obter_concluintes_tecnico_distancia_tag():
    return obter_concluintes('1117376 SENAI Taguatinga', '31 Técnico de Nível Médio', '2 A distância', 'tecni_distan_con')

def obter_concluintes_tecnico_iti_presencial_tag():
    return obter_concluintes('1117376 SENAI Taguatinga', '32 Técnico de Nível Médio - Itinerário V Ensino Médio', '1 Presencial', 'tecni_iti_presen_con')

funcoes_con = {
    
    'concluintes': {
        'iniciacao_presencial': obter_concluintes_iniciacao_presencial_tag,
        'iniciacao_distancia': obter_concluintes_iniciacao_distancia_tag,
        'aprendizagem_presencial': obter_concluintes_aprendizagem_presencial_tag,
        'qualificacao_presencial': obter_concluintes_qualificacao_presencial_tag,
        'aprendizagem_distancia': obter_concluintes_aprendizagem_distancia_tag,
        'qualificacao_distancia': obter_concluintes_qualificacao_distancia_tag,
        'aperfeicoamento_presencial': obter_concluintes_aperfeicoamento_presencial_tag,
        'aperfeicoamento_distancia': obter_concluintes_aperfeicoamento_distancia_tag,
        'qualificacao_iti_presencial': obter_concluintes_tecnico_iti_presencial_tag,
        'aprendizagem_tec_presencial': obter_concluintes_aprendizagem_tecnica_presencial_tag,
        'tecnico_nm_presencial': obter_concluintes_tecnico_presencial_tag,
        'tecnico_nm_distancia': obter_concluintes_tecnico_distancia_tag,
        'tecnico_nm_iti_presencial': obter_concluintes_tecnico_iti_presencial_tag
    },
}

def obter_dados_por_tipo(categoria, tipo):
    chave = f"{categoria}_{tipo}"
    return {
        'concluintes': funcoes_con['concluintes'][chave](), 
    }