
# Importação dos pacotes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from obter_dados_tag_ha import obter_dados_por_tipo

arquivo = 'si_jan.xlsx'

dados = {
    'iniciacao': {
        'presencial': {
            'horas': obter_dados_por_tipo('iniciacao', 'presencial', arquivo)['horas'],
        },
        'distancia': {
            'horas': obter_dados_por_tipo('iniciacao', 'distancia', arquivo)['horas'],
        }
    },
    'aprendizagem': {
        'presencial': {
            'horas': obter_dados_por_tipo('aprendizagem', 'presencial', arquivo)['horas'],
        },
        'distancia': {
            'horas': obter_dados_por_tipo('aprendizagem', 'distancia', arquivo)['horas'],
        }
    },
    'qualificacao': {
        'presencial': {
            'horas': obter_dados_por_tipo('qualificacao', 'presencial', arquivo)['horas'],
        },
        'distancia': {
            'horas': obter_dados_por_tipo('qualificacao', 'distancia', arquivo)['horas'],
        }
    },
    'aperfeicoamento': {
        'presencial': {
            'horas': obter_dados_por_tipo('aperfeicoamento', 'presencial', arquivo)['horas'],
        },
        'distancia': {
            'horas': obter_dados_por_tipo('aperfeicoamento', 'distancia', arquivo)['horas'],
        }
    },
    'qualificacao_iti': {
        'presencial': {
            'horas': obter_dados_por_tipo('qualificacao_iti', 'presencial', arquivo)['horas'],
        }
    },
    'aprendizagem_tec': {
        'presencial': {
            'horas': obter_dados_por_tipo('aprendizagem_tec', 'presencial', arquivo)['horas'],
        }
    },
    'tecnico_nm': {
        'presencial': {
            'horas': obter_dados_por_tipo('tecnico_nm', 'presencial', arquivo)['horas'],
        },
        'distancia': {
            'horas': obter_dados_por_tipo('tecnico_nm', 'distancia', arquivo)['horas'],
        }
    },
    'tecnico_nm_iti': {
        'presencial': {
            'horas': obter_dados_por_tipo('tecnico_nm_iti', 'presencial', arquivo)['horas'],
        }
    }
}

# Navhagção para a pagina

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
senha = "Vitoria2625!"
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

################################################################   horas BOLSA ####################################################################################################

nav.refresh()

meses = [
    ("jan", "jan_inicia_presen_ha_2 Gratuidade Não Regimental"),
    ("fev", "fev_inicia_presen_ha_2 Gratuidade Não Regimental"),
    ("mar", "mar_inicia_presen_ha_2 Gratuidade Não Regimental"),
    ("abr", "abr_inicia_presen_ha_2 Gratuidade Não Regimental"),
    ("mai", "mai_inicia_presen_ha_2 Gratuidade Não Regimental"),
    ("jun", "jun_inicia_presen_ha_2 Gratuidade Não Regimental"),
    ("jul", "jul_inicia_presen_ha_2 Gratuidade Não Regimental"),
    ("ago", "ago_inicia_presen_ha_2 Gratuidade Não Regimental"),
    ("set", "set_inicia_presen_ha_2 Gratuidade Não Regimental"),
    ("out", "out_inicia_presen_ha_2 Gratuidade Não Regimental"),
    ("nov", "nov_inicia_presen_ha_2 Gratuidade Não Regimental"),
    ("dez", "dez_inicia_presen_ha_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):
   
    ha_bolsa_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5111'].indicador"))
    )
    ha_bolsa_mes.click()

    ha_bolsa_send = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_presen_ha_2 Gratuidade Não Regimental"
    
    ha_iniciacao_presencial_geral = dados['iniciacao']['presencial']['horas'].get(chave_dado, 0)

    ha_bolsa_send.send_keys(str(ha_iniciacao_presencial_geral))
    ha_bolsa_send.send_keys(Keys.ENTER)


############################################################   horas NAO GRATUITA ####################################################################################################

nav.refresh() 

meses = [
    ("jan", "jan_inicia_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_inicia_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_inicia_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_inicia_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_inicia_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_inicia_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_inicia_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_inicia_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_inicia_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_inicia_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_inicia_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_inicia_presen_ha_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):
    
    ha_ng_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5112'].indicador"))
    )
    ha_ng_mes.click()

    ha_ng_send = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_presen_ha_9 Pago por Pessoa Fisica ou Empresa"
    
    ha_iniciacao_presencial_ng = dados['iniciacao']['presencial']['horas'].get(chave_dado, 0)

    ha_ng_send.send_keys(str(ha_iniciacao_presencial_ng))
    ha_ng_send.send_keys(Keys.ENTER)


#########################################  INICIAÇÃO PROFISSIONAL A DISTANCIA  ##########################################################################################################


janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/225?cd_centro_resp=30303010201&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=INICIACAO%20PROFISSIONAL%20A%20DISTANCIA&id_grupo=1&ds_grupo=Inicia%C3%A7%C3%A3o%20Profissional&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA horas BOLSA ##################################################################################################

nav.refresh()

meses = [
    ("jan", "jan_inicia_distan_ha_2 Gratuidade Não Regimental"),
    ("fev", "fev_inicia_distan_ha_2 Gratuidade Não Regimental"),
    ("mar", "mar_inicia_distan_ha_2 Gratuidade Não Regimental"),
    ("abr", "abr_inicia_distan_ha_2 Gratuidade Não Regimental"),
    ("mai", "mai_inicia_distan_ha_2 Gratuidade Não Regimental"),
    ("jun", "jun_inicia_distan_ha_2 Gratuidade Não Regimental"),
    ("jul", "jul_inicia_distan_ha_2 Gratuidade Não Regimental"),
    ("ago", "ago_inicia_distan_ha_2 Gratuidade Não Regimental"),
    ("set", "set_inicia_distan_ha_2 Gratuidade Não Regimental"),
    ("out", "out_inicia_distan_ha_2 Gratuidade Não Regimental"),
    ("nov", "nov_inicia_distan_ha_2 Gratuidade Não Regimental"),
    ("dez", "dez_inicia_distan_ha_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    ha_ipd_bolsa_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5071'].indicador"))
    )
    ha_ipd_bolsa_mes.click()

    ha_ipd_bolsa_mes = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_distan_ha_2 Gratuidade Não Regimental"
    
    ha_iniciacao_distancia_bolsa = dados['iniciacao']['distancia']['horas'].get(chave_dado, 0)

    ha_ipd_bolsa_mes.send_keys(str(ha_iniciacao_distancia_bolsa))
    ha_ipd_bolsa_mes.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA horas NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_inicia_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_inicia_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_inicia_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_inicia_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_inicia_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_inicia_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_inicia_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_inicia_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_inicia_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_inicia_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_inicia_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_inicia_distan_ha_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    ha_ipd_ng_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5072'].indicador"))
    )
    ha_ipd_ng_mes.click()

    ha_ipd_ng_mes = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    chave_dado = f"{mes}_inicia_distan_ha_9 Pago por Pessoa Fisica ou Empresa"
    

    ha_iniciacao_distancia_ng = dados['iniciacao']['distancia']['horas'].get(chave_dado, 0)

    ha_ipd_ng_mes.send_keys(str(ha_iniciacao_distancia_ng))
    ha_ipd_ng_mes.send_keys(Keys.ENTER)


###################################################  Aprendizagem Industrial - Presencial #############################################################

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/230?cd_centro_resp=30303020101&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APRENDIZAGEM%20INDUSTRIAL%20PRESENCIAL&id_grupo=2&ds_grupo=Aprendizagem%20Industrial&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])


# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL horas NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_aprendi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_aprendi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_aprendi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aprendi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aprendi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aprendi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aprendi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aprendi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aprendi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aprendi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aprendi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aprendi_presen_ha_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    app_ng_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5119'].indicador")))
    app_ng_ha.click()


    app_ng_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    chave_dado = f"{mes}_aprendi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"
    
    ha_aprendizagem_presencial_ng = dados['aprendizagem']['presencial']['horas'].get(chave_dado, 0)

    app_ng_ha.send_keys(str(ha_aprendizagem_presencial_ng))
    app_ng_ha.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL horas REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_aprendi_presen_ha_1 Gratuidade Regimenta" ),
    ("fev", "fev_aprendi_presen_ha_1 Gratuidade Regimental"),
    ("mar", "mar_aprendi_presen_ha_1 Gratuidade Regimental"),
    ("abr", "abr_aprendi_presen_ha_1 Gratuidade Regimental"),
    ("mai", "mai_aprendi_presen_ha_1 Gratuidade Regimental"),
    ("jun", "jun_aprendi_presen_ha_1 Gratuidade Regimental"),
    ("jul", "jul_aprendi_presen_ha_1 Gratuidade Regimental"),
    ("ago", "ago_aprendi_presen_ha_1 Gratuidade Regimental"),
    ("set", "set_aprendi_presen_ha_1 Gratuidade Regimental"),
    ("out", "out_aprendi_presen_ha_1 Gratuidade Regimental"),
    ("nov", "nov_aprendi_presen_ha_1 Gratuidade Regimental"),
    ("dez", "dez_aprendi_presen_ha_1 Gratuidade Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    app_regimental_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5120'].indicador")))
    app_regimental_ha.click()

   
    app_regimental_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))


    chave_dado = f"{mes}_aprendi_presen_ha_1 Gratuidade Regimental"
    
   
    ha_aprendizagem_presencial_regimental = dados['aprendizagem']['presencial']['horas'].get(chave_dado, 0)

    app_regimental_ha.send_keys(str(ha_aprendizagem_presencial_regimental))
    app_regimental_ha.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL horas CONENIO

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/221?cd_centro_resp=30303020201&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=QUALIFICACAO%20PROFISSIONAL%20PRESENCIAL&id_grupo=3&ds_grupo=Qualifica%C3%A7%C3%A3o%20Industrial&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_qualifi_presen_ha_3 convênio"),
    ("fev", "fev_qualifi_presen_ha_3 convênio"),
    ("mar", "mar_qualifi_presen_ha_3 convênio"),
    ("abr", "abr_qualifi_presen_ha_3 convênio"),
    ("mai", "mai_qualifi_presen_ha_3 convênio"),
    ("jun", "jun_qualifi_presen_ha_3 convênio"),
    ("jul", "jul_qualifi_presen_ha_3 convênio"),
    ("ago", "ago_qualifi_presen_ha_3 convênio"),
    ("set", "set_qualifi_presen_ha_3 convênio"),
    ("out", "out_qualifi_presen_ha_3 convênio"),
    ("nov", "nov_qualifi_presen_ha_3 convênio"),
    ("dez", "dez_qualifi_presen_ha_3 convênio")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_convenio_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5021'].indicador")))
    qualifi_convenio_ha.click()

   
    qualifi_convenio_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

   
    chave_dado = f"{mes}_qualifi_presen_ha_3 convênio"
    
  
    ha_qualificacao_presencial_convenio = dados['qualificacao']['presencial']['horas'].get(chave_dado, 0)

    qualifi_convenio_ha.send_keys(str(ha_qualificacao_presencial_convenio))
    qualifi_convenio_ha.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL horas BOLSA

nav.refresh()

meses = [
    ("jan", "jan_qualifi_presen_ha_2 Gratuidade Não Regimental"),
    ("fev", "fev_qualifi_presen_ha_2 Gratuidade Não Regimental"),
    ("mar", "mar_qualifi_presen_ha_2 Gratuidade Não Regimental"),
    ("abr", "abr_qualifi_presen_ha_2 Gratuidade Não Regimental"),
    ("mai", "mai_qualifi_presen_ha_2 Gratuidade Não Regimental"),
    ("jun", "jun_qualifi_presen_ha_2 Gratuidade Não Regimental"),
    ("jul", "jul_qualifi_presen_ha_2 Gratuidade Não Regimental"),
    ("ago", "ago_qualifi_presen_ha_2 Gratuidade Não Regimental"),
    ("set", "set_qualifi_presen_ha_2 Gratuidade Não Regimental"),
    ("out", "out_qualifi_presen_ha_2 Gratuidade Não Regimental"),
    ("nov", "nov_qualifi_presen_ha_2 Gratuidade Não Regimental"),
    ("dez", "dez_qualifi_presen_ha_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_bolsa_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5029'].indicador")))
    qualifi_bolsa_ha.click()

   
    qualifi_bolsa_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    chave_dado = f"{mes}_qualifi_presen_ha_2 Gratuidade Não Regimental"
    
   
    ha_qualificacao_presencial_bolsa = dados['qualificacao']['presencial']['horas'].get(chave_dado, 0)

    qualifi_bolsa_ha.send_keys(str(ha_qualificacao_presencial_bolsa))
    qualifi_bolsa_ha.send_keys(Keys.ENTER)


    # SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL horas NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_qualifi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_qualifi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_qualifi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_qualifi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_qualifi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_qualifi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_qualifi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_qualifi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_qualifi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_qualifi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_qualifi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_qualifi_presen_ha_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_ng_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5030'].indicador")))
    qualifi_ng_ha.click()

   
    qualifi_ng_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_presen_ha_9 Pago por Pessoa Fisica ou Empresa"
    
    
    ha_qualificacao_presencial_nao_gratuita = dados['qualificacao']['presencial']['horas'].get(chave_dado, 0)

    qualifi_ng_ha.send_keys(str(ha_qualificacao_presencial_nao_gratuita))
    qualifi_ng_ha.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL horas Regimental

nav.refresh()

meses = [
    ("jan", "jan_qualifi_presen_ha_1 Gratuidade Regimental"),
    ("fev", "fev_qualifi_presen_ha_1 Gratuidade Regimental"),
    ("mar", "mar_qualifi_presen_ha_1 Gratuidade Regimental"),
    ("abr", "abr_qualifi_presen_ha_1 Gratuidade Regimental"),
    ("mai", "mai_qualifi_presen_ha_1 Gratuidade Regimental"),
    ("jun", "jun_qualifi_presen_ha_1 Gratuidade Regimental"),
    ("jul", "jul_qualifi_presen_ha_1 Gratuidade Regimental"),
    ("ago", "ago_qualifi_presen_ha_1 Gratuidade Regimental"),
    ("set", "set_qualifi_presen_ha_1 Gratuidade Regimental"),
    ("out", "out_qualifi_presen_ha_1 Gratuidade Regimental"),
    ("nov", "nov_qualifi_presen_ha_1 Gratuidade Regimental"),
    ("dez", "dez_qualifi_presen_ha_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    quali_regime_ha_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5031'].indicador")))
    quali_regime_ha_ha.click()

   
    quali_regime_ha_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_presen_ha_1 Gratuidade Regimental"
    
    
    ha_qualificacao_presencial_regimental = dados['qualificacao']['presencial']['horas'].get(chave_dado, 0)

    quali_regime_ha_ha.send_keys(str(ha_qualificacao_presencial_regimental))
    quali_regime_ha_ha.send_keys(Keys.ENTER)


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
    ("jan", "jan_aprendi_distan_ha_1 Gratuidade Regimental"),
    ("fev", "fev_aprendi_distan_ha_1 Gratuidade Regimental"),
    ("mar", "mar_aprendi_distan_ha_1 Gratuidade Regimental"),
    ("abr", "abr_aprendi_distan_ha_1 Gratuidade Regimental"),
    ("mai", "mai_aprendi_distan_ha_1 Gratuidade Regimental"),
    ("jun", "jun_aprendi_distan_ha_1 Gratuidade Regimental"),
    ("jul", "jul_aprendi_distan_ha_1 Gratuidade Regimental"),
    ("ago", "ago_aprendi_distan_ha_1 Gratuidade Regimental"),
    ("set", "set_aprendi_distan_ha_1 Gratuidade Regimental"),
    ("out", "out_aprendi_distan_ha_1 Gratuidade Regimental"),
    ("nov", "nov_aprendi_distan_ha_1 Gratuidade Regimental"),
    ("dez", "dez_aprendi_distan_ha_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    apre_regime_semi_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5137'].indicador")))
    apre_regime_semi_ha.click()

   
    apre_regime_semi_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aprendi_distan_ha_1 Gratuidade Regimental"
    
    
    ha_aprendizagem_distancia_regimental = dados['aprendizagem']['distancia']['horas'].get(chave_dado, 0)

    apre_regime_semi_ha.send_keys(str(ha_aprendizagem_distancia_regimental))
    apre_regime_semi_ha.send_keys(Keys.ENTER)



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
    ("jan", "jan_qualifi_distan_ha_2 Gratuidade Não Regimental"),
    ("fev", "fev_qualifi_distan_ha_2 Gratuidade Não Regimental"),
    ("mar", "mar_qualifi_distan_ha_2 Gratuidade Não Regimental"),
    ("abr", "abr_qualifi_distan_ha_2 Gratuidade Não Regimental"),
    ("mai", "mai_qualifi_distan_ha_2 Gratuidade Não Regimental"),
    ("jun", "jun_qualifi_distan_ha_2 Gratuidade Não Regimental"),
    ("jul", "jul_qualifi_distan_ha_2 Gratuidade Não Regimental"),
    ("ago", "ago_qualifi_distan_ha_2 Gratuidade Não Regimental"),
    ("set", "set_qualifi_distan_ha_2 Gratuidade Não Regimental"),
    ("out", "out_qualifi_distan_ha_2 Gratuidade Não Regimental"),
    ("nov", "nov_qualifi_distan_ha_2 Gratuidade Não Regimental"),
    ("dez", "dez_qualifi_distan_ha_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_bolsa_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5053'].indicador")))
    qualifi_semi_bolsa_ha.click()

   
    qualifi_semi_bolsa_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_distan_ha_2 Gratuidade Não Regimental"
    
    
    ha_qualifica_semi_bolsa = dados['qualificacao']['distancia']['horas'].get(chave_dado, 0)

    qualifi_semi_bolsa_ha.send_keys(str(ha_qualifica_semi_bolsa))
    qualifi_semi_bolsa_ha.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020401 - QUALIFICACAO PROFISSIONAL SEMIPRESENCIAL - NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_qualifi_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_qualifi_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_qualifi_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_qualifi_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_qualifi_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_qualifi_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_qualifi_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_qualifi_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_qualifi_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_qualifi_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_qualifi_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_qualifi_distan_ha_9 Pago por Pessoa Fisica ou Empresa")
]


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_ng_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5054'].indicador")))
    qualifi_semi_ng_ha.click()

   
    qualifi_semi_ng_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_distan_ha_9 Pago por Pessoa Fisica ou Empresa"
    
    
    ha_qualifica_semi_ng = dados['qualificacao']['distancia']['horas'].get(chave_dado, 0)

    qualifi_semi_ng_ha.send_keys(str(ha_qualifica_semi_ng))
    qualifi_semi_ng_ha.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020401 - QUALIFICACAO PROFISSIONAL SEMIPRESENCIAL - REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_qualifi_distan_ha_1 Gratuidade Regimental"),
    ("fev", "fev_qualifi_distan_ha_1 Gratuidade Regimental"),
    ("mar", "mar_qualifi_distan_ha_1 Gratuidade Regimental"),
    ("abr", "abr_qualifi_distan_ha_1 Gratuidade Regimental"),
    ("mai", "mai_qualifi_distan_ha_1 Gratuidade Regimental"),
    ("jun", "jun_qualifi_distan_ha_1 Gratuidade Regimental"),
    ("jul", "jul_qualifi_distan_ha_1 Gratuidade Regimental"),
    ("ago", "ago_qualifi_distan_ha_1 Gratuidade Regimental"),
    ("set", "set_qualifi_distan_ha_1 Gratuidade Regimental"),
    ("out", "out_qualifi_distan_ha_1 Gratuidade Regimental"),
    ("nov", "nov_qualifi_distan_ha_1 Gratuidade Regimental"),
    ("dez", "dez_qualifi_distan_ha_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_regimental_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5055'].indicador")))
    qualifi_semi_regimental_ha.click()

   
    qualifi_semi_regimental_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_distan_ha_1 Gratuidade Regimental"
    
    
    ha_qualifica_semi_regimental = dados['qualificacao']['distancia']['horas'].get(chave_dado, 0)

    qualifi_semi_regimental_ha.send_keys(str(ha_qualifica_semi_regimental))
    qualifi_semi_regimental_ha.send_keys(Keys.ENTER)
    
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
    ("jan", "jan_aperfei_presen_ha_2 Gratuidade Não Regimental"),
    ("fev", "fev_aperfei_presen_ha_2 Gratuidade Não Regimental"),
    ("mar", "mar_aperfei_presen_ha_2 Gratuidade Não Regimental"),
    ("abr", "abr_aperfei_presen_ha_2 Gratuidade Não Regimental"),
    ("mai", "mai_aperfei_presen_ha_2 Gratuidade Não Regimental"),
    ("jun", "jun_aperfei_presen_ha_2 Gratuidade Não Regimental"),
    ("jul", "jul_aperfei_presen_ha_2 Gratuidade Não Regimental"),
    ("ago", "ago_aperfei_presen_ha_2 Gratuidade Não Regimental"),
    ("set", "set_aperfei_presen_ha_2 Gratuidade Não Regimental"),
    ("out", "out_aperfei_presen_ha_2 Gratuidade Não Regimental"),
    ("nov", "nov_aperfei_presen_ha_2 Gratuidade Não Regimental"),
    ("dez", "dez_aperfei_presen_ha_2 Gratuidade Não Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_bolsa_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5089'].indicador")))
    aper_prese_bolsa_ha.click()

   
    aper_prese_bolsa_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_ha_2 Gratuidade Não Regimental"
    
    
    ha_aper_prese_bolsa = dados['aperfeicoamento']['presencial']['horas'].get(chave_dado, 0)

    aper_prese_bolsa_ha.send_keys(str(ha_aper_prese_bolsa))
    aper_prese_bolsa_ha.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_aperfei_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_aperfei_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_aperfei_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aperfei_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aperfei_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aperfei_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aperfei_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aperfei_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aperfei_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aperfei_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aperfei_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aperfei_presen_ha_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_ng_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5090'].indicador")))
    aper_prese_ng_ha.click()

   
    aper_prese_ng_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_ha_9 Pago por Pessoa Fisica ou Empresa"
    
    
    ha_aper_prese_ng = dados['aperfeicoamento']['presencial']['horas'].get(chave_dado, 0)

    aper_prese_ng_ha.send_keys(str(ha_aper_prese_ng))
    aper_prese_ng_ha.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - REGIMENTAL


nav.refresh()

meses = [
    ("jan", "jan_aperfei_presen_ha_1 Gratuidade Regimental"),
    ("fev", "fev_aperfei_presen_ha_1 Gratuidade Regimental"),
    ("mar", "mar_aperfei_presen_ha_1 Gratuidade Regimental"),
    ("abr", "abr_aperfei_presen_ha_1 Gratuidade Regimental"),
    ("mai", "mai_aperfei_presen_ha_1 Gratuidade Regimental"),
    ("jun", "jun_aperfei_presen_ha_1 Gratuidade Regimental"),
    ("jul", "jul_aperfei_presen_ha_1 Gratuidade Regimental"),
    ("ago", "ago_aperfei_presen_ha_1 Gratuidade Regimental"),
    ("set", "set_aperfei_presen_ha_1 Gratuidade Regimental"),
    ("out", "out_aperfei_presen_ha_1 Gratuidade Regimental"),
    ("nov", "nov_aperfei_presen_ha_1 Gratuidade Regimental"),
    ("dez", "dez_aperfei_presen_ha_1 Gratuidade Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_regimental_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5091'].indicador")))
    aper_prese_regimental_ha.click()

   
    aper_prese_regimental_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_ha_1 Gratuidade Regimental"
    
    
    ha_aper_prese_regimental = dados['aperfeicoamento']['presencial']['horas'].get(chave_dado, 0)

    aper_prese_regimental_ha.send_keys(str(ha_aper_prese_regimental))
    aper_prese_regimental_ha.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - haVENIO

nav.refresh()

meses = [
    ("jan", "jan_aperfei_presen_ha_3 Convênio"),
    ("fev", "fev_aperfei_presen_ha_3 Convênio"),
    ("mar", "mar_aperfei_presen_ha_3 Convênio"),
    ("abr", "abr_aperfei_presen_ha_3 Convênio"),
    ("mai", "mai_aperfei_presen_ha_3 Convênio"),
    ("jun", "jun_aperfei_presen_ha_3 Convênio"),
    ("jul", "jul_aperfei_presen_ha_3 Convênio"),
    ("ago", "ago_aperfei_presen_ha_3 Convênio"),
    ("set", "set_aperfei_presen_ha_3 Convênio"),
    ("out", "out_aperfei_presen_ha_3 Convênio"),
    ("nov", "nov_aperfei_presen_ha_3 Convênio"),
    ("dez", "dez_aperfei_presen_ha_3 Convênio")
]


for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_convenio_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5097'].indicador")))
    aper_prese_convenio_ha.click()

   
    aper_prese_convenio_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_presen_ha_3 Convênio"
    
    
    ha_aper_prese_convenio = dados['aperfeicoamento']['presencial']['horas'].get(chave_dado, 0)

    aper_prese_convenio_ha.send_keys(str(ha_aper_prese_convenio))
    aper_prese_convenio_ha.send_keys(Keys.ENTER)
    
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
    ("jan", "jan_aperfei_distan_ha_2 Gratuidade Não Regimental"),
    ("fev", "fev_aperfei_distan_ha_2 Gratuidade Não Regimental"),
    ("mar", "mar_aperfei_distan_ha_2 Gratuidade Não Regimental"),
    ("abr", "abr_aperfei_distan_ha_2 Gratuidade Não Regimental"),
    ("mai", "mai_aperfei_distan_ha_2 Gratuidade Não Regimental"),
    ("jun", "jun_aperfei_distan_ha_2 Gratuidade Não Regimental"),
    ("jul", "jul_aperfei_distan_ha_2 Gratuidade Não Regimental"),
    ("ago", "ago_aperfei_distan_ha_2 Gratuidade Não Regimental"),
    ("set", "set_aperfei_distan_ha_2 Gratuidade Não Regimental"),
    ("out", "out_aperfei_distan_ha_2 Gratuidade Não Regimental"),
    ("nov", "nov_aperfei_distan_ha_2 Gratuidade Não Regimental"),
    ("dez", "dez_aperfei_distan_ha_2 Gratuidade Não Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    aper_dista_bolsa_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5129'].indicador")))
    aper_dista_bolsa_ha.click()

   
    aper_dista_bolsa_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_distan_ha_2 Gratuidade Não Regimental"
    
    
    ha_aper_distan_bolsa = dados['aperfeicoamento']['distancia']['horas'].get(chave_dado, 0)

    aper_dista_bolsa_ha.send_keys(str(ha_aper_distan_bolsa))
    aper_dista_bolsa_ha.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020601 - APERF/ESPECIALI PROFISSIONAL A DISTANCIA NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "fev_aperfei_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_aperfei_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),  
    ("mar", "mar_aperfei_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aperfei_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aperfei_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aperfei_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aperfei_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aperfei_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aperfei_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aperfei_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aperfei_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aperfei_distan_ha_9 Pago por Pessoa Fisica ou Empresa")
]


for i, (mes, campo_dado) in enumerate(meses):

    aper_dista_ng_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5130'].indicador")))
    aper_dista_ng_ha.click()

   
    aper_dista_ng_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_distan_ha_9 Pago por Pessoa Fisica ou Empresa"
    
    ha_aper_distan_ng = dados['aperfeicoamento']['distancia']['horas'].get(chave_dado, 0)

    aper_dista_ng_ha.send_keys(str(ha_aper_distan_ng))
    aper_dista_ng_ha.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020601 - APERF/ESPECIALI PROFISSIONAL A DISTANCIA REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_aperfei_distan_ha_1 Gratuidade Regimental"),
    ("fev", "fev_aperfei_distan_ha_1 Gratuidade Regimental"),
    ("mar", "mar_aperfei_distan_ha_1 Gratuidade Regimental"),
    ("abr", "abr_aperfei_distan_ha_1 Gratuidade Regimental"),
    ("mai", "mai_aperfei_distan_ha_1 Gratuidade Regimental"),
    ("jun", "jun_aperfei_distan_ha_1 Gratuidade Regimental"),
    ("jul", "jul_aperfei_distan_ha_1 Gratuidade Regimental"),
    ("ago", "ago_aperfei_distan_ha_1 Gratuidade Regimental"),
    ("set", "set_aperfei_distan_ha_1 Gratuidade Regimental"),
    ("out", "out_aperfei_distan_ha_1 Gratuidade Regimental"),
    ("nov", "nov_aperfei_distan_ha_1 Gratuidade Regimental"),
    ("dez", "dez_aperfei_distan_ha_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    aper_dista_regimental_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5131'].indicador")))
    aper_dista_regimental_ha.click()

   
    aper_dista_regimental_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aperfei_distan_ha_1 Gratuidade Regimental"
    
    ha_aper_distan_regimental = dados['aperfeicoamento']['distancia']['horas'].get(chave_dado, 0)

    aper_dista_regimental_ha.send_keys(str(ha_aper_distan_regimental))
    aper_dista_regimental_ha.send_keys(Keys.ENTER)

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
    ("jan", "jan_qualifi_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("fev", "fev_qualifi_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("mar", "mar_qualifi_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("abr", "abr_qualifi_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("mai", "mai_qualifi_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("jun", "jun_qualifi_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("jul", "jul_qualifi_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("ago", "ago_qualifi_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("set", "set_qualifi_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("out", "out_qualifi_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("nov", "nov_qualifi_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("dez", "dez_qualifi_iti_presen_ha_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_iti_presencial_bolsa_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5041'].indicador")))
    qualifi_iti_presencial_bolsa_ha.click()

   
    qualifi_iti_presencial_bolsa_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_ha_2 Gratuidade Não Regimental"
    
    ha_quali_iti_presencial_bolsa = dados['qualificacao_iti']['presencial']['horas'].get(chave_dado, 0)

    qualifi_iti_presencial_bolsa_ha.send_keys(str(ha_quali_iti_presencial_bolsa))
    qualifi_iti_presencial_bolsa_ha.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020901 - QUALIFIC PROF PRESENC - ITINER V ENS MED - NAO GRATUITA

nav.refresh()

meses = [
    ("jan", "jan_qualifi_iti_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_qualifi_iti_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_qualifi_iti_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_qualifi_iti_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_qualifi_iti_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_qualifi_iti_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_qualifi_iti_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_qualifi_iti_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_qualifi_iti_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_qualifi_iti_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_qualifi_iti_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_qualifi_iti_presen_ha_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_iti_presencial_ng_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5042'].indicador")))
    qualifi_iti_presencial_ng_ha.click()

   
    qualifi_iti_presencial_ng_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_ha_9 Pago por Pessoa Fisica ou Empresa"
    
    ha_quali_iti_presencial_ng = dados['qualificacao_iti']['presencial']['horas'].get(chave_dado, 0)

    qualifi_iti_presencial_ng_ha.send_keys(str(ha_quali_iti_presencial_ng))
    qualifi_iti_presencial_ng_ha.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020901 - QUALIFIC PROF PRESENC - ITINER V ENS MED - REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_qualifi_iti_presen_ha_1 Gratuidade Regimental"),
    ("fev", "fev_qualifi_iti_presen_ha_1 Gratuidade Regimental"),
    ("mar", "mar_qualifi_iti_presen_ha_1 Gratuidade Regimental"),
    ("abr", "abr_qualifi_iti_presen_ha_1 Gratuidade Regimental"),
    ("mai", "mai_qualifi_iti_presen_ha_1 Gratuidade Regimental"),
    ("jun", "jun_qualifi_iti_presen_ha_1 Gratuidade Regimental"),
    ("jul", "jul_qualifi_iti_presen_ha_1 Gratuidade Regimental"),
    ("ago", "ago_qualifi_iti_presen_ha_1 Gratuidade Regimental"),
    ("set", "set_qualifi_iti_presen_ha_1 Gratuidade Regimental"),
    ("out", "out_qualifi_iti_presen_ha_1 Gratuidade Regimental"),
    ("nov", "nov_qualifi_iti_presen_ha_1 Gratuidade Regimental"),
    ("dez", "dez_qualifi_iti_presen_ha_1 Gratuidade Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    qualifi_iti_presencial_regimental_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5043'].indicador")))
    qualifi_iti_presencial_regimental_ha.click()

   
    qualifi_iti_presencial_regimental_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_qualifi_iti_presen_ha_1 Gratuidade Regimental"
    
    ha_quali_iti_presencial_regimental = dados['qualificacao_iti']['presencial']['horas'].get(chave_dado, 0)

    qualifi_iti_presencial_regimental_ha.send_keys(str(ha_quali_iti_presencial_regimental))
    qualifi_iti_presencial_regimental_ha.send_keys(Keys.ENTER)


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
    ("jan", "jan_aprendi_tec_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_aprendi_tec_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_aprendi_tec_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_aprendi_tec_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_aprendi_tec_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_aprendi_tec_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_aprendi_tec_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_aprendi_tec_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_aprendi_tec_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_aprendi_tec_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_aprendi_tec_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_aprendi_tec_presen_ha_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    aprendi_tec_presencial_ng_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5079'].indicador")))
    aprendi_tec_presencial_ng_ha.click()

   
    aprendi_tec_presencial_ng_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aprendi_tec_presen_ha_9 Pago por Pessoa Fisica ou Empresa"
    
    ha_aprendi_tec_presencial_ng = dados['aprendizagem_tec']['presencial']['horas'].get(chave_dado, 0)

    aprendi_tec_presencial_ng_ha.send_keys(str(ha_aprendi_tec_presencial_ng))
    aprendi_tec_presencial_ng_ha.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303040101 - APREND. IND. TEC. NIVEL MEDIO PRESENCIAL - REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_aprendi_tec_presen_ha_1 Gratuidade Regimental"),
    ("fev", "fev_aprendi_tec_presen_ha_1 Gratuidade Regimental"),
    ("mar", "mar_aprendi_tec_presen_ha_1 Gratuidade Regimental"),
    ("abr", "abr_aprendi_tec_presen_ha_1 Gratuidade Regimental"),
    ("mai", "mai_aprendi_tec_presen_ha_1 Gratuidade Regimental"),
    ("jun", "jun_aprendi_tec_presen_ha_1 Gratuidade Regimental"),
    ("jul", "jul_aprendi_tec_presen_ha_1 Gratuidade Regimental"),
    ("ago", "ago_aprendi_tec_presen_ha_1 Gratuidade Regimental"),
    ("set", "set_aprendi_tec_presen_ha_1 Gratuidade Regimental"),
    ("out", "out_aprendi_tec_presen_ha_1 Gratuidade Regimental"),
    ("nov", "nov_aprendi_tec_presen_ha_1 Gratuidade Regimental"),
    ("dez", "dez_aprendi_tec_presen_ha_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    aprendi_tec_presencial_regimental_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5080'].indicador")))
    aprendi_tec_presencial_regimental_ha.click()

   
    aprendi_tec_presencial_regimental_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_aprendi_tec_presen_ha_1 Gratuidade Regimental"
    
    ha_aprendi_tec_presencial_regimental = dados['aprendizagem_tec']['presencial']['horas'].get(chave_dado, 0)

    aprendi_tec_presencial_regimental_ha.send_keys(str(ha_aprendi_tec_presencial_regimental))
    aprendi_tec_presencial_regimental_ha.send_keys(Keys.ENTER)

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
    ("jan", "jan_tecni_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_tecni_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_tecni_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_tecni_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_tecni_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_tecni_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_tecni_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_tecni_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_tecni_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_tecni_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_tecni_presen_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_tecni_presen_ha_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_presencial_ng_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5143'].indicador")))
    tec_presencial_ng_ha.click()

   
    tec_presencial_ng_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_presen_ha_9 Pago por Pessoa Fisica ou Empresa"
    
    ha_tec_presencial_ng = dados['tecnico_nm']['presencial']['horas'].get(chave_dado, 0)

    tec_presencial_ng_ha.send_keys(str(ha_tec_presencial_ng))
    tec_presencial_ng_ha.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303040201 - TECNICO DE NIVEL MEDIO PRESENCIAL - REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_tecni_presen_ha_1 Gratuidade Regimental"),
    ("fev", "fev_tecni_presen_ha_1 Gratuidade Regimental"),
    ("mar", "mar_tecni_presen_ha_1 Gratuidade Regimental"),
    ("abr", "abr_tecni_presen_ha_1 Gratuidade Regimental"),
    ("mai", "mai_tecni_presen_ha_1 Gratuidade Regimental"),
    ("jun", "jun_tecni_presen_ha_1 Gratuidade Regimental"),
    ("jul", "jul_tecni_presen_ha_1 Gratuidade Regimental"),
    ("ago", "ago_tecni_presen_ha_1 Gratuidade Regimental"),
    ("set", "set_tecni_presen_ha_1 Gratuidade Regimental"),
    ("out", "out_tecni_presen_ha_1 Gratuidade Regimental"),
    ("nov", "nov_tecni_presen_ha_1 Gratuidade Regimental"),
    ("dez", "dez_tecni_presen_ha_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_presencial_regimental_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5144'].indicador")))
    tec_presencial_regimental_ha.click()

   
    tec_presencial_regimental_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_presen_ha_1 Gratuidade Regimental"
    
    ha_tec_presencial_regimental = dados['tecnico_nm']['presencial']['horas'].get(chave_dado, 0)

    tec_presencial_regimental_ha.send_keys(str(ha_tec_presencial_regimental))
    tec_presencial_regimental_ha.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303040201 - TECNICO DE NIVEL MEDIO PRESENCIAL - BOLSA   

nav.refresh()

meses = [
    ("jan", "jan_tecni_presen_ha_2 Gratuidade Não Regimental"),
    ("fev", "fev_tecni_presen_ha_2 Gratuidade Não Regimental"),
    ("mar", "mar_tecni_presen_ha_2 Gratuidade Não Regimental"),
    ("abr", "abr_tecni_presen_ha_2 Gratuidade Não Regimental"),
    ("mai", "mai_tecni_presen_ha_2 Gratuidade Não Regimental"),
    ("jun", "jun_tecni_presen_ha_2 Gratuidade Não Regimental"),
    ("jul", "jul_tecni_presen_ha_2 Gratuidade Não Regimental"),
    ("ago", "ago_tecni_presen_ha_2 Gratuidade Não Regimental"),
    ("set", "set_tecni_presen_ha_2 Gratuidade Não Regimental"),
    ("out", "out_tecni_presen_ha_2 Gratuidade Não Regimental"),
    ("nov", "nov_tecni_presen_ha_2 Gratuidade Não Regimental"),
    ("dez", "dez_tecni_presen_ha_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_presencial_bolsa_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5149'].indicador")))
    tec_presencial_bolsa_ha.click()

   
    tec_presencial_bolsa_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_presen_ha_2 Gratuidade Não Regimental"
    
    ha_tec_presencial_bolsa = dados['tecnico_nm']['presencial']['horas'].get(chave_dado, 0)

    tec_presencial_bolsa_ha.send_keys(str(ha_tec_presencial_bolsa))
    tec_presencial_bolsa_ha.send_keys(Keys.ENTER)


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
    ("jan", "jan_tecni_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_tecni_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_tecni_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_tecni_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_tecni_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_tecni_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_tecni_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_tecni_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_tecni_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_tecni_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_tecni_distan_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_tecni_distan_ha_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_distancia_ng_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5063'].indicador")))
    tec_distancia_ng_ha.click()

   
    tec_distancia_ng_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_distan_ha_9 Pago por Pessoa Fisica ou Empresa"
    
    ha_tec_distancia_ng = dados['tecnico_nm']['distancia']['horas'].get(chave_dado, 0)

    tec_distancia_ng_ha.send_keys(str(ha_tec_distancia_ng))
    tec_distancia_ng_ha.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303040401 - TECNICO DE NIVEL MEDIO SEMIPRESENCIAL REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_tecni_distan_ha_1 Gratuidade Regimental"),
    ("fev", "fev_tecni_distan_ha_1 Gratuidade Regimental"),
    ("mar", "mar_tecni_distan_ha_1 Gratuidade Regimental"),
    ("abr", "abr_tecni_distan_ha_1 Gratuidade Regimental"),
    ("mai", "mai_tecni_distan_ha_1 Gratuidade Regimental"),
    ("jun", "jun_tecni_distan_ha_1 Gratuidade Regimental"),
    ("jul", "jul_tecni_distan_ha_1 Gratuidade Regimental"),
    ("ago", "ago_tecni_distan_ha_1 Gratuidade Regimental"),
    ("set", "set_tecni_distan_ha_1 Gratuidade Regimental"),
    ("out", "out_tecni_distan_ha_1 Gratuidade Regimental"),
    ("nov", "nov_tecni_distan_ha_1 Gratuidade Regimental"),
    ("dez", "dez_tecni_distan_ha_1 Gratuidade Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    tec_distancia_regimental_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5064'].indicador")))
    tec_distancia_regimental_ha.click()

   
    tec_distancia_regimental_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_distan_ha_1 Gratuidade Regimental"
    
    ha_tec_distancia_regimental = dados['tecnico_nm']['distancia']['horas'].get(chave_dado, 0)

    tec_distancia_regimental_ha.send_keys(str(ha_tec_distancia_regimental))
    tec_distancia_regimental_ha.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303040401 - TECNICO DE NIVEL MEDIO SEMIPRESENCIAL BOLSA

nav.refresh()

meses = [
    ("jan", "jan_tecni_distan_ha_2 Gratuidade Não Regimental"),
    ("fev", "fev_tecni_distan_ha_2 Gratuidade Não Regimental"),
    ("mar", "mar_tecni_distan_ha_2 Gratuidade Não Regimental"),
    ("abr", "abr_tecni_distan_ha_2 Gratuidade Não Regimental"),
    ("mai", "mai_tecni_distan_ha_2 Gratuidade Não Regimental"),
    ("jun", "jun_tecni_distan_ha_2 Gratuidade Não Regimental"),
    ("jul", "jul_tecni_distan_ha_2 Gratuidade Não Regimental"),
    ("ago", "ago_tecni_distan_ha_2 Gratuidade Não Regimental"),
    ("set", "set_tecni_distan_ha_2 Gratuidade Não Regimental"),
    ("out", "out_tecni_distan_ha_2 Gratuidade Não Regimental"),
    ("nov", "nov_tecni_distan_ha_2 Gratuidade Não Regimental"),
    ("dez", "dez_tecni_distan_ha_2 Gratuidade Não Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    tec_distancia_bolsa_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5475'].indicador")))
    tec_distancia_bolsa_ha.click()

   
    tec_distancia_bolsa_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_distan_ha_2 Gratuidade Não Regimental"
    
    ha_tec_distancia_bolsa = dados['tecnico_nm']['distancia']['horas'].get(chave_dado, 0)

    tec_distancia_bolsa_ha.send_keys(str(ha_tec_distancia_bolsa))
    tec_distancia_bolsa_ha.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303040501 - TECN DE NIV MED ITINERARIOS PRESENCIAL BOLSA

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/228?cd_centro_resp=30303040501&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=TECN%20DE%20NIV%20MED%20ITINERARIOS%20PRESENCIAL&id_grupo=4&ds_grupo=T%C3%A9cnico%20de%20N%C3%ADvel%20M%C3%A9dio&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

meses = [
    ("jan", "jan_tecni_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("fev", "fev_tecni_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("mar", "mar_tecni_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("abr", "abr_tecni_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("mai", "mai_tecni_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("jun", "jun_tecni_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("jul", "jul_tecni_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("ago", "ago_tecni_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("set", "set_tecni_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("out", "out_tecni_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("nov", "nov_tecni_iti_presen_ha_2 Gratuidade Não Regimental"),
    ("dez", "dez_tecni_iti_presen_ha_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_iti_presencial_bolsa_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5101'].indicador")))
    tec_iti_presencial_bolsa_ha.click()

   
    tec_iti_presencial_bolsa_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_iti_presen_ha_2 Gratuidade Não Regimental"
    
    ha_tec_iti_presencial_bolsa = dados['tecnico_nm_iti']['presencial']['horas'].get(chave_dado, 0)

    tec_iti_presencial_bolsa_ha.send_keys(str(ha_tec_iti_presencial_bolsa))
    tec_iti_presencial_bolsa_ha.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303040501 - TECN DE NIV MED ITINERARIOS PRESENCIAL REGIMENTAL

nav.refresh()

meses = [
    ("jan", "jan_tecni_iti_presen_ha_1 Gratuidade Regimental"),
    ("fev", "fev_tecni_iti_presen_ha_1 Gratuidade Regimental"),
    ("mar", "mar_tecni_iti_presen_ha_1 Gratuidade Regimental"),
    ("abr", "abr_tecni_iti_presen_ha_1 Gratuidade Regimental"),
    ("mai", "mai_tecni_iti_presen_ha_1 Gratuidade Regimental"),
    ("jun", "jun_tecni_iti_presen_ha_1 Gratuidade Regimental"),
    ("jul", "jul_tecni_iti_presen_ha_1 Gratuidade Regimental"),
    ("ago", "ago_tecni_iti_presen_ha_1 Gratuidade Regimental"),
    ("set", "set_tecni_iti_presen_ha_1 Gratuidade Regimental"),
    ("out", "out_tecni_iti_presen_ha_1 Gratuidade Regimental"),
    ("nov", "nov_tecni_iti_presen_ha_1 Gratuidade Regimental"),
    ("dez", "dez_tecni_iti_presen_ha_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_iti_presencial_regimental_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5105'].indicador")))
    tec_iti_presencial_regimental_ha.click()

   
    tec_iti_presencial_regimental_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

 
    chave_dado = f"{mes}_tecni_iti_presen_ha_1 Gratuidade Regimental"
    
    ha_tec_iti_presencial_regimental = dados['tecnico_nm_iti']['presencial']['horas'].get(chave_dado, 0)

    tec_iti_presencial_regimental_ha.send_keys(str(ha_tec_iti_presencial_regimental))
    tec_iti_presencial_regimental_ha.send_keys(Keys.ENTER)
