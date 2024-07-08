import pandas as pd
import dask.dataframe as dd


arquivo = 'si_jan.xlsx'

def obter_hora_iniciacao_presencial_tag(arquivo):
    return f"{arquivo}: hora_iniciacao_presencial"

def obter_matriculas_iniciacao_presencial_tag(arquivo):
    return f"{arquivo}: mat_iniciacao_presencial_geral"

def obter_concluintes_iniciacao_presencial_tag(arquivo):
    return f"{arquivo}: con_iniciacao_presencial"

def obter_evadidos_iniciacao_presencial_tag(arquivo):
    return f"{arquivo}: eva_iniciacao_presencial"

#iniciacao Distancia

def obter_hora_iniciacao_distancia_tag(arquivo):
    return f"{arquivo}: hora_iniciacao_distancia"

def obter_matriculas_iniciacao_distancia_tag(arquivo):
    return f"{arquivo}: mat_iniciacao_distancia"

def obter_concluintes_iniciacao_distancia_tag(arquivo):
    return f"{arquivo}: con_iniciacao_distancia"

def obter_evadidos_iniciacao_distancia_tag(arquivo):
    return f"{arquivo}: eva_iniciacao_distancia"

#Aprendizagem Industrual

def obter_hora_aprendizagem_presencial_tag(arquivo):
    return f"{arquivo}: hora_aprendizagem_presencial"

def obter_matriculas_aprendizagem_presencial_tag(arquivo):
    return f"{arquivo}: mat_aprendizagem_presencial_geral"

def obter_concluintes_aprendizagem_presencial_tag(arquivo):
    return f"{arquivo}: con_aprendizagem_presencial"

def obter_evadidos_aprendizagem_presencial_tag(arquivo):
    return f"{arquivo}: eva_aprendizagem_presencial"

#Qualificacao Presencial

def obter_hora_qualificacao_presencial_tag(arquivo):
    return f"{arquivo}: hora_qualificacao_presencial"

def obter_matriculas_qualificacao_presencial_tag(arquivo):
    return f"{arquivo}: mat_qualificacao_presencial_geral"

def obter_concluintes_qualificacao_presencial_tag(arquivo):
    return f"{arquivo}: con_qualificacao_presencial"

def obter_evadidos_qualificacao_presencial_tag(arquivo):
    return f"{arquivo}: eva_qualificacao_presencial"

#Aprendizagem Distnacia

def obter_hora_aprendizagem_distancia_tag(arquivo):
    return f"{arquivo}: hora_aprendizagem_distancia"

def obter_matriculas_aprendizagem_distancia_tag(arquivo):
    return f"{arquivo}: mat_aprendizagem_distancia_geral"

def obter_concluintes_aprendizagem_distancia_tag(arquivo):
    return f"{arquivo}: con_aprendizagem_distancia"

def obter_evadidos_aprendizagem_distancia_tag(arquivo):
    return f"{arquivo}: eva_aprendizagem_distancia"


# Qualificacao Distancia

def obter_hora_qualificacao_distancia_tag(arquivo):
    return f"{arquivo}: hora_qualificacao_distancia"

def obter_matriculas_qualificacao_distancia_tag(arquivo):
    return f"{arquivo}: mat_qualificacao_distancia_geral"

def obter_concluintes_qualificacao_distancia_tag(arquivo):
    return f"{arquivo}: con_qualificacao_distancia"

def obter_evadidos_qualificacao_distancia_tag(arquivo):
    return f"{arquivo}: eva_qualificacao_distancia"

#Aperfeicoamento Presencial

def obter_hora_aperfeicoamento_presencial_tag(arquivo):
    return f"{arquivo}: hora_aperfeicoamento_presencial"

def obter_matriculas_aperfeicoamento_presencial_tag(arquivo):
    return f"{arquivo}: mat_aperfeicoamento_presencial_geral"

def obter_concluintes_aperfeicoamento_presencial_tag(arquivo):
    return f"{arquivo}: con_aperfeicoamento_presencial"

def obter_evadidos_aperfeicoamento_presencial_tag(arquivo):
    return f"{arquivo}: eva_aperfeicoamento_presencial"

#Aperfeicoamento Distancia

def obter_hora_aperfeicoamento_distancia_tag(arquivo):
    return f"{arquivo}: hora_aperfeicoamento_distancia"

def obter_matriculas_aperfeicoamento_distancia_tag(arquivo):
    return f"{arquivo}: mat_aperfeicoamento_distancia_geral"

def obter_concluintes_aperfeicoamento_distancia_tag(arquivo):
    return f"{arquivo}: con_aperfeicoamento_distancia"

def obter_evadidos_aperfeicoamento_distancia_tag(arquivo):
    return f"{arquivo}: eva_aperfeicoamento_distancia"

#Qualificacao Iti

def obter_hora_qualificacao_iti_presencial_tag(arquivo):
    return f"{arquivo}: hora_qualificacao_iti_presencial"

def obter_matriculas_qualificacao_itine_presencial_tag(arquivo):
    return f"{arquivo}: mat_qualificacao_iti_presencial_geral"

def obter_concluintes_qualificacao_itine_presencial_tag(arquivo):
    return f"{arquivo}: con_qualificacao_iti_presencial"

def obter_evadidos_qualificacao_itine_presencial_tag(arquivo):
    return f"{arquivo}: eva_qualificacao_iti_presencial"

#Aprendizagem Tecn

def obter_hora_aprendizagem_tec_presencial_tag(arquivo):
    return f"{arquivo}: hora_aprendizagem_tec_presencial"

def obter_matriculas_aprendizagem_tecnica_presencial_tag(arquivo):
    return f"{arquivo}: mat_aprendizagem_tec_presencial_geral"

def obter_concluintes_aprendizagem_tecnica_presencial_tag(arquivo):
    return f"{arquivo}: con_aprendizagem_tec_presencial"

def obter_evadidos_aprendizagem_tecnica_presencial_tag(arquivo):
    return f"{arquivo}: eva_aprendizagem_tec_presencial"

#Tecnico Presencial

def obter_hora_tecnico_presencial_tag(arquivo):
    return f"{arquivo}: hora_tecnico_nm_presencial"

def obter_matriculas_tecnico_presencial_tag(arquivo):
    return f"{arquivo}: mat_tecnico_nm_presencial_geral"

def obter_concluintes_tecnico_presencial_tag(arquivo):
    return f"{arquivo}: con_tecnico_nm_presencial"

def obter_evadidos_tecnico_presencial_tag(arquivo):
    return f"{arquivo}: eva_tecnico_nm_tec_presencial"

#Tecnico Distancia

def obter_hora_tecnico_distancia_tag(arquivo):
    return f"{arquivo}: hora_tecnico_nm_distancia"

def obter_matriculas_tecnico_distancia_tag(arquivo):
    return f"{arquivo}: mat_tecnico_nm_distancia_geral"

def obter_concluintes_tecnico_distancia_tag(arquivo):
    return f"{arquivo}: con_tecnico_nm_distancia"

def obter_evadidos_tecnico_distancia_tag(arquivo):
    return f"{arquivo}: eva_tecnico_nm_tec_distancia"

#Tecnico Itinerario

def obter_hora_tecnico_iti_presencial_tag(arquivo):
    return f"{arquivo}: hora_tecnico_iti_nm_presencial"

def obter_matriculas_tecnico_iti_presencial_tag(arquivo):
    return f"{arquivo}: mat_tecnico_iti_nm_presencial"

def obter_concluintes_tecnico_iti_presencial_tag(arquivo):
    return f"{arquivo}: con_tecnico_iti_nm_presencial"

def obter_evadidos_tecnico_iti_presencial_tag(arquivo):
    return f"{arquivo}: eva_tecnico_iti_nm_presencial"

funcoes = {
    'hora': {
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

    'concluintes': {
        'iniciacao_presencial': obter_concluintes_iniciacao_presencial_tag,
        'iniciacao_distancia': obter_concluintes_iniciacao_distancia_tag,
        'aprendizagem_presencial': obter_concluintes_aprendizagem_presencial_tag,
        'qualificacao_presencial': obter_concluintes_qualificacao_presencial_tag,
        'aprendizagem_distancia': obter_concluintes_aprendizagem_distancia_tag,
        'qualificacao_distancia': obter_concluintes_qualificacao_distancia_tag,
        'aperfeicoamento_presencial': obter_concluintes_aperfeicoamento_presencial_tag,
        'aperfeicoamento_distancia': obter_concluintes_aperfeicoamento_distancia_tag,
        'qualificacao_iti_presencial':obter_concluintes_qualificacao_itine_presencial_tag,
        'aprendizagem_tec_presencial': obter_concluintes_aprendizagem_tecnica_presencial_tag,
        'tecnico_nm_presencial': obter_concluintes_tecnico_presencial_tag,
        'tecnico_nm_distancia': obter_concluintes_tecnico_distancia_tag,
        'tecnico_nm_iti_presencial': obter_concluintes_tecnico_iti_presencial_tag
    },

    'evadidos': {
        'iniciacao_presencial': obter_evadidos_iniciacao_presencial_tag,
        'iniciacao_distancia': obter_evadidos_iniciacao_distancia_tag,
        'aprendizagem_presencial': obter_evadidos_aprendizagem_presencial_tag,
        'qualificacao_presencial': obter_evadidos_qualificacao_presencial_tag,
        'aprendizagem_distancia': obter_evadidos_aprendizagem_distancia_tag,
        'qualificacao_distancia': obter_evadidos_qualificacao_distancia_tag,
        'aperfeicoamento_presencial': obter_evadidos_aperfeicoamento_presencial_tag,
        'aperfeicoamento_distancia': obter_evadidos_aperfeicoamento_distancia_tag,
        'qualificacao_iti_presencial': obter_evadidos_qualificacao_itine_presencial_tag,
        'aprendizagem_tec_presencial': obter_evadidos_aprendizagem_tecnica_presencial_tag,
        'tecnico_nm_presencial': obter_evadidos_tecnico_presencial_tag,
        'tecnico_nm_distancia': obter_evadidos_tecnico_distancia_tag,
        'tecnico_nm_iti_presencial': obter_evadidos_tecnico_iti_presencial_tag
    }
}

def obter_dados_por_tipo(categoria, tipo, arquivo):
    chave = f"{categoria}_{tipo}"
    return {
        'hora': funcoes['hora'][chave](arquivo),
        'matriculas': funcoes['matriculas'][chave](arquivo),
        'concluintes': funcoes['concluintes'][chave](arquivo),
        'evadidos': funcoes['evadidos'][chave](arquivo)
    }

