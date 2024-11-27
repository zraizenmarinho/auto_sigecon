
# Importação dos pacotes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from obter_dados_sob_eva import obter_dados_por_tipo

dados = {
    'iniciacao': {
        'presencial': {
            'evadidos': obter_dados_por_tipo('iniciacao', 'presencial')['evadidos'],
        },
        'distancia': {
            'evadidos': obter_dados_por_tipo('iniciacao', 'distancia')['evadidos'],
        }
    },
    'aprendizagem': {
        'presencial': {
            'evadidos': obter_dados_por_tipo('aprendizagem', 'presencial')['evadidos'],
        },
        'distancia': {
            'evadidos': obter_dados_por_tipo('aprendizagem', 'distancia')['evadidos'],
        }
    },
    'qualificacao': {
        'presencial': {
            'evadidos': obter_dados_por_tipo('qualificacao', 'presencial')['evadidos'],
        },
        'distancia': {
            'evadidos': obter_dados_por_tipo('qualificacao', 'distancia')['evadidos'],
        }
    },
    'aperfeicoamento': {
        'presencial': {
            'evadidos': obter_dados_por_tipo('aperfeicoamento', 'presencial')['evadidos'],
        },
        'distancia': {
            'evadidos': obter_dados_por_tipo('aperfeicoamento', 'distancia')['evadidos'],
        }
    },
    'qualificacao_iti': {
        'presencial': {
            'evadidos': obter_dados_por_tipo('qualificacao_iti', 'presencial')['evadidos'],
        }
    },
    'aprendizagem_tec': {
        'presencial': {
            'evadidos': obter_dados_por_tipo('aprendizagem_tec', 'presencial')['evadidos'],
        }
    },
    'tecnico_nm': {
        'presencial': {
            'evadidos': obter_dados_por_tipo('tecnico_nm', 'presencial')['evadidos'],
        },
        'distancia': {
            'evadidos': obter_dados_por_tipo('tecnico_nm', 'distancia')['evadidos'],
        }
    },
    'tecnico_nm_iti': {
        'presencial': {
            'evadidos': obter_dados_por_tipo('tecnico_nm_iti', 'presencial')['evadidos'],
        }
    }
}


DEFAULT_WAIT = 20

def esperar_elemento(nav, locator, condition=EC.visibility_of_element_located, timeout=DEFAULT_WAIT):
    return WebDriverWait(nav, timeout).until(condition(locator))

# Navevagção para a pagina

url = 'http://sn-iis-02/SIGECON20/'

nav = webdriver.Firefox()

nav.get(url)

# Elemento Usuario
e_usuario = WebDriverWait(nav, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="UserName"]')))
usuario = "matheus.reck"
e_usuario.send_keys(usuario)

# Elemento Senha
e_senha = WebDriverWait(nav, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="Password"]')))
senha = Vi*******
e_senha.send_keys(senha)

# Elemento Ano
e_ano = WebDriverWait(nav, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="Ano"]')))
e_ano.click()
e_ano_2024 = WebDriverWait(nav, 5).until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="Ano"]/option[2]')))
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
    (By.PARTIAL_LINK_TEXT, 'Senai Sobradinho')))
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
    (By.XPATH, "//a[@href='/SIGECON20/Metas/MetasTipo/309/2024/0902030204/240?cd_centro_resp=30303010101&nm_unidade=SENAI%20SOBRADINHO&nm_centro_resp=INICIACAO%20PROFISSIONAL%20PRESENCIAL&id_grupo=1&ds_grupo=Inicia%C3%A7%C3%A3o%20Profissional&fase=Realiza%C3%A7%C3%A3o']"
)))

nav.execute_script("arguments[0].scrollIntoView(true);", e_grupo_meta)

e_grupo_meta.click()

#  30303010101 - INICIACAO PROFISSIONAL PRESENCIAL 

################################################################   evadidos BOLSA ####################################################################################################

nav.refresh()

meses = [
    ("jan", "jan_inicia_presen_eva_2 Gratuidade Não Regimental"),
    ("fev", "fev_inicia_presen_eva_2 Gratuidade Não Regimental"),
    ("mar", "mar_inicia_presen_eva_2 Gratuidade Não Regimental"),
    ("abr", "abr_inicia_presen_eva_2 Gratuidade Não Regimental"),
    ("mai", "mai_inicia_presen_eva_2 Gratuidade Não Regimental"),
    ("jun", "jun_inicia_presen_eva_2 Gratuidade Não Regimental"),
    ("jul", "jul_inicia_presen_eva_2 Gratuidade Não Regimental"),
    ("ago", "ago_inicia_presen_eva_2 Gratuidade Não Regimental"),
    ("set", "set_inicia_presen_eva_2 Gratuidade Não Regimental"),
    ("out", "out_inicia_presen_eva_2 Gratuidade Não Regimental"),
    ("nov", "nov_inicia_presen_eva_2 Gratuidade Não Regimental"),
    ("dez", "dez_inicia_presen_eva_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):
   
    eva_bolsa_mes = esperar_elemento(nav, (By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5153'].indicador"), timeout=10)
    
    eva_bolsa_mes.click()

    eva_bolsa_mes = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )


    chave_dado = f"{mes}_inicia_presen_eva_2 Gratuidade Não Regimental"
    
    eva_iniciacao_presencial_geral = dados['iniciacao']['presencial']['evadidos'].get(chave_dado, 0)

    eva_bolsa_mes.send_keys(str(eva_iniciacao_presencial_geral))
    eva_bolsa_mes.send_keys(Keys.ENTER)


############################################################   evadidos NAO GRATUITA ####################################################################################################

nav.refresh() 

meses = [
    ("jan", "jan_inicia_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_inicia_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_inicia_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_inicia_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_inicia_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_inicia_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_inicia_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_inicia_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_inicia_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_inicia_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_inicia_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_inicia_presen_eva_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):
    
    eva_ng_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5154'].indicador"))
    )
    eva_ng_mes.click()

    eva_ng_send = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_presen_eva_9 Pago por Pessoa Fisica ou Empresa"
    
    eva_iniciacao_presencial_ng = dados['iniciacao']['presencial']['evadidos'].get(chave_dado, 0)

    eva_ng_send.send_keys(str(eva_iniciacao_presencial_ng))
    eva_ng_send.send_keys(Keys.ENTER)


#########################################  INICIAÇÃO PROFISSIONAL A DISTANCIA  ##########################################################################################################


janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030204/244?cd_centro_resp=30303010201&nm_unidade=SENAI%20SOBRADINHO&nm_centro_resp=INICIACAO%20PROFISSIONAL%20A%20DISTANCIA&id_grupo=1&ds_grupo=Inicia%C3%A7%C3%A3o%20Profissional&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

#  30303010201 - INICIACAO PROFISSIONAL A DISTANCIA evadidos BOLSA ##################################################################################################

nav.refresh()

meses = [
    ("jan", "jan_inicia_distan_eva_2 Gratuidade Não Regimental"),
    ("fev", "fev_inicia_distan_eva_2 Gratuidade Não Regimental"),
    ("mar", "mar_inicia_distan_eva_2 Gratuidade Não Regimental"),
    ("abr", "abr_inicia_distan_eva_2 Gratuidade Não Regimental"),
    ("mai", "mai_inicia_distan_eva_2 Gratuidade Não Regimental"),
    ("jun", "jun_inicia_distan_eva_2 Gratuidade Não Regimental"),
    ("jul", "jul_inicia_distan_eva_2 Gratuidade Não Regimental"),
    ("ago", "ago_inicia_distan_eva_2 Gratuidade Não Regimental"),
    ("set", "set_inicia_distan_eva_2 Gratuidade Não Regimental"),
    ("out", "out_inicia_distan_eva_2 Gratuidade Não Regimental"),
    ("nov", "nov_inicia_distan_eva_2 Gratuidade Não Regimental"),
    ("dez", "dez_inicia_distan_eva_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    eva_ipd_bolsa_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5193'].indicador"))
    )
    eva_ipd_bolsa_mes.click()

    eva_ipd_bolsa_mes = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_distan_eva_2 Gratuidade Não Regimental"
    
    eva_iniciacao_distancia_bolsa = dados['iniciacao']['distancia']['evadidos'].get(chave_dado, 0)

    eva_ipd_bolsa_mes.send_keys(str(eva_iniciacao_distancia_bolsa))
    eva_ipd_bolsa_mes.send_keys(Keys.ENTER)


#  30303010201 - INICIACAO PROFISSIONAL A DISTANCIA evadidos NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_inicia_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_inicia_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_inicia_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_inicia_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_inicia_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_inicia_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_inicia_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_inicia_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_inicia_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_inicia_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_inicia_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_inicia_distan_eva_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    eva_ipd_ng_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5194'].indicador"))
    )
    eva_ipd_ng_mes.click()

    eva_ipd_ng_mes = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_distan_eva_9 Pago por Pessoa Fisica ou Empresa"
    

    eva_iniciacao_distancia_ng = dados['iniciacao']['distancia']['evadidos'].get(chave_dado, 0)

    eva_ipd_ng_mes.send_keys(str(eva_iniciacao_distancia_ng))
    eva_ipd_ng_mes.send_keys(Keys.ENTER)


###################################################  Aprendizagem Industrial - Presencial #############################################################

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030204/248?cd_centro_resp=30303020101&nm_unidade=SENAI%20SOBRADINHO&nm_centro_resp=APRENDIZAGEM%20INDUSTRIAL%20PRESENCIAL&id_grupo=2&ds_grupo=Aprendizagem%20Industrial&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])


#  30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL evadidos NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_aprendi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_aprendi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_aprendi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aprendi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aprendi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aprendi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aprendi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aprendi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aprendi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aprendi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aprendi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aprendi_presen_eva_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    app_ng_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5233'].indicador")))
    app_ng_eva.click()


    app_ng_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    chave_dado = f"{mes}_aprendi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"
    
    eva_aprendizagem_presencial_ng = dados['aprendizagem']['presencial']['evadidos'].get(chave_dado, 0)

    app_ng_eva.send_keys(str(eva_aprendizagem_presencial_ng))
    app_ng_eva.send_keys(Keys.ENTER)

# 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL evadidos REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_aprendi_presen_eva_1 Gratuidade Regimental"),
    ("fev", "fev_aprendi_presen_eva_1 Gratuidade Regimental"),
    ("mar", "mar_aprendi_presen_eva_1 Gratuidade Regimental"),
    ("abr", "abr_aprendi_presen_eva_1 Gratuidade Regimental"),
    ("mai", "mai_aprendi_presen_eva_1 Gratuidade Regimental"),
    ("jun", "jun_aprendi_presen_eva_1 Gratuidade Regimental"),
    ("jul", "jul_aprendi_presen_eva_1 Gratuidade Regimental"),
    ("ago", "ago_aprendi_presen_eva_1 Gratuidade Regimental"),
    ("set", "set_aprendi_presen_eva_1 Gratuidade Regimental"),
    ("out", "out_aprendi_presen_eva_1 Gratuidade Regimental"),
    ("nov", "nov_aprendi_presen_eva_1 Gratuidade Regimental"),
    ("dez", "dez_aprendi_presen_eva_1 Gratuidade Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    app_regimental_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5234'].indicador")))
    app_regimental_eva.click()

   
    app_regimental_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))


    chave_dado = f"{mes}_aprendi_presen_eva_1 Gratuidade Regimental"
    
   
    eva_aprendizagem_presencial_regimental = dados['aprendizagem']['presencial']['evadidos'].get(chave_dado, 0)

    app_regimental_eva.send_keys(str(eva_aprendizagem_presencial_regimental))
    app_regimental_eva.send_keys(Keys.ENTER)


# 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL evadidos BOLSA

nav.refresh()

meses = [
    ("jan", "jan_aprendi_presen_eva_2 Gratuidade Não Regimental"),
    ("fev", "fev_aprendi_presen_eva_2 Gratuidade Não Regimental"),
    ("mar", "mar_aprendi_presen_eva_2 Gratuidade Não Regimental"),
    ("abr", "abr_aprendi_presen_eva_2 Gratuidade Não Regimental"),
    ("mai", "mai_aprendi_presen_eva_2 Gratuidade Não Regimental"),
    ("jun", "jun_aprendi_presen_eva_2 Gratuidade Não Regimental"),
    ("jul", "jul_aprendi_presen_eva_2 Gratuidade Não Regimental"),
    ("ago", "ago_aprendi_presen_eva_2 Gratuidade Não Regimental"),
    ("set", "set_aprendi_presen_eva_2 Gratuidade Não Regimental"),
    ("out", "out_aprendi_presen_eva_2 Gratuidade Não Regimental"),
    ("nov", "nov_aprendi_presen_eva_2 Gratuidade Não Regimental"),
    ("dez", "dez_aprendi_presen_eva_2 Gratuidade Não Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    app_bolsa_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5478'].indicador")))
    app_bolsa_eva.click()

   
    app_bolsa_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))


    chave_dado = f"{mes}_aprendi_presen_con_2 Gratuidade Não Regimental"
    
   
    eva_aprendizagem_presencial_bolsa = dados['aprendizagem']['presencial']['evadidos'].get(chave_dado, 0)

    app_bolsa_eva.send_keys(str(eva_aprendizagem_presencial_bolsa))
    app_bolsa_eva.send_keys(Keys.ENTER)

# 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL evadidos BOLSA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030204/241?cd_centro_resp=30303020201&nm_unidade=SENAI%20SOBRADINHO&nm_centro_resp=QUALIFICACAO%20PROFISSIONAL%20PRESENCIAL&id_grupo=3&ds_grupo=Qualifica%C3%A7%C3%A3o%20Industrial&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_qualifi_presen_eva_2 Gratuidade Não Regimental"),
    ("fev", "fev_qualifi_presen_eva_2 Gratuidade Não Regimental"),
    ("mar", "mar_qualifi_presen_eva_2 Gratuidade Não Regimental"),
    ("abr", "abr_qualifi_presen_eva_2 Gratuidade Não Regimental"),
    ("mai", "mai_qualifi_presen_eva_2 Gratuidade Não Regimental"),
    ("jun", "jun_qualifi_presen_eva_2 Gratuidade Não Regimental"),
    ("jul", "jul_qualifi_presen_eva_2 Gratuidade Não Regimental"),
    ("ago", "ago_qualifi_presen_eva_2 Gratuidade Não Regimental"),
    ("set", "set_qualifi_presen_eva_2 Gratuidade Não Regimental"),
    ("out", "out_qualifi_presen_eva_2 Gratuidade Não Regimental"),
    ("nov", "nov_qualifi_presen_eva_2 Gratuidade Não Regimental"),
    ("dez", "dez_qualifi_presen_eva_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_bolsa_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5162'].indicador")))
    qualifi_bolsa_eva.click()

   
    qualifi_bolsa_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    chave_dado = f"{mes}_qualifi_presen_eva_2 Gratuidade Não Regimental"
    
   
    eva_qualificacao_presencial_bolsa = dados['qualificacao']['presencial']['evadidos'].get(chave_dado, 0)

    qualifi_bolsa_eva.send_keys(str(eva_qualificacao_presencial_bolsa))
    qualifi_bolsa_eva.send_keys(Keys.ENTER)


    #  30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL evadidos NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_qualifi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_qualifi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_qualifi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_qualifi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_qualifi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_qualifi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_qualifi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_qualifi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_qualifi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_qualifi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_qualifi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_qualifi_presen_eva_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_ng_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5163'].indicador")))
    qualifi_ng_eva.click()

   
    qualifi_ng_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_presen_eva_9 Pago por Pessoa Fisica ou Empresa"
    
    
    eva_qualificacao_presencial_nao_gratuita = dados['qualificacao']['presencial']['evadidos'].get(chave_dado, 0)

    qualifi_ng_eva.send_keys(str(eva_qualificacao_presencial_nao_gratuita))
    qualifi_ng_eva.send_keys(Keys.ENTER)


# 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL evadidos Regimental

nav.refresh()

meses = [
    ("jan", "jan_qualifi_presen_eva_1 Gratuidade Regimental"),
    ("fev", "fev_qualifi_presen_eva_1 Gratuidade Regimental"),
    ("mar", "mar_qualifi_presen_eva_1 Gratuidade Regimental"),
    ("abr", "abr_qualifi_presen_eva_1 Gratuidade Regimental"),
    ("mai", "mai_qualifi_presen_eva_1 Gratuidade Regimental"),
    ("jun", "jun_qualifi_presen_eva_1 Gratuidade Regimental"),
    ("jul", "jul_qualifi_presen_eva_1 Gratuidade Regimental"),
    ("ago", "ago_qualifi_presen_eva_1 Gratuidade Regimental"),
    ("set", "set_qualifi_presen_eva_1 Gratuidade Regimental"),
    ("out", "out_qualifi_presen_eva_1 Gratuidade Regimental"),
    ("nov", "nov_qualifi_presen_eva_1 Gratuidade Regimental"),
    ("dez", "dez_qualifi_presen_eva_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    quali_regime_eva_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5164'].indicador")))
    quali_regime_eva_eva.click()

   
    quali_regime_eva_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_presen_eva_1 Gratuidade Regimental"
    
    
    eva_qualificacao_presencial_regimental = dados['qualificacao']['presencial']['evadidos'].get(chave_dado, 0)

    quali_regime_eva_eva.send_keys(str(eva_qualificacao_presencial_regimental))
    quali_regime_eva_eva.send_keys(Keys.ENTER)


#  30303020401 - QUALIFICACAO PROFISSIONAL SEMIPRESENCIAL - BOLSA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030204/245?cd_centro_resp=30303020401&nm_unidade=SENAI%20SOBRADINHO&nm_centro_resp=QUALIFICACAO%20PROFISSIONAL%20SEMIPRESENCIAL&id_grupo=3&ds_grupo=Qualifica%C3%A7%C3%A3o%20Industrial&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)

nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_qualifi_distan_eva_2 Gratuidade Não Regimental"),
    ("fev", "fev_qualifi_distan_eva_2 Gratuidade Não Regimental"),
    ("mar", "mar_qualifi_distan_eva_2 Gratuidade Não Regimental"),
    ("abr", "abr_qualifi_distan_eva_2 Gratuidade Não Regimental"),
    ("mai", "mai_qualifi_distan_eva_2 Gratuidade Não Regimental"),
    ("jun", "jun_qualifi_distan_eva_2 Gratuidade Não Regimental"),
    ("jul", "jul_qualifi_distan_eva_2 Gratuidade Não Regimental"),
    ("ago", "ago_qualifi_distan_eva_2 Gratuidade Não Regimental"),
    ("set", "set_qualifi_distan_eva_2 Gratuidade Não Regimental"),
    ("out", "out_qualifi_distan_eva_2 Gratuidade Não Regimental"),
    ("nov", "nov_qualifi_distan_eva_2 Gratuidade Não Regimental"),
    ("dez", "dez_qualifi_distan_eva_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_bolsa_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5202'].indicador")))
    qualifi_semi_bolsa_eva.click()

   
    qualifi_semi_bolsa_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_distan_eva_2 Gratuidade Não Regimental"
    
    
    eva_qualifica_semi_bolsa = dados['qualificacao']['distancia']['evadidos'].get(chave_dado, 0)

    qualifi_semi_bolsa_eva.send_keys(str(eva_qualifica_semi_bolsa))
    qualifi_semi_bolsa_eva.send_keys(Keys.ENTER)

# 30303020401 - QUALIFICACAO PROFISSIONAL SEMIPRESENCIAL - NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_qualifi_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_qualifi_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_qualifi_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_qualifi_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_qualifi_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_qualifi_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_qualifi_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_qualifi_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_qualifi_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_qualifi_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_qualifi_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_qualifi_distan_eva_9 Pago por Pessoa Fisica ou Empresa")
]


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_ng_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5203'].indicador")))
    qualifi_semi_ng_eva.click()

   
    qualifi_semi_ng_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_distan_eva_9 Pago por Pessoa Fisica ou Empresa"
    
    
    eva_qualifica_semi_ng = dados['qualificacao']['distancia']['evadidos'].get(chave_dado, 0)

    qualifi_semi_ng_eva.send_keys(str(eva_qualifica_semi_ng))
    qualifi_semi_ng_eva.send_keys(Keys.ENTER)

# 30303020401 - QUALIFICACAO PROFISSIONAL SEMIPRESENCIAL - REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_qualifi_distan_eva_1 Gratuidade Regimental"),
    ("fev", "fev_qualifi_distan_eva_1 Gratuidade Regimental"),
    ("mar", "mar_qualifi_distan_eva_1 Gratuidade Regimental"),
    ("abr", "abr_qualifi_distan_eva_1 Gratuidade Regimental"),
    ("mai", "mai_qualifi_distan_eva_1 Gratuidade Regimental"),
    ("jun", "jun_qualifi_distan_eva_1 Gratuidade Regimental"),
    ("jul", "jul_qualifi_distan_eva_1 Gratuidade Regimental"),
    ("ago", "ago_qualifi_distan_eva_1 Gratuidade Regimental"),
    ("set", "set_qualifi_distan_eva_1 Gratuidade Regimental"),
    ("out", "out_qualifi_distan_eva_1 Gratuidade Regimental"),
    ("nov", "nov_qualifi_distan_eva_1 Gratuidade Regimental"),
    ("dez", "dez_qualifi_distan_eva_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_regimental_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5204'].indicador")))
    qualifi_semi_regimental_eva.click()

   
    qualifi_semi_regimental_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_distan_eva_1 Gratuidade Regimental"
    
    
    eva_qualifica_semi_regimental = dados['qualificacao']['distancia']['evadidos'].get(chave_dado, 0)

    qualifi_semi_regimental_eva.send_keys(str(eva_qualifica_semi_regimental))
    qualifi_semi_regimental_eva.send_keys(Keys.ENTER)

    
# 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - BOLSA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030204/249?cd_centro_resp=30303020501&nm_unidade=SENAI%20SOBRADINHO&nm_centro_resp=APERF%2FESPECIALIZ%20PROFISSIONAL%20PRESENCIAL&id_grupo=5&ds_grupo=Aperfei%C3%A7oamento%20Profissional&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_aperfei_presen_eva_2 Gratuidade Não Regimental"),
    ("fev", "fev_aperfei_presen_eva_2 Gratuidade Não Regimental"),
    ("mar", "mar_aperfei_presen_eva_2 Gratuidade Não Regimental"),
    ("abr", "abr_aperfei_presen_eva_2 Gratuidade Não Regimental"),
    ("mai", "mai_aperfei_presen_eva_2 Gratuidade Não Regimental"),
    ("jun", "jun_aperfei_presen_eva_2 Gratuidade Não Regimental"),
    ("jul", "jul_aperfei_presen_eva_2 Gratuidade Não Regimental"),
    ("ago", "ago_aperfei_presen_eva_2 Gratuidade Não Regimental"),
    ("set", "set_aperfei_presen_eva_2 Gratuidade Não Regimental"),
    ("out", "out_aperfei_presen_eva_2 Gratuidade Não Regimental"),
    ("nov", "nov_aperfei_presen_eva_2 Gratuidade Não Regimental"),
    ("dez", "dez_aperfei_presen_eva_2 Gratuidade Não Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_bolsa_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5242'].indicador")))
    aper_prese_bolsa_eva.click()

   
    aper_prese_bolsa_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_eva_2 Gratuidade Não Regimental"
    
    
    eva_aper_prese_bolsa = dados['aperfeicoamento']['presencial']['evadidos'].get(chave_dado, 0)

    aper_prese_bolsa_eva.send_keys(str(eva_aper_prese_bolsa))
    aper_prese_bolsa_eva.send_keys(Keys.ENTER)


#  - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_aperfei_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_aperfei_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_aperfei_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aperfei_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aperfei_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aperfei_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aperfei_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aperfei_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aperfei_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aperfei_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aperfei_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aperfei_presen_eva_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_ng_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5243'].indicador")))
    aper_prese_ng_eva.click()

   
    aper_prese_ng_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_eva_9 Pago por Pessoa Fisica ou Empresa"
    
    
    eva_aper_prese_ng = dados['aperfeicoamento']['presencial']['evadidos'].get(chave_dado, 0)

    aper_prese_ng_eva.send_keys(str(eva_aper_prese_ng))
    aper_prese_ng_eva.send_keys(Keys.ENTER)


# 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - REGIMENTAL


nav.refresh()

meses = [
    ("jan", "jan_aperfei_presen_eva_1 Gratuidade Regimental"),
    ("fev", "fev_aperfei_presen_eva_1 Gratuidade Regimental"),
    ("mar", "mar_aperfei_presen_eva_1 Gratuidade Regimental"),
    ("abr", "abr_aperfei_presen_eva_1 Gratuidade Regimental"),
    ("mai", "mai_aperfei_presen_eva_1 Gratuidade Regimental"),
    ("jun", "jun_aperfei_presen_eva_1 Gratuidade Regimental"),
    ("jul", "jul_aperfei_presen_eva_1 Gratuidade Regimental"),
    ("ago", "ago_aperfei_presen_eva_1 Gratuidade Regimental"),
    ("set", "set_aperfei_presen_eva_1 Gratuidade Regimental"),
    ("out", "out_aperfei_presen_eva_1 Gratuidade Regimental"),
    ("nov", "nov_aperfei_presen_eva_1 Gratuidade Regimental"),
    ("dez", "dez_aperfei_presen_eva_1 Gratuidade Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_regimental_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5244'].indicador")))
    aper_prese_regimental_eva.click()

   
    aper_prese_regimental_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_eva_1 Gratuidade Regimental"
    
    
    eva_aper_prese_regimental = dados['aperfeicoamento']['presencial']['evadidos'].get(chave_dado, 0)

    aper_prese_regimental_eva.send_keys(str(eva_aper_prese_regimental))
    aper_prese_regimental_eva.send_keys(Keys.ENTER)

# 30303020601 - APERF/ESPECIALI PROFISSIONAL A DISTANCIA BOLSA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030204/242?cd_centro_resp=30303020601&nm_unidade=SENAI%20SOBRADINHO&nm_centro_resp=APERF%2FESPECIALI%20PROFISSIONAL%20A%20DISTANCIA&id_grupo=5&ds_grupo=Aperfei%C3%A7oamento%20Profissional&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_aperfei_distan_eva_2 Gratuidade Não Regimental"),
    ("fev", "fev_aperfei_distan_eva_2 Gratuidade Não Regimental"),
    ("mar", "mar_aperfei_distan_eva_2 Gratuidade Não Regimental"),
    ("abr", "abr_aperfei_distan_eva_2 Gratuidade Não Regimental"),
    ("mai", "mai_aperfei_distan_eva_2 Gratuidade Não Regimental"),
    ("jun", "jun_aperfei_distan_eva_2 Gratuidade Não Regimental"),
    ("jul", "jul_aperfei_distan_eva_2 Gratuidade Não Regimental"),
    ("ago", "ago_aperfei_distan_eva_2 Gratuidade Não Regimental"),
    ("set", "set_aperfei_distan_eva_2 Gratuidade Não Regimental"),
    ("out", "out_aperfei_distan_eva_2 Gratuidade Não Regimental"),
    ("nov", "nov_aperfei_distan_eva_2 Gratuidade Não Regimental"),
    ("dez", "dez_aperfei_distan_eva_2 Gratuidade Não Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    aper_dista_bolsa_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5174'].indicador")))
    aper_dista_bolsa_eva.click()

   
    aper_dista_bolsa_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_distan_eva_2 Gratuidade Não Regimental"
    
    
    eva_aper_distan_bolsa = dados['aperfeicoamento']['distancia']['evadidos'].get(chave_dado, 0)

    aper_dista_bolsa_eva.send_keys(str(eva_aper_distan_bolsa))
    aper_dista_bolsa_eva.send_keys(Keys.ENTER)

# 30303020601 - APERF/ESPECIALI PROFISSIONAL A DISTANCIA NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "fev_aperfei_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_aperfei_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),  
    ("mar", "mar_aperfei_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aperfei_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aperfei_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aperfei_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aperfei_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aperfei_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aperfei_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aperfei_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aperfei_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aperfei_distan_eva_9 Pago por Pessoa Fisica ou Empresa")
]


for i, (mes, campo_dado) in enumerate(meses):

    aper_dista_ng_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5175'].indicador")))
    aper_dista_ng_eva.click()

   
    aper_dista_ng_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_distan_eva_9 Pago por Pessoa Fisica ou Empresa"
    
    eva_aper_distan_ng = dados['aperfeicoamento']['distancia']['evadidos'].get(chave_dado, 0)

    aper_dista_ng_eva.send_keys(str(eva_aper_distan_ng))
    aper_dista_ng_eva.send_keys(Keys.ENTER)

# 30303020601 - APERF/ESPECIALI PROFISSIONAL A DISTANCIA REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_aperfei_distan_eva_1 Gratuidade Regimental"),
    ("fev", "fev_aperfei_distan_eva_1 Gratuidade Regimental"),
    ("mar", "mar_aperfei_distan_eva_1 Gratuidade Regimental"),
    ("abr", "abr_aperfei_distan_eva_1 Gratuidade Regimental"),
    ("mai", "mai_aperfei_distan_eva_1 Gratuidade Regimental"),
    ("jun", "jun_aperfei_distan_eva_1 Gratuidade Regimental"),
    ("jul", "jul_aperfei_distan_eva_1 Gratuidade Regimental"),
    ("ago", "ago_aperfei_distan_eva_1 Gratuidade Regimental"),
    ("set", "set_aperfei_distan_eva_1 Gratuidade Regimental"),
    ("out", "out_aperfei_distan_eva_1 Gratuidade Regimental"),
    ("nov", "nov_aperfei_distan_eva_1 Gratuidade Regimental"),
    ("dez", "dez_aperfei_distan_eva_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    aper_dista_regimental_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5176'].indicador")))
    aper_dista_regimental_eva.click()

    aper_dista_regimental_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_distan_eva_1 Gratuidade Regimental"
    
    eva_aper_distan_regimental = dados['aperfeicoamento']['distancia']['evadidos'].get(chave_dado, 0)

    aper_dista_regimental_eva.send_keys(str(eva_aper_distan_regimental))
    aper_dista_regimental_eva.send_keys(Keys.ENTER)

# 30303020901 - QUALIFIC PROF PRESENC - ITINER V ENS MED - BOLSA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030204/246?cd_centro_resp=30303020901&nm_unidade=SENAI%20SOBRADINHO&nm_centro_resp=QUALIFIC%20PROF%20PRESENC%20-%20ITINER%20V%20ENS%20MED&id_grupo=3&ds_grupo=Qualifica%C3%A7%C3%A3o%20Industrial&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])


nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_qualifi_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("fev", "fev_qualifi_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("mar", "mar_qualifi_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("abr", "abr_qualifi_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("mai", "mai_qualifi_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("jun", "jun_qualifi_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("jul", "jul_qualifi_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("ago", "ago_qualifi_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("set", "set_qualifi_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("out", "out_qualifi_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("nov", "nov_qualifi_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("dez", "dez_qualifi_iti_presen_eva_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_iti_presencial_bolsa_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5214'].indicador")))
    qualifi_iti_presencial_bolsa_eva.click()

   
    qualifi_iti_presencial_bolsa_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_eva_2 Gratuidade Não Regimental"
    
    eva_quali_iti_presencial_bolsa = dados['qualificacao_iti']['presencial']['evadidos'].get(chave_dado, 0)

    qualifi_iti_presencial_bolsa_eva.send_keys(str(eva_quali_iti_presencial_bolsa))
    qualifi_iti_presencial_bolsa_eva.send_keys(Keys.ENTER)


# 30303020901 - QUALIFIC PROF PRESENC - ITINER V ENS MED - NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_qualifi_iti_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_qualifi_iti_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_qualifi_iti_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_qualifi_iti_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_qualifi_iti_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_qualifi_iti_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_qualifi_iti_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_qualifi_iti_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_qualifi_iti_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_qualifi_iti_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_qualifi_iti_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_qualifi_iti_presen_eva_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_iti_presencial_ng_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5215'].indicador")))
    qualifi_iti_presencial_ng_eva.click()

   
    qualifi_iti_presencial_ng_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_eva_9 Pago por Pessoa Fisica ou Empresa"
    
    eva_quali_iti_presencial_ng = dados['qualificacao_iti']['presencial']['evadidos'].get(chave_dado, 0)

    qualifi_iti_presencial_ng_eva.send_keys(str(eva_quali_iti_presencial_ng))
    qualifi_iti_presencial_ng_eva.send_keys(Keys.ENTER)


# 30303020901 - QUALIFIC PROF PRESENC - ITINER V ENS MED - REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_qualifi_iti_presen_eva_1 Gratuidade Regimental"),
    ("fev", "fev_qualifi_iti_presen_eva_1 Gratuidade Regimental"),
    ("mar", "mar_qualifi_iti_presen_eva_1 Gratuidade Regimental"),
    ("abr", "abr_qualifi_iti_presen_eva_1 Gratuidade Regimental"),
    ("mai", "mai_qualifi_iti_presen_eva_1 Gratuidade Regimental"),
    ("jun", "jun_qualifi_iti_presen_eva_1 Gratuidade Regimental"),
    ("jul", "jul_qualifi_iti_presen_eva_1 Gratuidade Regimental"),
    ("ago", "ago_qualifi_iti_presen_eva_1 Gratuidade Regimental"),
    ("set", "set_qualifi_iti_presen_eva_1 Gratuidade Regimental"),
    ("out", "out_qualifi_iti_presen_eva_1 Gratuidade Regimental"),
    ("nov", "nov_qualifi_iti_presen_eva_1 Gratuidade Regimental"),
    ("dez", "dez_qualifi_iti_presen_eva_1 Gratuidade Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_iti_presencial_regimental_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5216'].indicador")))
    qualifi_iti_presencial_regimental_eva.click()

   
    qualifi_iti_presencial_regimental_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_eva_1 Gratuidade Regimental"
    
    eva_quali_iti_presencial_regimental = dados['qualificacao_iti']['presencial']['evadidos'].get(chave_dado, 0)

    qualifi_iti_presencial_regimental_eva.send_keys(str(eva_quali_iti_presencial_regimental))
    qualifi_iti_presencial_regimental_eva.send_keys(Keys.ENTER)


# 30303040101 - APREND. IND. TEC. NIVEL MEDIO PRESENCIAL - NAO GRATUITA


from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030204/250?cd_centro_resp=30303040101&nm_unidade=SENAI%20SOBRADINHO&nm_centro_resp=APREND.%20IND.%20TEC.%20NIVEL%20MEDIO%20PRESENCIAL&id_grupo=11&ds_grupo=Aprendizagem%20Industrial%20T%C3%A9cnico%20de%20N%C3%ADvel%20M%C3%A9dio&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_aprendi_tec_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_aprendi_tec_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_aprendi_tec_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aprendi_tec_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aprendi_tec_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aprendi_tec_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aprendi_tec_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aprendi_tec_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aprendi_tec_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aprendi_tec_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aprendi_tec_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aprendi_tec_presen_eva_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    aprendi_tec_presencial_ng_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5253'].indicador")))
    aprendi_tec_presencial_ng_eva.click()

   
    aprendi_tec_presencial_ng_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aprendi_tec_presen_eva_9 Pago por Pessoa Fisica ou Empresa"
    
    eva_aprendi_tec_presencial_ng = dados['aprendizagem_tec']['presencial']['evadidos'].get(chave_dado, 0)

    aprendi_tec_presencial_ng_eva.send_keys(str(eva_aprendi_tec_presencial_ng))
    aprendi_tec_presencial_ng_eva.send_keys(Keys.ENTER)


#  30303040101 - APREND. IND. TEC. NIVEL MEDIO PRESENCIAL - REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_aprendi_tec_presen_eva_1 Gratuidade Regimental"),
    ("fev", "fev_aprendi_tec_presen_eva_1 Gratuidade Regimental"),
    ("mar", "mar_aprendi_tec_presen_eva_1 Gratuidade Regimental"),
    ("abr", "abr_aprendi_tec_presen_eva_1 Gratuidade Regimental"),
    ("mai", "mai_aprendi_tec_presen_eva_1 Gratuidade Regimental"),
    ("jun", "jun_aprendi_tec_presen_eva_1 Gratuidade Regimental"),
    ("jul", "jul_aprendi_tec_presen_eva_1 Gratuidade Regimental"),
    ("ago", "ago_aprendi_tec_presen_eva_1 Gratuidade Regimental"),
    ("set", "set_aprendi_tec_presen_eva_1 Gratuidade Regimental"),
    ("out", "out_aprendi_tec_presen_eva_1 Gratuidade Regimental"),
    ("nov", "nov_aprendi_tec_presen_eva_1 Gratuidade Regimental"),
    ("dez", "dez_aprendi_tec_presen_eva_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    aprendi_tec_presencial_regimental_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5254'].indicador")))
    aprendi_tec_presencial_regimental_eva.click()

   
    aprendi_tec_presencial_regimental_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aprendi_tec_presen_eva_1 Gratuidade Regimental"
    
    eva_aprendi_tec_presencial_regimental = dados['aprendizagem_tec']['presencial']['evadidos'].get(chave_dado, 0)

    aprendi_tec_presencial_regimental_eva.send_keys(str(eva_aprendi_tec_presencial_regimental))
    aprendi_tec_presencial_regimental_eva.send_keys(Keys.ENTER)

# 30303040201 - TECNICO DE NIVEL MEDIO PRESENCIAL - NAO GRATUITA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030204/243?cd_centro_resp=30303040201&nm_unidade=SENAI%20SOBRADINHO&nm_centro_resp=TECNICO%20DE%20NIVEL%20MEDIO%20PRESENCIAL&id_grupo=4&ds_grupo=T%C3%A9cnico%20de%20N%C3%ADvel%20M%C3%A9dio&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_tecni_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_tecni_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_tecni_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_tecni_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_tecni_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_tecni_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_tecni_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_tecni_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_tecni_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_tecni_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_tecni_presen_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_tecni_presen_eva_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_presencial_ng_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5185'].indicador")))
    tec_presencial_ng_eva.click()

   
    tec_presencial_ng_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_presen_eva_9 Pago por Pessoa Fisica ou Empresa"
    
    eva_tec_presencial_ng = dados['tecnico_nm']['presencial']['evadidos'].get(chave_dado, 0)

    tec_presencial_ng_eva.send_keys(str(eva_tec_presencial_ng))
    tec_presencial_ng_eva.send_keys(Keys.ENTER)

# 30303040201 - TECNICO DE NIVEL MEDIO PRESENCIAL - REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_tecni_presen_eva_1 Gratuidade Regimental"),
    ("fev", "fev_tecni_presen_eva_1 Gratuidade Regimental"),
    ("mar", "mar_tecni_presen_eva_1 Gratuidade Regimental"),
    ("abr", "abr_tecni_presen_eva_1 Gratuidade Regimental"),
    ("mai", "mai_tecni_presen_eva_1 Gratuidade Regimental"),
    ("jun", "jun_tecni_presen_eva_1 Gratuidade Regimental"),
    ("jul", "jul_tecni_presen_eva_1 Gratuidade Regimental"),
    ("ago", "ago_tecni_presen_eva_1 Gratuidade Regimental"),
    ("set", "set_tecni_presen_eva_1 Gratuidade Regimental"),
    ("out", "out_tecni_presen_eva_1 Gratuidade Regimental"),
    ("nov", "nov_tecni_presen_eva_1 Gratuidade Regimental"),
    ("dez", "dez_tecni_presen_eva_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_presencial_regimental_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5186'].indicador")))
    tec_presencial_regimental_eva.click()

   
    tec_presencial_regimental_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_presen_eva_1 Gratuidade Regimental"
    
    eva_tec_presencial_regimental = dados['tecnico_nm']['presencial']['evadidos'].get(chave_dado, 0)

    tec_presencial_regimental_eva.send_keys(str(eva_tec_presencial_regimental))
    tec_presencial_regimental_eva.send_keys(Keys.ENTER)


# 30303040401 - TECNICO DE NIVEL MEDIO SEMIPRESENCIAL NAO GRATUITA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030204/247?cd_centro_resp=30303040401&nm_unidade=SENAI%20SOBRADINHO&nm_centro_resp=TECNICO%20DE%20NIVEL%20MEDIO%20SEMIPRESENCIAL&id_grupo=4&ds_grupo=T%C3%A9cnico%20de%20N%C3%ADvel%20M%C3%A9dio&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_tecni_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_tecni_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_tecni_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_tecni_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_tecni_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_tecni_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_tecni_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_tecni_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_tecni_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_tecni_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_tecni_distan_eva_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_tecni_distan_eva_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_distancia_ng_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5225'].indicador")))
    tec_distancia_ng_eva.click()

   
    tec_distancia_ng_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_distan_eva_9 Pago por Pessoa Fisica ou Empresa"
    
    eva_tec_distancia_ng = dados['tecnico_nm']['distancia']['evadidos'].get(chave_dado, 0)

    tec_distancia_ng_eva.send_keys(str(eva_tec_distancia_ng))
    tec_distancia_ng_eva.send_keys(Keys.ENTER)

#30303040401 - TECNICO DE NIVEL MEDIO SEMIPRESENCIAL REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_tecni_distan_eva_1 Gratuidade Regimental"),
    ("fev", "fev_tecni_distan_eva_1 Gratuidade Regimental"),
    ("mar", "mar_tecni_distan_eva_1 Gratuidade Regimental"),
    ("abr", "abr_tecni_distan_eva_1 Gratuidade Regimental"),
    ("mai", "mai_tecni_distan_eva_1 Gratuidade Regimental"),
    ("jun", "jun_tecni_distan_eva_1 Gratuidade Regimental"),
    ("jul", "jul_tecni_distan_eva_1 Gratuidade Regimental"),
    ("ago", "ago_tecni_distan_eva_1 Gratuidade Regimental"),
    ("set", "set_tecni_distan_eva_1 Gratuidade Regimental"),
    ("out", "out_tecni_distan_eva_1 Gratuidade Regimental"),
    ("nov", "nov_tecni_distan_eva_1 Gratuidade Regimental"),
    ("dez", "dez_tecni_distan_eva_1 Gratuidade Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    tec_distancia_regimental_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5226'].indicador")))
    tec_distancia_regimental_eva.click()

   
    tec_distancia_regimental_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_distan_eva_1 Gratuidade Regimental"
    
    eva_tec_distancia_regimental = dados['tecnico_nm']['distancia']['evadidos'].get(chave_dado, 0)

    tec_distancia_regimental_eva.send_keys(str(eva_tec_distancia_regimental))
    tec_distancia_regimental_eva.send_keys(Keys.ENTER)


#  30303040501 - TECN DE NIV MED ITINERARIOS PRESENCIAL BOLSA

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030204/251?cd_centro_resp=30303040501&nm_unidade=SENAI%20SOBRADINHO&nm_centro_resp=TECN%20DE%20NIV%20MED%20ITINERARIOS%20PRESENCIAL&id_grupo=4&ds_grupo=T%C3%A9cnico%20de%20N%C3%ADvel%20M%C3%A9dio&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_tecni_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("fev", "fev_tecni_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("mar", "mar_tecni_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("abr", "abr_tecni_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("mai", "mai_tecni_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("jun", "jun_tecni_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("jul", "jul_tecni_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("ago", "ago_tecni_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("set", "set_tecni_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("out", "out_tecni_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("nov", "nov_tecni_iti_presen_eva_2 Gratuidade Não Regimental"),
    ("dez", "dez_tecni_iti_presen_eva_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_iti_presencial_bolsa_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5483'].indicador")))
    tec_iti_presencial_bolsa_eva.click()

   
    tec_iti_presencial_bolsa_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_iti_presen_eva_2 Gratuidade Não Regimental"
    
    eva_tec_iti_presencial_bolsa = dados['tecnico_nm_iti']['presencial']['evadidos'].get(chave_dado, 0)

    tec_iti_presencial_bolsa_eva.send_keys(str(eva_tec_iti_presencial_bolsa))
    tec_iti_presencial_bolsa_eva.send_keys(Keys.ENTER)

# 30303040501 - TECN DE NIV MED ITINERARIOS PRESENCIAL REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_tecni_iti_presen_eva_1 Gratuidade Regimental"),
    ("fev", "fev_tecni_iti_presen_eva_1 Gratuidade Regimental"),
    ("mar", "mar_tecni_iti_presen_eva_1 Gratuidade Regimental"),
    ("abr", "abr_tecni_iti_presen_eva_1 Gratuidade Regimental"),
    ("mai", "mai_tecni_iti_presen_eva_1 Gratuidade Regimental"),
    ("jun", "jun_tecni_iti_presen_eva_1 Gratuidade Regimental"),
    ("jul", "jul_tecni_iti_presen_eva_1 Gratuidade Regimental"),
    ("ago", "ago_tecni_iti_presen_eva_1 Gratuidade Regimental"),
    ("set", "set_tecni_iti_presen_eva_1 Gratuidade Regimental"),
    ("out", "out_tecni_iti_presen_eva_1 Gratuidade Regimental"),
    ("nov", "nov_tecni_iti_presen_eva_1 Gratuidade Regimental"),
    ("dez", "dez_tecni_iti_presen_eva_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_iti_presencial_regimental_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5260'].indicador")))
    tec_iti_presencial_regimental_eva.click()

   
    tec_iti_presencial_regimental_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_iti_presen_eva_1 Gratuidade Regimental"
    
    eva_tec_iti_presencial_regimental = dados['tecnico_nm_iti']['presencial']['evadidos'].get(chave_dado, 0)

    tec_iti_presencial_regimental_eva.send_keys(str(eva_tec_iti_presencial_regimental))
    tec_iti_presencial_regimental_eva.send_keys(Keys.ENTER)


# SENAI sobUATINGA - 30303040501 - TECN DE NIV MED ITINERARIOS PRESENCIAL NAO GRATUITA
