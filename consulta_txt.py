#d = 5044("Bolsa") ("ok)")
#c=  5065("Não Gratuita") 
b = 5106("Regimental")
b = 5102("Bolsa")


janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/227?cd_centro_resp=30303020501&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APERF%2FESPECIALIZ%20PROFISSIONAL%20PRESENCIAL&id_grupo=5&ds_grupo=Aperfei%C3%A7oamento%20Profissional&fase=Realiza%C3%A7%C3%A3o', '_self')")


meses = [
    ("fev", "fev_tecni_iti_presen_mat_1 Gratuidade Regimental"),
    ("mar", "mar_tecni_iti_presen_mat_1 Gratuidade Regimental"),
    ("abr", "abr_tecni_iti_presen_mat_1 Gratuidade Regimental"),
    ("mai", "mai_tecni_iti_presen_mat_1 Gratuidade Regimental"),
    ("jun", "jun_tecni_iti_presen_mat_1 Gratuidade Regimental"),
    ("jul", "jul_tecni_iti_presen_mat_1 Gratuidade Regimental"),
    ("ago", "ago_tecni_iti_presen_mat_1 Gratuidade Regimental"),
    ("set", "set_tecni_iti_presen_mat_1 Gratuidade Regimental"),
    ("out", "out_tecni_iti_presen_mat_1 Gratuidade Regimental"),
    ("nov", "nov_tecni_iti_presen_mat_1 Gratuidade Regimental"),
    ("dez", "dez_tecni_iti_presen_mat_1 Gratuidade Regimental")
]

dados = {
    'iniciacao': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('iniciacao', 'presencial', arquivo)['matriculas'],
        },
        'distancia': {
            'matriculas': obter_dados_por_tipo('iniciacao', 'distancia', arquivo)['matriculas'],
        }
    },
    'aprendizagem': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('aprendizagem', 'presencial', arquivo)['matriculas'],
        },
        'distancia': {
            'matriculas': obter_dados_por_tipo('aprendizagem', 'distancia', arquivo)['matriculas'],
        }
    },
    'qualificacao': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('qualificacao', 'presencial', arquivo)['matriculas'],
        },
        'distancia': {
            'matriculas': obter_dados_por_tipo('qualificacao', 'distancia', arquivo)['matriculas'],
        }
    },
    'aperfeicoamento': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('aperfeicoamento', 'presencial', arquivo)['matriculas'],
        },
        'distancia': {
            'matriculas': obter_dados_por_tipo('aperfeicoamento', 'distancia', arquivo)['matriculas'],
        }
    },
    'qualificacao_iti': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('qualificacao_iti', 'presencial', arquivo)['matriculas'],
        }
    },
    'aprendizagem_tec': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('aprendizagem_tec', 'presencial', arquivo)['matriculas'],
        }
    },
    'tecnico_nm': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('tecnico_nm', 'presencial', arquivo)['matriculas'],
        },
        'distancia': {
            'matriculas': obter_dados_por_tipo('tecnico_nm', 'distancia', arquivo)['matriculas'],
        }
    },
    'tecnico_nm_iti': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('tecnico_nm_iti', 'presencial', arquivo)['matriculas'],
        }
    }
}




{'fev_inicia_presen_mat_1 Gratuidade Regimental': 0, 'fev_inicia_presen_mat_2 Gratuidade Não Regimental': 0, 'fev_inicia_presen_mat_3 Convênio': 0, 'fev_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'mar_inicia_presen_mat_1 Gratuidade Regimental': 0, 'mar_inicia_presen_mat_2 Gratuidade Não Regimental': 0, 'mar_inicia_presen_mat_3 Convênio': 0, 'mar_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'abr_inicia_presen_mat_1 Gratuidade Regimental': 0, 'abr_inicia_presen_mat_2 Gratuidade Não Regimental': 0, 'abr_inicia_presen_mat_3 Convênio': 0, 'abr_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'mai_inicia_presen_mat_1 Gratuidade Regimental': 0, 'mai_inicia_presen_mat_2 Gratuidade Não Regimental': 0, 'mai_inicia_presen_mat_3 Convênio': 0, 'mai_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'jun_inicia_presen_mat_1 Gratuidade Regimental': 0, 'jun_inicia_presen_mat_2 Gratuidade Não Regimental': 0, 'jun_inicia_presen_mat_3 Convênio': 0, 'jun_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'jul_inicia_presen_mat_1 Gratuidade Regimental': 0, 'jul_inicia_presen_mat_2 Gratuidade Não RegiGratuidade Não Regimental': 0, 'ago_inicia_presen_mat_3 Convênio': 0, 'ago_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'set_inicia_presen_mat_1 Gratuidade Regimental': 0, 'set_inicia_presen_mat_2 Gratuidade Não Regimental': 0, 'set_inicia_presen_mat_3 Convênio': 0, 'set_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'out_inicia_presen_mat_1 Gratuidade Regimental': 0, 'out_inicia_presen_mat_2 Gratuidade Não Regimental': 0, 'out_inicia_presen_mat_3 Convênio': 0, 'out_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'nov_inicia_presen_mat_1 Gratuidade Regimental': 0, 'nov_inicia_presen_mat_2 Gratuidade Não Regimental': 0, 'nov_inicia_presen_mat_3 Convênio': 0, 'nov_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'dez_inicia_presen_mat_1 Gratuidade Regimental': 0, 'dez_inicia_presen_mat_2 Gratuidade Não Regimental': 0, 'dez_inicia_presen_mat_3 Convênio': 0, 'dez_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa': 0}