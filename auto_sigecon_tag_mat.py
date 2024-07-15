
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
usuario = "matheus.reck"
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

quali_ng_mat_jan.send_keys(tag_qualificacao_presencial['jan_mat_bolsa'])

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

quali_regime_mat_jan.send_keys(tag_qualificacao_presencial['jan_mat_bolsa'])

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