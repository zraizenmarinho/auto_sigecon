# Importação dos pacotes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

#SENAI TAGUATINGA INICIAÇÃO PROFISSIONAL PRESENCIAL

from si_janeiro_m_c_e import obter_matriculas_por_tipo_jan #
from si_janeiro_m_c_e import obter_matriculas_por_tipo #
from si_janeiro import obter_hora_por_tipo
from si_janeiro_m_c_e import obter_concluintes_por_tipo #
from si_janeiro_m_c_e import obter_evasao_por_tipo #

mat_jan = obter_matriculas_por_tipo_jan('si_jan.xlsx')
mat = obter_matriculas_por_tipo('si_jan.xlsx')
ha = obter_hora_por_tipo('si_jan.xlsx')
con = obter_concluintes_por_tipo('si_jan.xlsx')
eva = obter_evasao_por_tipo('si_jan.xlsx')


#SENAI TAGUATINGA INICIAÇÃO PROFISSIONAL A DISTANCIA

from si_janeiro_m_c_e import obter_matriculas_IPD_TAG_jan #
from si_janeiro_m_c_e import obter_matriculas_IPD_TAG #
from si_janeiro import obter_hora_IPD_TAG 
from si_janeiro_m_c_e import obter_concluintes_IPD_TAG #
from si_janeiro_m_c_e import obter_evasao_IPD_TAG #

mat_jan_IPD = obter_matriculas_IPD_TAG_jan('si_jan.xlsx')
mat_IPD = obter_matriculas_IPD_TAG('si_jan.xlsx')
ha_IPD = obter_hora_IPD_TAG('si_jan.xlsx')
con_IPD = obter_concluintes_IPD_TAG('si_jan.xlsx')
eva_IPD = obter_evasao_IPD_TAG('si_jan.xlsx')

#SENAI TAGUATINGA APRENDIZAGEM INDUSTRIAL PRESENCIAL

from si_janeiro_m_c_e import obter_matriculas_AP_TAG_jan #
from si_janeiro_m_c_e import obter_matriculas_AP_TAG #
from si_janeiro import obter_hora_AP_TAG
from si_janeiro_m_c_e import obter_concluintes_AP_TAG #
from si_janeiro_m_c_e import obter_evasao_AP_TAG #

mat_jan_AP = obter_matriculas_AP_TAG_jan('si_jan.xlsx')
mat_AP = obter_matriculas_AP_TAG('si_jan.xlsx')
ha_AP = obter_hora_AP_TAG('si_jan.xlsx')
con_AP = obter_concluintes_AP_TAG('si_jan.xlsx')
eva_AP = obter_evasao_AP_TAG('si_jan.xlsx')



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
senha = "Ps4753159!"
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

e_uni_tag1 = WebDriverWait(nav, 10).until(EC.visibility_of_element_located(
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

# SENAI TAGUATINGA - 30303010101 - INICIACAO PROFISSIONAL PRESENCIAL MATRICULA BOLSA

################################################################   MATRICULA BOLSA JANEIRO ########################################################################################################

em_bolsa_click = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-tipo="1"]')))

em_bolsa_click.click()

em_bolsa_s = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

em_bolsa_s.send_keys(mat_jan['jan_ip_mat_bolsa'])

em_bolsa_s.send_keys(Keys.ENTER)

############################################################   Matricula Bolsa - Fevereiro ########################################################################################################

mat_bolsa_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5113'].indicador")))

mat_bolsa_fev.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5113"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat['fev_ip_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################   MATRICULA BOLSA MARRÇO ########################################################################################################

mat_bolsa_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5113'].indicador")))

mat_bolsa_mar.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5113"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat['mar_ip_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################   Matricula Bolsa - Abril ########################################################################################################


mat_bolsa_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5113'].indicador")))

mat_bolsa_abr.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5113"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat['abr_ip_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################   Matricula Bolsa - Maio ########################################################################################################

mat_bolsa_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5113'].indicador")))

mat_bolsa_mai.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5113"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat['mai_ip_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################   Matricula Bolsa - Junho ########################################################################################################

mat_bolsa_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5113'].indicador")))

mat_bolsa_jun.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5113"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat['jun_ip_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################   Matricula Bolsa - Julho ########################################################################################################

mat_bolsa_jul = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5113'].indicador")))

mat_bolsa_jul.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5113"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat['jul_ip_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################   Matricula Bolsa - Agosto ########################################################################################################

mat_bolsa_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5113'].indicador")))

mat_bolsa_ago.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5113"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat['ago_ip_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER) 

############################################################   Matricula Bolsa - Setembro ######################################################################################################## 

mat_bolsa_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5113'].indicador")))

mat_bolsa_set.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5113"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat['set_ip_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER) 

############################################################   Matricula Bolsa - Outubro ########################################################################################################

mat_bolsa_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5113'].indicador")))

mat_bolsa_out.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5113"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat['out_ip_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################   Matricula Bolsa - Novembro ########################################################################################################

mat_bolsa_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5113'].indicador")))

mat_bolsa_nov.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5113"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat['nov_ip_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################   Matricula Bolsa - Dezembro ########################################################################################################

mat_bolsa_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5113'].indicador")))

mat_bolsa_dez.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5113"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat['dez_ip_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010101 - INICIACAO PROFISSIONAL PRESENCIAL MATRICULA NÃO GRATUITA

############################################################   Matricula Não Gratuita - Janeiro ####################################################################################################

mat_n_g_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5114'].indicador")))

mat_n_g_jan.click()

mat_n_g_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5114"
)))

mat_n_g_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_g_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_g_send.send_keys(str(mat_jan['jan_ip_mat_n_gratuita']))

mat_n_g_send.send_keys(Keys.ENTER)

############################################################   Matricula Não Gratuita - Fevereiro ##################################################################################################

mat_n_g_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5114'].indicador")))

mat_n_g_fev.click()

mat_n_g_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5114"
)))

mat_n_g_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_g_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_g_send.send_keys(str(mat['fev_ip_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_g_send.send_keys(Keys.ENTER)

############################################################   Matricula Não Gratuita - Março ##################################################################################################

mat_n_g_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5114'].indicador")))

mat_n_g_mar.click()

mat_n_g_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5114"
)))

mat_n_g_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_g_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_g_send.send_keys(str(mat['mar_ip_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_g_send.send_keys(Keys.ENTER)


############################################################   Matricula Não Gratuita - Abril ##################################################################################################

mat_n_g_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5114'].indicador")))

mat_n_g_abr.click()

mat_n_g_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5114"
)))

mat_n_g_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_g_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_g_send.send_keys(str(mat['abr_ip_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_g_send.send_keys(Keys.ENTER)

############################################################   Matricula Não Gratuita - Maio ##################################################################################################

mat_n_g_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5114'].indicador")))

mat_n_g_mai.click()

mat_n_g_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5114"
)))

mat_n_g_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_g_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_g_send.send_keys(str(mat['mai_ip_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_g_send.send_keys(Keys.ENTER)


############################################################   Matricula Não Gratuita - Junho ##################################################################################################

mat_n_g_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5114'].indicador")))

mat_n_g_jun.click()

mat_n_g_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5114"
)))

mat_n_g_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_g_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_g_send.send_keys(str(mat['jun_ip_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_g_send.send_keys(Keys.ENTER)

############################################################   Matricula Não Gratuita - Julho ##################################################################################################

mat_n_g_jul = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5114'].indicador")))

mat_n_g_jul.click()

mat_n_g_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5114"
)))

mat_n_g_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_g_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_g_send.send_keys(str(mat['jul_ip_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_g_send.send_keys(Keys.ENTER)

############################################################   Matricula Não Gratuita - Agosto ##################################################################################################

mat_n_g_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5114'].indicador")))

mat_n_g_ago.click()

mat_n_g_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5114"
)))

mat_n_g_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_g_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_g_send.send_keys(str(mat['ago_ip_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_g_send.send_keys(Keys.ENTER)

############################################################   Matricula Não Gratuita - Setembro ##################################################################################################

mat_n_g_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5114'].indicador")))

mat_n_g_set.click()

mat_n_g_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5114"
)))

mat_n_g_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_g_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_g_send.send_keys(str(mat['set_ip_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_g_send.send_keys(Keys.ENTER)

############################################################   Matricula Não Gratuita - Outubro ##################################################################################################

mat_n_g_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5114'].indicador")))

mat_n_g_out.click()

mat_n_g_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5114"
)))

mat_n_g_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_g_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_g_send.send_keys(str(mat['out_ip_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_g_send.send_keys(Keys.ENTER)

############################################################   Matricula Não Gratuita - Novembro ##################################################################################################

mat_n_g_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5114'].indicador")))

mat_n_g_nov.click()

mat_n_g_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5114"
)))

mat_n_g_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_g_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_g_send.send_keys(str(mat['nov_ip_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_g_send.send_keys(Keys.ENTER)

############################################################   Matricula Não Gratuita - Dezembro ##################################################################################################

mat_n_g_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5114'].indicador")))

mat_n_g_dez.click()

mat_n_g_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5114"
)))

mat_n_g_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_g_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_g_send.send_keys(str(mat['dez_ip_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_g_send.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010101 - INICIACAO PROFISSINAL PRESENCIAL CONCLUINTE BOLSA

############################################################   Concluinte Bolsa - Janeiro ##################################################################################################

conc_bolsa_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5107'].indicador")))

conc_bolsa_jan.click()

con_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5107"
)))

conc_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_bolsa_send.send_keys(str(con['jan_ip_con_2 Gratuidade Não Regimental']))

conc_bolsa_send.send_keys(Keys.ENTER)

############################################################   Concluinte Bolsa - Fevereiro ##################################################################################################

conc_bolsa_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5107'].indicador")))

conc_bolsa_fev.click()

con_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5107"
)))

conc_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_bolsa_send.send_keys(str(con['fev_ip_con_2 Gratuidade Não Regimental']))

conc_bolsa_send.send_keys(Keys.ENTER)

############################################################   Concluinte Bolsa - Março ##################################################################################################

conc_bolsa_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5107'].indicador")))

conc_bolsa_mar.click()

con_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5107"
)))

conc_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_bolsa_send.send_keys(str(con['mar_ip_con_2 Gratuidade Não Regimental']))

conc_bolsa_send.send_keys(Keys.ENTER)

############################################################   Concluinte Bolsa - Abril ##################################################################################################

conc_bolsa_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5107'].indicador")))

conc_bolsa_abr.click()

con_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5107"
)))

conc_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_bolsa_send.send_keys(str(con['abr_ip_con_2 Gratuidade Não Regimental']))

conc_bolsa_send.send_keys(Keys.ENTER)

############################################################   Concluinte Bolsa - Maio ##################################################################################################

conc_bolsa_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5107'].indicador")))

conc_bolsa_mai.click()

con_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5107"
)))

conc_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_bolsa_send.send_keys(str(con['mai_ip_con_2 Gratuidade Não Regimental']))

conc_bolsa_send.send_keys(Keys.ENTER)

############################################################   Concluinte Bolsa - Junho ##################################################################################################

conc_bolsa_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5107'].indicador")))

conc_bolsa_jun.click()

con_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5107"
)))

conc_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_bolsa_send.send_keys(str(con['jun_ip_con_2 Gratuidade Não Regimental']))

conc_bolsa_send.send_keys(Keys.ENTER)

############################################################   Concluinte Bolsa - Julho ##################################################################################################

conc_bolsa_jul = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5107'].indicador")))

conc_bolsa_jul.click()

con_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5107"
)))

conc_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_bolsa_send.send_keys(str(con['jul_ip_con_2 Gratuidade Não Regimental']))

conc_bolsa_send.send_keys(Keys.ENTER)

############################################################   Concluinte Bolsa - Agosto ##################################################################################################

conc_bolsa_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5107'].indicador")))

conc_bolsa_ago.click()

con_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5107"
)))

conc_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_bolsa_send.send_keys(str(con['ago_ip_con_2 Gratuidade Não Regimental']))

conc_bolsa_send.send_keys(Keys.ENTER)

############################################################   Concluinte Bolsa - Setembro ##################################################################################################

conc_bolsa_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5107'].indicador")))

conc_bolsa_set.click()

con_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5107"
)))

conc_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_bolsa_send.send_keys(str(con['set_ip_con_2 Gratuidade Não Regimental']))

conc_bolsa_send.send_keys(Keys.ENTER)

############################################################   Concluinte Bolsa - Outubro ##################################################################################################

conc_bolsa_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5107'].indicador")))

conc_bolsa_out.click()

con_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5107"
)))

conc_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_bolsa_send.send_keys(str(con['out_ip_con_2 Gratuidade Não Regimental']))

conc_bolsa_send.send_keys(Keys.ENTER)

############################################################   Concluinte Bolsa - Novembro ##################################################################################################

conc_bolsa_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5107'].indicador")))

conc_bolsa_nov.click()

con_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5107"
)))

conc_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_bolsa_send.send_keys(str(con['nov_ip_con_2 Gratuidade Não Regimental']))

conc_bolsa_send.send_keys(Keys.ENTER)

############################################################   Concluinte Bolsa - Dezembro ##################################################################################################

conc_bolsa_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5107'].indicador")))

conc_bolsa_dez.click()

con_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5107"
)))

conc_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_bolsa_send.send_keys(str(con['dez_ip_con_2 Gratuidade Não Regimental']))

conc_bolsa_send.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010101 - INICIACAO PROFISSINAL PRESENCIAL CONCLUINTE NAO GRATUITA

############################################################   Concluinte Não Gratuita - Janeiro ####################################################################################################

conc_n_g_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5108'].indicador")))

conc_n_g_jan.click()

conc_n_g_jan_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5108"
)))

conc_n_g_jan_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_n_g_jan_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_n_g_jan_send.send_keys(str(con['jan_ip_con_9 Pago por Pessoa Fisica ou Empresa']))

conc_n_g_jan_send.send_keys(Keys.ENTER)

############################################################   Concluinte Não Gratuita - Fevereiro ###########################################################################################################

conc_n_g_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5108'].indicador")))

conc_n_g_fev.click()

conc_n_g_fev_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5108"
)))

conc_n_g_fev_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_n_g_fev_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_n_g_fev_send.send_keys(str(con['fev_ip_con_9 Pago por Pessoa Fisica ou Empresa']))

conc_n_g_fev_send.send_keys(Keys.ENTER)

############################################################   Concluinte Não Gratuita - Março ###########################################################################################################

conc_n_g_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5108'].indicador")))

conc_n_g_mar.click()

conc_n_g_mar_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5108"
)))

conc_n_g_mar_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_n_g_mar_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_n_g_mar_send.send_keys(str(con['mar_ip_con_9 Pago por Pessoa Fisica ou Empresa']))

conc_n_g_mar_send.send_keys(Keys.ENTER)

############################################################   Concluinte Não Gratuita - Abril ###########################################################################################################

conc_n_g_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5108'].indicador")))

conc_n_g_abr.click()

conc_n_g_abr_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5108"
)))

conc_n_g_abr_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_n_g_abr_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_n_g_abr_send.send_keys(str(con['abr_ip_con_9 Pago por Pessoa Fisica ou Empresa']))

conc_n_g_abr_send.send_keys(Keys.ENTER)

############################################################   Concluinte Não Gratuita - Maio ###########################################################################################################

conc_n_g_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5108'].indicador")))

conc_n_g_mai.click()

conc_n_g_mai_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5108"
)))

conc_n_g_mai_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_n_g_mai_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_n_g_mai_send.send_keys(str(con['mai_ip_con_9 Pago por Pessoa Fisica ou Empresa']))

conc_n_g_mai_send.send_keys(Keys.ENTER)


############################################################   Concluinte Não Gratuita - Junho ###########################################################################################################

conc_n_g_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5108'].indicador")))

conc_n_g_jun.click()

conc_n_g_jun_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5108"
)))

conc_n_g_jun_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_n_g_jun_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_n_g_jun_send.send_keys(str(con['jun_ip_con_9 Pago por Pessoa Fisica ou Empresa']))

conc_n_g_jun_send.send_keys(Keys.ENTER)


############################################################   Concluinte Não Gratuita - Julho ###########################################################################################################

conc_n_g_jul = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5108'].indicador")))

conc_n_g_jul.click()

conc_n_g_jul_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5108"
)))

conc_n_g_jul_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_n_g_jul_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_n_g_jul_send.send_keys(str(con['jul_ip_con_9 Pago por Pessoa Fisica ou Empresa']))

conc_n_g_jul_send.send_keys(Keys.ENTER)

############################################################   Concluinte Não Gratuita - Agosto ###########################################################################################################

conc_n_g_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5108'].indicador")))

conc_n_g_ago.click()

conc_n_g_ago_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5108"
)))

conc_n_g_ago_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_n_g_ago_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_n_g_ago_send.send_keys(str(con['ago_ip_con_9 Pago por Pessoa Fisica ou Empresa']))

conc_n_g_ago_send.send_keys(Keys.ENTER)

############################################################   Concluinte Não Gratuita - Setembro ###########################################################################################################

conc_n_g_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5108'].indicador")))

conc_n_g_set.click()

conc_n_g_set_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5108"
)))

conc_n_g_set_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_n_g_set_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_n_g_set_send.send_keys(str(con['set_ip_con_9 Pago por Pessoa Fisica ou Empresa']))

conc_n_g_set_send.send_keys(Keys.ENTER)

############################################################   Concluinte Não Gratuita - Outubro ###########################################################################################################

conc_n_g_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5108'].indicador")))

conc_n_g_out.click()

conc_n_g_out_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5108"
)))

conc_n_g_out_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_n_g_out_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_n_g_out_send.send_keys(str(con['out_ip_con_9 Pago por Pessoa Fisica ou Empresa']))

conc_n_g_out_send.send_keys(Keys.ENTER)

############################################################   Concluinte Não Gratuita - Novembro ###########################################################################################################

conc_n_g_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5108'].indicador")))

conc_n_g_nov.click()

conc_n_g_nov_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5108"
)))

conc_n_g_nov_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_n_g_nov_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_n_g_nov_send.send_keys(str(con['nov_ip_con_9 Pago por Pessoa Fisica ou Empresa']))

conc_n_g_nov_send.send_keys(Keys.ENTER)

############################################################   Concluinte Não Gratuita - Dezembro ###########################################################################################################

conc_n_g_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5108'].indicador")))

conc_n_g_dez.click()

conc_n_g_dez_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5108"
)))

conc_n_g_dez_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

conc_n_g_dez_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

conc_n_g_dez_send.send_keys(str(con['dez_ip_con_9 Pago por Pessoa Fisica ou Empresa']))

conc_n_g_dez_send.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010101 - INICIACAO PROFISSINAL PRESENCIAL EVASAO BOLSA

############################################################   Evasão Bolsa -Janeiro ###########################################################################################################

eva_bolsa_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5109'].indicador")))

eva_bolsa_jan.click()

eva_bolsa_jan_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5109"
)))

eva_bolsa_jan_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_bolsa_jan_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_bolsa_jan_send.send_keys(str(eva['jan_ip_eva_2 Gratuidade Não Regimental']))

eva_bolsa_jan_send.send_keys(Keys.ENTER)

############################################################   Evasão Bolsa -Fevereiro ###########################################################################################################

eva_bolsa_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5109'].indicador")))

eva_bolsa_fev.click()

eva_bolsa_fev_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5109"
)))

eva_bolsa_fev_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_bolsa_fev_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_bolsa_fev_send.send_keys(str(eva['fev_ip_eva_2 Gratuidade Não Regimental']))

eva_bolsa_fev_send.send_keys(Keys.ENTER)

############################################################   Evasão Bolsa -Março ###########################################################################################################

eva_bolsa_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5109'].indicador")))

eva_bolsa_mar.click()

eva_bolsa_mar_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5109"
)))

eva_bolsa_mar_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_bolsa_mar_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_bolsa_mar_send.send_keys(str(eva['mar_ip_eva_2 Gratuidade Não Regimental']))

eva_bolsa_mar_send.send_keys(Keys.ENTER)

############################################################   Evasão Bolsa -Abril ###########################################################################################################

eva_bolsa_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5109'].indicador")))

eva_bolsa_abr.click()

eva_bolsa_abr_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5109"
)))

eva_bolsa_abr_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_bolsa_abr_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_bolsa_abr_send.send_keys(str(eva['abr_ip_eva_2 Gratuidade Não Regimental']))

eva_bolsa_abr_send.send_keys(Keys.ENTER)

############################################################   Evasão Bolsa -Maio ###########################################################################################################

eva_bolsa_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5109'].indicador")))

eva_bolsa_mai.click()

eva_bolsa_mai_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5109"
)))

eva_bolsa_mai_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_bolsa_mai_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_bolsa_mai_send.send_keys(str(eva['mai_ip_eva_2 Gratuidade Não Regimental']))

eva_bolsa_mai_send.send_keys(Keys.ENTER)

################################################ Evasão Bolsa -Junho ############################################################################

eva_bolsa_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5109'].indicador")))

eva_bolsa_jun.click()

eva_bolsa_jun_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5109"
)))

eva_bolsa_jun_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_bolsa_jun_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_bolsa_jun_send.send_keys(str(eva['jun_ip_eva_2 Gratuidade Não Regimental']))

eva_bolsa_jun_send.send_keys(Keys.ENTER)

############################################################   Evasão Bolsa -Julho ###########################################################################################################

eva_bolsa_jul = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5109'].indicador")))

eva_bolsa_jul.click()

eva_bolsa_jul_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5109"
)))

eva_bolsa_jul_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_bolsa_jul_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_bolsa_jul_send.send_keys(str(eva['jul_ip_eva_2 Gratuidade Não Regimental']))

eva_bolsa_jul_send.send_keys(Keys.ENTER)


############################################################   Evasão Bolsa -Agosto ###########################################################################################################

eva_bolsa_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5109'].indicador")))

eva_bolsa_ago.click()

eva_bolsa_ago_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5109"
)))

eva_bolsa_ago_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_bolsa_ago_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_bolsa_ago_send.send_keys(str(eva['ago_ip_eva_2 Gratuidade Não Regimental']))

eva_bolsa_ago_send.send_keys(Keys.ENTER)

############################################################   Evasão Bolsa -Setembro ###########################################################################################################

eva_bolsa_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5109'].indicador")))

eva_bolsa_set.click()

eva_bolsa_set_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5109"
)))

eva_bolsa_set_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_bolsa_set_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_bolsa_set_send.send_keys(str(eva['set_ip_eva_2 Gratuidade Não Regimental']))

eva_bolsa_set_send.send_keys(Keys.ENTER)

############################################################   Evasão Bolsa -Outubro ###########################################################################################################

eva_bolsa_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5109'].indicador")))

eva_bolsa_out.click()

eva_bolsa_out_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5109"
)))

eva_bolsa_out_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_bolsa_out_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_bolsa_out_send.send_keys(str(eva['out_ip_eva_2 Gratuidade Não Regimental']))

eva_bolsa_out_send.send_keys(Keys.ENTER)

############################################################   Evasão Bolsa -Novembro ###########################################################################################################

eva_bolsa_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5109'].indicador")))

eva_bolsa_nov.click()

eva_bolsa_nov_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5109"
)))

eva_bolsa_nov_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_bolsa_nov_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_bolsa_nov_send.send_keys(str(eva['nov_ip_eva_2 Gratuidade Não Regimental']))

eva_bolsa_nov_send.send_keys(Keys.ENTER)

############################################################   Evasão Bolsa -Dezembro ###########################################################################################################

eva_bolsa_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5109'].indicador")))

eva_bolsa_dez.click()

eva_bolsa_dez_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5109"
)))

eva_bolsa_dez_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_bolsa_dez_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_bolsa_dez_send.send_keys(str(eva['dez_ip_eva_2 Gratuidade Não Regimental']))

eva_bolsa_dez_send.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010101 - INICIACAO PROFISSINAL PRESENCIAL EVASAO NAO GRATUITA

############################################################   Evasão Não Gratuita - Janeiro ###########################################################################################################

eva_ngrat_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5110'].indicador")))

eva_ngrat_jan.click()

eva_ngrat_jan_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5110"
)))

eva_ngrat_jan_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_ngrat_jan_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_ngrat_jan_send.send_keys(str(eva['jan_ip_eva_9 Pago por Pessoa Fisica ou Empresa']))

eva_ngrat_jan_send.send_keys(Keys.ENTER)

############################################################   Evasão Não Gratuita - Fevereiro ####################################################################

eva_ngrat_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5110'].indicador")))

eva_ngrat_fev.click()

eva_ngrat_fev_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5110"
)))

eva_ngrat_fev_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_ngrat_fev_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_ngrat_fev_send.send_keys(str(eva['fev_ip_eva_9 Pago por Pessoa Fisica ou Empresa']))

eva_ngrat_fev_send.send_keys(Keys.ENTER)

############################################################   Evasão Não Gratuita - Março ####################################################################

eva_ngrat_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5110'].indicador")))

eva_ngrat_mar.click()

eva_ngrat_mar_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5110"
)))

eva_ngrat_mar_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_ngrat_mar_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_ngrat_mar_send.send_keys(str(eva['mar_ip_eva_9 Pago por Pessoa Fisica ou Empresa']))

eva_ngrat_mar_send.send_keys(Keys.ENTER)


############################################################   Evasão Não Gratuita - Abril ####################################################################

eva_ngrat_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5110'].indicador")))

eva_ngrat_abr.click()

eva_ngrat_abr_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5110"
)))

eva_ngrat_abr_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_ngrat_abr_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_ngrat_abr_send.send_keys(str(eva['abr_ip_eva_9 Pago por Pessoa Fisica ou Empresa']))

eva_ngrat_abr_send.send_keys(Keys.ENTER)

############################################################   Evasão Não Gratuita - Maio ####################################################################

eva_ngrat_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5110'].indicador")))

eva_ngrat_mai.click()

eva_ngrat_mai_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5110"
)))

eva_ngrat_mai_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_ngrat_mai_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_ngrat_mai_send.send_keys(str(eva['mai_ip_eva_9 Pago por Pessoa Fisica ou Empresa']))

eva_ngrat_mai_send.send_keys(Keys.ENTER)

############################################################   Evasão Não Gratuita - Junho ####################################################################

eva_ngrat_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5110'].indicador")))

eva_ngrat_jun.click()

eva_ngrat_jun_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5110"
)))

eva_ngrat_jun_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_ngrat_jun_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_ngrat_jun_send.send_keys(str(eva['mai_ip_eva_9 Pago por Pessoa Fisica ou Empresa']))

eva_ngrat_jun_send.send_keys(Keys.ENTER)

############################################################   Evasão Não Gratuita - Julho ####################################################################

eva_ngrat_jul = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5110'].indicador")))

eva_ngrat_jul.click()

eva_ngrat_jul_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5110"
)))

eva_ngrat_jul_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_ngrat_jul_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_ngrat_jul_send.send_keys(str(eva['jul_ip_eva_9 Pago por Pessoa Fisica ou Empresa']))

eva_ngrat_jul_send.send_keys(Keys.ENTER)

############################################################   Evasão Não Gratuita - Agosto ####################################################################

eva_ngrat_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5110'].indicador")))

eva_ngrat_ago.click()

eva_ngrat_ago_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5110"
)))

eva_ngrat_ago_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_ngrat_ago_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_ngrat_ago_send.send_keys(str(eva['ago_ip_eva_9 Pago por Pessoa Fisica ou Empresa']))

eva_ngrat_ago_send.send_keys(Keys.ENTER)

############################################################   Evasão Não Gratuita - Setembro ####################################################################

eva_ngrat_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5110'].indicador")))

eva_ngrat_set.click()

eva_ngrat_set_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5110"
)))

eva_ngrat_set_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_ngrat_set_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_ngrat_set_send.send_keys(str(eva['set_ip_eva_9 Pago por Pessoa Fisica ou Empresa']))

eva_ngrat_set_send.send_keys(Keys.ENTER)

############################################################   Evasão Não Gratuita - Outubro ####################################################################

eva_ngrat_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5110'].indicador")))

eva_ngrat_out.click()

eva_ngrat_out_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5110"
)))

eva_ngrat_out_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_ngrat_out_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_ngrat_out_send.send_keys(str(eva['out_ip_eva_9 Pago por Pessoa Fisica ou Empresa']))

eva_ngrat_out_send.send_keys(Keys.ENTER)

############################################################   Evasão Não Gratuita - Novembro ####################################################################

eva_ngrat_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5110'].indicador")))

eva_ngrat_nov.click()

eva_ngrat_nov_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5110"
)))

eva_ngrat_nov_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_ngrat_nov_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_ngrat_nov_send.send_keys(str(eva['nov_ip_eva_9 Pago por Pessoa Fisica ou Empresa']))

eva_ngrat_nov_send.send_keys(Keys.ENTER)

############################################################   Evasão Não Gratuita - Dezembro ####################################################################

eva_ngrat_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5110'].indicador")))

eva_ngrat_dez.click()

eva_ngrat_dez_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5110"
)))

eva_ngrat_dez_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_ngrat_dez_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_ngrat_dez_send.send_keys(str(eva['dez_ip_eva_9 Pago por Pessoa Fisica ou Empresa']))

eva_ngrat_dez_send.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010101 - INICIACAO PROFISSINAL PRESENCIAL HORA ALUNO BOLSA

############################################################   Hora Aluno Bolsa - Janeiro ####################################################################

ha_bolsa_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5111'].indicador")))

ha_bolsa_jan.click()

ha_bolsa_jan_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5111"
)))

ha_bolsa_jan_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_bolsa_jan_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_bolsa_jan_send.send_keys(str(ha['jan_ip_ha_2 Gratuidade Não Regimental']))

ha_bolsa_jan_send.send_keys(Keys.ENTER)

############################################################   Hora Aluno Bolsa - Fevereiro ####################################################################

ha_bolsa_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5111'].indicador")))

ha_bolsa_fev.click()

ha_bolsa_fev_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5111"
)))

ha_bolsa_fev_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_bolsa_fev_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_bolsa_fev_send.send_keys(str(ha['fev_ip_ha_2 Gratuidade Não Regimental']))

ha_bolsa_fev_send.send_keys(Keys.ENTER)


############################################################   Hora Aluno Bolsa - Março ####################################################################

ha_bolsa_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5111'].indicador")))

ha_bolsa_mar.click()

ha_bolsa_mar_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5111"
)))

ha_bolsa_mar_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_bolsa_mar_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_bolsa_mar_send.send_keys(str(ha['mar_ip_ha_2 Gratuidade Não Regimental']))

ha_bolsa_mar_send.send_keys(Keys.ENTER)

############################################################   Hora Aluno Bolsa - Abril ####################################################################

ha_bolsa_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5111'].indicador")))

ha_bolsa_abr.click()

ha_bolsa_abr_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5111"
)))

ha_bolsa_abr_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_bolsa_abr_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_bolsa_abr_send.send_keys(str(ha['abr_ip_ha_2 Gratuidade Não Regimental']))

ha_bolsa_abr_send.send_keys(Keys.ENTER)

############################################################   Hora Aluno Bolsa - Maio ####################################################################

ha_bolsa_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5111'].indicador")))

ha_bolsa_mai.click()

ha_bolsa_mai_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5111"
)))

ha_bolsa_mai_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_bolsa_mai_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_bolsa_mai_send.send_keys(str(ha['mai_ip_ha_2 Gratuidade Não Regimental']))

ha_bolsa_mai_send.send_keys(Keys.ENTER)


############################################################   Hora Aluno Bolsa - Junho ####################################################################

ha_bolsa_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5111'].indicador")))

ha_bolsa_jun.click()

ha_bolsa_jun_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5111"
)))

ha_bolsa_jun_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_bolsa_jun_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_bolsa_jun_send.send_keys(str(ha['jun_ip_ha_2 Gratuidade Não Regimental']))

ha_bolsa_jun_send.send_keys(Keys.ENTER)

############################################################   Hora Aluno Bolsa - Julho ####################################################################

ha_bolsa_juL = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5111'].indicador")))

ha_bolsa_juL.click()

ha_bolsa_juL_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5111"
)))

ha_bolsa_juL_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_bolsa_juL_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_bolsa_juL_send.send_keys(str(ha['jul_ip_ha_2 Gratuidade Não Regimental']))

ha_bolsa_juL_send.send_keys(Keys.ENTER)

############################################################   Hora Aluno Bolsa - Agosto ####################################################################

ha_bolsa_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5111'].indicador")))

ha_bolsa_ago.click()

ha_bolsa_ago_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5111"
)))

ha_bolsa_ago_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_bolsa_ago_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_bolsa_ago_send.send_keys(str(ha['ago_ip_ha_2 Gratuidade Não Regimental']))

ha_bolsa_ago_send.send_keys(Keys.ENTER)

############################################################   Hora Aluno Bolsa - Setembro ####################################################################

ha_bolsa_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5111'].indicador")))

ha_bolsa_set.click()

ha_bolsa_set_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5111"
)))

ha_bolsa_set_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_bolsa_set_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_bolsa_set_send.send_keys(str(ha['set_ip_ha_2 Gratuidade Não Regimental']))

ha_bolsa_set_send.send_keys(Keys.ENTER)

############################################################   Hora Aluno Bolsa - Outubro ####################################################################

ha_bolsa_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5111'].indicador")))

ha_bolsa_out.click()

ha_bolsa_out_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5111"
)))

ha_bolsa_out_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_bolsa_out_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_bolsa_out_send.send_keys(str(ha['out_ip_ha_2 Gratuidade Não Regimental']))

ha_bolsa_out_send.send_keys(Keys.ENTER)

############################################################   Hora Aluno Bolsa - Novembro ####################################################################

ha_bolsa_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5111'].indicador")))

ha_bolsa_nov.click()

ha_bolsa_nov_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5111"
)))

ha_bolsa_nov_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_bolsa_nov_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_bolsa_nov_send.send_keys(str(ha['nov_ip_ha_2 Gratuidade Não Regimental']))

ha_bolsa_nov_send.send_keys(Keys.ENTER)

############################################################   Hora Aluno Bolsa - Dezembro ####################################################################

ha_bolsa_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5111'].indicador")))

ha_bolsa_dez.click()

ha_bolsa_dez_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5111"
)))

ha_bolsa_dez_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_bolsa_dez_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_bolsa_dez_send.send_keys(str(ha['dez_ip_ha_2 Gratuidade Não Regimental']))

ha_bolsa_dez_send.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010101 - INICIACAO PROFISSINAL PRESENCIAL HORA ALUNO NAO GRATUITA

############################################################   Hora Aluno Não Gratuita - Janeiro ####################################################################

ha_n_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5112'].indicador")))

ha_n_jan.click()

ha_n_jan_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5112"
)))

ha_n_jan_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_jan_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_jan_send.send_keys(str(ha['jan_ip_ha_9 Pago por Pessoa Fisica ou Empresa']))

ha_n_jan_send.send_keys(Keys.ENTER)

############################################################   Hora Aluno Não Gratuita - Fevereiro ####################################################################

ha_n_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5112'].indicador")))

ha_n_fev.click()

ha_n_fev_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5112"
)))

ha_n_fev_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_fev_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_fev_send.send_keys(str(ha['fev_ip_ha_9 Pago por Pessoa Fisica ou Empresa']))

ha_n_fev_send.send_keys(Keys.ENTER)

############################################################   Hora Aluno Não Gratuita - Março ####################################################################

ha_n_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5112'].indicador")))

ha_n_mar.click()

ha_n_mar_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5112"
)))

ha_n_mar_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_mar_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_mar_send.send_keys(str(ha['mar_ip_ha_9 Pago por Pessoa Fisica ou Empresa']))

ha_n_mar_send.send_keys(Keys.ENTER)

############################################################   Hora Aluno Não Gratuita - Abril ####################################################################

ha_n_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5112'].indicador")))

ha_n_abr.click()

ha_n_abr_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5112"
)))

ha_n_abr_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_abr_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_abr_send.send_keys(str(ha['abr_ip_ha_9 Pago por Pessoa Fisica ou Empresa']))

ha_n_abr_send.send_keys(Keys.ENTER)

############################################################   Hora Aluno Não Gratuita - Maio ####################################################################

ha_n_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5112'].indicador")))

ha_n_mai.click()

ha_n_mai_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5112"
)))

ha_n_mai_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_mai_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_mai_send.send_keys(str(ha['mai_ip_ha_9 Pago por Pessoa Fisica ou Empresa']))

ha_n_mai_send.send_keys(Keys.ENTER)


############################################################   Hora Aluno Não Gratuita - Junho ####################################################################

ha_n_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5112'].indicador")))

ha_n_jun.click()

ha_n_jun_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5112"
)))

ha_n_jun_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_jun_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_jun_send.send_keys(str(ha['jun_ip_ha_9 Pago por Pessoa Fisica ou Empresa']))

ha_n_jun_send.send_keys(Keys.ENTER)


############################################################   Hora Aluno Não Gratuita - Julho ####################################################################

ha_n_jul = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5112'].indicador")))

ha_n_jul.click()

ha_n_jul_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5112"
)))

ha_n_jul_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_jul_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_jul_send.send_keys(str(ha['jul_ip_ha_9 Pago por Pessoa Fisica ou Empresa']))

ha_n_jul_send.send_keys(Keys.ENTER)


############################################################   Hora Aluno Não Gratuita - Agosto ####################################################################

ha_n_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5112'].indicador")))

ha_n_ago.click()

ha_n_ago_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5112"
)))

ha_n_ago_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_ago_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_ago_send.send_keys(str(ha['ago_ip_ha_9 Pago por Pessoa Fisica ou Empresa']))

ha_n_ago_send.send_keys(Keys.ENTER)


############################################################   Hora Aluno Não Gratuita - Setembro ####################################################################

ha_n_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5112'].indicador")))

ha_n_set.click()

ha_n_set_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5112"
)))

ha_n_set_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_set_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_set_send.send_keys(str(ha['set_ip_ha_9 Pago por Pessoa Fisica ou Empresa']))

ha_n_set_send.send_keys(Keys.ENTER)


############################################################   Hora Aluno Não Gratuita - Outubro ####################################################################

ha_n_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5112'].indicador")))

ha_n_out.click()

ha_n_out_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5112"
)))

ha_n_out_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_out_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_out_send.send_keys(str(ha['out_ip_ha_9 Pago por Pessoa Fisica ou Empresa']))

ha_n_out_send.send_keys(Keys.ENTER)

############################################################   Hora Aluno Não Gratuita - Novembro ####################################################################

ha_n_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5112'].indicador")))

ha_n_nov.click()

ha_n_nov_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5112"
)))

ha_n_nov_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_nov_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_nov_send.send_keys(str(ha['nov_ip_ha_9 Pago por Pessoa Fisica ou Empresa']))

ha_n_nov_send.send_keys(Keys.ENTER)

############################################################ Hora Aluno Não Gratuita - Dezembro ########################################################


ha_n_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5112'].indicador")))

ha_n_dez.click()

ha_n_dez_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5112"
)))

ha_n_dez_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_dez_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_dez_send.send_keys(str(ha['dez_ip_ha_9 Pago por Pessoa Fisica ou Empresa']))

ha_n_dez_send.send_keys(Keys.ENTER)

#########################################  INICIAÇÃO PROFISSIONAL A DISTANCIA  #########################################################################


janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/225?cd_centro_resp=30303010201&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=INICIACAO%20PROFISSIONAL%20A%20DISTANCIA&id_grupo=1&ds_grupo=Inicia%C3%A7%C3%A3o%20Profissional&fase=Realiza%C3%A7%C3%A3o', '_self')")

# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA MATRICULA BOLSA

############################################################ Matricula - Bolsa Janeiro ##########################################################

mat_bolsa_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5073'].indicador")))

mat_bolsa_jan.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5073"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat_jan_IPD['jan_ipd_mat_bolsa']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################ Matricula - Bolsa Fevereiro ########################################################

mat_bolsa_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5073'].indicador")))

mat_bolsa_fev.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5073"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat_IPD['fev_ipd_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################ Matricula - Bolsa Março ##########################################################

mat_bolsa_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5073'].indicador")))

mat_bolsa_mar.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5073"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat_IPD['mar_ipd_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################ Matricula - Bolsa Abril ##########################################################

mat_bolsa_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5073'].indicador")))

mat_bolsa_abr.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5073"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat_IPD['abr_ipd_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################ Matricula - Bolsa Maio ############################################################

mat_bolsa_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5073'].indicador")))

mat_bolsa_mai.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5073"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat_IPD['mai_ipd_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################ Matricula - Bolsa Junho ##########################################################

mat_bolsa_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5073'].indicador")))

mat_bolsa_jun.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5073"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat_IPD['jun_ipd_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################ Matricula - Bolsa Julho ##########################################################

mat_bolsa_jul = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5073'].indicador")))

mat_bolsa_jul.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5073"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat_IPD['jul_ipd_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################ Matricula - Bolsa Agosto ##########################################################

mat_bolsa_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5073'].indicador")))

mat_bolsa_ago.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5073"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat_IPD['ago_ipd_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################ Matricula - Bolsa Setembro #########################################################

mat_bolsa_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5073'].indicador")))

mat_bolsa_set.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5073"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat_IPD['set_ipd_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

############################################################ Matricula - Bolsa Outubro ##########################################################

mat_bolsa_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5073'].indicador")))

mat_bolsa_out.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5073"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat_IPD['out_ipd_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

########################################################### Matricula - Bolsa Novembro ##########################################################

mat_bolsa_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5073'].indicador")))

mat_bolsa_nov.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5073"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat_IPD['nov_ipd_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)


############################################################ Matricula - Bolsa Dezembro #########################################################

mat_bolsa_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5073'].indicador")))

mat_bolsa_dez.click()

mat_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5073"
)))

mat_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_bolsa_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_bolsa_send.send_keys(str(mat_IPD['dez_ipd_mat_2 Gratuidade Não Regimental']))

mat_bolsa_send.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA MATRICULA NAO GRATUITA

############################################################ Matricula - Não Gratuita Janeiro #########################################################

mat_n_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5074'].indicador")))

mat_n_jan.click()

mat_n_jan_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5074"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_jan_IPD['jan_ipd_mat_n_gratuita']))

mat_n_send.send_keys(Keys.ENTER)

############################################################ Matricula - Não Gratuita Fevereiro ########################################################

mat_n_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5074'].indicador")))

mat_n_fev.click()

mat_n_fev_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5074"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_IPD['fev_ipd_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_send.send_keys(Keys.ENTER)

############################################################ Matricula - Não Gratuita Março #########################################################

mat_n_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5074'].indicador")))

mat_n_mar.click()

mat_n_mar_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5074"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_IPD['mar_ipd_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_send.send_keys(Keys.ENTER)

############################################################ Matricula - Não Gratuita Abril #########################################################

mat_n_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5074'].indicador")))

mat_n_abr.click()

mat_n_mar_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5074"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_IPD['abr_ipd_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_send.send_keys(Keys.ENTER)


############################################################ Matricula - Não Gratuita Maio #########################################################


mat_n_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5074'].indicador")))

mat_n_mai.click()

mat_n_mai_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5074"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_IPD['mai_ipd_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_send.send_keys(Keys.ENTER)


############################################################ Matricula - Não Gratuita Junho #########################################################

mat_n_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5074'].indicador")))

mat_n_jun.click()

mat_n_jun_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5074"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_IPD['jun_ipd_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_send.send_keys(Keys.ENTER)


############################################################ Matricula - Não Gratuita Julho #########################################################

mat_n_jul = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5074'].indicador")))

mat_n_jul.click()

mat_n_jul_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5074"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_IPD['jul_ipd_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_send.send_keys(Keys.ENTER)

############################################################ Matricula - Não Gratuita Agosto #########################################################

mat_n_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5074'].indicador")))

mat_n_ago.click()

mat_n_ago_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5074"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_IPD['ago_ipd_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_send.send_keys(Keys.ENTER)


############################################################ Matricula - Não Gratuita Setembro #########################################################

mat_n_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5074'].indicador")))

mat_n_set.click()

mat_n_set_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5074"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_IPD['set_ipd_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_send.send_keys(Keys.ENTER)

############################################################ Matricula - Não Gratuita Outubro #########################################################

mat_n_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5074'].indicador")))

mat_n_out.click()

mat_n_out_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5074"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_IPD['out_ipd_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_send.send_keys(Keys.ENTER)

############################################################ Matricula - Não Gratuita Novembro #########################################################

mat_n_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5074'].indicador")))

mat_n_nov.click()

mat_n_nov_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5074"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_IPD['nov_ipd_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_send.send_keys(Keys.ENTER)

############################################################ Matricula - Não Gratuita Dezembro #########################################################

mat_n_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5074'].indicador")))

mat_n_dez.click()

mat_n_dez_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5074"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_IPD['dez_ipd_mat_9 Pago por Pessoa Fisica ou Empresa']))

mat_n_send.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA CONCLUINTES BOLSA

############################################################ Concluinte - Bolsa Janeiro #########################################################

con_b_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5067'].indicador")))

con_b_jan.click()

con_b_jan_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5067"
)))

con_bpopover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_jansend = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_jansend.send_keys(str(con_IPD['jan_ipd_con_2 Gratuidade Não Regimental']))

con_b_jan.send_keys(Keys.ENTER)


############################################################ Concluinte - Bolsa Fevereiro ########################################################

con_b_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5067'].indicador")))

con_b_fev.click()

con_b_fev_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5067"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_fev_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_fev_send.send_keys(str(con_IPD['fev_ipd_con_2 Gratuidade Não Regimental']))

con_b_fev.send_keys(Keys.ENTER)

############################################################ Concluinte - Bolsa Março ########################################################

con_b_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5067'].indicador")))

con_b_mar.click()

con_b_mar_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5067"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_mar_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_mar_send.send_keys(str(con_IPD['mar_ipd_con_2 Gratuidade Não Regimental']))

con_b_mar.send_keys(Keys.ENTER)

############################################################ Concluinte - Bolsa Abril ########################################################

con_b_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5067'].indicador")))

con_b_abr.click()

con_b_abr_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5067"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_abr_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_abr_send.send_keys(str(con_IPD['abr_ipd_con_2 Gratuidade Não Regimental']))

con_b_abr.send_keys(Keys.ENTER)


############################################################ Concluinte - Bolsa Maio ########################################################

con_b_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5067'].indicador")))

con_b_mai.click()

con_b_mai_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5067"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_mai_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_mai_send.send_keys(str(con_IPD['mai_ipd_con_2 Gratuidade Não Regimental']))

con_b_mai.send_keys(Keys.ENTER)

############################################################ Concluinte - Bolsa Junho ########################################################

con_b_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5067'].indicador")))

con_b_jun.click()

con_b_jun_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5067"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_jun_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_jun_send.send_keys(str(con_IPD['jun_ipd_con_2 Gratuidade Não Regimental']))

con_b_jun.send_keys(Keys.ENTER)


############################################################ Concluinte - Bolsa Julho ########################################################

con_b_jul = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5067'].indicador")))

con_b_jul.click()

con_b_jul_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5067"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_jul_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_jul_send.send_keys(str(con_IPD['jul_ipd_con_2 Gratuidade Não Regimental']))

con_b_jul.send_keys(Keys.ENTER)

############################################################ Concluinte - Bolsa Agosto ########################################################

con_b_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5067'].indicador")))

con_b_ago.click()

con_b_ago_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5067"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_ago_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_ago_send.send_keys(str(con_IPD['ago_ipd_con_2 Gratuidade Não Regimental']))

con_b_ago.send_keys(Keys.ENTER)

############################################################ Concluinte - Bolsa Setembro ########################################################

con_b_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5067'].indicador")))

con_b_set.click()

con_b_set_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5067"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_set_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_set_send.send_keys(str(con_IPD['set_ipd_con_2 Gratuidade Não Regimental']))

con_b_set.send_keys(Keys.ENTER)

############################################################ Concluinte - Bolsa Outubro ########################################################

con_b_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5067'].indicador")))

con_b_out.click()

con_b_out_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5067"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_out_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_out_send.send_keys(str(con_IPD['out_ipd_con_2 Gratuidade Não Regimental']))

con_b_out.send_keys(Keys.ENTER)

############################################################ Concluinte - Bolsa Novembro ########################################################

con_b_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5067'].indicador")))

con_b_nov.click()

con_b_nov_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5067"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_nov_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_nov_send.send_keys(str(con_IPD['nov_ipd_con_2 Gratuidade Não Regimental']))

con_b_nov.send_keys(Keys.ENTER)


############################################################ Concluinte - Bolsa Dezembro ########################################################

con_b_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5067'].indicador")))

con_b_dez.click()

con_b_dez_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5067"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_dez_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_dez_send.send_keys(str(con_IPD['dez_ipd_con_2 Gratuidade Não Regimental']))

con_b_dez.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA CONCLUINTES NAO GRATUITA

############################################################ Concluinte - Não Gratuita Janeiro ########################################################

con_b_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5068'].indicador")))

con_b_jan.click()

con_b_jan_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5068"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_jan_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_jan_send.send_keys(str(con_IPD['jan_ipd_con_9 Pago por Pessoa Fisica ou Empresa']))

con_b_jan.send_keys(Keys.ENTER)

############################################################ Concluinte - Não Gratuita Fevereiro  ########################################################

con_b_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5068'].indicador")))

con_b_fev.click()

con_b_fev_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5068"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_fev_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_fev_send.send_keys(str(con_IPD['fev_ipd_con_9 Pago por Pessoa Fisica ou Empresa']))

con_b_fev.send_keys(Keys.ENTER)

############################################################ Concluinte - Não Gratuita Março ########################################################

con_b_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5068'].indicador")))

con_b_mar.click()

con_b_mar_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5068"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_mar_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_mar_send.send_keys(str(con_IPD['mar_ipd_con_9 Pago por Pessoa Fisica ou Empresa']))

con_b_fev.send_keys(Keys.ENTER)

############################################################ Concluinte - Não Gratuita Abril ########################################################

con_b_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5068'].indicador")))

con_b_abr.click()

con_b_abr_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5068"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_abr_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_abr_send.send_keys(str(con_IPD['abr_ipd_con_9 Pago por Pessoa Fisica ou Empresa']))

con_b_abr.send_keys(Keys.ENTER)

############################################################ Concluinte - Não Gratuita Maio ########################################################

con_b_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5068'].indicador")))

con_b_mai.click()

con_b_mai_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5068"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_mai_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_mai_send.send_keys(str(con_IPD['mai_ipd_con_9 Pago por Pessoa Fisica ou Empresa']))

con_b_mai.send_keys(Keys.ENTER)


############################################################ Concluinte - Não Gratuita Junho ########################################################

con_b_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5068'].indicador")))

con_b_jun.click()

con_b_jun_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5068"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_jun_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_jun_send.send_keys(str(con_IPD['jun_ipd_con_9 Pago por Pessoa Fisica ou Empresa']))

con_b_mai.send_keys(Keys.ENTER)


############################################################ Concluinte - Não Gratuita Julho ########################################################

con_b_jul = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5068'].indicador")))

con_b_jul.click()

con_b_jul_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5068"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_jul_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_jul_send.send_keys(str(con_IPD['jul_ipd_con_9 Pago por Pessoa Fisica ou Empresa']))

con_b_jul.send_keys(Keys.ENTER)

############################################################ Concluinte - Não Gratuita Agosto ########################################################

con_b_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5068'].indicador")))

con_b_ago.click()

con_b_ago_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5068"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_ago_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_ago_send.send_keys(str(con_IPD['ago_ipd_con_9 Pago por Pessoa Fisica ou Empresa']))

con_b_ago.send_keys(Keys.ENTER)

############################################################ Concluinte - Não Gratuita Setembro ########################################################

con_b_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5068'].indicador")))

con_b_set.click()

con_b_set_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5068"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_set_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_set_send.send_keys(str(con_IPD['set_ipd_con_9 Pago por Pessoa Fisica ou Empresa']))

con_b_set.send_keys(Keys.ENTER)


############################################################ Concluinte - Não Gratuita Outubro ########################################################

con_b_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5068'].indicador")))

con_b_out.click()

con_b_out_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5068"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_out_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_out_send.send_keys(str(con_IPD['out_ipd_con_9 Pago por Pessoa Fisica ou Empresa']))

con_b_out.send_keys(Keys.ENTER)

############################################################ Concluinte - Não Gratuita Novembro ########################################################

con_b_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5068'].indicador")))

con_b_nov.click()

con_b_nov_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5068"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_nov_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_nov_send.send_keys(str(con_IPD['nov_ipd_con_9 Pago por Pessoa Fisica ou Empresa']))

con_b_nov.send_keys(Keys.ENTER)

############################################################ Concluinte - Não Gratuita Dezembro ########################################################

con_b_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5068'].indicador")))

con_b_dez.click()

con_b_dez_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5068"
)))

con_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

con_b_dez_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

con_b_dez_send.send_keys(str(con_IPD['dez_ipd_con_9 Pago por Pessoa Fisica ou Empresa']))

con_b_dez.send_keys(Keys.ENTER)

############################################################ Evasão - Bolsa Janeiro ########################################################

eva_b_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5069'].indicador")))

eva_b_jan.click()

eva_b_jan_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5069"
)))

eva_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_b_jan_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_b_jan_send.send_keys(str(eva_IPD['jan_ipd_eva_2 Gratuidade Não Regimental']))

eva_b_jan.send_keys(Keys.ENTER)

############################################################ Evasão - Bolsa Fevereiro ########################################################

eva_b_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5069'].indicador")))

eva_b_fev.click()

eva_b_fev_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5069"
)))

eva_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_b_fev_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_b_fev_send.send_keys(str(eva_IPD['fev_ipd_eva_2 Gratuidade Não Regimental']))

eva_b_fev.send_keys(Keys.ENTER)

############################################################ Evasão - Bolsa Março ########################################################

eva_b_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5069'].indicador")))

eva_b_mar.click()

eva_b_mar_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5069"
)))

eva_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_b_mar_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_b_mar_send.send_keys(str(eva_IPD['mar_ipd_eva_2 Gratuidade Não Regimental']))

eva_b_mar.send_keys(Keys.ENTER)

############################################################ Evasão - Bolsa Abril ########################################################

eva_b_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5069'].indicador")))

eva_b_abr.click()

eva_b_abr_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5069"
)))

eva_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_b_abr_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_b_abr_send.send_keys(str(eva_IPD['abr_ipd_eva_2 Gratuidade Não Regimental']))

eva_b_abr.send_keys(Keys.ENTER)

############################################################ Evasão - Bolsa Maio ########################################################

eva_b_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5069'].indicador")))

eva_b_mai.click()

eva_b_mai_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5069"
)))

eva_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_b_mai_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_b_mai_send.send_keys(str(eva_IPD['mai_ipd_eva_2 Gratuidade Não Regimental']))

eva_b_mai.send_keys(Keys.ENTER)


############################################################ Evasão - Bolsa Junho ########################################################

eva_b_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5069'].indicador")))

eva_b_jun.click()

eva_b_jun_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5069"
)))

eva_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_b_jun_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_b_jun_send.send_keys(str(eva_IPD['jun_ipd_eva_2 Gratuidade Não Regimental']))

eva_b_jun.send_keys(Keys.ENTER)

############################################################ Evasão - Bolsa Julho ########################################################

eva_b_jul = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5069'].indicador")))

eva_b_jul.click()

eva_b_jul_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5069"
)))

eva_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_b_jul_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_b_jul_send.send_keys(str(eva_IPD['jul_ipd_eva_2 Gratuidade Não Regimental']))

eva_b_jul.send_keys(Keys.ENTER)

############################################################ Evasão - Bolsa Agosto ########################################################

eva_b_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5069'].indicador")))

eva_b_ago.click()

eva_b_ago_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5069"
)))

eva_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_b_ago_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_b_ago_send.send_keys(str(eva_IPD['ago_ipd_eva_2 Gratuidade Não Regimental']))

eva_b_ago.send_keys(Keys.ENTER)

############################################################ Evasão - Bolsa Setembro ########################################################

eva_b_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5069'].indicador")))

eva_b_set.click()

eva_b_set_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5069"
)))

eva_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_b_set_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_b_set_send.send_keys(str(eva_IPD['set_ipd_eva_2 Gratuidade Não Regimental']))

eva_b_set.send_keys(Keys.ENTER)

############################################################ Evasão - Bolsa Outubro ########################################################

eva_b_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5069'].indicador")))

eva_b_out.click()

eva_b_out_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5069"
)))

eva_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_b_out_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_b_out_send.send_keys(str(eva_IPD['out_ipd_eva_2 Gratuidade Não Regimental']))

eva_b_out.send_keys(Keys.ENTER)

############################################################ Evasão - Bolsa Novembro ########################################################

eva_b_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5069'].indicador")))

eva_b_nov.click()

eva_b_nov_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5069"
)))

eva_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_b_nov_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_b_nov_send.send_keys(str(eva_IPD['nov_ipd_eva_2 Gratuidade Não Regimental']))

eva_b_nov.send_keys(Keys.ENTER)

############################################################ Evasão - Bolsa Dezembro ########################################################

eva_b_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5069'].indicador")))

eva_b_dez.click()

eva_b_dez_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5069"
)))

eva_b_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_b_dez_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_b_dez_send.send_keys(str(eva_IPD['dez_ipd_eva_2 Gratuidade Não Regimental']))

eva_b_dez.send_keys(Keys.ENTER)

# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA EVASAO NAO GRATUITA

############################################################ Evasão - Não Gratui Janeiro ########################################################

eva_n_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5070'].indicador")))

eva_n_jan.click()

eva_n_jan_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5070"
)))

eva_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_n_jan_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_n_jan_send.send_keys(str(eva_IPD['jan_ipd_eva_9 Pago por Pessoa Fisica ou Empresa']))


############################################################ Evasão - Não Gratui Fevereiro ########################################################

eva_n_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5070'].indicador")))

eva_n_fev.click()

eva_n_fev_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5070"
)))

eva_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_n_fev_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_n_fev_send.send_keys(str(eva_IPD['fev_ipd_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratui Março ########################################################

eva_n_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5070'].indicador")))

eva_n_mar.click()

eva_n_mar_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5070"
)))

eva_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_n_mar_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_n_mar_send.send_keys(str(eva_IPD['mar_ipd_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratui Abril ########################################################

eva_n_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5070'].indicador")))

eva_n_abr.click()

eva_n_abr_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5070"
)))

eva_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_n_abr_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_n_abr_send.send_keys(str(eva_IPD['abr_ipd_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratui Maio ########################################################

eva_n_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5070'].indicador")))

eva_n_mai.click()

eva_n_mai_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5070"
)))

eva_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_n_mai_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_n_mai_send.send_keys(str(eva_IPD['mai_ipd_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratui Junho ########################################################

eva_n_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5070'].indicador")))

eva_n_jun.click()

eva_n_jun_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5070"
)))

eva_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_n_jun_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_n_jun_send.send_keys(str(eva_IPD['jun_ipd_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratui Julho ########################################################

eva_n_jul = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5070'].indicador")))

eva_n_jul.click()

eva_n_jul_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5070"
)))

eva_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_n_jul_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_n_jul_send.send_keys(str(eva_IPD['jul_ipd_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratui Agosto ########################################################

eva_n_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5070'].indicador")))

eva_n_ago.click()

eva_n_ago_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5070"
)))

eva_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_n_ago_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_n_ago_send.send_keys(str(eva_IPD['ago_ipd_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratui Setembro ########################################################

eva_n_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5070'].indicador")))

eva_n_set.click()

eva_n_set_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5070"
)))

eva_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_n_set_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_n_set_send.send_keys(str(eva_IPD['set_ipd_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratui Outubro ########################################################

eva_n_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5070'].indicador")))

eva_n_out.click()

eva_n_out_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5070"
)))

eva_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_n_out_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_n_out_send.send_keys(str(eva_IPD['out_ipd_eva_9 Pago por Pessoa Fisica ou Empresa']))  


############################################################ Evasão - Não Gratui Novembro ########################################################

eva_n_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5070'].indicador")))

eva_n_nov.click()

eva_n_nov_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5070"
)))

eva_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_n_nov_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_n_nov_send.send_keys(str(eva_IPD['nov_ipd_eva_9 Pago por Pessoa Fisica ou Empresa']))  

############################################################ Evasão - Não Gratui Dezembro #######################################################

eva_n_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5070'].indicador")))

eva_n_dez.click()

eva_n_dez_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5070"
)))

eva_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eva_n_dez_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eva_n_dez_send.send_keys(str(eva_IPD['dez_ipd_eva_9 Pago por Pessoa Fisica ou Empresa']))

# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA HORA ALUNO BOLSA

############################################################ Hora Aluno - Bolsa Janeiro #######################################################

ha_b_jan = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5071'].indicador")))

ha_b_jan.click()

ha_b_jan_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5071"
)))

ha_b_jan_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_b_jan_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_b_jan_send.send_keys(str(ha_IPD['jan_ipd_ha_2 Gratuidade Não Regimental'])) 

############################################################ Hora Aluno - Bolsa Fevereiro #######################################################

ha_b_fev = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5071'].indicador")))

ha_b_fev.click()

ha_b_fev_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5071"
)))

ha_b_fev_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_b_fev_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_b_fev_send.send_keys(str(ha_IPD['fev_ipd_ha_2 Gratuidade Não Regimental'])) 


############################################################ Hora Aluno - Bolsa Março #######################################################

ha_b_mar = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5071'].indicador")))

ha_b_mar.click()

ha_b_mar_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5071"
)))

ha_b_mar_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_b_mar_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_b_mar_send.send_keys(str(ha_IPD['mar_ipd_ha_2 Gratuidade Não Regimental'])) 

############################################################ Hora Aluno - Bolsa Abril #######################################################

ha_b_abr = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5071'].indicador")))

ha_b_abr.click()

ha_b_abr_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5071"
)))

ha_b_abr_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_b_abr_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_b_abr_send.send_keys(str(ha_IPD['abr_ipd_ha_2 Gratuidade Não Regimental'])) 

############################################################ Hora Aluno - Bolsa Maio #######################################################

ha_b_mai = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5071'].indicador")))

ha_b_mai.click()

ha_b_mai_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5071"
)))

ha_b_mai_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_b_mai_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_b_mai_send.send_keys(str(ha_IPD['mai_ipd_ha_2 Gratuidade Não Regimental'])) 

############################################################ Hora Aluno - Bolsa Junho #######################################################

ha_b_jun = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5071'].indicador")))

ha_b_jun.click()

ha_b_jun_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5071"
)))

ha_b_jun_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_b_jun_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_b_jun_send.send_keys(str(ha_IPD['jun_ipd_ha_2 Gratuidade Não Regimental'])) 


############################################################ Hora Aluno - Bolsa Julho #######################################################

ha_b_jul = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5071'].indicador")))

ha_b_jul.click()

ha_b_jul_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5071"
)))

ha_b_jul_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_b_jul_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_b_jul_send.send_keys(str(ha_IPD['jul_ipd_ha_2 Gratuidade Não Regimental'])) 


############################################################ Hora Aluno - Bolsa Agosto #######################################################

ha_b_ago = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5071'].indicador")))

ha_b_ago.click()

ha_b_ago_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5071"
)))

ha_b_ago_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_b_ago_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_b_ago_send.send_keys(str(ha_IPD['ago_ipd_ha_2 Gratuidade Não Regimental'])) 

############################################################ Hora Aluno - Bolsa Setembro #######################################################

ha_b_set = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5071'].indicador")))

ha_b_set.click()

ha_b_set_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5071"
)))

ha_b_set_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_b_set_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_b_set_send.send_keys(str(ha_IPD['set_ipd_ha_2 Gratuidade Não Regimental'])) 

############################################################ Hora Aluno - Bolsa Outubro #######################################################

ha_b_out = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5071'].indicador")))

ha_b_out.click()

ha_b_out_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5071"
)))

ha_b_out_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_b_out_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_b_out_send.send_keys(str(ha_IPD['out_ipd_ha_2 Gratuidade Não Regimental'])) 


############################################################ Hora Aluno - Bolsa Novembro #######################################################

ha_b_nov = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5071'].indicador")))

ha_b_nov.click()

ha_b_nov_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5071"
)))

ha_b_nov_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_b_nov_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_b_nov_send.send_keys(str(ha_IPD['nov_ipd_ha_2 Gratuidade Não Regimental'])) 

############################################################ Hora Aluno - Bolsa Dezembro #######################################################

ha_b_dez = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5071'].indicador")))

ha_b_dez.click()

ha_b_dez_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5071"
)))

ha_b_dez_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_b_dez_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_b_dez_send.send_keys(str(ha_IPD['dez_ipd_ha_2 Gratuidade Não Regimental']))

# SENAI TAGUATINGA - 30303010201 - INICIACAO PROFISSIONAL A DISTANCIA HORA ALUNO NAO GRATUITA

############################################################ Hora Aluno - Nao Gratuita Janeiro #######################################################

ha_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5072'].indicador")))

ha_n.click()

ha_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5072"
)))

ha_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_send.send_keys(str(ha_IPD['jan_ipd_ha_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Hora Aluno - Nao Gratuita Fevereiro #######################################################

ha_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5072'].indicador")))

ha_n.click()

ha_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5072"
)))

ha_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_send.send_keys(str(ha_IPD['fev_ipd_ha_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Hora Aluno - Nao Gratuita Março #######################################################

ha_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5072'].indicador")))

ha_n.click()

ha_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5072"
)))

ha_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_send.send_keys(str(ha_IPD['mar_ipd_ha_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Hora Aluno - Nao Gratuita Abril #######################################################

ha_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5072'].indicador")))

ha_n.click()

ha_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5072"
)))

ha_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_send.send_keys(str(ha_IPD['abr_ipd_ha_9 Pago por Pessoa Fisica ou Empresa'])) 


############################################################ Hora Aluno - Nao Gratuita Maio #######################################################

ha_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5072'].indicador")))

ha_n.click()

ha_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5072"
)))

ha_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_send.send_keys(str(ha_IPD['mai_ipd_ha_9 Pago por Pessoa Fisica ou Empresa'])) 


############################################################ Hora Aluno - Nao Gratuita Junho #######################################################

ha_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5072'].indicador")))

ha_n.click()

ha_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5072"
)))

ha_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_send.send_keys(str(ha_IPD['jun_ipd_ha_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Hora Aluno - Nao Gratuita Julho #######################################################

ha_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5072'].indicador")))

ha_n.click()

ha_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5072"
)))

ha_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_send.send_keys(str(ha_IPD['jul_ipd_ha_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Hora Aluno - Nao Gratuita Agosto #######################################################

ha_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5072'].indicador")))

ha_n.click()

ha_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5072"
)))

ha_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_send.send_keys(str(ha_IPD['ago_ipd_ha_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Hora Aluno - Nao Gratuita Setembro #######################################################

ha_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5072'].indicador")))

ha_n.click()

ha_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5072"
)))

ha_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_send.send_keys(str(ha_IPD['set_ipd_ha_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Hora Aluno - Nao Gratuita Outubro #######################################################

ha_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5072'].indicador")))

ha_n.click()

ha_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5072"
)))

ha_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_send.send_keys(str(ha_IPD['out_ipd_ha_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Hora Aluno - Nao Gratuita Novembro #######################################################

ha_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5072'].indicador")))

ha_n.click()

ha_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5072"
)))

ha_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_send.send_keys(str(ha_IPD['nov_ipd_ha_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Hora Aluno - Nao Gratuita Dezembro #######################################################

ha_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5072'].indicador")))

ha_n.click()

ha_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5072"
)))

ha_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

ha_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

ha_n_send.send_keys(str(ha_IPD['dez_ipd_ha_9 Pago por Pessoa Fisica ou Empresa'])) 

###################################################  Aprendizagem Industrial - Presencial #############################################################

janela_atual = nav.current_window_handle

nav.execute_script("window.open('http://sn-iis-02/SIGECON20/Metas/MetasTipo/309/2024/0902030201/230?cd_centro_resp=30303020101&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=APRENDIZAGEM%20INDUSTRIAL%20PRESENCIAL&id_grupo=2&ds_grupo=Aprendizagem%20Industrial&fase=Realiza%C3%A7%C3%A3o', '_self')")

# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL MATRICULA NAO GRATUITA

############################################################ Matrícula - Nao Gratuita Janeiro #######################################################

mat_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5121'].indicador")))

mat_n.click()

mat_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5121"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_jan_AP['jan_ip_mat_n_gratuita'])) 

############################################################ Matrícula - Nao Gratuita Fevereiro #######################################################

mat_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5121'].indicador")))

mat_n.click()

mat_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5121"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_AP ['fev_ap_mat_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Matrícula - Nao Gratuita Março #######################################################

mat_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5121'].indicador")))

mat_n.click()

mat_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5121"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_AP ['mar_ap_mat_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Matrícula - Nao Gratuita Abril #######################################################

mat_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5121'].indicador")))

mat_n.click()

mat_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5121"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_AP ['abr_ap_mat_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Matrícula - Nao Gratuita Maio #######################################################

mat_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5121'].indicador")))

mat_n.click()

mat_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5121"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_AP ['mai_ap_mat_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Matrícula - Nao Gratuita Junho #######################################################

mat_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5121'].indicador")))

mat_n.click()

mat_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5121"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_AP ['jun_ap_mat_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Matrícula - Nao Gratuita Julho #######################################################

mat_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5121'].indicador")))

mat_n.click()

mat_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5121"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_AP ['jul_ap_mat_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Matrícula - Nao Gratuita Agosto #######################################################

mat_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5121'].indicador")))

mat_n.click()

mat_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5121"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_AP ['ago_ap_mat_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Matrícula - Nao Gratuita Setembro #######################################################

mat_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5121'].indicador")))

mat_n.click()

mat_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5121"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_AP ['set_ap_mat_9 Pago por Pessoa Fisica ou Empresa'])) 


############################################################ Matrícula - Nao Gratuita Outubro #######################################################

mat_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5121'].indicador")))

mat_n.click()

mat_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5121"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_AP ['out_ap_mat_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Matrícula - Nao Gratuita Novembro #######################################################

mat_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5121'].indicador")))

mat_n.click()

mat_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5121"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_AP ['nov_ap_mat_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Matrícula - Nao Gratuita Dezembro #######################################################

mat_n = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5121'].indicador")))

mat_n.click()

mat_n_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5121"
)))

mat_n_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_n_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_n_send.send_keys(str(mat_AP ['dez_ap_mat_9 Pago por Pessoa Fisica ou Empresa'])) 

# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL MATRICULA REGIMENTAL

############################################################ Matrícula - Regimental Janeiro #######################################################

mat_r = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5122'].indicador")))

mat_r.click()

mat_r_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5122"
)))

mat_r_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_r_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_r_send.send_keys(str(mat_jan_AP['jan_ip_mat_regi'])) 

############################################################ Matrícula - Regimental Fevereiro #######################################################

mat_r = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5122'].indicador")))

mat_r.click()

mat_r_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5122"
)))

mat_r_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_r_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_r_send.send_keys(str(mat_AP['fev_ap_mat_1 Gratuidade Regimental'])) 


############################################################ Matrícula - Regimental Março #######################################################

mat_r = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5122'].indicador")))

mat_r.click()

mat_r_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5122"
)))

mat_r_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_r_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_r_send.send_keys(str(mat_AP['mar_ap_mat_1 Gratuidade Regimental'])) 

############################################################ Matrícula - Regimental Abril #######################################################

mat_r = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5122'].indicador")))

mat_r.click()

mat_r_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5122"
)))

mat_r_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_r_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_r_send.send_keys(str(mat_AP['abr_ap_mat_1 Gratuidade Regimental'])) 

############################################################ Matrícula - Regimental Maio #######################################################

mat_r = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5122'].indicador")))

mat_r.click()

mat_r_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5122"
)))

mat_r_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_r_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_r_send.send_keys(str(mat_AP['mai_ap_mat_1 Gratuidade Regimental'])) 

############################################################ Matrícula - Regimental Junho #######################################################

mat_r = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5122'].indicador")))

mat_r.click()

mat_r_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5122"
)))

mat_r_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_r_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_r_send.send_keys(str(mat_AP['jun_ap_mat_1 Gratuidade Regimental'])) 

############################################################ Matrícula - Regimental Julho #######################################################

mat_r = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5122'].indicador")))

mat_r.click()

mat_r_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5122"
)))

mat_r_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_r_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_r_send.send_keys(str(mat_AP['jul_ap_mat_1 Gratuidade Regimental'])) 

############################################################ Matrícula - Regimental Agosto #######################################################

mat_r = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5122'].indicador")))

mat_r.click()

mat_r_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5122"
)))

mat_r_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_r_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_r_send.send_keys(str(mat_AP['ago_ap_mat_1 Gratuidade Regimental'])) 

############################################################ Matrícula - Regimental Setembro #######################################################

mat_r = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5122'].indicador")))

mat_r.click()

mat_r_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5122"
)))

mat_r_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_r_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_r_send.send_keys(str(mat_AP['set_ap_mat_1 Gratuidade Regimental'])) 

############################################################ Matrícula - Regimental Outubro #######################################################

mat_r = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5122'].indicador")))

mat_r.click()

mat_r_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5122"
)))

mat_r_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_r_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_r_send.send_keys(str(mat_AP['out_ap_mat_1 Gratuidade Regimental'])) 

############################################################ Matrícula - Regimental Novembro #######################################################

mat_r = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5122'].indicador")))

mat_r.click()

mat_r_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5122"
)))

mat_r_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_r_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_r_send.send_keys(str(mat_AP['nov_ap_mat_1 Gratuidade Regimental'])) 

############################################################ Matrícula - Regimental Dezembro #######################################################


mat_r = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5122'].indicador")))

mat_r.click()

mat_r_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5122"
)))

mat_r_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_r_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_r_send.send_keys(str(mat_AP['dez_ap_mat_1 Gratuidade Regimental']))

# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL CONCLUINTES NAO GRATUITA

############################################################ Concluinte - Nao Gratuita Janeiro #######################################################


mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5115'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5115"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['jan_ap_con_9 Pago por Pessoa Fisica ou Empresa'])) 

############################################################ Concluinte - Nao Gratuita Fevereiro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5115'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5115"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['fev_ap_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte - Nao Gratuita Março #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5115'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5115"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['mar_ap_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte - Nao Gratuita Abril #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5115'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5115"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['abr_ap_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte - Nao Gratuita Maio #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5115'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5115"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['mai_ap_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte - Nao Gratuita Junho #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5115'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5115"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['jun_ap_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte - Nao Gratuita Julho #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5115'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5115"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['jul_ap_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte - Nao Gratuita Agosto #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5115'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5115"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['ago_ap_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte - Nao Gratuita Setembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5115'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5115"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['set_ap_con_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Concluinte - Nao Gratuita Outubro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5115'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5115"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['out_ap_con_9 Pago por Pessoa Fisica ou Empresa']))


############################################################ Concluinte - Nao Gratuita Novembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5115'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5115"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['nov_ap_con_9 Pago por Pessoa Fisica ou Empresa']))




############################################################ Concluinte - Nao Gratuita Dezembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5115'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5115"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['dez_ap_con_9 Pago por Pessoa Fisica ou Empresa']))


# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL CONCLUINTES REGIMENTAL

############################################################ Concluinte - Regimental Janeiro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5116'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5116"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['jan_ap_con_1 Gratuidade Regimental']))

############################################################ Concluinte - Regimental Fevereiro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5116'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5116"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['fev_ap_con_1 Gratuidade Regimental']))

############################################################ Concluinte - Regimental Março #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5116'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5116"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['mar_ap_con_1 Gratuidade Regimental']))

############################################################ Concluinte - Regimental Abril #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5116'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5116"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['abr_ap_con_1 Gratuidade Regimental']))

############################################################ Concluinte - Regimental Maio #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5116'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5116"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['mai_ap_con_1 Gratuidade Regimental']))

############################################################ Concluinte - Regimental Junho #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5116'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5116"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['jun_ap_con_1 Gratuidade Regimental']))

############################################################ Concluinte - Regimental Julho #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5116'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5116"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['jul_ap_con_1 Gratuidade Regimental']))

############################################################ Concluinte - Regimental Agosto #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5116'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5116"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['ago_ap_con_1 Gratuidade Regimental']))

############################################################ Concluinte - Regimental Setembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5116'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5116"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['set_ap_con_1 Gratuidade Regimental']))

############################################################ Concluinte - Regimental Outubro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5116'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5116"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['out_ap_con_1 Gratuidade Regimental']))

############################################################ Concluinte - Regimental Novembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5116'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5116"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['nov_ap_con_1 Gratuidade Regimental']))

############################################################ Concluinte - Regimental Dezembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5116'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5116"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(con_AP['dez_ap_con_1 Gratuidade Regimental']))

# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL EVASAO NAO GRATUITA

############################################################ Evasão - Não Gratuita Janeiro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5117'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5117"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['jan_ap_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratuita Fevereiro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5117'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5117"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['fev_ap_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratuita Março #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5117'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5117"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['mar_ap_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratuita Abril #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5117'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5117"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['abr_ap_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratuita Maio #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5117'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5117"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['mai_ap_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratuita Junho #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5117'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5117"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['jun_ap_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratuita Julho #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5117'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5117"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['jul_ap_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratuita Agosto #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5117'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5117"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['ago_ap_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratuita Setembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5117'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5117"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['set_ap_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratuita Outubro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5117'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5117"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['out_ap_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratuita Novembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5117'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5117"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['nov_ap_eva_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Evasão - Não Gratuita Dezembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5117'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5117"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['dez_ap_eva_9 Pago por Pessoa Fisica ou Empresa']))

# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL EVASAO REGIMENTAL

############################################################ Evasão - Regimental Janeiro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5118'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5118"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['jan_ap_eva_1 Gratuidade Regimental']))

############################################################ Evasão - Regimental Fevereiro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5118'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5118"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['fev_ap_eva_1 Gratuidade Regimental']))

############################################################ Evasão - Regimental Março #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5118'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5118"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['mar_ap_eva_1 Gratuidade Regimental']))

############################################################ Evasão - Regimental Abril #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5118'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5118"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['abr_ap_eva_1 Gratuidade Regimental']))

############################################################ Evasão - Regimental Maio #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5118'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5118"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['mai_ap_eva_1 Gratuidade Regimental']))

############################################################ Evasão - Regimental Junho #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5118'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5118"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['jun_ap_eva_1 Gratuidade Regimental']))

############################################################ Evasão - Regimental Julho #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5118'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5118"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['jul_ap_eva_1 Gratuidade Regimental']))

############################################################ Evasão - Regimental Agosto #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5118'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5118"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['ago_ap_eva_1 Gratuidade Regimental']))

############################################################ Evasão - Regimental Setembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5118'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5118"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['set_ap_eva_1 Gratuidade Regimental']))


############################################################ Evasão - Regimental Outubro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5118'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5118"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['out_ap_eva_1 Gratuidade Regimental']))

############################################################ Evasão - Regimental Novembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5118'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5118"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['nov_ap_eva_1 Gratuidade Regimental']))


############################################################ Evasão - Regimental Dezembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5118'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5118"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(eva_AP['dez_ap_eva_1 Gratuidade Regimental']))

# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL HORA ALUNO NAO GRATUITA

############################################################ Hora aluno - Não Gratuita Janeiro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5119'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5119"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['jan_ap_ha_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Hora aluno - Não Gratuita Fevereiro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5119'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5119"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['fev_ap_ha_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Hora aluno - Não Gratuita Março #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5119'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5119"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['mar_ap_ha_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Hora aluno - Não Gratuita Abril #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5119'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5119"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['abr_ap_ha_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Hora aluno - Não Gratuita Maio #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(8) > [id='5119'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5119"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['mai_ap_ha_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Hora aluno - Não Gratuita Junho #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(9) > [id='5119'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5119"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['jun_ap_ha_9 Pago por Pessoa Fisica ou Empresa']))


############################################################ Hora aluno - Não Gratuita Julho #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(10) > [id='5119'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5119"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['jul_ap_ha_9 Pago por Pessoa Fisica ou Empresa']))


############################################################ Hora aluno - Não Gratuita Agosto #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(11) > [id='5119'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5119"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['ago_ap_ha_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Hora aluno - Não Gratuita Setembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(12) > [id='5119'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5119"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['set_ap_ha_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Hora aluno - Não Gratuita Outubro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(13) > [id='5119'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5119"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['out_ap_ha_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Hora aluno - Não Gratuita Novembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(14) > [id='5119'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5119"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['nov_ap_ha_9 Pago por Pessoa Fisica ou Empresa']))

############################################################ Hora aluno - Não Gratuita Dezembro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(15) > [id='5119'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5119"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['dez_ap_ha_9 Pago por Pessoa Fisica ou Empresa']))

# SENAI TAGUATINGA - 30303020101 - APRENDIZAGEM INDUSTRIAL PRESENCIAL HORA ALUNO REGIMENTAL

############################################################ Hora aluno - Regimental janeiro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5120'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5120"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['jan_ap_ha_1 Gratuidade Regimental']))

############################################################ Hora aluno - Regimental Fevereiro #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(5) > [id='5120'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5120"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['fev_ap_ha_1 Gratuidade Regimental']))


############################################################ Hora aluno - Regimental Março #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(6) > [id='5120'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5120"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['mar_ap_ha_1 Gratuidade Regimental']))

############################################################ Hora aluno - Regimental Abril #######################################################

mat_c = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(7) > [id='5120'].indicador")))

mat_c.click()

mat_c_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5120"
)))

mat_c_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

mat_c_send = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

mat_c_send.send_keys(str(ha_AP['abr_ap_ha_1 Gratuidade Regimental']))


############################################################ Hora aluno - Regimental Maio #######################################################

############################################################ Hora aluno - Regimental Junho #######################################################

############################################################ Hora aluno - Regimental Julho #######################################################

############################################################ Hora aluno - Regimental Agosto #######################################################

############################################################ Hora aluno - Regimental Setembro #######################################################

############################################################ Hora aluno - Regimental Outubro #######################################################

############################################################ Hora aluno - Regimental Novembro #######################################################

############################################################ Hora aluno - Regimental Dezembro #######################################################




