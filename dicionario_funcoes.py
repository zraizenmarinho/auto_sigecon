meses = [
    ("jan", "jan_11 Aprendizagem Industrial básica_1 Presencial_ha_1 Gratuidade Regimental")
    ("fev", "fev_11 Aprendizagem Industrial básica_1 Presencial_ha_1 Gratuidade Regimental"),
    ("mar", "mar_11 Aprendizagem Industrial básica_1 Presencial_ha_1 Gratuidade Regimental"),
    ("abr", "abr_11 Aprendizagem Industrial básica_1 Presencial_ha_1 Gratuidade Regimental"),
    ("mai", "mai_11 Aprendizagem Industrial básica_1 Presencial_ha_1 Gratuidade Regimental"),
    ("jun", "jun_11 Aprendizagem Industrial básica_1 Presencial_ha_1 Gratuidade Regimental"),
    ("jul", "jul_11 Aprendizagem Industrial básica_1 Presencial_ha_1 Gratuidade Regimental"),
    ("ago", "ago_11 Aprendizagem Industrial básica_1 Presencial_ha_1 Gratuidade Regimental"),
    ("set", "set_11 Aprendizagem Industrial básica_1 Presencial_ha_1 Gratuidade Regimental"),
    ("out", "out_11 Aprendizagem Industrial básica_1 Presencial_ha_1 Gratuidade Regimental"),
    ("nov", "nov_11 Aprendizagem Industrial básica_1 Presencial_ha_1 Gratuidade Regimental"),
    ("dez", "dez_11 Aprendizagem Industrial básica_1 Presencial_ha_1 Gratuidade Regimental")
]



# Matricula Janeiro
from si_janeiro_m_c_e import (
    #tag_iniciacao_presencial,
    #tag_iniciacao_distancia,
    #tag_aprendizagem_presencial,
    #tag_qualificacao_presencial,
    #tag_aprendizagem_distancia,
    #tag_qualificacao_distancia,
    #tag_aperfeicoamento_presencial,
    tag_aperfeicoamento_distancia,
    tag_qualificacao_iti_presencial,
    tag_aprendizagem_tec,
    tag_tecnico_presencial,
    tag_tecnico_distancia,
    tag_tecnico_iti_presencial
)

dados = {
    'iniciacao': {
        'presencial': obter_dados_por_tipo('iniciacao', 'presencial', arquivo),
        'distancia': obter_dados_por_tipo('iniciacao', 'distancia', arquivo)
    },
    'aprendizagem': {
        'presencial': obter_dados_por_tipo('aprendizagem', 'presencial', arquivo),
        'distancia': obter_dados_por_tipo('aprendizagem', 'distancia', arquivo)
    },
    'qualificacao': {
        'presencial': obter_dados_por_tipo('qualificacao', 'presencial', arquivo),
        'distancia': obter_dados_por_tipo('qualificacao', 'distancia', arquivo)
    },
    'aperfeicoamento': {
        'presencial': obter_dados_por_tipo('aperfeicoamento', 'presencial', arquivo),
        'distancia': obter_dados_por_tipo('aperfeicoamento', 'distancia', arquivo)
    },
    'qualificacao_iti': {
        'presencial': obter_dados_por_tipo('qualificacao_iti', 'presencial', arquivo)
    },
    'aprendizagem_tec': {
        'presencial': obter_dados_por_tipo('aprendizagem_tec', 'presencial', arquivo)
    },
    'tecnico_nm': {
        'presencial': obter_dados_por_tipo('tecnico_nm', 'presencial', arquivo),
        'distancia': obter_dados_por_tipo('tecnico_nm', 'distancia', arquivo)
    },
    'tecnico_nm_iti': {
        'presencial': obter_dados_por_tipo('tecnico_nm_iti', 'presencial', arquivo),
    }
}