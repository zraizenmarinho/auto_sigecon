from supabase import create_client, Client

url = "https://rrlcjzoliigmswfbnzgz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJybGNqem9saWlnbXN3ZmJuemd6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjUzNzEwODQsImV4cCI6MjA0MDk0NzA4NH0.O9QG-fope78SqhveVEwDzwU37ZZjOMTf__m7zbsAY3w"

class MatriculasPorTipoFinanciamentoJan:
    def __init__(self, supabase_client: Client):
        self.supabase = supabase_client
    
    def contar_matriculas(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento):
        response = self.supabase.table("si_ep").select("*") \
            .eq("UNIDADE_ATENDIMENTO", unidade) \
            .eq("MODALIDADE", modalidade) \
            .eq("TIPO_ACAO", tipo_acao) \
            .eq("MES_REFERENCIA", mes_rela) \
            .in_("DT_ENTRADA_MÊS", mes_referencia) \
            .in_("DT_ENTRADA_ANO", anos_referencia) \
            .eq("TIPO_FINANCIAMENTO", tipo_financiamento) \
            .execute()
        data = response.data
        return len(data)

def obter_matriculas_por_tipo_jan(supabase_url, supabase_key, unidade, modalidade, tipo_acao):
    supabase_client = create_client(supabase_url, supabase_key)
    matriculas_por_tipo = MatriculasPorTipoFinanciamentoJan(supabase_client)

    mes_rela = '12024'
    mes_referencia = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    anos_referencia = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
    
    jan_mat_regi = matriculas_por_tipo.contar_matriculas(unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, '1 Gratuidade Regimental')
    jan_mat_bolsa = matriculas_por_tipo.contar_matriculas(unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, '2 Gratuidade Não Regimental')
    jan_mat_convenio = matriculas_por_tipo.contar_matriculas(unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, '3 Convênio')
    jan_mat_n_gratuita = matriculas_por_tipo.contar_matriculas(unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, '9 Pago por Pessoa Fisica ou Empresa')

    return {
        "jan_mat_regi": jan_mat_regi,
        "jan_mat_bolsa": jan_mat_bolsa,
        "jan_mat_convenio": jan_mat_convenio,
        "jan_mat_n_gratuita": jan_mat_n_gratuita
    }

sob_iniciacao_presencial = obter_matriculas_por_tipo_jan(url, key, '5171003 SENAI Sobradinho', '5 Iniciação Profissional', '1 Presencial')
sob_iniciacao_distancia = obter_matriculas_por_tipo_jan(url, key, '5171003 SENAI Sobradinho', '5 Iniciação Profissional', '2 A distância')
sob_aprendizagem_presencial = obter_matriculas_por_tipo_jan(url, key, '5171003 SENAI Sobradinho', '11 Aprendizagem Industrial básica', '1 Presencial')
sob_qualificacao_presencial = obter_matriculas_por_tipo_jan(url, key, '5171003 SENAI Sobradinho', '21 Qualificação Profissional', '1 Presencial')
sob_aprendizagem_distancia = obter_matriculas_por_tipo_jan(url, key, '5171003 SENAI Sobradinho', '11 Aprendizagem Industrial básica', '2 A distância')
sob_qualificacao_distancia = obter_matriculas_por_tipo_jan(url, key, '5171003 SENAI Sobradinho', '21 Qualificação Profissional', '2 A distância')
sob_aperfeicoamento_presencial = obter_matriculas_por_tipo_jan(url, key, '5171003 SENAI Sobradinho', '58 Aperfeiçoamento/Especialização Profissional', '1 Presencial')
sob_aperfeicoamento_distancia = obter_matriculas_por_tipo_jan(url, key, '5171003 SENAI Sobradinho', '58 Aperfeiçoamento/Especialização Profissional', '2 A distância')
sob_qualificacao_iti_presencial = obter_matriculas_por_tipo_jan(url, key, '5171003 SENAI Sobradinho', '22 Qualificação Profissional - Itinerário V Ensino Médio', '1 Presencial')
sob_aprendizagem_tec = obter_matriculas_por_tipo_jan(url, key, '5171003 SENAI Sobradinho', '15 Aprendizagem Industrial Técnica de Nível Médio', '1 Presencial')
sob_tecnico_presencial = obter_matriculas_por_tipo_jan(url, key, '5171003 SENAI Sobradinho', '31 Técnico de Nível Médio', '1 Presencial')
sob_tecnico_distancia = obter_matriculas_por_tipo_jan(url, key, '5171003 SENAI Sobradinho', '31 Técnico de Nível Médio', '2 A distância')
sob_tecnico_iti_presencial = obter_matriculas_por_tipo_jan(url, key, '5171003 SENAI Sobradinho', '32 Técnico de Nível Médio - Itinerário V Ensino Médio', '1 Presencial')
