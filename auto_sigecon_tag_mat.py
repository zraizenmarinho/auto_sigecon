
# Importação dos pacotes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from obter_dados_tag_mat import obter_dados_por_tipo

arquivo = 'si_jan.xlsx'

from mat_tag import (
    tag_iniciacao_presencial,
    tag_iniciacao_distancia,
    tag_aprendizagem_presencial,
    tag_qualificacao_presencial,
    tag_aprendizagem_distancia,
    tag_qualificacao_distancia,
    tag_aperfeicoamento_presencial,
    tag_aperfeicoamento_distancia,
    tag_qualificacao_iti_presencial,
    tag_aprendizagem_tec,
    tag_tecnico_presencial,
    tag_tecnico_distancia,
    tag_tecnico_iti_presencial
)

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

# Navevagção para a pagina

url = 'http://sn-iis-02/SIGECON20/'

nav = webdriver.Firefox()

nav.get(url)

# Elemento Usuario
e_usuario = WebDriverWait(nav, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="UserName"]')))
usuario = "maheus.reck"
e_usuario.send_keys(usuario)

# Elemento Senha
e_senha = WebDriverWait(nav, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="Password"]')))
senha = "Ps4159753!"
e_senha.send_keys(senha)

# Elemento Ano
e_ano = WebDriverWait(nav, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="Ano"]')))
e_ano.click()
e_ano_2024 = WebDriverWait(nav, 5).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/form/fieldset/div[3]/select/option[1]')))
e_ano_2024.click()

# Elemento Entidade
e_entidade = WebDriverWait(nav, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="Cod_Empresa"]')))
e_entidade.click()
e_entidade_senai = WebDriverWait(nav, 5).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/form/fieldset/div[4]/select/option[3]')))
e_entidade_senai.click()

# Elemento Entrar
e_entrar = WebDriverWait(nav, 5).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/form/fieldset/div[6]/input')))
e_entrar.click()

#################################################################   Elemento unidade SENAI TAGUATINGA ###################################################################################

e_uni_tag1 = WebDriverWait(nav, 15).until(EC.visibility_of_element_located(
    (By.PARTIAL_LINK_TEXT, 'Senai Taguatinga')))
e_uni_tag1.click()

################################################################   Elemento CR INICIACAO PROFISSIONAL PRESENCIAL ########################################################################

e_cr_inici_prese = WebDriverWait(nav, 5).until(EC.visibility_of_element_located(
    (By.PARTIAL_LINK_TEXT, 'INICIACAO PROFISSIONAL PRESENCIAL')))
e_cr_inici_prese.click()

################################################################   Elemento FICHA DE PRODUÇÃO ############################################################################################

e_ficha_prod = WebDriverWait(nav, 15).until(EC.visibility_of_element_located(
    (By.LINK_TEXT, 'Produção')))

nav.execute_script("arguments[0].scrollIntoView(true);", e_ficha_prod)

nav.execute_script("arguments[0].click();", e_ficha_prod)

################################################################   Elemento GRUPO DE META ###############################################################################################

e_grupo_meta = WebDriverWait(nav, 30).until(EC.visibility_of_element_located(
    (By.XPATH, "//a[@href='/SIGECON20/Metas/MetasTipo/309/2024/0902030201/229?cd_centro_resp=30303010101&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=INICIACAO%20PROFISSIONAL%20PRESENCIAL&id_grupo=1&ds_grupo=Inicia%C3%A7%C3%A3o%20Profissional&fase=Realiza%C3%A7%C3%A3o']"
)))

nav.execute_script("arguments[0].scrollIntoView(true);", e_grupo_meta)

e_grupo_meta.click()

# SENAI TAGUATINGA - 30303010101 - INICIACAO PROFISSIONAL PRESENCIAL 

################################################################   MATRICULA BOLSA ####################################################################################################

em_bolsa_click = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5113'].indicador")))

em_bolsa_click.click()

em_bolsa_s = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

em_bolsa_s.send_keys(tag_iniciacao_presencial['jan_mat_bolsa'])

em_bolsa_s.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_inicia_presen_mat_2 Gratuidade Não Regimental"),
    ("mar", "mar_inicia_presen_mat_2 Gratuidade Não Regimental"),
    ("abr", "abr_inicia_presen_mat_2 Gratuidade Não Regimental"),
    ("mai", "mai_inicia_presen_mat_2 Gratuidade Não Regimental"),
    ("jun", "jun_inicia_presen_mat_2 Gratuidade Não Regimental"),
    ("jul", "jul_inicia_presen_mat_2 Gratuidade Não Regimental"),
    ("ago", "ago_inicia_presen_mat_2 Gratuidade Não Regimental"),
    ("set", "set_inicia_presen_mat_2 Gratuidade Não Regimental"),
    ("out", "out_inicia_presen_mat_2 Gratuidade Não Regimental"),
    ("nov", "nov_inicia_presen_mat_2 Gratuidade Não Regimental"),
    ("dez", "dez_inicia_presen_mat_2 Gratuidade Não Regimental")
]


em_bolsa_click = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5113'].indicador"))
)
em_bolsa_click.click()

for i, (mes, campo_dado) in enumerate(meses):
   
    mat_bolsa_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5113'].indicador"))
    )
    mat_bolsa_mes.click()

    mat_bolsa_send = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_presen_mat_2 Gratuidade Não Regimental"
    
    mat_iniciacao_presencial_geral = dados['iniciacao']['presencial']['matriculas'].get(chave_dado, 0)

    mat_bolsa_send.send_keys(str(mat_iniciacao_presencial_geral))
    mat_bolsa_send.send_keys(Keys.ENTER)


############################################################   MATRICULA NAO GRATUITA ####################################################################################################

mem_ng_click = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5114'].indicador")))

mem_ng_click.click()

em_ng_s = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

em_ng_s.send_keys(tag_iniciacao_presencial['jan_mat_n_gratuita'])

em_ng_s.send_keys(Keys.ENTER)

 

meses = [
    ("fev", "fev_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa")
]


em_ng_click = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5114'].indicador")))
em_ng_click.click()


for i, (mes, campo_dado) in enumerate(meses):
    
    mat_ng_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5114'].indicador"))
    )
    mat_ng_mes.click()

    mat_ng_send = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa"
    
    mat_iniciacao_presencial_ng = dados['iniciacao']['presencial']['matriculas'].get(chave_dado, 0)

    mat_ng_send.send_keys(str(mat_iniciacao_presencial_ng))
    mat_ng_send.send_keys(Keys.ENTER)


#########################################  INICIAÇÃO PROFISSIONAL A DISTANCIA  ##########################################################################################################

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/225?cd_centro_resp=30303010201&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=INICIACAO%20PROFISSIONAL%20A%20DISTANCIA&id_grupo=1&ds_grupo=Inicia%C3%A7%C3%A3o%20Profissional&fase=Realiza%C3%A7%C3%A3o', '_self')")

# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA MATRICULA BOLSA ##################################################################################################

ipd_bolsa_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5073'].indicador")))

ipd_bolsa_mat_jan.click()

ipd_bolsa_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

ipd_bolsa_mat_jan.send_keys(tag_iniciacao_distancia['jan_mat_bolsa'])

ipd_bolsa_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_inicia_distan_mat_2 Gratuidade Não Regimental"),
    ("mar", "mar_inicia_distan_mat_2 Gratuidade Não Regimental"),
    ("abr", "abr_inicia_distan_mat_2 Gratuidade Não Regimental"),
    ("mai", "mai_inicia_distan_mat_2 Gratuidade Não Regimental"),
    ("jun", "jun_inicia_distan_mat_2 Gratuidade Não Regimental"),
    ("jul", "jul_inicia_distan_mat_2 Gratuidade Não Regimental"),
    ("ago", "ago_inicia_distan_mat_2 Gratuidade Não Regimental"),
    ("set", "set_inicia_distan_mat_2 Gratuidade Não Regimental"),
    ("out", "out_inicia_distan_mat_2 Gratuidade Não Regimental"),
    ("nov", "nov_inicia_distan_mat_2 Gratuidade Não Regimental"),
    ("dez", "dez_inicia_distan_mat_2 Gratuidade Não Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    mat_ipd_bolsa_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5073'].indicador"))
    )
    mat_ipd_bolsa_mes.click()

    mat_ipd_bolsa_mes = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_distan_mat_2 Gratuidade Não Regimental"
    
    mat_iniciacao_distancia_bolsa = dados['iniciacao']['distancia']['matriculas'].get(chave_dado, 0)

    mat_ipd_bolsa_mes.send_keys(str(mat_iniciacao_distancia_bolsa))
    mat_ipd_bolsa_mes.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA MATRICULA NAO GRATUITA

ipd_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5074'].indicador")))

ipd_ng_mat_jan.click()

ipd_ng_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

ipd_ng_mat_jan.send_keys(tag_iniciacao_distancia['jan_mat_n_gratuita'])

ipd_ng_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_inicia_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_inicia_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_inicia_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_inicia_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_inicia_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_inicia_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_inicia_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_inicia_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_inicia_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_inicia_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_inicia_distan_mat_9 Pago por Pessoa Fisica ou Empresa")
]


ipd_ng_mat_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5074'].indicador")))
ipd_ng_mat_jan.click()

nav.refresh()

for i, (mes, campo_dado) in enumerate(meses):

    mat_ipd_ng_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5074'].indicador"))
    )
    mat_ipd_ng_mes.click()

    mat_ipd_ng_mes = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_distan_mat_9 Pago por Pessoa Fisica ou Empresa"
    

    mat_iniciacao_distancia_ng = dados['iniciacao']['distancia']['matriculas'].get(chave_dado, 0)

    mat_ipd_ng_mes.send_keys(str(mat_iniciacao_distancia_ng))
    mat_ipd_ng_mes.send_keys(Keys.ENTER)


###################################################  Aprendizagem Industrial - Presencial #############################################################

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/230?cd_centro_resp=30303020101&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APRENDIZAGEM%20INDUSTRIAL%20PRESENCIAL&id_grupo=2&ds_grupo=Aprendizagem%20Industrial&fase=Realiza%C3%A7%C3%A3o', '_blank')")

janela_atual = nav.current_window_handle

todas_janelas = nav.window_handles

for janela in todas_janelas:
    if janela != janela_atual:
        nav.switch_to.window(janela)
        break

# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL MATRICULA NAO GRATUITA

app_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-tipo="1"]')))

app_ng_mat_jan.click()

app_ng_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

app_ng_mat_jan.send_keys(tag_aprendizagem_presencial['jan_mat_n_gratuita'])

app_ng_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_aprendi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_aprendi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aprendi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aprendi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aprendi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aprendi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aprendi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aprendi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aprendi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aprendi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aprendi_presen_mat_9 Pago por Pessoa Fisica ou Empresa")
]


app_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5121'].indicador")))
app_ng_mat.click()

nav.refresh()


for i, (mes, campo_dado) in enumerate(meses):

    app_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5121'].indicador")))
    app_ng_mat.click()


    app_ng_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    chave_dado = f"{mes}_aprendi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"
    
    mat_aprendizagem_presencial_ng = dados['aprendizagem']['presencial']['matriculas'].get(chave_dado, 0)

    app_ng_mat.send_keys(str(mat_aprendizagem_presencial_ng))
    app_ng_mat.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL MATRICULA REGIMENTAL

app_regimental_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5122'].indicador")))

app_regimental_mat_jan.click()

app_regimental_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

app_regimental_mat_jan.send_keys(tag_aprendizagem_presencial['jan_mat_regi'])

app_regimental_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("mar", "mar_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("abr", "abr_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("mai", "mai_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("jun", "jun_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("jul", "jul_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("ago", "ago_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("set", "set_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("out", "out_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("nov", "nov_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("dez", "dez_aprendi_presen_mat_1 Gratuidade Regimental")
]


app_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5122'].indicador")))
app_regimental_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    app_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5122'].indicador")))
    app_regimental_mat.click()

   
    app_regimental_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))


    chave_dado = f"{mes}_aprendi_presen_mat_1 Gratuidade Regimental"
    
   
    mat_aprendizagem_presencial_regimental = dados['aprendizagem']['presencial']['matriculas'].get(chave_dado, 0)

    app_regimental_mat.send_keys(str(mat_aprendizagem_presencial_regimental))
    app_regimental_mat.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL MATRICULA CONVENIO

janela_atual = nav.current_window_handle


nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/221?cd_centro_resp=30303020201&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=QUALIFICACAO%20PROFISSIONAL%20PRESENCIAL&id_grupo=3&ds_grupo=Qualifica%C3%A7%C3%A3o%20Industrial&fase=Realiza%C3%A7%C3%A3o', '_self')")


quali_convenio_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5022'].indicador")))

quali_convenio_mat_jan.click()

quali_convenio_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

quali_convenio_mat_jan.send_keys(tag_qualificacao_presencial['jan_mat_convenio'])

quali_convenio_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_qualifi_presen_mat_3 Convênio"),
    ("mar", "mar_qualifi_presen_mat_3 Convênio"),
    ("abr", "abr_qualifi_presen_mat_3 Convênio"),
    ("mai", "mai_qualifi_presen_mat_3 Convênio"),
    ("jun", "jun_qualifi_presen_mat_3 Convênio"),
    ("jul", "jul_qualifi_presen_mat_3 Convênio"),
    ("ago", "ago_qualifi_presen_mat_3 Convênio"),
    ("set", "set_qualifi_presen_mat_3 Convênio"),
    ("out", "out_qualifi_presen_mat_3 Convênio"),
    ("nov", "nov_qualifi_presen_mat_3 Convênio"),
    ("dez", "dez_qualifi_presen_mat_3 Convênio")
]
qualifi_convenio_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5022'].indicador")))
qualifi_convenio_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_convenio_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5022'].indicador")))
    qualifi_convenio_mat.click()

   
    qualifi_convenio_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

   
    chave_dado = f"{mes}_qualifi_presen_mat_3 Convênio"
    
  
    mat_qualificacao_presencial_convenio = dados['qualificacao']['presencial']['matriculas'].get(chave_dado, 0)

    qualifi_convenio_mat.send_keys(str(mat_qualificacao_presencial_convenio))
    qualifi_convenio_mat.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL MATRICULA BOLSA

quali_bolsa_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5032'].indicador")))

quali_bolsa_mat_jan.click()

quali_bolsa_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

quali_bolsa_mat_jan.send_keys(tag_qualificacao_presencial['jan_mat_bolsa'])

quali_bolsa_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_qualifi_presen_mat_2 Gratuidade Não Regimental"),
    ("mar", "mar_qualifi_presen_mat_2 Gratuidade Não Regimental"),
    ("abr", "abr_qualifi_presen_mat_2 Gratuidade Não Regimental"),
    ("mai", "mai_qualifi_presen_mat_2 Gratuidade Não Regimental"),
    ("jun", "jun_qualifi_presen_mat_2 Gratuidade Não Regimental"),
    ("jul", "jul_qualifi_presen_mat_2 Gratuidade Não Regimental"),
    ("ago", "ago_qualifi_presen_mat_2 Gratuidade Não Regimental"),
    ("set", "set_qualifi_presen_mat_2 Gratuidade Não Regimental"),
    ("out", "out_qualifi_presen_mat_2 Gratuidade Não Regimental"),
    ("nov", "nov_qualifi_presen_mat_2 Gratuidade Não Regimental"),
    ("dez", "dez_qualifi_presen_mat_2 Gratuidade Não Regimental")
]


qualifi_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5022'].indicador")))
qualifi_bolsa_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5032'].indicador")))
    qualifi_bolsa_mat.click()

   
    qualifi_bolsa_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    chave_dado = f"{mes}_qualifi_presen_mat_2 Gratuidade Não Regimental"
    
   
    mat_qualificacao_presencial_bolsa = dados['qualificacao']['presencial']['matriculas'].get(chave_dado, 0)

    qualifi_bolsa_mat.send_keys(str(mat_qualificacao_presencial_bolsa))
    qualifi_bolsa_mat.send_keys(Keys.ENTER)


    # SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL MATRICULA NAO GRATUITA

quali_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5033'].indicador")))

quali_ng_mat_jan.click()

quali_ng_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

quali_ng_mat_jan.send_keys(tag_qualificacao_presencial['jan_mat_n_gratuita'])

quali_ng_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_qualifi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_qualifi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_qualifi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_qualifi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_qualifi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_qualifi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_qualifi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_qualifi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_qualifi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_qualifi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_qualifi_presen_mat_9 Pago por Pessoa Fisica ou Empresa")
]

qualifi_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5033'].indicador")))
qualifi_ng_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5033'].indicador")))
    qualifi_ng_mat.click()

   
    qualifi_ng_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"
    
    
    mat_qualificacao_presencial_nao_gratuita = dados['qualificacao']['presencial']['matriculas'].get(chave_dado, 0)

    qualifi_ng_mat.send_keys(str(mat_qualificacao_presencial_nao_gratuita))
    qualifi_ng_mat.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL MATRICULA Regimental

quali_regime_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5034'].indicador")))

quali_regime_mat_jan.click()

quali_regime_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

quali_regime_mat_jan.send_keys(tag_qualificacao_presencial['jan_mat_regi'])

quali_regime_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_qualifi_presen_mat_1 Gratuidade Regimental"),
    ("mar", "mar_qualifi_presen_mat_1 Gratuidade Regimental"),
    ("abr", "abr_qualifi_presen_mat_1 Gratuidade Regimental"),
    ("mai", "mai_qualifi_presen_mat_1 Gratuidade Regimental"),
    ("jun", "jun_qualifi_presen_mat_1 Gratuidade Regimental"),
    ("jul", "jul_qualifi_presen_mat_1 Gratuidade Regimental"),
    ("ago", "ago_qualifi_presen_mat_1 Gratuidade Regimental"),
    ("set", "set_qualifi_presen_mat_1 Gratuidade Regimental"),
    ("out", "out_qualifi_presen_mat_1 Gratuidade Regimental"),
    ("nov", "nov_qualifi_presen_mat_1 Gratuidade Regimental"),
    ("dez", "dez_qualifi_presen_mat_1 Gratuidade Regimental")
]


quali_regime_mat_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5034'].indicador")))
quali_regime_mat_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    quali_regime_mat_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5034'].indicador")))
    quali_regime_mat_mat.click()

   
    quali_regime_mat_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_presen_mat_1 Gratuidade Regimental"
    
    
    mat_qualificacao_presencial_regimental = dados['qualificacao']['presencial']['matriculas'].get(chave_dado, 0)

    quali_regime_mat_mat.send_keys(str(mat_qualificacao_presencial_regimental))
    quali_regime_mat_mat.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020301 - APRENDIZAGEM INDUSTRIAL A DISTANCIA - REGIMENTAL


janela_atual = nav.current_window_handle


nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/232?cd_centro_resp=30303020301&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APRENDIZAGEM%20INDUSTRIAL%20A%20DISTANCIA&id_grupo=2&ds_grupo=Aprendizagem%20Industrial&fase=Realiza%C3%A7%C3%A3o', '_self')")


apre_regime_semi_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5138'].indicador")))

apre_regime_semi_mat_jan.click()

apre_regime_semi_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

apre_regime_semi_mat_jan.send_keys(tag_aprendizagem_distancia['jan_mat_regi'])

apre_regime_semi_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("mar", "mar_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("abr", "abr_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("mai", "mai_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("jun", "jun_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("jul", "jul_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("ago", "ago_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("set", "set_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("out", "out_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("nov", "nov_aprendi_presen_mat_1 Gratuidade Regimental"),
    ("dez", "dez_aprendi_presen_mat_1 Gratuidade Regimental")
]


apre_regime_semi_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5138'].indicador")))
apre_regime_semi_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    apre_regime_semi_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5138'].indicador")))
    apre_regime_semi_mat.click()

   
    apre_regime_semi_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aprendi_presen_mat_1 Gratuidade Regimental"
    
    
    mat_aprendizagem_distancia_regimental = dados['aprendizagem']['distancia']['matriculas'].get(chave_dado, 0)

    apre_regime_semi_mat.send_keys(str(mat_aprendizagem_distancia_regimental))
    apre_regime_semi_mat.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020401 - QUALIFICACAO PROFISSIONAL SEMIPRESENCIAL - BOLSA


janela_atual = nav.current_window_handle


nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/223?cd_centro_resp=30303020401&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=QUALIFICACAO%20PROFISSIONAL%20SEMIPRESENCIAL&id_grupo=3&ds_grupo=Qualifica%C3%A7%C3%A3o%20Industrial&fase=Realiza%C3%A7%C3%A3o', '_self')")


qualifi_semi_bolsa_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5138'].indicador")))

qualifi_semi_bolsa_mat_jan.click()

qualifi_semi_bolsa_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

qualifi_semi_bolsa_mat_jan.send_keys(tag_qualificacao_distancia['jan_mat_bolsa'])

qualifi_semi_bolsa_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_qualifi_distan_mat_2 Gratuidade Não Regimental"),
    ("mar", "mar_qualifi_distan_mat_2 Gratuidade Não Regimental"),
    ("abr", "abr_qualifi_distan_mat_2 Gratuidade Não Regimental"),
    ("mai", "mai_qualifi_distan_mat_2 Gratuidade Não Regimental"),
    ("jun", "jun_qualifi_distan_mat_2 Gratuidade Não Regimental"),
    ("jul", "jul_qualifi_distan_mat_2 Gratuidade Não Regimental"),
    ("ago", "ago_qualifi_distan_mat_2 Gratuidade Não Regimental"),
    ("set", "set_qualifi_distan_mat_2 Gratuidade Não Regimental"),
    ("out", "out_qualifi_distan_mat_2 Gratuidade Não Regimental"),
    ("nov", "nov_qualifi_distan_mat_2 Gratuidade Não Regimental"),
    ("dez", "dez_qualifi_distan_mat_2 Gratuidade Não Regimental")
]


qualifi_semi_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5138'].indicador")))
qualifi_semi_bolsa_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5138'].indicador")))
    qualifi_semi_bolsa_mat.click()

   
    qualifi_semi_bolsa_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_distan_mat_2 Gratuidade Não Regimental"
    
    
    mat_qualifica_semi_bolsa = dados['qualificacao']['distancia']['matriculas'].get(chave_dado, 0)

    qualifi_semi_bolsa_mat.send_keys(str(mat_qualifica_semi_bolsa))
    qualifi_semi_bolsa_mat.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020401 - QUALIFICACAO PROFISSIONAL SEMIPRESENCIAL - NAO GRATUITA

qualifi_semi_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5057'].indicador")))

qualifi_semi_ng_mat_jan.click()

qualifi_semi_ng_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

qualifi_semi_ng_mat_jan.send_keys(tag_qualificacao_distancia['jan_mat_n_gratuita'])

qualifi_semi_ng_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_qualifi_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_qualifi_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_qualifi_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_qualifi_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_qualifi_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_qualifi_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_qualifi_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_qualifi_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_qualifi_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_qualifi_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_qualifi_distan_mat_9 Pago por Pessoa Fisica ou Empresa")
]


qualifi_semi_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5138'].indicador")))
qualifi_semi_ng_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5138'].indicador")))
    qualifi_semi_ng_mat.click()

   
    qualifi_semi_ng_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_distan_mat_9 Pago por Pessoa Fisica ou Empresa"
    
    
    mat_qualifica_semi_ng = dados['qualificacao']['distancia']['matriculas'].get(chave_dado, 0)

    qualifi_semi_ng_mat.send_keys(str(mat_qualifica_semi_ng))
    qualifi_semi_ng_mat.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020401 - QUALIFICACAO PROFISSIONAL SEMIPRESENCIAL - REGIMENTAL

qualifi_semi_regimental_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5058'].indicador")))

qualifi_semi_regimental_mat_jan.click()

qualifi_semi_regimental_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

qualifi_semi_regimental_mat_jan.send_keys(tag_qualificacao_distancia['jan_mat_regi'])

qualifi_semi_regimental_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_qualifi_distan_mat_1 Gratuidade Regimental"),
    ("mar", "mar_qualifi_distan_mat_1 Gratuidade Regimental"),
    ("abr", "abr_qualifi_distan_mat_1 Gratuidade Regimental"),
    ("mai", "mai_qualifi_distan_mat_1 Gratuidade Regimental"),
    ("jun", "jun_qualifi_distan_mat_1 Gratuidade Regimental"),
    ("jul", "jul_qualifi_distan_mat_1 Gratuidade Regimental"),
    ("ago", "ago_qualifi_distan_mat_1 Gratuidade Regimental"),
    ("set", "set_qualifi_distan_mat_1 Gratuidade Regimental"),
    ("out", "out_qualifi_distan_mat_1 Gratuidade Regimental"),
    ("nov", "nov_qualifi_distan_mat_1 Gratuidade Regimental"),
    ("dez", "dez_qualifi_distan_mat_1 Gratuidade Regimental")
]

qualifi_semi_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5058'].indicador")))
qualifi_semi_regimental_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5058'].indicador")))
    qualifi_semi_regimental_mat.click()

   
    qualifi_semi_regimental_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_distan_mat_1 Gratuidade Regimental"
    
    
    mat_qualifica_semi_regimental = dados['qualificacao']['distancia']['matriculas'].get(chave_dado, 0)

    qualifi_semi_regimental_mat.send_keys(str(mat_qualifica_semi_regimental))
    qualifi_semi_regimental_mat.send_keys(Keys.ENTER)
    
# SENAI TAGUATINGA - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - BOLSA

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/227?cd_centro_resp=30303020501&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APERF%2FESPECIALIZ%20PROFISSIONAL%20PRESENCIAL&id_grupo=5&ds_grupo=Aperfei%C3%A7oamento%20Profissional&fase=Realiza%C3%A7%C3%A3o', '_self')")


aper_prese_bolsa_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5092'].indicador")))

aper_prese_bolsa_mat_jan.click()

aper_prese_bolsa_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

aper_prese_bolsa_mat_jan.send_keys(tag_aperfeicoamento_presencial['jan_mat_bolsa'])

aper_prese_bolsa_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_aperfei_presen_mat_2 Gratuidade Não Regimental"),
    ("mar", "mar_aperfei_presen_mat_2 Gratuidade Não Regimental"),
    ("abr", "abr_aperfei_presen_mat_2 Gratuidade Não Regimental"),
    ("mai", "mai_aperfei_presen_mat_2 Gratuidade Não Regimental"),
    ("jun", "jun_aperfei_presen_mat_2 Gratuidade Não Regimental"),
    ("jul", "jul_aperfei_presen_mat_2 Gratuidade Não Regimental"),
    ("ago", "ago_aperfei_presen_mat_2 Gratuidade Não Regimental"),
    ("set", "set_aperfei_presen_mat_2 Gratuidade Não Regimental"),
    ("out", "out_aperfei_presen_mat_2 Gratuidade Não Regimental"),
    ("nov", "nov_aperfei_presen_mat_2 Gratuidade Não Regimental"),
    ("dez", "dez_aperfei_presen_mat_2 Gratuidade Não Regimental")
]


aper_prese_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5092'].indicador")))
aper_prese_bolsa_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5092'].indicador")))
    aper_prese_bolsa_mat.click()

   
    aper_prese_bolsa_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_mat_2 Gratuidade Não Regimental"
    
    
    mat_aper_prese_bolsa = dados['aperfeicoamento']['presencial']['matriculas'].get(chave_dado, 0)

    aper_prese_bolsa_mat.send_keys(str(mat_aper_prese_bolsa))
    aper_prese_bolsa_mat.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - NAO GRATUITA


aper_prese_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5093'].indicador")))

aper_prese_ng_mat_jan.click()

aper_prese_ng_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

aper_prese_ng_mat_jan.send_keys(tag_aperfeicoamento_presencial['jan_mat_n_gratuita'])

aper_prese_ng_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_aperfei_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_aperfei_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aperfei_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aperfei_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aperfei_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aperfei_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aperfei_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aperfei_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aperfei_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aperfei_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aperfei_presen_mat_9 Pago por Pessoa Fisica ou Empresa")
]


aper_prese_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5093'].indicador")))
aper_prese_ng_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5093'].indicador")))
    aper_prese_ng_mat.click()

   
    aper_prese_ng_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_mat_9 Pago por Pessoa Fisica ou Empresa"
    
    
    mat_aper_prese_ng = dados['aperfeicoamento']['presencial']['matriculas'].get(chave_dado, 0)

    aper_prese_ng_mat.send_keys(str(mat_aper_prese_ng))
    aper_prese_ng_mat.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - REGIMENTAL


aper_prese_regimental_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5094'].indicador")))

aper_prese_regimental_mat_jan.click()

aper_prese_regimental_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

aper_prese_regimental_mat_jan.send_keys(tag_aperfeicoamento_presencial['jan_mat_regi'])

aper_prese_regimental_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_aperfei_presen_mat_1 Gratuidade Regimental"),
    ("mar", "mar_aperfei_presen_mat_1 Gratuidade Regimental"),
    ("abr", "abr_aperfei_presen_mat_1 Gratuidade Regimental"),
    ("mai", "mai_aperfei_presen_mat_1 Gratuidade Regimental"),
    ("jun", "jun_aperfei_presen_mat_1 Gratuidade Regimental"),
    ("jul", "jul_aperfei_presen_mat_1 Gratuidade Regimental"),
    ("ago", "ago_aperfei_presen_mat_1 Gratuidade Regimental"),
    ("set", "set_aperfei_presen_mat_1 Gratuidade Regimental"),
    ("out", "out_aperfei_presen_mat_1 Gratuidade Regimental"),
    ("nov", "nov_aperfei_presen_mat_1 Gratuidade Regimental"),
    ("dez", "dez_aperfei_presen_mat_1 Gratuidade Regimental")
]

aper_prese_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5094'].indicador")))
aper_prese_regimental_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5094'].indicador")))
    aper_prese_regimental_mat.click()

   
    aper_prese_regimental_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_mat_1 Gratuidade Regimental"
    
    
    mat_aper_prese_regimental = dados['aperfeicoamento']['presencial']['matriculas'].get(chave_dado, 0)

    aper_prese_regimental_mat.send_keys(str(mat_aper_prese_regimental))
    aper_prese_regimental_mat.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - CONVENIO

aper_prese_convenio_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5098'].indicador")))

aper_prese_convenio_mat_jan.click()

aper_prese_convenio_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

aper_prese_convenio_mat_jan.send_keys(tag_aperfeicoamento_presencial['jan_mat_convenio'])

aper_prese_convenio_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_aperfei_presen_mat_3 Convênio"),
    ("mar", "mar_aperfei_presen_mat_3 Convênio"),
    ("abr", "abr_aperfei_presen_mat_3 Convênio"),
    ("mai", "mai_aperfei_presen_mat_3 Convênio"),
    ("jun", "jun_aperfei_presen_mat_3 Convênio"),
    ("jul", "jul_aperfei_presen_mat_3 Convênio"),
    ("ago", "ago_aperfei_presen_mat_3 Convênio"),
    ("set", "set_aperfei_presen_mat_3 Convênio"),
    ("out", "out_aperfei_presen_mat_3 Convênio"),
    ("nov", "nov_aperfei_presen_mat_3 Convênio"),
    ("dez", "dez_aperfei_presen_mat_3 Convênio")
]

aper_prese_convenio_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5098'].indicador")))
aper_prese_convenio_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_convenio_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5098'].indicador")))
    aper_prese_convenio_mat.click()

   
    aper_prese_convenio_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_mat_3 Convênio"
    
    
    mat_aper_prese_convenio = dados['aperfeicoamento']['presencial']['matriculas'].get(chave_dado, 0)

    aper_prese_convenio_mat.send_keys(str(mat_aper_prese_convenio))
    aper_prese_convenio_mat.send_keys(Keys.ENTER)
    
# SENAI TAGUATINGA - 30303020601 - APERF/ESPECIALI PROFISSIONAL A DISTANCIA BOLSA

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/231?cd_centro_resp=30303020601&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APERF%2FESPECIALI%20PROFISSIONAL%20A%20DISTANCIA&id_grupo=5&ds_grupo=Aperfei%C3%A7oamento%20Profissional&fase=Realiza%C3%A7%C3%A3o', '_self')")


aper_distan_bolsa_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5132'].indicador")))

aper_distan_bolsa_mat_jan.click()

aper_distan_bolsa_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

aper_distan_bolsa_mat_jan.send_keys(tag_aperfeicoamento_distancia['jan_mat_bolsa'])

aper_distan_bolsa_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

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

aper_dista_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5132'].indicador")))
aper_dista_bolsa_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    aper_dista_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5132'].indicador")))
    aper_dista_bolsa_mat.click()

   
    aper_dista_bolsa_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_distan_mat_2 Gratuidade Não Regimental"
    
    
    mat_aper_distan_bolsa = dados['aperfeicoamento']['distancia']['matriculas'].get(chave_dado, 0)

    aper_dista_bolsa_mat.send_keys(str(mat_aper_distan_bolsa))
    aper_dista_bolsa_mat.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020601 - APERF/ESPECIALI PROFISSIONAL A DISTANCIA NAO GRATUITA

aper_distan_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5133'].indicador")))

aper_distan_ng_mat_jan.click()

aper_distan_ng_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

aper_distan_ng_mat_jan.send_keys(tag_aperfeicoamento_distancia['jan_mat_bolsa'])

aper_distan_ng_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_aperfei_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),  
    ("mar", "mar_aperfei_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aperfei_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aperfei_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aperfei_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aperfei_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aperfei_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aperfei_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aperfei_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aperfei_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aperfei_distan_mat_9 Pago por Pessoa Fisica ou Empresa")
]

aper_dista_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5133'].indicador")))
aper_dista_ng_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    aper_dista_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5133'].indicador")))
    aper_dista_ng_mat.click()

   
    aper_dista_ng_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_distan_mat_2 Gratuidade Não Regimental"
    
    mat_aper_distan_ng = dados['aperfeicoamento']['distancia']['matriculas'].get(chave_dado, 0)

    aper_dista_ng_mat.send_keys(str(mat_aper_distan_bolsa))
    aper_dista_ng_mat.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020601 - APERF/ESPECIALI PROFISSIONAL A DISTANCIA REGIMENTAL


aper_distan_regimental_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5134'].indicador")))

aper_distan_regimental_mat_jan.click()

aper_distan_regimental_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

aper_distan_regimental_mat_jan.send_keys(tag_aperfeicoamento_distancia['jan_mat_regi'])

aper_distan_regimental_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_aperfei_distan_mat_1 Gratuidade Regimental"),
    ("mar", "mar_aperfei_distan_mat_1 Gratuidade Regimental"),
    ("abr", "abr_aperfei_distan_mat_1 Gratuidade Regimental"),
    ("mai", "mai_aperfei_distan_mat_1 Gratuidade Regimental"),
    ("jun", "jun_aperfei_distan_mat_1 Gratuidade Regimental"),
    ("jul", "jul_aperfei_distan_mat_1 Gratuidade Regimental"),
    ("ago", "ago_aperfei_distan_mat_1 Gratuidade Regimental"),
    ("set", "set_aperfei_distan_mat_1 Gratuidade Regimental"),
    ("out", "out_aperfei_distan_mat_1 Gratuidade Regimental"),
    ("nov", "nov_aperfei_distan_mat_1 Gratuidade Regimental"),
    ("dez", "dez_aperfei_distan_mat_1 Gratuidade Regimental")
]

aper_dista_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5134'].indicador")))
aper_dista_regimental_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    aper_dista_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5134'].indicador")))
    aper_dista_regimental_mat.click()

   
    aper_dista_regimental_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_distan_mat_1 Gratuidade Regimental"
    
    mat_aper_distan_regimental = dados['aperfeicoamento']['distancia']['matriculas'].get(chave_dado, 0)

    aper_dista_regimental_mat.send_keys(str(mat_aper_distan_regimental))
    aper_dista_regimental_mat.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020901 - QUALIFIC PROF PRESENC - ITINER V ENS MED - BOLSA

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/222?cd_centro_resp=30303020901&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=QUALIFIC%20PROF%20PRESENC%20-%20ITINER%20V%20ENS%20MED&id_grupo=3&ds_grupo=Qualifica%C3%A7%C3%A3o%20Industrial&fase=Realiza%C3%A7%C3%A3o', '_self')")

qualifi_iti_presencial_bolsa_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5044'].indicador")))

qualifi_iti_presencial_bolsa_mat_jan.click()

qualifi_iti_presencial_bolsa_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

qualifi_iti_presencial_bolsa_mat_jan.send_keys(tag_qualificacao_iti_presencial['jan_mat_bolsa'])

qualifi_iti_presencial_bolsa_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("mar", "mar_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("abr", "abr_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("mai", "mai_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("jun", "jun_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("jul", "jul_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("ago", "ago_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("set", "set_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("out", "out_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("nov", "nov_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("dez", "dez_qualifi_iti_presen_mat_2 Gratuidade Não Regimental")
]

qualifi_iti_presencial_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5044'].indicador")))
qualifi_iti_presencial_bolsa_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_iti_presencial_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5044'].indicador")))
    qualifi_iti_presencial_bolsa_mat.click()

   
    qualifi_iti_presencial_bolsa_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"
    
    mat_quali_iti_presencial_bolsa = dados['qualificacao_iti']['presencial']['matriculas'].get(chave_dado, 0)

    qualifi_iti_presencial_bolsa_mat.send_keys(str(mat_quali_iti_presencial_bolsa))
    qualifi_iti_presencial_bolsa_mat.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020901 - QUALIFIC PROF PRESENC - ITINER V ENS MED - NAO GRATUITA

qualifi_iti_presencial_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5045'].indicador")))

qualifi_iti_presencial_ng_mat_jan.click()

qualifi_iti_presencial_ng_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

qualifi_iti_presencial_ng_mat_jan.send_keys(tag_qualificacao_iti_presencial['jan_mat_n_gratuita'])

qualifi_iti_presencial_ng_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("mar", "mar_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("abr", "abr_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("mai", "mai_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("jun", "jun_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("jul", "jul_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("ago", "ago_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("set", "set_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("out", "out_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("nov", "nov_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("dez", "dez_qualifi_iti_presen_mat_2 Gratuidade Não Regimental")
]

qualifi_iti_presencial_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5045'].indicador")))
qualifi_iti_presencial_ng_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_iti_presencial_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5045'].indicador")))
    qualifi_iti_presencial_ng_mat.click()

   
    qualifi_iti_presencial_ng_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"
    
    mat_quali_iti_presencial_ng = dados['qualificacao_iti']['presencial']['matriculas'].get(chave_dado, 0)

    qualifi_iti_presencial_ng_mat.send_keys(str(mat_quali_iti_presencial_ng))
    qualifi_iti_presencial_ng_mat.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020901 - QUALIFIC PROF PRESENC - ITINER V ENS MED - BOLSA

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/222?cd_centro_resp=30303020901&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=QUALIFIC%20PROF%20PRESENC%20-%20ITINER%20V%20ENS%20MED&id_grupo=3&ds_grupo=Qualifica%C3%A7%C3%A3o%20Industrial&fase=Realiza%C3%A7%C3%A3o', '_self')")

qualifi_iti_presencial_bolsa_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5044'].indicador")))

qualifi_iti_presencial_bolsa_mat_jan.click()

qualifi_iti_presencial_bolsa_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

qualifi_iti_presencial_bolsa_mat_jan.send_keys(tag_qualificacao_iti_presencial['jan_mat_bolsa'])

qualifi_iti_presencial_bolsa_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("mar", "mar_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("abr", "abr_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("mai", "mai_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("jun", "jun_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("jul", "jul_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("ago", "ago_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("set", "set_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("out", "out_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("nov", "nov_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("dez", "dez_qualifi_iti_presen_mat_2 Gratuidade Não Regimental")
]

qualifi_iti_presencial_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5044'].indicador")))
qualifi_iti_presencial_bolsa_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_iti_presencial_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5044'].indicador")))
    qualifi_iti_presencial_bolsa_mat.click()

   
    qualifi_iti_presencial_bolsa_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_mat_2 Gratuidade Não Regimental"
    
    mat_quali_iti_presencial_bolsa = dados['qualificacao_iti']['presencial']['matriculas'].get(chave_dado, 0)

    qualifi_iti_presencial_bolsa_mat.send_keys(str(mat_quali_iti_presencial_bolsa))
    qualifi_iti_presencial_bolsa_mat.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020901 - QUALIFIC PROF PRESENC - ITINER V ENS MED - REGIMENTAL

qualifi_iti_presencial_regimental_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5046'].indicador")))

qualifi_iti_presencial_regimental_mat_jan.click()

qualifi_iti_presencial_regimental_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

qualifi_iti_presencial_regimental_mat_jan.send_keys(tag_qualificacao_iti_presencial['jan_mat_regi'])

qualifi_iti_presencial_regimental_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_qualifi_iti_presen_mat_1 Gratuidade Regimental"),
    ("mar", "mar_qualifi_iti_presen_mat_1 Gratuidade Regimental"),
    ("abr", "abr_qualifi_iti_presen_mat_1 Gratuidade Regimental"),
    ("mai", "mai_qualifi_iti_presen_mat_1 Gratuidade Regimental"),
    ("jun", "jun_qualifi_iti_presen_mat_1 Gratuidade Regimental"),
    ("jul", "jul_qualifi_iti_presen_mat_1 Gratuidade Regimental"),
    ("ago", "ago_qualifi_iti_presen_mat_1 Gratuidade Regimental"),
    ("set", "set_qualifi_iti_presen_mat_1 Gratuidade Regimental"),
    ("out", "out_qualifi_iti_presen_mat_1 Gratuidade Regimental"),
    ("nov", "nov_qualifi_iti_presen_mat_1 Gratuidade Regimental"),
    ("dez", "dez_qualifi_iti_presen_mat_1 Gratuidade Regimental")
]

qualifi_iti_presencial_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5046'].indicador")))
qualifi_iti_presencial_regimental_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_iti_presencial_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5046'].indicador")))
    qualifi_iti_presencial_regimental_mat.click()

   
    qualifi_iti_presencial_regimental_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_mat_1 Gratuidade Regimental"
    
    mat_quali_iti_presencial_regimental = dados['qualificacao_iti']['presencial']['matriculas'].get(chave_dado, 0)

    qualifi_iti_presencial_regimental_mat.send_keys(str(mat_quali_iti_presencial_regimental))
    qualifi_iti_presencial_regimental_mat.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303040101 - APREND. IND. TEC. NIVEL MEDIO PRESENCIAL - NAO GRATUITA

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/226?cd_centro_resp=30303040101&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APREND.%20IND.%20TEC.%20NIVEL%20MEDIO%20PRESENCIAL&id_grupo=11&ds_grupo=Aprendizagem%20Industrial%20T%C3%A9cnico%20de%20N%C3%ADvel%20M%C3%A9dio&fase=Realiza%C3%A7%C3%A3o', '_self')")


aprendi_tec_presencial_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5081'].indicador")))

aprendi_tec_presencial_ng_mat_jan.click()

aprendi_tec_presencial_ng_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

aprendi_tec_presencial_ng_mat_jan.send_keys(tag_qualificacao_iti_presencial['jan_mat_n_gratuita'])

aprendi_tec_presencial_ng_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa")
]

aprendi_tec_presencial_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5081'].indicador")))
aprendi_tec_presencial_ng_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    aprendi_tec_presencial_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5081'].indicador")))
    aprendi_tec_presencial_ng_mat.click()

   
    aprendi_tec_presencial_ng_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_mat_1 Gratuidade Regimental"
    
    mat_aprendi_tec_presencial_ng = dados['aprendizagem_tec']['presencial']['matriculas'].get(chave_dado, 0)

    aprendi_tec_presencial_ng_mat.send_keys(str(mat_aprendi_tec_presencial_ng))
    aprendi_tec_presencial_ng_mat.send_keys(Keys.ENTER)
    
# SENAI TAGUATINGA - 30303040101 - APREND. IND. TEC. NIVEL MEDIO PRESENCIAL - REGIMENTAL

aprendi_tec_presencial_regimental_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5082'].indicador")))

aprendi_tec_presencial_regimental_mat_jan.click()

aprendi_tec_presencial_regimental_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

aprendi_tec_presencial_regimental_mat_jan.send_keys(tag_qualificacao_iti_presencial['jan_mat_regi'])

aprendi_tec_presencial_regimental_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa")
]

aprendi_tec_presencial_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5082'].indicador")))
aprendi_tec_presencial_regimental_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    aprendi_tec_presencial_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5082'].indicador")))
    aprendi_tec_presencial_regimental_mat.click()

   
    aprendi_tec_presencial_regimental_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_mat_1 Gratuidade Regimental"
    
    mat_aprendi_tec_presencial_regimental = dados['aprendizagem_tec']['presencial']['matriculas'].get(chave_dado, 0)

    aprendi_tec_presencial_regimental_mat.send_keys(str(mat_aprendi_tec_presencial_regimental))
    aprendi_tec_presencial_regimental_mat.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303040201 - TECNICO DE NIVEL MEDIO PRESENCIAL - NAO GRATUITA

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/CentroResponsabilidade/Index/309/2024/0902030201/233?cd_centro_resp=30303040201&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=TECNICO%20DE%20NIVEL%20MEDIO%20PRESENCIAL', '_self')")

tec_presencial_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5145'].indicador")))

tec_presencial_ng_mat_jan.click()

tec_presencial_ng_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

tec_presencial_ng_mat_jan.send_keys(tag_tecnico_presencial['jan_mat_n_gratuita'])

tec_presencial_ng_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_tecni_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_tecni_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_tecni_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_tecni_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_tecni_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_tecni_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_tecni_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_tecni_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_tecni_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_tecni_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_tecni_presen_mat_9 Pago por Pessoa Fisica ou Empresa")
]

tec_presencial_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5145'].indicador")))
tec_presencial_ng_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    tec_presencial_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5145'].indicador")))
    tec_presencial_ng_mat.click()

   
    tec_presencial_ng_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_presen_mat_9 Pago por Pessoa Fisica ou Empresa"
    
    mat_tec_presencial_ng = dados['tecnico_nm']['presencial']['matriculas'].get(chave_dado, 0)

    tec_presencial_ng_mat.send_keys(str(mat_tec_presencial_ng))
    tec_presencial_ng_mat.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303040201 - TECNICO DE NIVEL MEDIO PRESENCIAL - REGIMENTAL

tec_presencial_regimental_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5146'].indicador")))

tec_presencial_regimental_mat_jan.click()

tec_presencial_regimental_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

tec_presencial_regimental_mat_jan.send_keys(tag_tecnico_presencial['jan_mat_regi'])

tec_presencial_regimental_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_tecni_presen_mat_1 Gratuidade Regimental"),
    ("mar", "mar_tecni_presen_mat_1 Gratuidade Regimental"),
    ("abr", "abr_tecni_presen_mat_1 Gratuidade Regimental"),
    ("mai", "mai_tecni_presen_mat_1 Gratuidade Regimental"),
    ("jun", "jun_tecni_presen_mat_1 Gratuidade Regimental"),
    ("jul", "jul_tecni_presen_mat_1 Gratuidade Regimental"),
    ("ago", "ago_tecni_presen_mat_1 Gratuidade Regimental"),
    ("set", "set_tecni_presen_mat_1 Gratuidade Regimental"),
    ("out", "out_tecni_presen_mat_1 Gratuidade Regimental"),
    ("nov", "nov_tecni_presen_mat_1 Gratuidade Regimental"),
    ("dez", "dez_tecni_presen_mat_1 Gratuidade Regimental")
]

tec_presencial_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5146'].indicador")))
tec_presencial_regimental_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    tec_presencial_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5146'].indicador")))
    tec_presencial_regimental_mat.click()

   
    tec_presencial_regimental_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_presen_mat_1 Gratuidade Regimental"
    
    mat_tec_presencial_regimental = dados['tecnico_nm']['presencial']['matriculas'].get(chave_dado, 0)

    tec_presencial_regimental_mat.send_keys(str(mat_tec_presencial_regimental))
    tec_presencial_regimental_mat.send_keys(Keys.ENTER)
    

# SENAI TAGUATINGA - 30303040201 - TECNICO DE NIVEL MEDIO PRESENCIAL - BOLSA   

tec_presencial_bolsa_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5150'].indicador")))

tec_presencial_bolsa_mat_jan.click()

tec_presencial_bolsa_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

tec_presencial_bolsa_mat_jan.send_keys(tag_tecnico_presencial['jan_mat_bolsa'])

tec_presencial_bolsa_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_tecni_presen_mat_2 Gratuidade Não Regimental"),
    ("mar", "mar_tecni_presen_mat_2 Gratuidade Não Regimental"),
    ("abr", "abr_tecni_presen_mat_2 Gratuidade Não Regimental"),
    ("mai", "mai_tecni_presen_mat_2 Gratuidade Não Regimental"),
    ("jun", "jun_tecni_presen_mat_2 Gratuidade Não Regimental"),
    ("jul", "jul_tecni_presen_mat_2 Gratuidade Não Regimental"),
    ("ago", "ago_tecni_presen_mat_2 Gratuidade Não Regimental"),
    ("set", "set_tecni_presen_mat_2 Gratuidade Não Regimental"),
    ("out", "out_tecni_presen_mat_2 Gratuidade Não Regimental"),
    ("nov", "nov_tecni_presen_mat_2 Gratuidade Não Regimental"),
    ("dez", "dez_tecni_presen_mat_2 Gratuidade Não Regimental")
]


tec_presencial_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5150'].indicador")))
tec_presencial_bolsa_mat.click()


for i, (mes, campo_dado) in enumerate(meses):

    tec_presencial_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5150'].indicador")))
    tec_presencial_bolsa_mat.click()

   
    tec_presencial_bolsa_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_presen_mat_1 Gratuidade Regimental"
    
    mat_tec_presencial_bolsa = dados['tecnico_nm']['presencial']['matriculas'].get(chave_dado, 0)

    tec_presencial_bolsa_mat.send_keys(str(mat_tec_presencial_bolsa))
    tec_presencial_bolsa_mat.send_keys(Keys.ENTER)
