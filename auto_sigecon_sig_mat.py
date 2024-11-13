
# Importação dos pacotes
from socket import timeout
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from obter_dados_sig_mat import obter_dados_por_tipo

from mat_sig import (
    sig_iniciacao_presencial,
    sig_iniciacao_distancia,
    sig_aprendizagem_presencial,
    sig_qualificacao_presencial,
    sig_aprendizagem_distancia,
    sig_qualificacao_distancia,
    sig_aperfeicoamento_presencial,
    sig_aperfeicoamento_distancia,
    sig_qualificacao_iti_presencial,
    sig_aprendizagem_tec,
    sig_tecnico_presencial,
    sig_tecnico_distancia,
    sig_tecnico_iti_presencial
)

dados = {
    'iniciacao': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('iniciacao', 'presencial')['matriculas'],
        },
        'distancia': {
            'matriculas': obter_dados_por_tipo('iniciacao', 'distancia')['matriculas'],
        }
    },
    'aprendizagem': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('aprendizagem', 'presencial')['matriculas'],
        },
        'distancia': {
            'matriculas': obter_dados_por_tipo('aprendizagem', 'distancia')['matriculas'],
        }
    },
    'qualificacao': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('qualificacao', 'presencial')['matriculas'],
        },
        'distancia': {
            'matriculas': obter_dados_por_tipo('qualificacao', 'distancia')['matriculas'],
        }
    },
    'aperfeicoamento': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('aperfeicoamento', 'presencial')['matriculas'],
        },
        'distancia': {
            'matriculas': obter_dados_por_tipo('aperfeicoamento', 'distancia')['matriculas'],
        }
    },
    'qualificacao_iti': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('qualificacao_iti', 'presencial')['matriculas'],
        }
    },
    'aprendizagem_tec': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('aprendizagem_tec', 'presencial')['matriculas'],
        }
    },
    'tecnico_nm': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('tecnico_nm', 'presencial')['matriculas'],
        },
        'distancia': {
            'matriculas': obter_dados_por_tipo('tecnico_nm', 'distancia')['matriculas'],
        }
    },
    'tecnico_nm_iti': {
        'presencial': {
            'matriculas': obter_dados_por_tipo('tecnico_nm_iti', 'presencial')['matriculas'],
        }
    }
}

DEFAULT_WAIT = 15

def esperar_elemento(nav, locator, condition=EC.visibility_of_element_located, timeout=DEFAULT_WAIT):
    return WebDriverWait(nav, timeout).until(condition(locator))

# Navegação para a página
url = 'http://sn-iis-02/SIGECON20/'
nav = webdriver.Firefox()
nav.get(url)

# Elemento Usuario
e_usuario = esperar_elemento(nav, (By.XPATH, '//*[@id="UserName"]'))
usuario = "matheus.reck"
e_usuario.send_keys(usuario)

# Elemento Senha
e_senha = esperar_elemento(nav, (By.XPATH, '//*[@id="Password"]'))
senha = "Vitoria2625!"
e_senha.send_keys(senha)

# Elemento Ano
e_ano = esperar_elemento(nav, (By.XPATH, '//*[@id="Ano"]'))
e_ano.click()
e_ano_2024 = esperar_elemento(nav, (By.XPATH, '//*[@id="Ano"]/option[2]'))
e_ano_2024.click()

# Elemento Entidade
e_entidade = esperar_elemento(nav, (By.XPATH, '//*[@id="Cod_Empresa"]'))
e_entidade.click()
e_entidade_senai = esperar_elemento(nav, (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/form/fieldset/div[4]/select/option[3]'))
e_entidade_senai.click()

# Elemento Entrar
e_entrar = esperar_elemento(nav, (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/form/fieldset/div[6]/input'))
e_entrar.click()

# Elemento unidade SENAI TAGUATINGA
e_uni_tag1 = esperar_elemento(nav, (By.PARTIAL_LINK_TEXT, 'Senai Sig'))
e_uni_tag1.click()

# Elemento CR INICIACAO PROFISSIONAL PRESENCIAL
e_cr_inici_prese = esperar_elemento(nav, (By.PARTIAL_LINK_TEXT, 'INICIACAO PROFISSIONAL PRESENCIAL'))
e_cr_inici_prese.click()

# Elemento FICHA DE PRODUÇÃO
e_ficha_prod = esperar_elemento(nav, (By.LINK_TEXT, 'Produção'))

nav.execute_script("arguments[0].scrollIntoView(true);", e_ficha_prod)
nav.execute_script("arguments[0].click();", e_ficha_prod)

# Elemento GRUPO DE META

e_grupo_meta = esperar_elemento(nav, (By.XPATH, "//a[@href='/http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030205/210?cd_centro_resp=30303010101&nm_unidade=SENAI%20SIG&nm_centro_resp=INICIACAO%20PROFISSIONAL%20PRESENCIAL&id_grupo=1&ds_grupo=Inicia%C3%A7%C3%A3o%20Profissional&fase=Realiza%C3%A7%C3%A3o']"))

nav.execute_script("arguments[0].scrollIntoView(true);", e_grupo_meta)
e_grupo_meta.click()

# SENAI sigA - 30303010101 - INICIACAO PROFISSIONAL PRESENCIAL

# MATRICULA BOLSA
nav.refresh()

em_bolsa_click = esperar_elemento(nav, (By.CSS_SELECTOR, "td:nth-child(4) > [id='4913'].indicador"))
em_bolsa_click.click()

em_bolsa_s = esperar_elemento(nav, (By.XPATH, "(//input[@type='text'])[8]"))
em_bolsa_s.send_keys(sig_iniciacao_presencial['jan_mat_bolsa'])
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

for i, (mes, campo_dado) in enumerate(meses):
    mat_bolsa_mes = esperar_elemento(nav, (By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='4913'].indicador"), timeout=10)
    mat_bolsa_mes.click()

    mat_bolsa_send = esperar_elemento(nav, (By.XPATH, "(//input[@type='text'])[8]"))

    chave_dado = f"{mes}_inicia_presen_mat_2 Gratuidade Não Regimental"
    mat_iniciacao_presencial_geral = dados['iniciacao']['presencial']['matriculas'].get(chave_dado, 0)

    mat_bolsa_send.send_keys(str(mat_iniciacao_presencial_geral))
    mat_bolsa_send.send_keys(Keys.ENTER)


############################################################   MATRICULA NAO GRATUITA ####################################################################################################

mem_ng_click = esperar_elemento(nav, (By.CSS_SELECTOR, "td:nth-child(4) > [id='4914'].indicador"))
mem_ng_click.click()

em_ng_s = esperar_elemento(nav,(By.XPATH, "(//input[@type='text'])[8]"))
em_ng_s.send_keys(sig_iniciacao_presencial['jan_mat_n_gratuita'])
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

for i, (mes, campo_dado) in enumerate(meses):
    
    mat_ng_mes = esperar_elemento(nav, (By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='4914'].indicador"), timeout=10)
    mat_ng_mes.click()

    mat_ng_send = esperar_elemento(nav, (By.XPATH, "(//input[@type='text'])[8]"))

    chave_dado = f"{mes}_inicia_presen_mat_9 Pago por Pessoa Fisica ou Empresa"
    mat_iniciacao_presencial_ng = dados['iniciacao']['presencial']['matriculas'].get(chave_dado, 0)

    mat_ng_send.send_keys(str(mat_iniciacao_presencial_ng))
    mat_ng_send.send_keys(Keys.ENTER)


#########################################  INICIAÇÃO PROFISSIONAL A DISTANCIA ########################################################################################################

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030205/253?cd_centro_resp=30303010201&nm_unidade=SENAI%20SIG&nm_centro_resp=INICIACAO%20PROFISSIONAL%20A%20DISTANCIA&id_grupo=1&ds_grupo=Inicia%C3%A7%C3%A3o%20Profissional&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

# SENAI sigUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA MATRICULA BOLSA ##################################################################################################

ipd_bolsa_mat_jan = esperar_elemento(nav, (By.CSS_SELECTOR, "td:nth-child(4) > [id='5277'].indicador"))
ipd_bolsa_mat_jan.click()

ipd_bolsa_mat_jan = esperar_elemento(nav, (By.XPATH, "(//input[@type='text'])[8]"))
ipd_bolsa_mat_jan.send_keys(sig_iniciacao_distancia['jan_mat_bolsa'])
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

    mat_ipd_bolsa_mes = esperar_elemento(nav, (By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5277'].indicador"), timeout=10)
    mat_ipd_bolsa_mes.click()

    mat_ipd_bolsa_mes = esperar_elemento(nav, (By.XPATH, "(//input[@type='text'])[8]"))
    

    chave_dado = f"{mes}_inicia_distan_mat_2 Gratuidade Não Regimental"
    mat_iniciacao_distancia_bolsa = dados['iniciacao']['distancia']['matriculas'].get(chave_dado, 0)

    mat_ipd_bolsa_mes.send_keys(str(mat_iniciacao_distancia_bolsa))
    mat_ipd_bolsa_mes.send_keys(Keys.ENTER)


# SENAI sigUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA MATRICULA NAO GRATUITA

ipd_ng_mat_jan = esperar_elemento(nav, (By.CSS_SELECTOR, "td:nth-child(4) > [id='5278'].indicador"))
ipd_ng_mat_jan.click()

ipd_ng_mat_jan = esperar_elemento(nav, (By.XPATH, "(//input[@type='text'])[8]"))
ipd_ng_mat_jan.send_keys(sig_iniciacao_distancia['jan_mat_n_gratuita'])
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

nav.refresh()

for i, (mes, campo_dado) in enumerate(meses):

    mat_ipd_ng_mes = esperar_elemento(nav, (By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5278'].indicador"), timeout=10)
    mat_ipd_ng_mes.click()

    mat_ipd_ng_mes = esperar_elemento(nav, (By.XPATH, "(//input[@type='text'])[8]"))

    chave_dado = f"{mes}_inicia_distan_mat_9 Pago por Pessoa Fisica ou Empresa"
    mat_iniciacao_distancia_ng = dados['iniciacao']['distancia']['matriculas'].get(chave_dado, 0)

    mat_ipd_ng_mes.send_keys(str(mat_iniciacao_distancia_ng))
    mat_ipd_ng_mes.send_keys(Keys.ENTER)


###################################################  Aprendizagem Industrial - Presencial #############################################################

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030205/307?cd_centro_resp=30303020101&nm_unidade=SENAI%20SIG&nm_centro_resp=APRENDIZAGEM%20INDUSTRIAL%20PRESENCIAL&id_grupo=2&ds_grupo=Aprendizagem%20Industrial&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])


# SENAI sigUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL MATRICULA NAO GRATUITA

app_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-tipo="1"]')))

app_ng_mat_jan.click()

app_ng_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

app_ng_mat_jan.send_keys(sig_aprendizagem_presencial['jan_mat_n_gratuita'])

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


app_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5443'].indicador")))
app_ng_mat.click()

nav.refresh()


for i, (mes, campo_dado) in enumerate(meses):

    app_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5443'].indicador")))
    app_ng_mat.click()


    app_ng_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

    chave_dado = f"{mes}_aprendi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"
    
    mat_aprendizagem_presencial_ng = dados['aprendizagem']['presencial']['matriculas'].get(chave_dado, 0)

    app_ng_mat.send_keys(str(mat_aprendizagem_presencial_ng))
    app_ng_mat.send_keys(Keys.ENTER)
    

# SENAI sigUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL MATRICULA REGIMENTAL

app_regimental_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5434'].indicador")))

app_regimental_mat_jan.click()

app_regimental_mat_jan = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

app_regimental_mat_jan.send_keys(sig_aprendizagem_presencial['jan_mat_regi'])

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


for i, (mes, campo_dado) in enumerate(meses):

    app_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5434'].indicador")))
    app_regimental_mat.click()

   
    app_regimental_mat = WebDriverWait(nav, 15).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))


    chave_dado = f"{mes}_aprendi_presen_mat_1 Gratuidade Regimental"
    
   
    mat_aprendizagem_presencial_regimental = dados['aprendizagem']['presencial']['matriculas'].get(chave_dado, 0)

    app_regimental_mat.send_keys(str(mat_aprendizagem_presencial_regimental))
    app_regimental_mat.send_keys(Keys.ENTER)


# SENAI sigA  - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030205/256?cd_centro_resp=30303020201&nm_unidade=SENAI%20SIG&nm_centro_resp=QUALIFICACAO%20PROFISSIONAL%20PRESENCIAL&id_grupo=3&ds_grupo=Qualifica%C3%A7%C3%A3o%20Industrial&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

# SENAI sigA  - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL

quali_bolsa_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5308'].indicador")))

quali_bolsa_mat_jan.click()

quali_bolsa_mat_jan.send_keys(sig_qualificacao_presencial['jan_mat_bolsa'])

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

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5308'].indicador")))
    qualifi_bolsa_mat.click()

    chave_dado = f"{mes}_qualifi_presen_mat_2 Gratuidade Não Regimental"
    
    mat_qualificacao_presencial_bolsa = dados['qualificacao']['presencial']['matriculas'].get(chave_dado, 0)

    qualifi_bolsa_mat.send_keys(str(mat_qualificacao_presencial_bolsa))
    qualifi_bolsa_mat.send_keys(Keys.ENTER)


    # SENAI sigUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL MATRICULA NAO GRATUITA

quali_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5309'].indicador")))

quali_ng_mat_jan.click()

quali_ng_mat_jan.send_keys(sig_qualificacao_presencial['jan_mat_n_gratuita'])

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

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5309'].indicador")))
    qualifi_ng_mat.click()

    chave_dado = f"{mes}_qualifi_presen_mat_9 Pago por Pessoa Fisica ou Empresa"

    mat_qualificacao_presencial_nao_gratuita = dados['qualificacao']['presencial']['matriculas'].get(chave_dado, 0)

    qualifi_ng_mat.send_keys(str(mat_qualificacao_presencial_nao_gratuita))
    qualifi_ng_mat.send_keys(Keys.ENTER)


# SENAI sigUATINGA - 30303020201 - QUALIFICACAO PROFISSIONAL PRESENCIAL MATRICULA Regimental

quali_regime_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5310'].indicador")))

quali_regime_mat_jan.click()

quali_regime_mat_jan.send_keys(sig_qualificacao_presencial['jan_mat_regi'])

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

for i, (mes, campo_dado) in enumerate(meses):

    quali_regime_mat_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5310'].indicador")))
    quali_regime_mat_mat.click()

    chave_dado = f"{mes}_qualifi_presen_mat_1 Gratuidade Regimental"
    
    mat_qualificacao_presencial_regimental = dados['qualificacao']['presencial']['matriculas'].get(chave_dado, 0)

    quali_regime_mat_mat.send_keys(str(mat_qualificacao_presencial_regimental))
    quali_regime_mat_mat.send_keys(Keys.ENTER)

# SENAI sigUATINGA - 30303020401 - QUALIFICACAO PROFISSIONAL SEMIPRESENCIAL - BOLSA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030205/254?cd_centro_resp=30303020401&nm_unidade=SENAI%20SIG&nm_centro_resp=QUALIFICACAO%20PROFISSIONAL%20SEMIPRESENCIAL&id_grupo=3&ds_grupo=Qualifica%C3%A7%C3%A3o%20Industrial&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()


qualifi_semi_bolsa_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5288'].indicador")))

qualifi_semi_bolsa_mat_jan.click()

qualifi_semi_bolsa_mat_jan.send_keys(sig_qualificacao_distancia['jan_mat_bolsa'])

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

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5288'].indicador")))
    qualifi_semi_bolsa_mat.click()

    chave_dado = f"{mes}_qualifi_distan_mat_2 Gratuidade Não Regimental"
    
    mat_qualifica_semi_bolsa = dados['qualificacao']['distancia']['matriculas'].get(chave_dado, 0)

    qualifi_semi_bolsa_mat.send_keys(str(mat_qualifica_semi_bolsa))
    qualifi_semi_bolsa_mat.send_keys(Keys.ENTER)

# SENAI sigUATINGA - 30303020401 - QUALIFICACAO PROFISSIONAL SEMIPRESENCIAL - NAO GRATUITA

qualifi_semi_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5289'].indicador")))

qualifi_semi_ng_mat_jan.click()

qualifi_semi_ng_mat_jan.send_keys(sig_qualificacao_distancia['jan_mat_n_gratuita'])

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

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5289'].indicador")))
    qualifi_semi_ng_mat.click()

    chave_dado = f"{mes}_qualifi_distan_mat_9 Pago por Pessoa Fisica ou Empresa"
    
    mat_qualifica_semi_ng = dados['qualificacao']['distancia']['matriculas'].get(chave_dado, 0)

    qualifi_semi_ng_mat.send_keys(str(mat_qualifica_semi_ng))
    qualifi_semi_ng_mat.send_keys(Keys.ENTER)

# SENAI sigUATINGA - 30303020401 - QUALIFICACAO PROFISSIONAL SEMIPRESENCIAL - REGIMENTAL

qualifi_semi_regimental_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5290'].indicador")))

qualifi_semi_regimental_mat_jan.click()

qualifi_semi_regimental_mat_jan.send_keys(sig_qualificacao_distancia['jan_mat_regi'])

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

for i, (mes, campo_dado) in enumerate(meses):

    qualifi_semi_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5290'].indicador")))
    qualifi_semi_regimental_mat.click()

    chave_dado = f"{mes}_qualifi_distan_mat_1 Gratuidade Regimental"
    
    mat_qualifica_semi_regimental = dados['qualificacao']['distancia']['matriculas'].get(chave_dado, 0)

    qualifi_semi_regimental_mat.send_keys(str(mat_qualifica_semi_regimental))
    qualifi_semi_regimental_mat.send_keys(Keys.ENTER)


# SENAI sigUATINGA - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - BOLSA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030205/257?cd_centro_resp=30303020501&nm_unidade=SENAI%20SIG&nm_centro_resp=APERF%2FESPECIALIZ%20PROFISSIONAL%20PRESENCIAL&id_grupo=5&ds_grupo=Aperfei%C3%A7oamento%20Profissional&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

aper_prese_bolsa_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5320'].indicador")))

aper_prese_bolsa_mat_jan.click()

aper_prese_bolsa_mat_jan.send_keys(sig_aperfeicoamento_presencial['jan_mat_bolsa'])

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


for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5320'].indicador")))
    aper_prese_bolsa_mat.click()

    chave_dado = f"{mes}_aperfei_presen_mat_2 Gratuidade Não Regimental"
    
    mat_aper_prese_bolsa = dados['aperfeicoamento']['presencial']['matriculas'].get(chave_dado, 0)

    aper_prese_bolsa_mat.send_keys(str(mat_aper_prese_bolsa))
    aper_prese_bolsa_mat.send_keys(Keys.ENTER)


# SENAI sigUATINGA - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - NAO GRATUITA


aper_prese_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5321'].indicador")))

aper_prese_ng_mat_jan.click()

aper_prese_ng_mat_jan.send_keys(sig_aperfeicoamento_presencial['jan_mat_n_gratuita'])

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

for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5321'].indicador")))
    aper_prese_ng_mat.click()

    chave_dado = f"{mes}_aperfei_presen_mat_9 Pago por Pessoa Fisica ou Empresa"
    
    mat_aper_prese_ng = dados['aperfeicoamento']['presencial']['matriculas'].get(chave_dado, 0)

    aper_prese_ng_mat.send_keys(str(mat_aper_prese_ng))
    aper_prese_ng_mat.send_keys(Keys.ENTER)


# SENAI sigUATINGA - 30303020501 - APERF/ESPECIALIZ PROFISSIONAL PRESENCIAL - REGIMENTAL


aper_prese_regimental_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5322'].indicador")))

aper_prese_regimental_mat_jan.click()

aper_prese_regimental_mat_jan.send_keys(sig_aperfeicoamento_presencial['jan_mat_regi'])

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

for i, (mes, campo_dado) in enumerate(meses):

    aper_prese_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5322'].indicador")))
    aper_prese_regimental_mat.click()

    chave_dado = f"{mes}_aperfei_presen_mat_1 Gratuidade Regimental"
    
    mat_aper_prese_regimental = dados['aperfeicoamento']['presencial']['matriculas'].get(chave_dado, 0)

    aper_prese_regimental_mat.send_keys(str(mat_aper_prese_regimental))
    aper_prese_regimental_mat.send_keys(Keys.ENTER)

# SENAI sigUATINGA - 30303020601 - APERF/ESPECIALI PROFISSIONAL A DISTANCIA BOLSA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030205/252?cd_centro_resp=30303020601&nm_unidade=SENAI%20SIG&nm_centro_resp=APERF%2FESPECIALI%20PROFISSIONAL%20A%20DISTANCIA&id_grupo=5&ds_grupo=Aperfei%C3%A7oamento%20Profissional&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

aper_distan_bolsa_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5269'].indicador")))

aper_distan_bolsa_mat_jan.click()

aper_distan_bolsa_mat_jan.send_keys(sig_aperfeicoamento_distancia['jan_mat_bolsa'])

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

for i, (mes, campo_dado) in enumerate(meses):

    aper_dista_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5269'].indicador")))
    aper_dista_bolsa_mat.click()

    chave_dado = f"{mes}_aperfei_distan_mat_2 Gratuidade Não Regimental"
    
    mat_aper_distan_bolsa = dados['aperfeicoamento']['distancia']['matriculas'].get(chave_dado, 0)

    aper_dista_bolsa_mat.send_keys(str(mat_aper_distan_bolsa))
    aper_dista_bolsa_mat.send_keys(Keys.ENTER)

# SENAI sigUATINGA - 30303020601 - APERF/ESPECIALI PROFISSIONAL A DISTANCIA NAO GRATUITA

aper_distan_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5270'].indicador")))

aper_distan_ng_mat_jan.click()

aper_distan_ng_mat_jan.send_keys(sig_aperfeicoamento_distancia['jan_mat_n_gratuita'])

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

for i, (mes, campo_dado) in enumerate(meses):

    aper_dista_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5270'].indicador")))
    aper_dista_ng_mat.click()

    chave_dado = f"{mes}_aperfei_distan_mat_9 Pago por Pessoa Fisica ou Empresa"
    
    mat_aper_distan_ng = dados['aperfeicoamento']['distancia']['matriculas'].get(chave_dado, 0)

    aper_dista_ng_mat.send_keys(str(mat_aper_distan_ng))
    aper_dista_ng_mat.send_keys(Keys.ENTER)


# SENAI sigUATINGA - 30303040101 - APREND. IND. TEC. NIVEL MEDIO PRESENCIAL - NAO GRATUITA


from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030205/308?cd_centro_resp=30303040101&nm_unidade=SENAI%20SIG&nm_centro_resp=APREND.%20IND.%20TEC.%20NIVEL%20MEDIO%20PRESENCIAL&id_grupo=11&ds_grupo=Aprendizagem%20Industrial%20T%C3%A9cnico%20de%20N%C3%ADvel%20M%C3%A9dio&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

aprendi_tec_presencial_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5441'].indicador")))

aprendi_tec_presencial_ng_mat_jan.click()

aprendi_tec_presencial_ng_mat_jan.send_keys(sig_aprendizagem_tec['jan_mat_n_gratuita'])

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

for i, (mes, campo_dado) in enumerate(meses):

    aprendi_tec_presencial_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5441'].indicador")))
    aprendi_tec_presencial_ng_mat.click()

    chave_dado = f"{mes}_aprendi_tec_presen_mat_9 Pago por Pessoa Fisica ou Empresa"
    
    mat_aprendi_tec_presencial_ng = dados['aprendizagem_tec']['presencial']['matriculas'].get(chave_dado, 0)

    aprendi_tec_presencial_ng_mat.send_keys(str(mat_aprendi_tec_presencial_ng))
    aprendi_tec_presencial_ng_mat.send_keys(Keys.ENTER)


# SENAI sigUATINGA - 30303040101 - APREND. IND. TEC. NIVEL MEDIO PRESENCIAL - REGIMENTAL

aprendi_tec_presencial_regimental_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5442'].indicador")))

aprendi_tec_presencial_regimental_mat_jan.click()

aprendi_tec_presencial_regimental_mat_jan.send_keys(sig_aprendizagem_tec['jan_mat_regi'])

aprendi_tec_presencial_regimental_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_aprendi_tec_presen_mat_1 Gratuidade Regimental"),
    ("mar", "mar_aprendi_tec_presen_mat_1 Gratuidade Regimental"),
    ("abr", "abr_aprendi_tec_presen_mat_1 Gratuidade Regimental"),
    ("mai", "mai_aprendi_tec_presen_mat_1 Gratuidade Regimental"),
    ("jun", "jun_aprendi_tec_presen_mat_1 Gratuidade Regimental"),
    ("jul", "jul_aprendi_tec_presen_mat_1 Gratuidade Regimental"),
    ("ago", "ago_aprendi_tec_presen_mat_1 Gratuidade Regimental"),
    ("set", "set_aprendi_tec_presen_mat_1 Gratuidade Regimental"),
    ("out", "out_aprendi_tec_presen_mat_1 Gratuidade Regimental"),
    ("nov", "nov_aprendi_tec_presen_mat_1 Gratuidade Regimental"),
    ("dez", "dez_aprendi_tec_presen_mat_1 Gratuidade Regimental")
]


for i, (mes, campo_dado) in enumerate(meses):

    aprendi_tec_presencial_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5442'].indicador")))
    aprendi_tec_presencial_regimental_mat.click()

    chave_dado = f"{mes}_aprendi_tec_presen_mat_1 Gratuidade Regimental"
    
    mat_aprendi_tec_presencial_regimental = dados['aprendizagem_tec']['presencial']['matriculas'].get(chave_dado, 0)

    aprendi_tec_presencial_regimental_mat.send_keys(str(mat_aprendi_tec_presencial_regimental))
    aprendi_tec_presencial_regimental_mat.send_keys(Keys.ENTER)

# SENAI sigUATINGA - 30303040201 - TECNICO DE NIVEL MEDIO PRESENCIAL - NAO GRATUITA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030205/255?cd_centro_resp=30303040201&nm_unidade=SENAI%20SIG&nm_centro_resp=TECNICO%20DE%20NIVEL%20MEDIO%20PRESENCIAL&id_grupo=4&ds_grupo=T%C3%A9cnico%20de%20N%C3%ADvel%20M%C3%A9dio&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

tec_presencial_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5297'].indicador")))

tec_presencial_ng_mat_jan.click()

tec_presencial_ng_mat_jan.send_keys(sig_tecnico_presencial['jan_mat_n_gratuita'])

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

for i, (mes, campo_dado) in enumerate(meses):

    tec_presencial_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5297'].indicador")))
    tec_presencial_ng_mat.click()

    chave_dado = f"{mes}_tecni_presen_mat_9 Pago por Pessoa Fisica ou Empresa"
    
    mat_tec_presencial_ng = dados['tecnico_nm']['presencial']['matriculas'].get(chave_dado, 0)

    tec_presencial_ng_mat.send_keys(str(mat_tec_presencial_ng))
    tec_presencial_ng_mat.send_keys(Keys.ENTER)

# SENAI sigUATINGA - 30303040201 - TECNICO DE NIVEL MEDIO PRESENCIAL - REGIMENTAL

tec_presencial_regimental_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5298'].indicador")))

tec_presencial_regimental_mat_jan.click()

tec_presencial_regimental_mat_jan.send_keys(sig_tecnico_presencial['jan_mat_regi'])

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


for i, (mes, campo_dado) in enumerate(meses):

    tec_presencial_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5298'].indicador")))
    tec_presencial_regimental_mat.click()

   
    chave_dado = f"{mes}_tecni_presen_mat_1 Gratuidade Regimental"
    
    mat_tec_presencial_regimental = dados['tecnico_nm']['presencial']['matriculas'].get(chave_dado, 0)

    tec_presencial_regimental_mat.send_keys(str(mat_tec_presencial_regimental))
    tec_presencial_regimental_mat.send_keys(Keys.ENTER)


# SENAI sigUATINGA - 30303040401 - TECNICO DE NIVEL MEDIO SEMIPRESENCIAL NAO GRATUITA

from selenium import webdriver

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030205/258?cd_centro_resp=30303040401&nm_unidade=SENAI%20SIG&nm_centro_resp=TECNICO%20DE%20NIVEL%20MEDIO%20SEMIPRESENCIAL&id_grupo=4&ds_grupo=T%C3%A9cnico%20de%20N%C3%ADvel%20M%C3%A9dio&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()

nav.switch_to.window(nav.window_handles[0])

nav.refresh()

tec_distancia_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5329'].indicador")))

tec_distancia_ng_mat_jan.click()

tec_distancia_ng_mat_jan.send_keys(sig_tecnico_distancia['jan_mat_n_gratuita'])

tec_distancia_ng_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_tecni_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_tecni_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_tecni_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_tecni_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_tecni_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_tecni_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_tecni_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_tecni_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_tecni_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_tecni_distan_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_tecni_distan_mat_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_distancia_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5329'].indicador")))
    tec_distancia_ng_mat.click()

    chave_dado = f"{mes}_tecni_distan_mat_9 Pago por Pessoa Fisica ou Empresa"
    
    mat_tec_distancia_ng = dados['tecnico_nm']['distancia']['matriculas'].get(chave_dado, 0)

    tec_distancia_ng_mat.send_keys(str(mat_tec_distancia_ng))
    tec_distancia_ng_mat.send_keys(Keys.ENTER)

# SENAI sigUATINGA - 30303040401 - TECNICO DE NIVEL MEDIO SEMIPRESENCIAL REGIMENTAL

tec_distancia_regimental_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5330'].indicador")))

tec_distancia_regimental_mat_jan.click()

tec_distancia_regimental_mat_jan.send_keys(sig_tecnico_distancia['jan_mat_regi'])

tec_distancia_regimental_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_tecni_distan_mat_1 Gratuidade Regimental"),
    ("mar", "mar_tecni_distan_mat_1 Gratuidade Regimental"),
    ("abr", "abr_tecni_distan_mat_1 Gratuidade Regimental"),
    ("mai", "mai_tecni_distan_mat_1 Gratuidade Regimental"),
    ("jun", "jun_tecni_distan_mat_1 Gratuidade Regimental"),
    ("jul", "jul_tecni_distan_mat_1 Gratuidade Regimental"),
    ("ago", "ago_tecni_distan_mat_1 Gratuidade Regimental"),
    ("set", "set_tecni_distan_mat_1 Gratuidade Regimental"),
    ("out", "out_tecni_distan_mat_1 Gratuidade Regimental"),
    ("nov", "nov_tecni_distan_mat_1 Gratuidade Regimental"),
    ("dez", "dez_tecni_distan_mat_1 Gratuidade Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_distancia_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5330'].indicador")))
    tec_distancia_regimental_mat.click()

    chave_dado = f"{mes}_tecni_distan_mat_1 Gratuidade Regimental"
    
    mat_tec_distancia_regimental = dados['tecnico_nm']['distancia']['matriculas'].get(chave_dado, 0)

    tec_distancia_regimental_mat.send_keys(str(mat_tec_distancia_regimental))
    tec_distancia_regimental_mat.send_keys(Keys.ENTER)

# SENAI sigUATINGA - 30303040501 - TECN DE NIV MED ITINERARIOS PRESENCIAL BOLSA

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030205/309?cd_centro_resp=30303040501&nm_unidade=SENAI%20SIG&nm_centro_resp=TECN%20DE%20NIV%20MED%20ITINERARIOS%20PRESENCIAL&id_grupo=4&ds_grupo=T%C3%A9cnico%20de%20N%C3%ADvel%20M%C3%A9dio&fase=Realiza%C3%A7%C3%A3o')")

nav.switch_to.window(nav.window_handles[-1])

nav.switch_to.window(janela_atual)
nav.close()


nav.switch_to.window(nav.window_handles[0])

nav.refresh()

tec_iti_presencial_bolsa_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5449'].indicador")))

tec_iti_presencial_bolsa_mat_jan.click()

tec_iti_presencial_bolsa_mat_jan.send_keys(sig_tecnico_iti_presencial['jan_mat_bolsa'])

tec_iti_presencial_bolsa_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_tecni_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("mar", "mar_tecni_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("abr", "abr_tecni_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("mai", "mai_tecni_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("jun", "jun_tecni_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("jul", "jul_tecni_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("ago", "ago_tecni_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("set", "set_tecni_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("out", "out_tecni_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("nov", "nov_tecni_iti_presen_mat_2 Gratuidade Não Regimental"),
    ("dez", "dez_tecni_iti_presen_mat_2 Gratuidade Não Regimental")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_iti_presencial_bolsa_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5449'].indicador")))
    tec_iti_presencial_bolsa_mat.click()
 
    chave_dado = f"{mes}_tecni_iti_presen_mat_2 Gratuidade Não Regimental"
    
    mat_tec_iti_presencial_bolsa = dados['tecnico_nm_iti']['presencial']['matriculas'].get(chave_dado, 0)

    tec_iti_presencial_bolsa_mat.send_keys(str(mat_tec_iti_presencial_bolsa))
    tec_iti_presencial_bolsa_mat.send_keys(Keys.ENTER)

# SENAI sigUATINGA - 30303040501 - TECN DE NIV MED ITINERARIOS PRESENCIAL REGIMENTAL


tec_iti_presencial_regimental_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5450'].indicador")))

tec_iti_presencial_regimental_mat_jan.click()

tec_iti_presencial_regimental_mat_jan.send_keys(sig_tecnico_iti_presencial['jan_mat_regi'])

tec_iti_presencial_regimental_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

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

for i, (mes, campo_dado) in enumerate(meses):

    tec_iti_presencial_regimental_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5450'].indicador")))
    tec_iti_presencial_regimental_mat.click()
 
    chave_dado = f"{mes}_tecni_iti_presen_mat_1 Gratuidade Regimental"
    
    mat_tec_iti_presencial_regimental = dados['tecnico_nm_iti']['presencial']['matriculas'].get(chave_dado, 0)

    tec_iti_presencial_regimental_mat.send_keys(str(mat_tec_iti_presencial_regimental))
    tec_iti_presencial_regimental_mat.send_keys(Keys.ENTER)


# SENAI sigUATINGA - 30303040501 - TECN DE NIV MED ITINERARIOS PRESENCIAL NAO GRATUITA


tec_iti_presencial_ng_mat_jan = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5490'].indicador")))

tec_iti_presencial_ng_mat_jan.click()

tec_iti_presencial_ng_mat_jan.send_keys(sig_tecnico_iti_presencial['jan_mat_regi'])

tec_iti_presencial_ng_mat_jan.send_keys(Keys.ENTER)

nav.refresh()

meses = [
    ("fev", "fev_tecni_iti_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mar", "mar_tecni_iti_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("abr", "abr_tecni_iti_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("mai", "mai_tecni_iti_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jun", "jun_tecni_iti_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("jul", "jul_tecni_iti_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("ago", "ago_tecni_iti_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("set", "set_tecni_iti_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("out", "out_tecni_iti_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("nov", "nov_tecni_iti_presen_mat_9 Pago por Pessoa Fisica ou Empresa"),
    ("dez", "dez_tecni_iti_presen_mat_9 Pago por Pessoa Fisica ou Empresa")
]

for i, (mes, campo_dado) in enumerate(meses):

    tec_iti_presencial_ng_mat = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5490'].indicador")))
    tec_iti_presencial_ng_mat.click()
 
    chave_dado = f"{mes}_tecni_iti_presen_mat_9 Pago por Pessoa Fisica ou Empresa"
    
    mat_tec_iti_presencial_ng = dados['tecnico_nm_iti']['presencial']['matriculas'].get(chave_dado, 0)

    tec_iti_presencial_ng_mat.send_keys(str(mat_tec_iti_presencial_ng))
    tec_iti_presencial_ng_mat.send_keys(Keys.ENTER)    