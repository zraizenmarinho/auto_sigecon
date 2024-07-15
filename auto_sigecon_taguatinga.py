
# Importação dos pacotes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from obter_dados import obter_dados_por_tipo
arquivo = 'si_jan.xlsx'

# Variaveis indexando as funções

# Matricula Janeiro

from si_janeiro_m_c_e import (
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

# Navevagção para a pagina

url = 'http://sn-iis-02/SIGECON20/'

nav = webdriver.Firefox()

nav.get(url)

# Elemento Usuario
e_usuario = WebDriverWait(nav, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="UserName"]')))
usuario = ""
e_usuario.send_keys(usuario)

# Elemento Senha
e_senha = WebDriverWait(nav, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="Password"]')))
senha = ""
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

#################################################################   Elemento unidade SENAI TAGUATINGA ###########################################################################################

e_uni_tag1 = WebDriverWait(nav, 15).until(EC.visibility_of_element_located(
    (By.PARTIAL_LINK_TEXT, 'Senai Taguatinga')))
e_uni_tag1.click()

################################################################   Elemento CR INICIACAO PROFISSIONAL PRESENCIAL ################################################################################

e_cr_inici_prese = WebDriverWait(nav, 5).until(EC.visibility_of_element_located(
    (By.PARTIAL_LINK_TEXT, 'INICIACAO PROFISSIONAL PRESENCIAL')))
e_cr_inici_prese.click()

################################################################   Elemento FICHA DE PRODUÇÃO ###################################################################################################

e_ficha_prod = WebDriverWait(nav, 15).until(EC.visibility_of_element_located(
    (By.LINK_TEXT, 'Produção')))

nav.execute_script("arguments[0].scrollIntoView(true);", e_ficha_prod)

nav.execute_script("arguments[0].click();", e_ficha_prod)

################################################################   Elemento GRUPO DE META ########################################################################################################

e_grupo_meta = WebDriverWait(nav, 30).until(EC.visibility_of_element_located(
    (By.XPATH, "//a[@href='/SIGECON20/Metas/MetasTipo/309/2024/0902030201/229?cd_centro_resp=30303010101&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=INICIACAO%20PROFISSIONAL%20PRESENCIAL&id_grupo=1&ds_grupo=Inicia%C3%A7%C3%A3o%20Profissional&fase=Realiza%C3%A7%C3%A3o']"
)))

nav.execute_script("arguments[0].scrollIntoView(true);", e_grupo_meta)

e_grupo_meta.click()

# SENAI TAGUATINGA - 30303010101 - INICIACAO PROFISSIONAL PRESENCIAL 

################################################################   MATRICULA BOLSA ########################################################################################################

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


em_bolsa_click = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5113'].indicador")))
em_bolsa_click.click()


for i, (mes, campo_dado) in enumerate(meses):
    mat_bolsa_mes = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5113'].indicador")))
    mat_bolsa_mes.click()

    mat_bolsa_send = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    mat_iniciacao_presencial_geral = dados['iniciacao']['presencial']['matriculas']
    
    # Convertendo campo_dado para int
    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")

    else:
        mat_bolsa_send.send_keys(str(mat_iniciacao_presencial_geral[campo_dado_int]))
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
   
    mat_ng_mes = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5114'].indicador")))
    mat_ng_mes.click()

    mat_ng_mes = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    mat_iniciacao_presencial_geral_ng = dados['iniciacao']['presencial']['matriculas']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")

    else:
        mat_ng_mes.send_keys(str(mat_iniciacao_presencial_geral_ng[campo_dado]))
        mat_ng_mes.send_keys(Keys.ENTER)


############################################################   Concluinte Bolsa - Janeiro ##################################################################################################

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
con_b = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5107'].indicador")))
con_b.click()

nav.refresh()


for i, (mes, campo_dado) in enumerate(meses):
   
    concluinte = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5107'].indicador")))
    concluinte.click()

    concluinte = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    con_iniciacao_presencial_geral_bolsa = dados['iniciacao']['presencial']['concluintes']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    
    else:
        concluinte.send_keys(str(con_iniciacao_presencial_geral_bolsa[campo_dado]))
        concluinte.send_keys(Keys.ENTER)
    

# SENAI TAGUATINGA - 30303010101 - INICIACAO PROFISSINAL PRESENCIAL CONCLUINTE NAO GRATUITA

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
con_ng = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5108'].indicador")))
con_ng.click()

nav.refresh()


for i, (mes, campo_dado) in enumerate(meses):
   
    concluinte_ng_ip = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5108'].indicador")))
    concluinte_ng_ip.click()

    concluinte_ng_ip = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    con_iniciacao_presencial_geral_ng = dados['iniciacao']['presencial']['concluintes']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    
    else:
        concluinte_ng_ip.send_keys(str(con_iniciacao_presencial_geral_ng[campo_dado]))
        concluinte_ng_ip.send_keys(Keys.ENTER)

############################################################   Evasão Bolsa -Janeiro ###########################################################################################################

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

eva_b = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5109'].indicador")))
eva_b.click()

nav.refresh()


for i, (mes, campo_dado) in enumerate(meses):
   
    eva_b_ip = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4+ i}) > [id='5109'].indicador")))
    eva_b_ip.click()

    eva_b_ip = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    eva_iniciacao_presencial_bolsa = dados['iniciacao']['presencial']['evadidos']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        eva_b_ip.send_keys(str(eva_iniciacao_presencial_bolsa[campo_dado]))
        eva_b_ip.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010101 - INICIACAO PROFISSINAL PRESENCIAL EVASAO NAO GRATUITA

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
eva_ng = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5110'].indicador")))
eva_ng.click()

nav.refresh()


for i, (mes, campo_dado) in enumerate(meses):
   
    eva_ng = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5110'].indicador")))
    eva_ng.click()

    eva_ng = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    eva_iniciacao_presencial_ng = dados['iniciacao']['presencial']['evadidos']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        eva_ng.send_keys(str(eva_iniciacao_presencial_ng[campo_dado]))
        eva_ng.send_keys(Keys.ENTER)



# SENAI TAGUATINGA - 30303010101 - INICIACAO PROFISSINAL PRESENCIAL HORA ALUNO BOLSA

meses = [
    ("jan", "jan_5 Iniciação Profissional_1 Presencial_ha_2 Gratuidade Não Regimental"),
    ("fev", "fev_5 Iniciação Profissional_1 Presencial_ha_2 Gratuidade Não Regimental"),
    ("mar", "mar_5 Iniciação Profissional_1 Presencial_ha_2 Gratuidade Não Regimental"),
    ("abr", "abr_5 Iniciação Profissional_1 Presencial_ha_2 Gratuidade Não Regimental"),
    ("mai", "mai_5 Iniciação Profissional_1 Presencial_ha_2 Gratuidade Não Regimental"),
    ("jun", "jun_5 Iniciação Profissional_1 Presencial_ha_2 Gratuidade Não Regimental"),
    ("jul", "jul_5 Iniciação Profissional_1 Presencial_ha_2 Gratuidade Não Regimental"),
    ("ago", "ago_5 Iniciação Profissional_1 Presencial_ha_2 Gratuidade Não Regimental"),
    ("set", "set_5 Iniciação Profissional_1 Presencial_ha_2 Gratuidade Não Regimental"),
    ("out", "out_5 Iniciação Profissional_1 Presencial_ha_2 Gratuidade Não Regimental"),
    ("nov", "nov_5 Iniciação Profissional_1 Presencial_ha_2 Gratuidade Não Regimental"),
    ("dez", "dez_5 Iniciação Profissional_1 Presencial_ha_2 Gratuidade Não Regimental")
	
]
hora_bolsa_ip = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5111'].indicador")))
hora_bolsa_ip.click()

nav.refresh()


for i, (mes, campo_dado) in enumerate(meses):
   
    hora_bolsa_ip = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5111'].indicador")))
    hora_bolsa_ip.click()

    hora_bolsa_ip = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))
    
    ha_iniciacao_presencial_bolsa = dados['iniciacao']['presencial']['hora']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        hora_bolsa_ip.send_keys(str(ha_iniciacao_presencial_bolsa[campo_dado]))
        hora_bolsa_ip.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010101 - INICIACAO PROFISSINAL PRESENCIAL HORA ALUNO NAO GRATUITA

############################################################   Hora Aluno Não Gratuita - Janeiro ####################################################################

meses = [
    ("jan", "jan_5 Iniciação Profissional_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_5 Iniciação Profissional_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_5 Iniciação Profissional_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_5 Iniciação Profissional_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_5 Iniciação Profissional_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_5 Iniciação Profissional_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_5 Iniciação Profissional_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_5 Iniciação Profissional_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_5 Iniciação Profissional_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_5 Iniciação Profissional_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_5 Iniciação Profissional_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_5 Iniciação Profissional_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa")

	
]
hora_ng_ip = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5112'].indicador")))
hora_ng_ip.click()

nav.refresh()


for i, (mes, campo_dado) in enumerate(meses):
   
    hora_ng_ip = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5112'].indicador")))
    hora_ng_ip.click()

    hora_ng_ip = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    ha_iniciacao_presencial_ng = dados['iniciacao']['presencial']['hora']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        hora_ng_ip.send_keys(str(ha_iniciacao_presencial_ng[campo_dado]))
        hora_ng_ip.send_keys(Keys.ENTER)

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



ipd_bolsa_mat_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5073'].indicador")))
ipd_bolsa_mat_jan.click()


for i, (mes, campo_dado) in enumerate(meses):

    ipd_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5073'].indicador")))
    ipd_bolsa_mat.click()

   
    ipd_bolsa_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    mat_iniciacao_distancia_bolsa = dados['iniciacao']['distancia']['matriculas']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        ipd_bolsa_mat.send_keys(str(mat_iniciacao_distancia_bolsa[campo_dado]))
        ipd_bolsa_mat.send_keys(Keys.ENTER)



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

    ipd_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5074'].indicador")))
    ipd_ng_mat.click()

   
    ipd_ng_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    mat_iniciacao_distancia_ng = dados['iniciacao']['distancia']['matriculas']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        ipd_bolsa_mat.send_keys(str(mat_iniciacao_distancia_ng[campo_dado]))
        ipd_bolsa_mat.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA CONCLUINTES BOLSA

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


ipd_bolsa_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5067'].indicador")))
ipd_bolsa_con.click()

nav.refresh()


for i, (mes, campo_dado) in enumerate(meses):

    ipd_bolsa_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5067'].indicador")))
    ipd_bolsa_con.click()

   
    ipd_bolsa_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    con_iniciacao_distancia_bolsa = dados['iniciacao']['distancia']['concluintes']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        ipd_bolsa_con.send_keys(str(con_iniciacao_distancia_bolsa[campo_dado]))
        ipd_bolsa_con.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA CONCLUINTES NAO GRATUITA

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


ipd_ng_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5068'].indicador")))
ipd_ng_con.click()

nav.refresh()


for i, (mes, campo_dado) in enumerate(meses):

    ipd_ng_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5068'].indicador")))
    ipd_ng_con.click()

   
    ipd_ng_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    con_iniciacao_distancia_ng = dados['iniciacao']['distancia']['concluintes']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        ipd_ng_con.send_keys(str(con_iniciacao_distancia_ng[campo_dado]))
        ipd_ng_con.send_keys(Keys.ENTER)

############################################################ Evasão - Bolsa Janeiro ########################################################

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



ipd_bolsa_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5069'].indicador")))
ipd_bolsa_eva.click()

nav.refresh()


for i, (mes, campo_dado) in enumerate(meses):

    ipd_bolsa_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5069'].indicador")))
    ipd_bolsa_eva.click()

   
    ipd_bolsa_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))
  
    eva_iniciacao_distancia_bolsa = dados['iniciacao']['distancia']['evadidos']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        ipd_bolsa_eva.send_keys(str(eva_iniciacao_distancia_bolsa[campo_dado]))
        ipd_bolsa_eva.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA EVASAO NAO GRATUITA

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


ipd_ng_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5070'].indicador")))
ipd_ng_eva.click()

nav.refresh()


for i, (mes, campo_dado) in enumerate(meses):

    ipd_ng_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5070'].indicador")))
    ipd_ng_eva.click()

   
    ipd_ng_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))
     
    eva_iniciacao_distancia_ng = dados['iniciacao']['distancia']['evadidos']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        ipd_ng_eva.send_keys(str(eva_iniciacao_distancia_ng[campo_dado]))
        ipd_ng_eva.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA HORA ALUNO BOLSA

meses = [
    ("jan", "jan_5 Iniciação Profissional_2 A distância_ha_2 Gratuidade Não Regimental"),
    ("fev", "fev_5 Iniciação Profissional_2 A distância_ha_2 Gratuidade Não Regimental"),
    ("mar", "mar_5 Iniciação Profissional_2 A distância_ha_2 Gratuidade Não Regimental"),
    ("abr", "abr_5 Iniciação Profissional_2 A distância_ha_2 Gratuidade Não Regimental"),
    ("mai", "mai_5 Iniciação Profissional_2 A distância_ha_2 Gratuidade Não Regimental"),
    ("jun", "jun_5 Iniciação Profissional_2 A distância_ha_2 Gratuidade Não Regimental"),
    ("jul", "jul_5 Iniciação Profissional_2 A distância_ha_2 Gratuidade Não Regimental"),
    ("ago", "ago_5 Iniciação Profissional_2 A distância_ha_2 Gratuidade Não Regimental"),
    ("set", "set_5 Iniciação Profissional_2 A distância_ha_2 Gratuidade Não Regimental"),
    ("out", "out_5 Iniciação Profissional_2 A distância_ha_2 Gratuidade Não Regimental"),
    ("nov", "nov_5 Iniciação Profissional_2 A distância_ha_2 Gratuidade Não Regimental"),
    ("dez", "dez_5 Iniciação Profissional_2 A distância_ha_2 Gratuidade Não Regimental")
]



ipd_bolsa_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5071'].indicador")))
ipd_bolsa_ha.click()

nav.refresh()


for i, (mes, campo_dado) in enumerate(meses):

    ipd_bolsa_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5071'].indicador")))
    ipd_bolsa_ha.click()

   
    ipd_bolsa_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    hora_iniciacao_distancia_bolsa = dados['iniciacao']['distancia']['hora']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        ipd_bolsa_ha.send_keys(str(hora_iniciacao_distancia_bolsa[campo_dado]))
        ipd_bolsa_ha.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA HORA ALUNO NAO GRATUITA

meses = [
    ("jan", "jan_5 Iniciação Profissional_2 A distância_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_5 Iniciação Profissional_2 A distância_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_5 Iniciação Profissional_2 A distância_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_5 Iniciação Profissional_2 A distância_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_5 Iniciação Profissional_2 A distância_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_5 Iniciação Profissional_2 A distância_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_5 Iniciação Profissional_2 A distância_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_5 Iniciação Profissional_2 A distância_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_5 Iniciação Profissional_2 A distância_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_5 Iniciação Profissional_2 A distância_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_5 Iniciação Profissional_2 A distância_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_5 Iniciação Profissional_2 A distância_ha_9 Pago por Pessoa Fisica ou Empresa")
]


ipd_ng_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5072'].indicador")))
ipd_ng_ha.click()

nav.refresh()


for i, (mes, campo_dado) in enumerate(meses):

    ipd_ng_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5072'].indicador")))
    ipd_ng_ha.click()

   
    ipd_ng_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    hora_iniciacao_distancia_ng = dados['iniciacao']['distancia']['hora']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        ipd_ng_ha.send_keys(str(hora_iniciacao_distancia_ng[campo_dado]))
        ipd_ng_ha.send_keys(Keys.ENTER)

###################################################  Aprendizagem Industrial - Presencial #############################################################

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/230?cd_centro_resp=30303020101&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APRENDIZAGEM%20INDUSTRIAL%20PRESENCIAL&id_grupo=2&ds_grupo=Aprendizagem%20Industrial&fase=Realiza%C3%A7%C3%A3o', '_blank')")

# Pegar o identificador da janela atual
janela_atual = nav.current_window_handle

# Pegar todos os identificadores de janela
todas_janelas = nav.window_handles

# Alternar para a nova janela (a última na lista de identificadores)
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

    mat_aprendizagem_presencial_ng = dados['aprendizagem']['presencial']['matriculas']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        app_ng_mat.send_keys(str(mat_aprendizagem_presencial_ng[campo_dado]))
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

    mat_aprendizagem_presencial_regimental = dados['aprendizagem']['presencial']['matriculas']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        app_regimental_mat.send_keys(str(mat_aprendizagem_presencial_regimental[campo_dado]))
        app_regimental_mat.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL CONCLUINTES NAO GRATUITA

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

app_ng_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5115'].indicador")))
app_ng_con.click()

nav.refresh()

for i, (mes, campo_dado) in enumerate(meses):

    app_ng_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5115'].indicador")))
    app_ng_con.click()

   
    app_ng_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    con_aprendizagem_presencial_ng = dados['aprendizagem']['presencial']['concluintes']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        app_ng_con.send_keys(str(con_aprendizagem_presencial_ng[campo_dado]))
        app_ng_con.send_keys(Keys.ENTER)



# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL CONCLUINTES REGIMENTAL


meses = [
    ("jan", "jan_aprendi_presen_con_1 Gratuidade Regimental"),
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

app_regimental_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5116'].indicador")))
app_regimental_con.click()

nav.refresh()

for i, (mes, campo_dado) in enumerate(meses):

    app_regimental_con = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5116'].indicador")))
    app_regimental_con.click()

   
    app_regimental_con = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    con_aprendizagem_presencial_regimental = dados['aprendizagem']['presencial']['concluintes']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        app_regimental_con.send_keys(str(con_aprendizagem_presencial_regimental[campo_dado]))
        app_regimental_con.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL EVASAO NAO GRATUITA

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

app_ng_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5117'].indicador")))
app_ng_eva.click()

nav.refresh()

for i, (mes, campo_dado) in enumerate(meses):

    app_ng_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5117'].indicador")))
    app_ng_eva.click()

   
    app_ng_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    eva_aprendizagem_presencial_ng = dados['aprendizagem']['presencial']['evadidos']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        app_ng_eva.send_keys(str(eva_aprendizagem_presencial_ng[campo_dado]))
        app_ng_eva.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL EVASAO REGIMENTAL


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

app_regimental_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5118'].indicador")))
app_regimental_eva.click()

nav.refresh()

for i, (mes, campo_dado) in enumerate(meses):

    app_regimental_eva = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5118'].indicador")))
    app_regimental_eva.click()

   
    app_regimental_eva = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    eva_aprendizagem_presencial_regimental = dados['aprendizagem']['presencial']['concluintes']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        app_regimental_eva.send_keys(str(eva_aprendizagem_presencial_regimental[campo_dado]))
        app_regimental_eva.send_keys(Keys.ENTER)


# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL HORA ALUNO NAO GRATUITA

meses = [
    ("jan", "jan_11 Aprendizagem Industrial básica_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("fev", "fev_11 Aprendizagem Industrial básica_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_11 Aprendizagem Industrial básica_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_11 Aprendizagem Industrial básica_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_11 Aprendizagem Industrial básica_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_11 Aprendizagem Industrial básica_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_11 Aprendizagem Industrial básica_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_11 Aprendizagem Industrial básica_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_11 Aprendizagem Industrial básica_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_11 Aprendizagem Industrial básica_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_11 Aprendizagem Industrial básica_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_11 Aprendizagem Industrial básica_1 Presencial_ha_9 Pago por Pessoa Fisica ou Empresa")
]

app_ng_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5119'].indicador")))
app_ng_ha.click()

nav.refresh()

for i, (mes, campo_dado) in enumerate(meses):

    app_ng_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5119'].indicador")))
    app_ng_ha.click()

   
    app_ng_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    ha_aprendizagem_presencial_ng = dados['aprendizagem']['presencial']['hora']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        app_ng_ha.send_keys(str(ha_aprendizagem_presencial_ng[campo_dado]))
        app_ng_ha.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL HORA ALUNO REGIMENTAL

meses = [
    ("jan", "jan_11 Aprendizagem Industrial básica_1 Presencial_ha_1 Gratuidade Regimental"),
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

app_regimental_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5120'].indicador")))
app_regimental_ha.click()

nav.refresh()

for i, (mes, campo_dado) in enumerate(meses):

    app_regimental_ha = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({4 + i}) > [id='5120'].indicador")))
    app_regimental_ha.click()

   
    app_regimental_ha = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    ha_aprendizagem_presencial_regimental = dados['aprendizagem']['presencial']['hora']

    try:
        campo_dado_int = int(campo_dado)
    except ValueError:
        print(f"Campo preenchido: {campo_dado}")
    else:
        app_ng_ha.send_keys(str(ha_aprendizagem_presencial_regimental[campo_dado]))
        app_ng_ha.send_keys(Keys.ENTER)

####################################################################################################################

janela_atual = nav.current_window_handle


nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/221?cd_centro_resp=30303020201&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=QUALIFICACAO%20PROFISSIONAL%20PRESENCIAL&id_grupo=3&ds_grupo=Qualifica%C3%A7%C3%A3o%20Industrial&fase=Realiza%C3%A7%C3%A3o', '_self')")


# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL MATRICULA CONVENIO

############################################################ Matricula- Convenio Janeiro ###########################################


mat_c = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5022'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5022"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_jan_QP['jan_qp_mat_convenio']))

############################################################ Matricula- Convenio Fevereiro ###########################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5022'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5022"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['fev_qp_mat_3 Convênio']))

############################################################ Matricula- Convenio Março ###########################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5022'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5022"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['mar_qp_mat_3 Convênio']))

############################################################ Matricula- Convenio Abril ###########################################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5022'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5022"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['abr_qp_mat_3 Convênio']))

############################################################ Matricula- Convenio Maio ###########################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5022'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5022"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['mai_qp_mat_3 Convênio']))

############################################################ Matricula- Convenio Junho ###########################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5022'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5022"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['jun_qp_mat_3 Convênio']))

############################################################ Matricula- Convenio Julho ###########################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5022'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5022"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['jul_qp_mat_3 Convênio']))

############################################################ Matricula- Convenio Agosto ###########################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5022'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5022"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['ago_qp_mat_3 Convênio']))

############################################################ Matricula- Convenio Setembro ###########################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5022'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5022"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['set_qp_mat_3 Convênio']))

############################################################ Matricula- Convenio Outubro ###########################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5022'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5022"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['out_qp_mat_3 Convênio']))

############################################################ Matricula- Convenio Novembro ###########################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5022'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5022"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['nov_qp_mat_3 Convênio']))

############################################################ Matricula- Convenio Dezembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5022'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5022"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['dez_qp_mat_3 Convênio']))

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL MATRICULA BOLSA

############################################################ Matricula- Bolsa Janeiro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5032'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5032"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_jan_QP['jan_qp_mat_bolsa']))

############################################################ Matricula- Bolsa Fevereiro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5032'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5032"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['fev_qp_mat_2 Gratuidade Não Regimental']))


############################################################ Matricula- Bolsa Marco ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5032'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5032"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['mar_qp_mat_2 Gratuidade Não Regimental']))

############################################################ Matricula- Bolsa Abril ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5032'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5032"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['abr_qp_mat_2 Gratuidade Não Regimental']))

############################################################ Matricula- Bolsa Maio ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5032'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5032"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['mai_qp_mat_2 Gratuidade Não Regimental']))

############################################################ Matricula- Bolsa Junho ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5032'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5032"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['jun_qp_mat_2 Gratuidade Não Regimental']))

############################################################ Matricula- Bolsa Julho ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5032'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5032"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['jul_qp_mat_2 Gratuidade Não Regimental']))


############################################################ Matricula- Bolsa Agosto ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5032'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5032"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['ago_qp_mat_2 Gratuidade Não Regimental']))

############################################################ Matricula- Bolsa Setembro ##########################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5032'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5032"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['set_qp_mat_2 Gratuidade Não Regimental']))

############################################################ Matricula- Bolsa Outubro ##########################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5032'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5032"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['out_qp_mat_2 Gratuidade Não Regimental']))

############################################################ Matricula- Bolsa Novembro ##########################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5032'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5032"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['nov_qp_mat_2 Gratuidade Não Regimental']))

############################################################ Matricula- Bolsa Dezembro ##########################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5032'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5032"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['dez_qp_mat_2 Gratuidade Não Regimental']))

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL MATRICULA NAO GRATUITA

############################################################ Matricula- Nao Gratuita Janeiro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5033'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5033"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_jan_QP['jan_qp_mat_n_gratuita']))

############################################################ Matricula- Nao Gratuita Fevereiro ##########################

#Mudança so no "td:nth-child" e [id='']
mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5033'].indicador")))

mat_c.click()

# Estatico
mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5033"
)))
#Estatico
mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))
#Estatico
mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

#Mudança na chamada da variavel
mat_c_send.send_keys(str(mat_QP['fev_qp_mat_9 Pago por Pessoa Fisica ou Empresa']))


############################################################ Matricula- Nao Gratuita Marco ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5033'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5033"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['mar_qp_mat_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Matricula- Nao Gratuita Abril ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5033'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5033"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['abr_qp_mat_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Matricula- Nao Gratuita Maio ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5033'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5033"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['mai_qp_mat_9 Pago por Pessoa Fisica ou Empresa']))


############################################################ Matricula- Nao Gratuita Junho ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5033'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5033"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['jun_qp_mat_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Matricula- Nao Gratuita Julho ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5033'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5033"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['jul_qp_mat_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Matricula- Nao Gratuita Agosto ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5033'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5033"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['ago_qp_mat_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Matricula- Nao Gratuita Setembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5033'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5033"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['set_qp_mat_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Matricula- Nao Gratuita Outubro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5033'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5033"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['out_qp_mat_9 Pago por Pessoa Fisica ou Empresa']))


############################################################ Matricula- Nao Gratuita Novembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5033'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5033"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['nov_qp_mat_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Matricula- Nao Gratuita Dezembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5033'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5033"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['dez_qp_mat_9 Pago por Pessoa Fisica ou Empresa']))

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL MATRICULA REGIMENTAL

############################################################ Matricula Regimental Janeiro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5034'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5034"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_jan_QP['jan_qp_mat_regi']))

############################################################ Matricula Regimental Fevereiro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5034'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5034"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['fev_qp_mat_1 Gratuidade Regimental']))

############################################################ Matricula Regimental Marco ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5034'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5034"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['mar_qp_mat_1 Gratuidade Regimental']))

############################################################ Matricula Regimental Abril ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5034'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5034"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['abr_qp_mat_1 Gratuidade Regimental']))

############################################################ Matricula Regimental Maio ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5034'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5034"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['mai_qp_mat_1 Gratuidade Regimental']))

############################################################ Matricula Regimental Junho ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5034'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5034"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['jun_qp_mat_1 Gratuidade Regimental']))

############################################################ Matricula Regimental Julho ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5034'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5034"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['jul_qp_mat_1 Gratuidade Regimental']))


############################################################ Matricula Regimental Agosto ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5034'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5034"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['ago_qp_mat_1 Gratuidade Regimental']))

############################################################ Matricula Regimental Setembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5034'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5034"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['set_qp_mat_1 Gratuidade Regimental']))

############################################################ Matricula Regimental Outubro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5034'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5034"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['out_qp_mat_1 Gratuidade Regimental']))


############################################################ Matricula Regimental Novembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5034'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5034"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['nov_qp_mat_1 Gratuidade Regimental']))

############################################################ Matricula Regimental Dezembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5034'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5034"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(mat_QP['dez_qp_mat_1 Gratuidade Regimental']))

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL CONCLUINTES CONVENIO

############################################################ Concluinte Convenio Janeiro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5019'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5019"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['jan_qp_con_3 Convênio']))

############################################################ Concluinte Convenio Fevereiro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5019'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5019"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['fev_qp_con_3 Convênio']))

############################################################ Concluinte Convenio Marco ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5019'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5019"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['mar_qp_con_3 Convênio']))


############################################################ Concluinte Convenio Abril ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5019'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5019"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['abr_qp_con_3 Convênio']))


############################################################ Concluinte Convenio Maio ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5019'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5019"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['mai_qp_con_3 Convênio']))

############################################################ Concluinte Convenio Junho ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5019'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5019"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['jun_qp_con_3 Convênio']))

############################################################ Concluinte Convenio Julho ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5019'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5019"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['jul_qp_con_3 Convênio']))

############################################################ Concluinte Convenio Agosto ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5019'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5019"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['ago_qp_con_3 Convênio']))

############################################################ Concluinte Convenio Setembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5019'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5019"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['set_qp_con_3 Convênio']))

############################################################ Concluinte Convenio Outubro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5019'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5019"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['out_qp_con_3 Convênio']))

############################################################ ConcluinteConvenio Novembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5019'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5019"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['nov_qp_con_3 Convênio']))

############################################################ Concluinte Convenio Dezembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5019'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5019"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['dez_qp_con_3 Convênio']))

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL CONCLUINTES BOLSA

############################################################ Concluinte Bolsa Janeiro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5023'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5023"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['jan_qp_con_2 Gratuidade Não Regimental']))

############################################################ Concluinte Bolsa Fevereiro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5023'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5023"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['fev_qp_con_2 Gratuidade Não Regimental']))

############################################################ Concluinte Bolsa Março ##########################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5023'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5023"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['mar_qp_con_2 Gratuidade Não Regimental']))

############################################################ Concluinte Bolsa Abril ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5023'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5023"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['abr_qp_con_2 Gratuidade Não Regimental']))


############################################################ Concluinte Bolsa Maio ##########################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5023'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5023"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['mai_qp_con_2 Gratuidade Não Regimental']))


############################################################ Concluinte Bolsa Junho ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5023'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5023"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['jun_qp_con_2 Gratuidade Não Regimental']))


############################################################ Concluinte Bolsa Julho ##########################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5023'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5023"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['jul_qp_con_2 Gratuidade Não Regimental']))



############################################################ Concluinte Bolsa Agosto ##########################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5023'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5023"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['ago_qp_con_2 Gratuidade Não Regimental']))


############################################################ Concluinte Bolsa Setembro ##########################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5023'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5023"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['set_qp_con_2 Gratuidade Não Regimental']))


############################################################ Concluinte Bolsa Outubro ##########################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5023'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5023"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['out_qp_con_2 Gratuidade Não Regimental']))


############################################################ Concluinte Bolsa Novembro ##########################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5023'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5023"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['nov_qp_con_2 Gratuidade Não Regimental']))



############################################################ Concluinte Bolsa Dezembro ##########################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5023'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5023"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['dez_qp_con_2 Gratuidade Não Regimental']))

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL CONCLUINTE NAO GRATUITA

############################################################ Concluinte Nao Gratuita Janeiro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5024'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5024"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['jan_qp_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte Nao Gratuita Fevereiro ##########################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5024'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5024"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['fev_qp_con_9 Pago por Pessoa Fisica ou Empresa']))


############################################################ Concluinte Nao Gratuita Marco ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5024'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5024"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['mar_qp_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte Nao Gratuita Abril ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5024'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5024"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['abr_qp_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte Nao Gratuita Maio ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5024'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5024"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['mai_qp_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte Nao Gratuita Junho ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5024'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5024"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['jun_qp_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte Nao Gratuita Julho ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5024'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5024"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['jul_qp_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte Nao Gratuita Agosto ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5024'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5024"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['ago_qp_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte Nao Gratuita Setembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5024'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5024"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['set_qp_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte Nao Gratuita Outubro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5024'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5024"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['out_qp_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte Nao Gratuita Novembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5024'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5024"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['nov_qp_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte Nao Gratuita Dezembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5024'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5024"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['dez_qp_con_9 Pago por Pessoa Fisica ou Empresa']))

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL CONCLUINTE REGIMENTAL

############################################################ Concluinte Regimental Janeiro  ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5025'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5025"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['jan_qp_con_1 Gratuidade Regimental']))

############################################################ Concluinte Regimental Fevereiro  ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5025'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5025"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['fev_qp_con_1 Gratuidade Regimental']))

############################################################ Concluinte Regimental MArco ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5025'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5025"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['mar_qp_con_1 Gratuidade Regimental']))

############################################################ Concluinte Regimental Abril  ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5025'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5025"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['abr_qp_con_1 Gratuidade Regimental']))

############################################################ Concluinte Regimental Maio  ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5025'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5025"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['mai_qp_con_1 Gratuidade Regimental']))

############################################################ Concluinte Regimental Junho  ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5025'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5025"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['jun_qp_con_1 Gratuidade Regimental']))

############################################################ Concluinte Regimental Julho  ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5025'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5025"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['jul_qp_con_1 Gratuidade Regimental']))

############################################################ Concluinte Regimental Agosto  ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5025'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5025"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['ago_qp_con_1 Gratuidade Regimental']))


############################################################ Concluinte Regimental Setembro  ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5025'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5025"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['set_qp_con_1 Gratuidade Regimental']))

############################################################ Concluinte Regimental Outubro  ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5025'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5025"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['out_qp_con_1 Gratuidade Regimental']))

############################################################ Concluinte Regimental Novembro  ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5025'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5025"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['nov_qp_con_1 Gratuidade Regimental']))

############################################################ Concluinte Regimental Dezembro  ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5025'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5025"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_QP['dez_qp_con_1 Gratuidade Regimental']))

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL EVASAO CONVENIO

############################################################ Evasao Convenio Janeiro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5020'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5020"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['jan_qp_eva_3 Convênio']))


############################################################ Evasao Convenio Fevereiro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5020'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5020"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['fev_qp_eva_3 Convênio']))

############################################################ Evasao Convenio Marco ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5020'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5020"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['mar_qp_eva_3 Convênio']))


############################################################ Evasao Convenio Abril ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5020'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5020"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['abr_qp_eva_3 Convênio']))


############################################################ Evasao Convenio Maio ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5020'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5020"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['mai_qp_eva_3 Convênio']))


############################################################ Evasao Convenio Junho ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5020'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5020"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['jun_qp_eva_3 Convênio']))

############################################################ Evasao Convenio Julho ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5020'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5020"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['jul_qp_eva_3 Convênio']))


############################################################ Evasao Convenio Agosto ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5020'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5020"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['ago_qp_eva_3 Convênio']))


############################################################ Evasao Convenio Setembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5020'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5020"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['set_qp_eva_3 Convênio']))



############################################################ Evasao Convenio Outubro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5020'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5020"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['out_qp_eva_3 Convênio']))


############################################################ Evasao Convenio Novembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5020'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5020"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['nov_qp_eva_3 Convênio']))


############################################################ Evasao Convenio Dezembro ##########################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5020'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5020"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['dez_qp_eva_3 Convênio']))

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL EVASAO BOLSA

#JANEIRO

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5026'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5026"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['jan_qp_eva_2 Gratuidade Não Regimental']))


#FEVEREIRO

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5026'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5026"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['fev_qp_eva_2 Gratuidade Não Regimental']))

#MARCO

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5026'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5026"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['mar_qp_eva_2 Gratuidade Não Regimental']))

#ABRIL

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5026'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5026"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['abr_qp_eva_2 Gratuidade Não Regimental']))

#MAIO

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5026'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5026"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['mai_qp_eva_2 Gratuidade Não Regimental']))

#Junho

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5026'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5026"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['jun_qp_eva_2 Gratuidade Não Regimental']))

#Julho

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5026'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5026"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['jul_qp_eva_2 Gratuidade Não Regimental']))

#Agosto

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5026'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5026"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['ago_qp_eva_2 Gratuidade Não Regimental']))

#Setembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5026'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5026"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['set_qp_eva_2 Gratuidade Não Regimental']))

#Outubro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5026'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5026"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['out_qp_eva_2 Gratuidade Não Regimental']))

#Novembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5026'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5026"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['nov_qp_eva_2 Gratuidade Não Regimental']))

#Dezembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5026'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5026"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['dez_qp_eva_2 Gratuidade Não Regimental']))

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL EVASAO NAO GRATUITA

#Janeiro
mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5027'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5027"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['jan_qp_eva_9 Pago por Pessoa Fisica ou Empresa']))

#Fevereiro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5027'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5027"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['fev_qp_eva_9 Pago por Pessoa Fisica ou Empresa']))

#Marco

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5027'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5027"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['mar_qp_eva_9 Pago por Pessoa Fisica ou Empresa']))

#Abril

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5027'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5027"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['abr_qp_eva_9 Pago por Pessoa Fisica ou Empresa']))


#Maio

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5027'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5027"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['mai_qp_eva_9 Pago por Pessoa Fisica ou Empresa']))

#Junho

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5027'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5027"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['jun_qp_eva_9 Pago por Pessoa Fisica ou Empresa']))


#Julho

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5027'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5027"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['jul_qp_eva_9 Pago por Pessoa Fisica ou Empresa']))

#Agosto

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5027'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5027"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['ago_qp_eva_9 Pago por Pessoa Fisica ou Empresa']))

#Setembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5027'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5027"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['set_qp_eva_9 Pago por Pessoa Fisica ou Empresa']))


#Outubro


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5027'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5027"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['out_qp_eva_9 Pago por Pessoa Fisica ou Empresa']))

#Novembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5027'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5027"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['nov_qp_eva_9 Pago por Pessoa Fisica ou Empresa']))

#Dezembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5027'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5027"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['dez_qp_eva_9 Pago por Pessoa Fisica ou Empresa']))

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL EVASAO REGIMENTAL

#Janeiro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5028'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5028"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['jan_qp_eva_1 Gratuidade Regimental']))

#Fevereiro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5028'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5028"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['fev_qp_eva_1 Gratuidade Regimental']))

#Marco

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5028'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5028"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['mar_qp_eva_1 Gratuidade Regimental']))

#Abril


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5028'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5028"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['abr_qp_eva_1 Gratuidade Regimental']))

#Maio

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5028'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5028"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['mai_qp_eva_1 Gratuidade Regimental']))


#Junho

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5028'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5028"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['jun_qp_eva_1 Gratuidade Regimental']))

#Julho

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5028'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5028"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['jul_qp_eva_1 Gratuidade Regimental']))

#Agosto

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5028'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5028"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['ago_qp_eva_1 Gratuidade Regimental']))

#Setembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5028'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5028"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['set_qp_eva_1 Gratuidade Regimental']))

#Outubro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5028'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5028"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['out_qp_eva_1 Gratuidade Regimental']))

#Novembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5028'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5028"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['nov_qp_eva_1 Gratuidade Regimental']))

#Dezembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5028'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5028"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_QP['dez_qp_eva_1 Gratuidade Regimental']))

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL HORA ALUNO CONVENIO

#Janeiro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5021'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5021"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['jan_qp_ha_3 Convênio']))

#Fevereiro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5021'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5021"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['fev_qp_ha_3 Convênio']))

#Marco

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5021'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5021"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['mar_qp_ha_3 Convênio']))

#Abril

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5021'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5021"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['abr_qp_ha_3 Convênio']))


#Maio

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5021'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5021"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['mai_qp_ha_3 Convênio']))


#Junho

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5021'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5021"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['jun_qp_ha_3 Convênio']))

#Julho

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5021'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5021"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['jul_qp_ha_3 Convênio']))

#Agosto

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5021'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5021"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['ago_qp_ha_3 Convênio']))

#Setembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5021'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5021"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['set_qp_ha_3 Convênio']))

#Outubro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5021'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5021"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['out_qp_ha_3 Convênio']))

#Novembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5021'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5021"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['nov_qp_ha_3 Convênio']))


#Dezembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5021'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5021"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['dez_qp_ha_3 Convênio']))

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL HORA ALUNO BOLSA

#Janeiro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5029'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5029"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['jan_qp_ha_2 Gratuidade Não Regimental']))

#Fevereiro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5029'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5029"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['fev_qp_ha_2 Gratuidade Não Regimental']))

#Marco

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5029'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5029"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['mar_qp_ha_2 Gratuidade Não Regimental']))

#Abril

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5029'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5029"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['abr_qp_ha_2 Gratuidade Não Regimental']))

#Maio

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5029'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5029"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['mai_qp_ha_2 Gratuidade Não Regimental']))

#Junho

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5029'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5029"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['jun_qp_ha_2 Gratuidade Não Regimental']))

#Julho

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5029'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5029"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['jul_qp_ha_2 Gratuidade Não Regimental']))

#Agosto


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5029'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5029"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['ago_qp_ha_2 Gratuidade Não Regimental']))

#Setembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5029'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5029"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['set_qp_ha_2 Gratuidade Não Regimental']))

#Outubro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5029'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5029"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['out_qp_ha_2 Gratuidade Não Regimental']))

#Novembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5029'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5029"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['nov_qp_ha_2 Gratuidade Não Regimental']))

#Dezembro


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5029'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5029"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['dez_qp_ha_2 Gratuidade Não Regimental']))

# SENAI TAGUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL HORA ALUNO NAO GRATUITA

#Janeiro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5030'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5030"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['jan_qp_ha_9 Pago por Pessoa Fisica ou Empresa']))

#Fevereiro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5030'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5030"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['fev_qp_ha_9 Pago por Pessoa Fisica ou Empresa']))

#Marco

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5030'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5030"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['mar_qp_ha_9 Pago por Pessoa Fisica ou Empresa']))

#Abril

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5030'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5030"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['abr_qp_ha_9 Pago por Pessoa Fisica ou Empresa']))

#Maio

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5030'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5030"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['mai_qp_ha_9 Pago por Pessoa Fisica ou Empresa']))

#Junho

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5030'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5030"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['jun_qp_ha_9 Pago por Pessoa Fisica ou Empresa']))

#Julho

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5030'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5030"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['jul_qp_ha_9 Pago por Pessoa Fisica ou Empresa']))

#Agosto

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5030'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5030"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['ago_qp_ha_9 Pago por Pessoa Fisica ou Empresa']))


#Setembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5030'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5030"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['set_qp_ha_9 Pago por Pessoa Fisica ou Empresa']))

#Outubro


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5030'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5030"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['out_qp_ha_9 Pago por Pessoa Fisica ou Empresa']))

#Novembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5030'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5030"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['nov_qp_ha_9 Pago por Pessoa Fisica ou Empresa']))

#Dezembro

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5030'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5030"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_QP['dez_qp_ha_9 Pago por Pessoa Fisica ou Empresa']))

