from supabase import create_client, Client

url = "https://rrlcjzoliigmswfbnzgz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJybGNqem9saWlnbXN3ZmJuemd6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjUzNzEwODQsImV4cCI6MjA0MDk0NzA4NH0.O9QG-fope78SqhveVEwDzwU37ZZjOMTf__m7zbsAY3w"

supabase: Client = create_client(url, key)

def obter_evadidos(unidade, modalidade, tipo_acao, chave_prefixo):
    class EvadidosPorTipoFinanciamento:
        def __init__(self, supabase_client):
            self.supabase = supabase_client
        
        def contar_evadidos(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento,tipo_situacao):
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
        
    evariculas_por_tipo = EvadidosPorTipoFinanciamento(supabase)

    # Mapeamento dos tipos de financiamento para consolidar
    mapa_financiamento = {
        '1 Gratuidade Regimental': [
            '1 Gratuidade Regimental', 
            '101 Emprega + Novo Emprego (desempregados)', 
            '104 Novo Brasil Mais Produtivo'
        ],
        '9 Pago por Pessoa Fisica ou Empresa': [
            '9 Pago por Pessoa Fisica ou Empresa', 
            '901 Pago pelo SESI', 
            '903 Pago pela Rede Privada de Educação'
        ],
        '2 Gratuidade Não Regimental': ['2 Gratuidade Não Regimental'],
        '3 Convênio': ['3 Convênio']
    }

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
    
        # Coleta as matrículas para cada mês e tipo de financiamento consolidado
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento_padrao, tipos_equivalentes in mapa_financiamento.items():
            chave_resultado = f"{mes_atual}_{chave_prefixo}_{tipo_financiamento_padrao}"
            
            # Inicializa a soma de matrículas para os tipos equivalentes dentro do tipo padrão
            total_evadidos = 0
            
            # Conta as matrículas para cada tipo equivalente e acumula no total
            for tipo in tipos_equivalentes:
                total_evadidos += evariculas_por_tipo.contar_evadidos(
                    unidade, modalidade, tipo_acao, '102024', mes_referencia, '2024', tipo, '4 Evadida'
                )
            
            # Armazena o total de matrículas para a chave de financiamento consolidada
            resultados_eva[chave_resultado] = total_evadidos

    return resultados_eva

def obter_evadidos_iniciacao_presencial_sig():
    return obter_evadidos('5325373 SENAI SIG', '5 Iniciação Profissional', '1 Presencial', 'inicia_presen_eva')

def obter_evadidos_iniciacao_distancia_sig():
    return obter_evadidos('5325373 SENAI SIG', '5 Iniciação Profissional', '2 A distância', 'inicia_distan_eva')

def obter_evadidos_aprendizagem_presencial_sig():
    return obter_evadidos('5325373 SENAI SIG', '11 Aprendizagem Industrial básica', '1 Presencial', 'aprendi_presen_eva')

def obter_evadidos_qualificacao_presencial_sig():
    return obter_evadidos('5325373 SENAI SIG', '21 Qualificação Profissional', '1 Presencial', 'qualifi_presen_eva')

def obter_evadidos_aprendizagem_distancia_sig():
    return obter_evadidos('5325373 SENAI SIG', '11 Aprendizagem Industrial básica', '2 A distância', 'aprendi_distan_eva')

def obter_evadidos_qualificacao_distancia_sig():
    return obter_evadidos('5325373 SENAI SIG', '21 Qualificação Profissional', '2 A distância', 'qualifi_distan_eva')

def obter_evadidos_aperfeicoamento_presencial_sig():
    return obter_evadidos('5325373 SENAI SIG', '58 Aperfeiçoamento/Especialização Profissional', '1 Presencial', 'aperfei_presen_eva')

def obter_evadidos_aperfeicoamento_distancia_sig():
    return obter_evadidos('5325373 SENAI SIG', '58 Aperfeiçoamento/Especialização Profissional', '2 A distância', 'aperfei_distan_eva')

def obter_evadidos_qualificacao_itine_presencial_sig():
    return obter_evadidos('5325373 SENAI SIG', '22 Qualificação Profissional - Itinerário V Ensino Médio', '1 Presencial', 'qualifi_iti_presen_eva')

def obter_evadidos_aprendizagem_tecnica_presencial_sig():
    return obter_evadidos('5325373 SENAI SIG', '15 Aprendizagem Industrial Técnica de Nível Médio', '1 Presencial', 'aprendi_tec_presen_eva')

def obter_evadidos_tecnico_presencial_sig():
    return obter_evadidos('5325373 SENAI SIG', '31 Técnico de Nível Médio', '1 Presencial', 'tecni_presen_eva')

def obter_evadidos_tecnico_distancia_sig():
    return obter_evadidos('5325373 SENAI SIG', '31 Técnico de Nível Médio', '2 A distância', 'tecni_distan_eva')

def obter_evadidos_tecnico_iti_presencial_sig():
    return obter_evadidos('5325373 SENAI SIG', '32 Técnico de Nível Médio - Itinerário V Ensino Médio', '1 Presencial', 'tecni_iti_presen_eva')

funcoes_eva = {
    
    'evadidos': {
        'iniciacao_presencial': obter_evadidos_iniciacao_presencial_sig,
        'iniciacao_distancia': obter_evadidos_iniciacao_distancia_sig,
        'aprendizagem_presencial': obter_evadidos_aprendizagem_presencial_sig,
        'qualificacao_presencial': obter_evadidos_qualificacao_presencial_sig,
        'aprendizagem_distancia': obter_evadidos_aprendizagem_distancia_sig,
        'qualificacao_distancia': obter_evadidos_qualificacao_distancia_sig,
        'aperfeicoamento_presencial': obter_evadidos_aperfeicoamento_presencial_sig,
        'aperfeicoamento_distancia': obter_evadidos_aperfeicoamento_distancia_sig,
        'qualificacao_iti_presencial': obter_evadidos_tecnico_iti_presencial_sig,
        'aprendizagem_tec_presencial': obter_evadidos_aprendizagem_tecnica_presencial_sig,
        'tecnico_nm_presencial': obter_evadidos_tecnico_presencial_sig,
        'tecnico_nm_distancia': obter_evadidos_tecnico_distancia_sig,
        'tecnico_nm_iti_presencial': obter_evadidos_tecnico_iti_presencial_sig
    },
}

def obter_dados_por_tipo(categoria, tipo):
    chave = f"{categoria}_{tipo}"
    return {
        'evadidos': funcoes_eva['evadidos'][chave](), 
    }