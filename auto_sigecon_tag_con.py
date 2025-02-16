
# Importação dos pacotes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from obter_dados_tag_con import obter_dados_por_tipo

arquivo = 'si_jan.xlsx'

dados = {
    'iniciacao': {
        'presencial': {
            'concluintes': obter_dados_por_tipo('iniciacao', 'presencial')['concluintes'],
        },
        'distancia': {
            'concluintes': obter_dados_por_tipo('iniciacao', 'distancia')['concluintes'],
        }
    },
    'aprendizagem': {
        'presencial': {
            'concluintes': obter_dados_por_tipo('aprendizagem', 'presencial')['concluintes'],
        },
        'distancia': {
            'concluintes': obter_dados_por_tipo('aprendizagem', 'distancia')['concluintes'],
        }
    },
    'qualificacao': {
        'presencial': {
            'concluintes': obter_dados_por_tipo('qualificacao', 'presencial')['concluintes'],
        },
        'distancia': {
            'concluintes': obter_dados_por_tipo('qualificacao', 'distancia')['concluintes'],
        }
    },
    'aperfeicoamento': {
        'presencial': {
            'concluintes': obter_dados_por_tipo('aperfeicoamento', 'presencial')['concluintes'],
        },
        'distancia': {
            'concluintes': obter_dados_por_tipo('aperfeicoamento', 'distancia')['concluintes'],
        }
    },
    'qualificacao_iti': {
        'presencial': {
            'concluintes': obter_dados_por_tipo('qualificacao_iti', 'presencial')['concluintes'],
        }
    },
    'aprendizagem_tec': {
        'presencial': {
            'concluintes': obter_dados_por_tipo('aprendizagem_tec', 'presencial')['concluintes'],
        }
    },
    'tecnico_nm': {
        'presencial': {
            'concluintes': obter_dados_por_tipo('tecnico_nm', 'presencial')['concluintes'],
        },
        'distancia': {
            'concluintes': obter_dados_por_tipo('tecnico_nm', 'distancia')['concluintes'],
        }
    },
    'tecnico_nm_iti': {
        'presencial': {
            'concluintes': obter_dados_por_tipo('tecnico_nm_iti', 'presencial')['concluintes'],
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

################################################################   Concluintes BOLSA ####################################################################################################

nav.refresh()

meses = [
    ("jan", "jan_inicia_presen_con_2 Gratuidade Não Regimental"),
    ("fev", "fev_inicia_presen_con_2 Gratuidade Não Regimental"),
    ("mar", "mar_inicia_presen_con_2 Gratuidade Não Regimental"),
    ("abr", "abr_inicia_presen_con_2 Gratuidade Não Regimental"),
    ("mai", "mai_inicia_presen_con_2 Gratuidade Não Regimental"),
    ("jun", "jun_inicia_presen_con_2 Gratuidade Não Regimental"),
    ("jul", "jul_inicia_presen_con_2 Gratuidade Não Regimental"),
    ("ago", "ago_inicia_presen_con_2 Gratuidade Não Regimental"),
    ("set", "set_inicia_presen_con_2 Gratuidade Não Regimental"),
    ("out", "out_inicia_presen_con_2 Gratuidade Não Regimental"),
    ("nov", "nov_inicia_presen_con_2 Gratuidade Não Regimental"),
    ("dez", "dez_inicia_presen_con_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):
   
    con_bolsa_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5107'].indicador"))
    )
    con_bolsa_mes.click()

    con_bolsa_send = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_presen_con_2 Gratuidade Não Regimental"
    
    con_iniciacao_presencial_geral = dados['iniciacao']['presencial']['concluintes'].get(chave_dado, 0)

    con_bolsa_send.send_keys(str(con_iniciacao_presencial_geral))
    con_bolsa_send.send_keys(Keys.ENTER)


############################################################   Concluintes NAO GRATUITA ####################################################################################################

nav.refresh() 

meses = [
    ("jan", "jan_inicia_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_inicia_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_inicia_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_inicia_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_inicia_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_inicia_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_inicia_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_inicia_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_inicia_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_inicia_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_inicia_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_inicia_presen_con_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):
    
    con_ng_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5108'].indicador"))
    )
    con_ng_mes.click()

    con_ng_send = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_presen_con_9 Pago por Pessoa Fisica ou Empresa"
    
    con_iniciacao_presencial_ng = dados['iniciacao']['presencial']['concluintes'].get(chave_dado, 0)

    con_ng_send.send_keys(str(con_iniciacao_presencial_ng))
    con_ng_send.send_keys(Keys.ENTER)


#########################################  INICIAÇÃO PROFISSIONAL A DISTANCIA  ##########################################################################################################


janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/225?cd_centro_resp=30303010201&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=INICIACAO%20PROFISSIONAL%20A%20DISTANCIA&id_grupo=1&ds_grupo=Inicia%C3%A7%C3%A3o%20Profissional&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA Concluintes BOLSA ##################################################################################################

nav.refresh()

meses = [
    ("jan", "jan_inicia_distan_con_2 Gratuidade Não Regimental"),
    ("fev", "fev_inicia_distan_con_2 Gratuidade Não Regimental"),
    ("mar", "mar_inicia_distan_con_2 Gratuidade Não Regimental"),
    ("abr", "abr_inicia_distan_con_2 Gratuidade Não Regimental"),
    ("mai", "mai_inicia_distan_con_2 Gratuidade Não Regimental"),
    ("jun", "jun_inicia_distan_con_2 Gratuidade Não Regimental"),
    ("jul", "jul_inicia_distan_con_2 Gratuidade Não Regimental"),
    ("ago", "ago_inicia_distan_con_2 Gratuidade Não Regimental"),
    ("set", "set_inicia_distan_con_2 Gratuidade Não Regimental"),
    ("out", "out_inicia_distan_con_2 Gratuidade Não Regimental"),
    ("nov", "nov_inicia_distan_con_2 Gratuidade Não Regimental"),
    ("dez", "dez_inicia_distan_con_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    con_ipd_bolsa_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5067'].indicador"))
    )
    con_ipd_bolsa_mes.click()

    con_ipd_bolsa_mes = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_distan_con_2 Gratuidade Não Regimental"
    
    con_iniciacao_distancia_bolsa = dados['iniciacao']['distancia']['concluintes'].get(chave_dado, 0)

    con_ipd_bolsa_mes.send_keys(str(con_iniciacao_distancia_bolsa))
    con_ipd_bolsa_mes.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA Concluintes NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_inicia_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_inicia_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_inicia_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_inicia_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_inicia_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_inicia_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_inicia_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_inicia_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_inicia_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_inicia_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_inicia_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_inicia_distan_con_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    con_ipd_ng_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5068'].indicador"))
    )
    con_ipd_ng_mes.click()

    con_ipd_ng_mes = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_distan_con_9 Pago por Pessoa Fisica ou Empresa"
    

    con_iniciacao_distancia_ng = dados['iniciacao']['distancia']['concluintes'].get(chave_dado, 0)

    con_ipd_ng_mes.send_keys(str(con_iniciacao_distancia_ng))
    con_ipd_ng_mes.send_keys(Keys.ENTER)


###################################################  Aprendizagem Industrial - Presencial #############################################################

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/230?cd_centro_resp=30303020101&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APRENDIZAGEM%20INDUSTRIAL%20PRESENCIAL&id_grupo=2&ds_grupo=Aprendizagem%20Industrial&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])


# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL Concluintes NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_aprendi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_aprendi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_aprendi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aprendi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aprendi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aprendi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aprendi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aprendi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aprendi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aprendi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aprendi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aprendi_presen_con_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    app_ng_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5115'].indicador")))
    app_ng_con.click()


    app_ng_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    chave_dado = f"{mes}_aprendi_presen_con_9 Pago por Pessoa Fisica ou Empresa"
    
    con_aprendizagem_presencial_ng = dados['aprendizagem']['presencial']['concluintes'].get(chave_dado, 0)

    app_ng_con.send_keys(str(con_aprendizagem_presencial_ng))
    app_ng_con.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL Concluintes REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_aprendi_presen_con_1 Gratuidade Regimenta" ),
    ("fev", "fev_aprendi_presen_con_1 Gratuidade Regimental"),
    ("mar", "mar_aprendi_presen_con_1 Gratuidade Regimental"),
    ("abr", "abr_aprendi_presen_con_1 Gratuidade Regimental"),
    ("mai", "mai_aprendi_presen_con_1 Gratuidade Regimental"),
    ("jun", "jun_aprendi_presen_con_1 Gratuidade Regimental"),
    ("jul", "jul_aprendi_presen_con_1 Gratuidade Regimental"),
    ("ago", "ago_aprendi_presen_con_1 Gratuidade Regimental"),
    ("set", "set_aprendi_presen_con_1 Gratuidade Regimental"),
    ("out", "out_aprendi_presen_con_1 Gratuidade Regimental"),
    ("nov", "nov_aprendi_presen_con_1 Gratuidade Regimental"),
    ("dez", "dez_aprendi_presen_con_1 Gratuidade Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    app_regimental_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5116'].indicador")))
    app_regimental_con.click()

   
    app_regimental_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))


    chave_dado = f"{mes}_aprendi_presen_con_1 Gratuidade Regimental"
    
   
    con_aprendizagem_presencial_regimental = dados['aprendizagem']['presencial']['concluintes'].get(chave_dado, 0)

    app_regimental_con.send_keys(str(con_aprendizagem_presencial_regimental))
    app_regimental_con.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL Concluintes CONVENIO

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/221?cd_centro_resp=30303020201&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=QUALIFICACAO%20PROFISSIONAL%20PRESENCIAL&id_grupo=3&ds_grupo=Qualifica%C3%A7%C3%A3o%20Industrial&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_qualifi_presen_con_3 Convênio"),
    ("fev", "fev_qualifi_presen_con_3 Convênio"),
    ("mar", "mar_qualifi_presen_con_3 Convênio"),
    ("abr", "abr_qualifi_presen_con_3 Convênio"),
    ("mai", "mai_qualifi_presen_con_3 Convênio"),
    ("jun", "jun_qualifi_presen_con_3 Convênio"),
    ("jul", "jul_qualifi_presen_con_3 Convênio"),
    ("ago", "ago_qualifi_presen_con_3 Convênio"),
    ("set", "set_qualifi_presen_con_3 Convênio"),
    ("out", "out_qualifi_presen_con_3 Convênio"),
    ("nov", "nov_qualifi_presen_con_3 Convênio"),
    ("dez", "dez_qualifi_presen_con_3 Convênio")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_convenio_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5019'].indicador")))
    qualifi_convenio_con.click()

   
    qualifi_convenio_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

   
    chave_dado = f"{mes}_qualifi_presen_con_3 Convênio"
    
  
    con_qualificacao_presencial_convenio = dados['qualificacao']['presencial']['concluintes'].get(chave_dado, 0)

    qualifi_convenio_con.send_keys(str(con_qualificacao_presencial_convenio))
    qualifi_convenio_con.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL Concluintes BOLSA

nav.refresh()

meses = [
    ("jan", "jan_qualifi_presen_con_2 Gratuidade Não Regimental"),
    ("fev", "fev_qualifi_presen_con_2 Gratuidade Não Regimental"),
    ("mar", "mar_qualifi_presen_con_2 Gratuidade Não Regimental"),
    ("abr", "abr_qualifi_presen_con_2 Gratuidade Não Regimental"),
    ("mai", "mai_qualifi_presen_con_2 Gratuidade Não Regimental"),
    ("jun", "jun_qualifi_presen_con_2 Gratuidade Não Regimental"),
    ("jul", "jul_qualifi_presen_con_2 Gratuidade Não Regimental"),
    ("ago", "ago_qualifi_presen_con_2 Gratuidade Não Regimental"),
    ("set", "set_qualifi_presen_con_2 Gratuidade Não Regimental"),
    ("out", "out_qualifi_presen_con_2 Gratuidade Não Regimental"),
    ("nov", "nov_qualifi_presen_con_2 Gratuidade Não Regimental"),
    ("dez", "dez_qualifi_presen_con_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_bolsa_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5023'].indicador")))
    qualifi_bolsa_con.click()

   
    qualifi_bolsa_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    chave_dado = f"{mes}_qualifi_presen_con_2 Gratuidade Não Regimental"
    
   
    con_qualificacao_presencial_bolsa = dados['qualificacao']['presencial']['concluintes'].get(chave_dado, 0)

    qualifi_bolsa_con.send_keys(str(con_qualificacao_presencial_bolsa))
    qualifi_bolsa_con.send_keys(Keys.ENTER)


    # SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL Concluintes NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_qualifi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_qualifi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_qualifi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_qualifi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_qualifi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_qualifi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_qualifi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_qualifi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_qualifi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_qualifi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_qualifi_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_qualifi_presen_con_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_ng_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5024'].indicador")))
    qualifi_ng_con.click()

   
    qualifi_ng_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_presen_con_9 Pago por Pessoa Fisica ou Empresa"
    
    
    con_qualificacao_presencial_nao_gratuita = dados['qualificacao']['presencial']['concluintes'].get(chave_dado, 0)

    qualifi_ng_con.send_keys(str(con_qualificacao_presencial_nao_gratuita))
    qualifi_ng_con.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL Concluintes Regimental

nav.refresh()

meses = [
    ("jan", "jan_qualifi_presen_con_1 Gratuidade Regimental"),
    ("fev", "fev_qualifi_presen_con_1 Gratuidade Regimental"),
    ("mar", "mar_qualifi_presen_con_1 Gratuidade Regimental"),
    ("abr", "abr_qualifi_presen_con_1 Gratuidade Regimental"),
    ("mai", "mai_qualifi_presen_con_1 Gratuidade Regimental"),
    ("jun", "jun_qualifi_presen_con_1 Gratuidade Regimental"),
    ("jul", "jul_qualifi_presen_con_1 Gratuidade Regimental"),
    ("ago", "ago_qualifi_presen_con_1 Gratuidade Regimental"),
    ("set", "set_qualifi_presen_con_1 Gratuidade Regimental"),
    ("out", "out_qualifi_presen_con_1 Gratuidade Regimental"),
    ("nov", "nov_qualifi_presen_con_1 Gratuidade Regimental"),
    ("dez", "dez_qualifi_presen_con_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    quali_regime_con_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5025'].indicador")))
    quali_regime_con_con.click()

   
    quali_regime_con_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_presen_con_1 Gratuidade Regimental"
    
    
    con_qualificacao_presencial_regimental = dados['qualificacao']['presencial']['concluintes'].get(chave_dado, 0)

    quali_regime_con_con.send_keys(str(con_qualificacao_presencial_regimental))
    quali_regime_con_con.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020301 - APRENDIZAGEM INDUSTRIAL A DISTANCIA - REGIMENTAL

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/232?cd_centro_resp=30303020301&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APRENDIZAGEM%20INDUSTRIAL%20A%20DISTANCIA&id_grupo=2&ds_grupo=Aprendizagem%20Industrial&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_aprendi_distan_con_1 Gratuidade Regimental"),
    ("fev", "fev_aprendi_distan_con_1 Gratuidade Regimental"),
    ("mar", "mar_aprendi_distan_con_1 Gratuidade Regimental"),
    ("abr", "abr_aprendi_distan_con_1 Gratuidade Regimental"),
    ("mai", "mai_aprendi_distan_con_1 Gratuidade Regimental"),
    ("jun", "jun_aprendi_distan_con_1 Gratuidade Regimental"),
    ("jul", "jul_aprendi_distan_con_1 Gratuidade Regimental"),
    ("ago", "ago_aprendi_distan_con_1 Gratuidade Regimental"),
    ("set", "set_aprendi_distan_con_1 Gratuidade Regimental"),
    ("out", "out_aprendi_distan_con_1 Gratuidade Regimental"),
    ("nov", "nov_aprendi_distan_con_1 Gratuidade Regimental"),
    ("dez", "dez_aprendi_distan_con_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    apre_regime_semi_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5135'].indicador")))
    apre_regime_semi_con.click()

   
    apre_regime_semi_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aprendi_distan_con_1 Gratuidade Regimental"
    
    
    con_aprendizagem_distancia_regimental = dados['aprendizagem']['distancia']['concluintes'].get(chave_dado, 0)

    apre_regime_semi_con.send_keys(str(con_aprendizagem_distancia_regimental))
    apre_regime_semi_con.send_keys(Keys.ENTER)



# SENAI TAGUATINGA - 30303020401 - QUALIFICACAO PROFISSIONAL SEMIPRESENCIAL - BOLSA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/223?cd_centro_resp=30303020401&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=QUALIFICACAO%20PROFISSIONAL%20SEMIPRESENCIAL&id_grupo=3&ds_grupo=Qualifica%C3%A7%C3%A3o%20Industrial&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)

nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_qualifi_distan_con_2 Gratuidade Não Regimental"),
    ("fev", "fev_qualifi_distan_con_2 Gratuidade Não Regimental"),
    ("mar", "mar_qualifi_distan_con_2 Gratuidade Não Regimental"),
    ("abr", "abr_qualifi_distan_con_2 Gratuidade Não Regimental"),
    ("mai", "mai_qualifi_distan_con_2 Gratuidade Não Regimental"),
    ("jun", "jun_qualifi_distan_con_2 Gratuidade Não Regimental"),
    ("jul", "jul_qualifi_distan_con_2 Gratuidade Não Regimental"),
    ("ago", "ago_qualifi_distan_con_2 Gratuidade Não Regimental"),
    ("set", "set_qualifi_distan_con_2 Gratuidade Não Regimental"),
    ("out", "out_qualifi_distan_con_2 Gratuidade Não Regimental"),
    ("nov", "nov_qualifi_distan_con_2 Gratuidade Não Regimental"),
    ("dez", "dez_qualifi_distan_con_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_bolsa_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5047'].indicador")))
    qualifi_semi_bolsa_con.click()

   
    qualifi_semi_bolsa_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_distan_con_2 Gratuidade Não Regimental"
    
    
    con_qualifica_semi_bolsa = dados['qualificacao']['distancia']['concluintes'].get(chave_dado, 0)

    qualifi_semi_bolsa_con.send_keys(str(con_qualifica_semi_bolsa))
    qualifi_semi_bolsa_con.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020401 - QUALIFICACAO PROFISSIONAL SEMIPRESENCIAL - NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_qualifi_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_qualifi_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_qualifi_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_qualifi_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_qualifi_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_qualifi_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_qualifi_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_qualifi_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_qualifi_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_qualifi_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_qualifi_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_qualifi_distan_con_9 Pago por Pessoa Fisica ou Empresa")
]


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_ng_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5048'].indicador")))
    qualifi_semi_ng_con.click()

   
    qualifi_semi_ng_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_distan_con_9 Pago por Pessoa Fisica ou Empresa"
    
    
    con_qualifica_semi_ng = dados['qualificacao']['distancia']['concluintes'].get(chave_dado, 0)

    qualifi_semi_ng_con.send_keys(str(con_qualifica_semi_ng))
    qualifi_semi_ng_con.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020401 - QUALIFICACAO PROFISSIONAL SEMIPRESENCIAL - REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_qualifi_distan_con_1 Gratuidade Regimental"),
    ("fev", "fev_qualifi_distan_con_1 Gratuidade Regimental"),
    ("mar", "mar_qualifi_distan_con_1 Gratuidade Regimental"),
    ("abr", "abr_qualifi_distan_con_1 Gratuidade Regimental"),
    ("mai", "mai_qualifi_distan_con_1 Gratuidade Regimental"),
    ("jun", "jun_qualifi_distan_con_1 Gratuidade Regimental"),
    ("jul", "jul_qualifi_distan_con_1 Gratuidade Regimental"),
    ("ago", "ago_qualifi_distan_con_1 Gratuidade Regimental"),
    ("set", "set_qualifi_distan_con_1 Gratuidade Regimental"),
    ("out", "out_qualifi_distan_con_1 Gratuidade Regimental"),
    ("nov", "nov_qualifi_distan_con_1 Gratuidade Regimental"),
    ("dez", "dez_qualifi_distan_con_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_regimental_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5049'].indicador")))
    qualifi_semi_regimental_con.click()

   
    qualifi_semi_regimental_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_distan_con_1 Gratuidade Regimental"
    
    
    con_qualifica_semi_regimental = dados['qualificacao']['distancia']['concluintes'].get(chave_dado, 0)

    qualifi_semi_regimental_con.send_keys(str(con_qualifica_semi_regimental))
    qualifi_semi_regimental_con.send_keys(Keys.ENTER)
    
# SENAI TAGUATINGA - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - BOLSA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/227?cd_centro_resp=30303020501&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APERF%2FESPECIALIZ%20PROFISSIONAL%20PRESENCIAL&id_grupo=5&ds_grupo=Aperfei%C3%A7oamento%20Profissional&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_aperfei_presen_con_2 Gratuidade Não Regimental"),
    ("fev", "fev_aperfei_presen_con_2 Gratuidade Não Regimental"),
    ("mar", "mar_aperfei_presen_con_2 Gratuidade Não Regimental"),
    ("abr", "abr_aperfei_presen_con_2 Gratuidade Não Regimental"),
    ("mai", "mai_aperfei_presen_con_2 Gratuidade Não Regimental"),
    ("jun", "jun_aperfei_presen_con_2 Gratuidade Não Regimental"),
    ("jul", "jul_aperfei_presen_con_2 Gratuidade Não Regimental"),
    ("ago", "ago_aperfei_presen_con_2 Gratuidade Não Regimental"),
    ("set", "set_aperfei_presen_con_2 Gratuidade Não Regimental"),
    ("out", "out_aperfei_presen_con_2 Gratuidade Não Regimental"),
    ("nov", "nov_aperfei_presen_con_2 Gratuidade Não Regimental"),
    ("dez", "dez_aperfei_presen_con_2 Gratuidade Não Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_bolsa_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5083'].indicador")))
    aper_prese_bolsa_con.click()

   
    aper_prese_bolsa_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_con_2 Gratuidade Não Regimental"
    
    
    con_aper_prese_bolsa = dados['aperfeicoamento']['presencial']['concluintes'].get(chave_dado, 0)

    aper_prese_bolsa_con.send_keys(str(con_aper_prese_bolsa))
    aper_prese_bolsa_con.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_aperfei_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_aperfei_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_aperfei_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aperfei_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aperfei_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aperfei_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aperfei_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aperfei_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aperfei_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aperfei_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aperfei_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aperfei_presen_con_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_ng_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5084'].indicador")))
    aper_prese_ng_con.click()

   
    aper_prese_ng_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_con_9 Pago por Pessoa Fisica ou Empresa"
    
    
    con_aper_prese_ng = dados['aperfeicoamento']['presencial']['concluintes'].get(chave_dado, 0)

    aper_prese_ng_con.send_keys(str(con_aper_prese_ng))
    aper_prese_ng_con.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - REGIMENTAL


nav.refresh()

meses = [
    ("jan", "jan_aperfei_presen_con_1 Gratuidade Regimental"),
    ("fev", "fev_aperfei_presen_con_1 Gratuidade Regimental"),
    ("mar", "mar_aperfei_presen_con_1 Gratuidade Regimental"),
    ("abr", "abr_aperfei_presen_con_1 Gratuidade Regimental"),
    ("mai", "mai_aperfei_presen_con_1 Gratuidade Regimental"),
    ("jun", "jun_aperfei_presen_con_1 Gratuidade Regimental"),
    ("jul", "jul_aperfei_presen_con_1 Gratuidade Regimental"),
    ("ago", "ago_aperfei_presen_con_1 Gratuidade Regimental"),
    ("set", "set_aperfei_presen_con_1 Gratuidade Regimental"),
    ("out", "out_aperfei_presen_con_1 Gratuidade Regimental"),
    ("nov", "nov_aperfei_presen_con_1 Gratuidade Regimental"),
    ("dez", "dez_aperfei_presen_con_1 Gratuidade Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_regimental_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5085'].indicador")))
    aper_prese_regimental_con.click()

   
    aper_prese_regimental_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_con_1 Gratuidade Regimental"
    
    
    con_aper_prese_regimental = dados['aperfeicoamento']['presencial']['concluintes'].get(chave_dado, 0)

    aper_prese_regimental_con.send_keys(str(con_aper_prese_regimental))
    aper_prese_regimental_con.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - CONVENIO

nav.refresh()

meses = [
    ("jan", "jan_aperfei_presen_con_3 Convênio"),
    ("fev", "fev_aperfei_presen_con_3 Convênio"),
    ("mar", "mar_aperfei_presen_con_3 Convênio"),
    ("abr", "abr_aperfei_presen_con_3 Convênio"),
    ("mai", "mai_aperfei_presen_con_3 Convênio"),
    ("jun", "jun_aperfei_presen_con_3 Convênio"),
    ("jul", "jul_aperfei_presen_con_3 Convênio"),
    ("ago", "ago_aperfei_presen_con_3 Convênio"),
    ("set", "set_aperfei_presen_con_3 Convênio"),
    ("out", "out_aperfei_presen_con_3 Convênio"),
    ("nov", "nov_aperfei_presen_con_3 Convênio"),
    ("dez", "dez_aperfei_presen_con_3 Convênio")
]


for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_convenio_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5095'].indicador")))
    aper_prese_convenio_con.click()

   
    aper_prese_convenio_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_con_3 Convênio"
    
    
    con_aper_prese_convenio = dados['aperfeicoamento']['presencial']['concluintes'].get(chave_dado, 0)

    aper_prese_convenio_con.send_keys(str(con_aper_prese_convenio))
    aper_prese_convenio_con.send_keys(Keys.ENTER)
    
# SENAI TAGUATINGA - 30303020601 - APERF/ESPECIALI PROFISSIONAL A DISTANCIA BOLSA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/231?cd_centro_resp=30303020601&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APERF%2FESPECIALI%20PROFISSIONAL%20A%20DISTANCIA&id_grupo=5&ds_grupo=Aperfei%C3%A7oamento%20Profissional&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_aperfei_distan_con_2 Gratuidade Não Regimental"),
    ("fev", "fev_aperfei_distan_con_2 Gratuidade Não Regimental"),
    ("mar", "mar_aperfei_distan_con_2 Gratuidade Não Regimental"),
    ("abr", "abr_aperfei_distan_con_2 Gratuidade Não Regimental"),
    ("mai", "mai_aperfei_distan_con_2 Gratuidade Não Regimental"),
    ("jun", "jun_aperfei_distan_con_2 Gratuidade Não Regimental"),
    ("jul", "jul_aperfei_distan_con_2 Gratuidade Não Regimental"),
    ("ago", "ago_aperfei_distan_con_2 Gratuidade Não Regimental"),
    ("set", "set_aperfei_distan_con_2 Gratuidade Não Regimental"),
    ("out", "out_aperfei_distan_con_2 Gratuidade Não Regimental"),
    ("nov", "nov_aperfei_distan_con_2 Gratuidade Não Regimental"),
    ("dez", "dez_aperfei_distan_con_2 Gratuidade Não Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    aper_dista_bolsa_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5123'].indicador")))
    aper_dista_bolsa_con.click()

   
    aper_dista_bolsa_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_distan_con_2 Gratuidade Não Regimental"
    
    
    con_aper_distan_bolsa = dados['aperfeicoamento']['distancia']['concluintes'].get(chave_dado, 0)

    aper_dista_bolsa_con.send_keys(str(con_aper_distan_bolsa))
    aper_dista_bolsa_con.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020601 - APERF/ESPECIALI PROFISSIONAL A DISTANCIA NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "fev_aperfei_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_aperfei_distan_con_9 Pago por Pessoa Fisica ou Empresa"),  
    ("mar", "mar_aperfei_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aperfei_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aperfei_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aperfei_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aperfei_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aperfei_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aperfei_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aperfei_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aperfei_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aperfei_distan_con_9 Pago por Pessoa Fisica ou Empresa")
]


for i, (mes, campo_dado) in enumerate(meses):

    aper_dista_ng_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5124'].indicador")))
    aper_dista_ng_con.click()

   
    aper_dista_ng_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_distan_con_9 Pago por Pessoa Fisica ou Empresa"
    
    con_aper_distan_ng = dados['aperfeicoamento']['distancia']['concluintes'].get(chave_dado, 0)

    aper_dista_ng_con.send_keys(str(con_aper_distan_ng))
    aper_dista_ng_con.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020601 - APERF/ESPECIALI PROFISSIONAL A DISTANCIA REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_aperfei_distan_con_1 Gratuidade Regimental"),
    ("fev", "fev_aperfei_distan_con_1 Gratuidade Regimental"),
    ("mar", "mar_aperfei_distan_con_1 Gratuidade Regimental"),
    ("abr", "abr_aperfei_distan_con_1 Gratuidade Regimental"),
    ("mai", "mai_aperfei_distan_con_1 Gratuidade Regimental"),
    ("jun", "jun_aperfei_distan_con_1 Gratuidade Regimental"),
    ("jul", "jul_aperfei_distan_con_1 Gratuidade Regimental"),
    ("ago", "ago_aperfei_distan_con_1 Gratuidade Regimental"),
    ("set", "set_aperfei_distan_con_1 Gratuidade Regimental"),
    ("out", "out_aperfei_distan_con_1 Gratuidade Regimental"),
    ("nov", "nov_aperfei_distan_con_1 Gratuidade Regimental"),
    ("dez", "dez_aperfei_distan_con_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    aper_dista_regimental_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5125'].indicador")))
    aper_dista_regimental_con.click()

   
    aper_dista_regimental_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_distan_con_1 Gratuidade Regimental"
    
    con_aper_distan_regimental = dados['aperfeicoamento']['distancia']['concluintes'].get(chave_dado, 0)

    aper_dista_regimental_con.send_keys(str(con_aper_distan_regimental))
    aper_dista_regimental_con.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020901 - QUALIFIC PROF PRESENC - ITINER V ENS MED - BOLSA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/222?cd_centro_resp=30303020901&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=QUALIFIC%20PROF%20PRESENC%20-%20ITINER%20V%20ENS%20MED&id_grupo=3&ds_grupo=Qualifica%C3%A7%C3%A3o%20Industrial&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_qualifi_iti_presen_con_2 Gratuidade Não Regimental"),
    ("fev", "fev_qualifi_iti_presen_con_2 Gratuidade Não Regimental"),
    ("mar", "mar_qualifi_iti_presen_con_2 Gratuidade Não Regimental"),
    ("abr", "abr_qualifi_iti_presen_con_2 Gratuidade Não Regimental"),
    ("mai", "mai_qualifi_iti_presen_con_2 Gratuidade Não Regimental"),
    ("jun", "jun_qualifi_iti_presen_con_2 Gratuidade Não Regimental"),
    ("jul", "jul_qualifi_iti_presen_con_2 Gratuidade Não Regimental"),
    ("ago", "ago_qualifi_iti_presen_con_2 Gratuidade Não Regimental"),
    ("set", "set_qualifi_iti_presen_con_2 Gratuidade Não Regimental"),
    ("out", "out_qualifi_iti_presen_con_2 Gratuidade Não Regimental"),
    ("nov", "nov_qualifi_iti_presen_con_2 Gratuidade Não Regimental"),
    ("dez", "dez_qualifi_iti_presen_con_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_iti_presencial_bolsa_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5035'].indicador")))
    qualifi_iti_presencial_bolsa_con.click()

   
    qualifi_iti_presencial_bolsa_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_con_2 Gratuidade Não Regimental"
    
    con_quali_iti_presencial_bolsa = dados['qualificacao_iti']['presencial']['concluintes'].get(chave_dado, 0)

    qualifi_iti_presencial_bolsa_con.send_keys(str(con_quali_iti_presencial_bolsa))
    qualifi_iti_presencial_bolsa_con.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020901 - QUALIFIC PROF PRESENC - ITINER V ENS MED - NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_qualifi_iti_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_qualifi_iti_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_qualifi_iti_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_qualifi_iti_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_qualifi_iti_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_qualifi_iti_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_qualifi_iti_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_qualifi_iti_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_qualifi_iti_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_qualifi_iti_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_qualifi_iti_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_qualifi_iti_presen_con_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_iti_presencial_ng_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5036'].indicador")))
    qualifi_iti_presencial_ng_con.click()

   
    qualifi_iti_presencial_ng_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_con_9 Pago por Pessoa Fisica ou Empresa"
    
    con_quali_iti_presencial_ng = dados['qualificacao_iti']['presencial']['concluintes'].get(chave_dado, 0)

    qualifi_iti_presencial_ng_con.send_keys(str(con_quali_iti_presencial_ng))
    qualifi_iti_presencial_ng_con.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020901 - QUALIFIC PROF PRESENC - ITINER V ENS MED - REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_qualifi_iti_presen_con_1 Gratuidade Regimental"),
    ("fev", "fev_qualifi_iti_presen_con_1 Gratuidade Regimental"),
    ("mar", "mar_qualifi_iti_presen_con_1 Gratuidade Regimental"),
    ("abr", "abr_qualifi_iti_presen_con_1 Gratuidade Regimental"),
    ("mai", "mai_qualifi_iti_presen_con_1 Gratuidade Regimental"),
    ("jun", "jun_qualifi_iti_presen_con_1 Gratuidade Regimental"),
    ("jul", "jul_qualifi_iti_presen_con_1 Gratuidade Regimental"),
    ("ago", "ago_qualifi_iti_presen_con_1 Gratuidade Regimental"),
    ("set", "set_qualifi_iti_presen_con_1 Gratuidade Regimental"),
    ("out", "out_qualifi_iti_presen_con_1 Gratuidade Regimental"),
    ("nov", "nov_qualifi_iti_presen_con_1 Gratuidade Regimental"),
    ("dez", "dez_qualifi_iti_presen_con_1 Gratuidade Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_iti_presencial_regimental_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5037'].indicador")))
    qualifi_iti_presencial_regimental_con.click()

   
    qualifi_iti_presencial_regimental_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_con_1 Gratuidade Regimental"
    
    con_quali_iti_presencial_regimental = dados['qualificacao_iti']['presencial']['concluintes'].get(chave_dado, 0)

    qualifi_iti_presencial_regimental_con.send_keys(str(con_quali_iti_presencial_regimental))
    qualifi_iti_presencial_regimental_con.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303040101 - APREND. IND. TEC. NIVEL MEDIO PRESENCIAL - NAO GRATUITA


from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/226?cd_centro_resp=30303040101&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APREND.%20IND.%20TEC.%20NIVEL%20MEDIO%20PRESENCIAL&id_grupo=11&ds_grupo=Aprendizagem%20Industrial%20T%C3%A9cnico%20de%20N%C3%ADvel%20M%C3%A9dio&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_aprendi_tec_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_aprendi_tec_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_aprendi_tec_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aprendi_tec_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aprendi_tec_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aprendi_tec_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aprendi_tec_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aprendi_tec_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aprendi_tec_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aprendi_tec_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aprendi_tec_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aprendi_tec_presen_con_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    aprendi_tec_presencial_ng_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5075'].indicador")))
    aprendi_tec_presencial_ng_con.click()

   
    aprendi_tec_presencial_ng_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aprendi_tec_presen_con_9 Pago por Pessoa Fisica ou Empresa"
    
    con_aprendi_tec_presencial_ng = dados['aprendizagem_tec']['presencial']['concluintes'].get(chave_dado, 0)

    aprendi_tec_presencial_ng_con.send_keys(str(con_aprendi_tec_presencial_ng))
    aprendi_tec_presencial_ng_con.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303040101 - APREND. IND. TEC. NIVEL MEDIO PRESENCIAL - REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_aprendi_tec_presen_con_1 Gratuidade Regimental"),
    ("fev", "fev_aprendi_tec_presen_con_1 Gratuidade Regimental"),
    ("mar", "mar_aprendi_tec_presen_con_1 Gratuidade Regimental"),
    ("abr", "abr_aprendi_tec_presen_con_1 Gratuidade Regimental"),
    ("mai", "mai_aprendi_tec_presen_con_1 Gratuidade Regimental"),
    ("jun", "jun_aprendi_tec_presen_con_1 Gratuidade Regimental"),
    ("jul", "jul_aprendi_tec_presen_con_1 Gratuidade Regimental"),
    ("ago", "ago_aprendi_tec_presen_con_1 Gratuidade Regimental"),
    ("set", "set_aprendi_tec_presen_con_1 Gratuidade Regimental"),
    ("out", "out_aprendi_tec_presen_con_1 Gratuidade Regimental"),
    ("nov", "nov_aprendi_tec_presen_con_1 Gratuidade Regimental"),
    ("dez", "dez_aprendi_tec_presen_con_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    aprendi_tec_presencial_regimental_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5076'].indicador")))
    aprendi_tec_presencial_regimental_con.click()

   
    aprendi_tec_presencial_regimental_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aprendi_tec_presen_con_1 Gratuidade Regimental"
    
    con_aprendi_tec_presencial_regimental = dados['aprendizagem_tec']['presencial']['concluintes'].get(chave_dado, 0)

    aprendi_tec_presencial_regimental_con.send_keys(str(con_aprendi_tec_presencial_regimental))
    aprendi_tec_presencial_regimental_con.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303040201 - TECNICO DE NIVEL MEDIO PRESENCIAL - NAO GRATUITA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/233?cd_centro_resp=30303040201&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=TECNICO%20DE%20NIVEL%20MEDIO%20PRESENCIAL&id_grupo=4&ds_grupo=T%C3%A9cnico%20de%20N%C3%ADvel%20M%C3%A9dio&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_tecni_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_tecni_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_tecni_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_tecni_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_tecni_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_tecni_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_tecni_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_tecni_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_tecni_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_tecni_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_tecni_presen_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_tecni_presen_con_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_presencial_ng_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5139'].indicador")))
    tec_presencial_ng_con.click()

   
    tec_presencial_ng_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_presen_con_9 Pago por Pessoa Fisica ou Empresa"
    
    con_tec_presencial_ng = dados['tecnico_nm']['presencial']['concluintes'].get(chave_dado, 0)

    tec_presencial_ng_con.send_keys(str(con_tec_presencial_ng))
    tec_presencial_ng_con.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303040201 - TECNICO DE NIVEL MEDIO PRESENCIAL - REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_tecni_presen_con_1 Gratuidade Regimental"),
    ("fev", "fev_tecni_presen_con_1 Gratuidade Regimental"),
    ("mar", "mar_tecni_presen_con_1 Gratuidade Regimental"),
    ("abr", "abr_tecni_presen_con_1 Gratuidade Regimental"),
    ("mai", "mai_tecni_presen_con_1 Gratuidade Regimental"),
    ("jun", "jun_tecni_presen_con_1 Gratuidade Regimental"),
    ("jul", "jul_tecni_presen_con_1 Gratuidade Regimental"),
    ("ago", "ago_tecni_presen_con_1 Gratuidade Regimental"),
    ("set", "set_tecni_presen_con_1 Gratuidade Regimental"),
    ("out", "out_tecni_presen_con_1 Gratuidade Regimental"),
    ("nov", "nov_tecni_presen_con_1 Gratuidade Regimental"),
    ("dez", "dez_tecni_presen_con_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_presencial_regimental_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5140'].indicador")))
    tec_presencial_regimental_con.click()

   
    tec_presencial_regimental_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_presen_con_1 Gratuidade Regimental"
    
    con_tec_presencial_regimental = dados['tecnico_nm']['presencial']['concluintes'].get(chave_dado, 0)

    tec_presencial_regimental_con.send_keys(str(con_tec_presencial_regimental))
    tec_presencial_regimental_con.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303040201 - TECNICO DE NIVEL MEDIO PRESENCIAL - BOLSA   

nav.refresh()

meses = [
    ("jan", "jan_tecni_presen_con_2 Gratuidade Não Regimental"),
    ("fev", "fev_tecni_presen_con_2 Gratuidade Não Regimental"),
    ("mar", "mar_tecni_presen_con_2 Gratuidade Não Regimental"),
    ("abr", "abr_tecni_presen_con_2 Gratuidade Não Regimental"),
    ("mai", "mai_tecni_presen_con_2 Gratuidade Não Regimental"),
    ("jun", "jun_tecni_presen_con_2 Gratuidade Não Regimental"),
    ("jul", "jul_tecni_presen_con_2 Gratuidade Não Regimental"),
    ("ago", "ago_tecni_presen_con_2 Gratuidade Não Regimental"),
    ("set", "set_tecni_presen_con_2 Gratuidade Não Regimental"),
    ("out", "out_tecni_presen_con_2 Gratuidade Não Regimental"),
    ("nov", "nov_tecni_presen_con_2 Gratuidade Não Regimental"),
    ("dez", "dez_tecni_presen_con_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_presencial_bolsa_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5147'].indicador")))
    tec_presencial_bolsa_con.click()

   
    tec_presencial_bolsa_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_presen_con_2 Gratuidade Não Regimental"
    
    con_tec_presencial_bolsa = dados['tecnico_nm']['presencial']['concluintes'].get(chave_dado, 0)

    tec_presencial_bolsa_con.send_keys(str(con_tec_presencial_bolsa))
    tec_presencial_bolsa_con.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303040401 - TECNICO DE NIVEL MEDIO SEMIPRESENCIAL NAO GRATUITA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/224?cd_centro_resp=30303040401&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=TECNICO%20DE%20NIVEL%20MEDIO%20SEMIPRESENCIAL&id_grupo=4&ds_grupo=T%C3%A9cnico%20de%20N%C3%ADvel%20M%C3%A9dio&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_tecni_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_tecni_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_tecni_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_tecni_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_tecni_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_tecni_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_tecni_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_tecni_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_tecni_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_tecni_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_tecni_distan_con_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_tecni_distan_con_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_distancia_ng_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5059'].indicador")))
    tec_distancia_ng_con.click()

   
    tec_distancia_ng_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_distan_con_9 Pago por Pessoa Fisica ou Empresa"
    
    con_tec_distancia_ng = dados['tecnico_nm']['distancia']['concluintes'].get(chave_dado, 0)

    tec_distancia_ng_con.send_keys(str(con_tec_distancia_ng))
    tec_distancia_ng_con.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303040401 - TECNICO DE NIVEL MEDIO SEMIPRESENCIAL REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_tecni_distan_con_1 Gratuidade Regimental"),
    ("fev", "fev_tecni_distan_con_1 Gratuidade Regimental"),
    ("mar", "mar_tecni_distan_con_1 Gratuidade Regimental"),
    ("abr", "abr_tecni_distan_con_1 Gratuidade Regimental"),
    ("mai", "mai_tecni_distan_con_1 Gratuidade Regimental"),
    ("jun", "jun_tecni_distan_con_1 Gratuidade Regimental"),
    ("jul", "jul_tecni_distan_con_1 Gratuidade Regimental"),
    ("ago", "ago_tecni_distan_con_1 Gratuidade Regimental"),
    ("set", "set_tecni_distan_con_1 Gratuidade Regimental"),
    ("out", "out_tecni_distan_con_1 Gratuidade Regimental"),
    ("nov", "nov_tecni_distan_con_1 Gratuidade Regimental"),
    ("dez", "dez_tecni_distan_con_1 Gratuidade Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    tec_distancia_regimental_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5060'].indicador")))
    tec_distancia_regimental_con.click()

   
    tec_distancia_regimental_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_distan_con_1 Gratuidade Regimental"
    
    con_tec_distancia_regimental = dados['tecnico_nm']['distancia']['concluintes'].get(chave_dado, 0)

    tec_distancia_regimental_con.send_keys(str(con_tec_distancia_regimental))
    tec_distancia_regimental_con.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303040401 - TECNICO DE NIVEL MEDIO SEMIPRESENCIAL BOLSA

nav.refresh()

meses = [
    ("jan", "jan_tecni_distan_con_2 Gratuidade Não Regimental"),
    ("fev", "fev_tecni_distan_con_2 Gratuidade Não Regimental"),
    ("mar", "mar_tecni_distan_con_2 Gratuidade Não Regimental"),
    ("abr", "abr_tecni_distan_con_2 Gratuidade Não Regimental"),
    ("mai", "mai_tecni_distan_con_2 Gratuidade Não Regimental"),
    ("jun", "jun_tecni_distan_con_2 Gratuidade Não Regimental"),
    ("jul", "jul_tecni_distan_con_2 Gratuidade Não Regimental"),
    ("ago", "ago_tecni_distan_con_2 Gratuidade Não Regimental"),
    ("set", "set_tecni_distan_con_2 Gratuidade Não Regimental"),
    ("out", "out_tecni_distan_con_2 Gratuidade Não Regimental"),
    ("nov", "nov_tecni_distan_con_2 Gratuidade Não Regimental"),
    ("dez", "dez_tecni_distan_con_2 Gratuidade Não Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    tec_distancia_bolsa_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5473'].indicador")))
    tec_distancia_bolsa_con.click()

   
    tec_distancia_bolsa_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_distan_con_2 Gratuidade Não Regimental"
    
    con_tec_distancia_bolsa = dados['tecnico_nm']['distancia']['concluintes'].get(chave_dado, 0)

    tec_distancia_bolsa_con.send_keys(str(con_tec_distancia_bolsa))
    tec_distancia_bolsa_con.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303040501 - TECN DE NIV MED ITINERARIOS PRESENCIAL BOLSA

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/228?cd_centro_resp=30303040501&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=TECN%20DE%20NIV%20MED%20ITINERARIOS%20PRESENCIAL&id_grupo=4&ds_grupo=T%C3%A9cnico%20de%20N%C3%ADvel%20M%C3%A9dio&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_tecni_iti_presen_con_2 Gratuidade Não Regimental"),
    ("fev", "fev_tecni_iti_presen_con_2 Gratuidade Não Regimental"),
    ("mar", "mar_tecni_iti_presen_con_2 Gratuidade Não Regimental"),
    ("abr", "abr_tecni_iti_presen_con_2 Gratuidade Não Regimental"),
    ("mai", "mai_tecni_iti_presen_con_2 Gratuidade Não Regimental"),
    ("jun", "jun_tecni_iti_presen_con_2 Gratuidade Não Regimental"),
    ("jul", "jul_tecni_iti_presen_con_2 Gratuidade Não Regimental"),
    ("ago", "ago_tecni_iti_presen_con_2 Gratuidade Não Regimental"),
    ("set", "set_tecni_iti_presen_con_2 Gratuidade Não Regimental"),
    ("out", "out_tecni_iti_presen_con_2 Gratuidade Não Regimental"),
    ("nov", "nov_tecni_iti_presen_con_2 Gratuidade Não Regimental"),
    ("dez", "dez_tecni_iti_presen_con_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_iti_presencial_bolsa_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5099'].indicador")))
    tec_iti_presencial_bolsa_con.click()

   
    tec_iti_presencial_bolsa_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_iti_presen_con_2 Gratuidade Não Regimental"
    
    con_tec_iti_presencial_bolsa = dados['tecnico_nm_iti']['presencial']['concluintes'].get(chave_dado, 0)

    tec_iti_presencial_bolsa_con.send_keys(str(con_tec_iti_presencial_bolsa))
    tec_iti_presencial_bolsa_con.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303040501 - TECN DE NIV MED ITINERARIOS PRESENCIAL REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_tecni_iti_presen_con_1 Gratuidade Regimental"),
    ("fev", "fev_tecni_iti_presen_con_1 Gratuidade Regimental"),
    ("mar", "mar_tecni_iti_presen_con_1 Gratuidade Regimental"),
    ("abr", "abr_tecni_iti_presen_con_1 Gratuidade Regimental"),
    ("mai", "mai_tecni_iti_presen_con_1 Gratuidade Regimental"),
    ("jun", "jun_tecni_iti_presen_con_1 Gratuidade Regimental"),
    ("jul", "jul_tecni_iti_presen_con_1 Gratuidade Regimental"),
    ("ago", "ago_tecni_iti_presen_con_1 Gratuidade Regimental"),
    ("set", "set_tecni_iti_presen_con_1 Gratuidade Regimental"),
    ("out", "out_tecni_iti_presen_con_1 Gratuidade Regimental"),
    ("nov", "nov_tecni_iti_presen_con_1 Gratuidade Regimental"),
    ("dez", "dez_tecni_iti_presen_con_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_iti_presencial_regimental_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5103'].indicador")))
    tec_iti_presencial_regimental_con.click()

   
    tec_iti_presencial_regimental_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_iti_presen_con_1 Gratuidade Regimental"
    
    con_tec_iti_presencial_regimental = dados['tecnico_nm_iti']['presencial']['concluintes'].get(chave_dado, 0)

    tec_iti_presencial_regimental_con.send_keys(str(con_tec_iti_presencial_regimental))
    tec_iti_presencial_regimental_con.send_keys(Keys.ENTER)

