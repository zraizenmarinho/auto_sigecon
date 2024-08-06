d = 5132("Bolsa") ("ok")
c=  5133("Não Gratuita") 
b = 5134("Regimental") 

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/227?cd_centro_resp=30303020501&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APERF%2FESPECIALIZ%20PROFISSIONAL%20PRESENCIAL&id_grupo=5&ds_grupo=Aperfei%C3%A7oamento%20Profissional&fase=Realiza%C3%A7%C3%A3o', '_self')")




meses = [
    ("fev", "fev_aperfei_distan_mat_2 Gratuidade Não Regimental"),
    ("mar", "mar_aperfei_distan_mat_2 Gratuidade Não Regimental"),
    ("abr", "abr_aperfei_distan_mat_2 Gratuidade Não Regimental"),
    ("mai", "mai_aperfei_distan_mat_2 Gratuidade Não Regimental"),
    ("jun", "jun_aperfei_distan_mat_2 Gratuidade Não Regimental"),
    ("jul", "jul_aperfei_distan_mat_2 Gratuidade Não Regimental"),
    ("ago", "ago_aperfei_distan_mat_2 Gratuidade Não Regimental"),
    ("set", "set_aperfei_distan_mat_2 Gratuidade Não Regimental"),
    ("out", "out_aperfei_distan_mat_2 Gratuidade Não Regimental"),
    ("nov", "nov_aperfei_distan_mat_2 Gratuidade Não Regimental"),
    ("dez", "dez_aperfei_distan_mat_2 Gratuidade Não Regimental")
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