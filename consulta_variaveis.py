

from si_janeiro_m_c_e import obter_matriculas_QP_TAG_jan #
from si_janeiro_m_c_e import obter_matriculas_QP_TAG #
from si_janeiro import obter_hora_QP_TAG
from si_janeiro_m_c_e import obter_concluintes_QP_TAG #
from si_janeiro_m_c_e import obter_evasao_QP_TAG #

mat_jan_QP = obter_matriculas_QP_TAG_jan('si_jan.xlsx')
mat_QP = obter_matriculas_QP_TAG('si_jan.xlsx')
ha_QP = obter_hora_QP_TAG('si_jan.xlsx')
con_QP = obter_concluintes_QP_TAG('si_jan.xlsx')
eva_QP = obter_evasao_QP_TAG('si_jan.xlsx')

print(eva_QP)

#Matricula JANEIRO

{'jan_qp_mat_regi': 814, 'jan_qp_mat_bolsa': 2, 'jan_qp_mat_convenio': 0, 'jan_qp_mat_n_gratuita': 337}

#MATRICULA MESES

{'fev_qp_mat_1 Gratuidade Regimental': 74, 'fev_qp_mat_2 Gratuidade Não Regimental': 0, 'fev_qp_mat_3 Convênio': 0, 'fev_qp_mat_9 Pago por Pessoa Fisica ou Empresa': 114, 'mar_qp_mat_1 Gratuidade Regimental': 317, 'mar_qp_mat_2 Gratuidade Não Regimental': 1, 'mar_qp_mat_3 Convênio': 0, 'mar_qp_mat_9 Pago por Pessoa Fisica ou Empresa': 1511, 'abr_qp_mat_1 Gratuidade Regimental': 0, 'abr_qp_mat_2 Gratuidade Não Regimental': 0, 'abr_qp_mat_3 Convênio': 0, 'abr_qp_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'mai_qp_mat_1 Gratuidade Regimental': 0, 'mai_qp_mat_2 Gratuidade Não Regimental': 0, 'mai_qp_mat_3 Convênio': 0, 'mai_qp_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'jun_qp_mat_1 Gratuidade Regimental': 0, 'jun_qp_mat_2 Gratuidade Não Regimental': 0, 'jun_qp_mat_3 Convênio': 0, 'jun_qp_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'jul_qp_mat_1 Gratuidade Regimental': 0, 'jul_qp_mat_2 Gratuidade Não Regimental': 0, 'jul_qp_mat_3 Convênio': 0, 'jul_qp_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'ago_qp_mat_1 Gratuidade Regimental': 0, 'ago_qp_mat_2 Gratuidade Não Regimental': 0, 'ago_qp_mat_3 Convênio': 0, 'ago_qp_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'set_qp_mat_1 Gratuidade Regimental': 0, 'set_qp_mat_2 Gratuidade Não Regimental': 0, 'set_qp_mat_3 Convênio': 0, 'set_qp_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'out_qp_mat_1 Gratuidade Regimental': 0, 'out_qp_mat_2 Gratuidade Não Regimental': 0, 'out_qp_mat_3 Convênio': 0, 'out_qp_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'nov_qp_mat_1 Gratuidade Regimental': 0, 'nov_qp_mat_2 Gratuidade Não Regimental': 0, 'nov_qp_mat_3 Convênio': 0, 'nov_qp_mat_9 Pago por Pessoa Fisica ou Empresa': 0, 'dez_qp_mat_1 Gratuidade Regimental': 0, 'dez_qp_mat_2 Gratuidade Não Regimental': 0, 'dez_qp_mat_3 Convênio': 0, 'dez_qp_mat_9 Pago por Pessoa Fisica ou Empresa': 0}


#HORA ALUNO

{'jan_qp_ha_1 Gratuidade Regimental': 9464, 'jan_qp_ha_2 Gratuidade Não Regimental': 0, 'jan_qp_ha_3 Convênio': 0, 'jan_qp_ha_9 Pago por Pessoa Fisica ou Empresa': 357, 'fev_qp_ha_1 Gratuidade Regimental': 22641, 'fev_qp_ha_2 Gratuidade Não Regimental': 0, 'fev_qp_ha_3 Convênio': 0, 'fev_qp_ha_9 Pago por Pessoa Fisica ou Empresa': 3949, 'mar_qp_ha_1 Gratuidade Regimental': 28708, 'mar_qp_ha_2 Gratuidade Não Regimental': 21, 'mar_qp_ha_3 Convênio': 0, 'mar_qp_ha_9 Pago por Pessoa Fisica ou Empresa': 98856, 'abr_qp_ha_1 Gratuidade Regimental': 0, 'abr_qp_ha_2 Gratuidade Não Regimental': 0, 'abr_qp_ha_3 Convênio': 0, 'abr_qp_ha_9 Pago por Pessoa Fisica ou Empresa': 0, 'mai_qp_ha_1 Gratuidade Regimental': 0, 'mai_qp_ha_2 Gratuidade Não Regimental': 0, 'mai_qp_ha_3 Convênio': 0, 'mai_qp_ha_9 Pago por Pessoa Fisica ou Empresa': 0, 'jun_qp_ha_1 Gratuidade Regimental': 0, 'jun_qp_ha_2 Gratuidade Não Regimental': 0, 'jun_qp_ha_3 Convênio': 0, 'jun_qp_ha_9 Pago por Pessoa Fisica ou Empresa': 0, 'jul_qp_ha_1 Gratuidade Regimental': 0, 'jul_qp_ha_2 Gratuidade Não Regimental': 0, 'jul_qp_ha_3 Convênio': 0, 'jul_qp_ha_9 Pago por Pessoa Fisica ou Empresa': 0, 'ago_qp_ha_1 Gratuidade Regimental': 0, 'ago_qp_ha_2 Gratuidade Não Regimental': 0, 'ago_qp_ha_3 Convênio': 0, 'ago_qp_ha_9 Pago por Pessoa Fisica ou Empresa': 0, 'set_qp_ha_1 Gratuidade Regimental': 0, 'set_qp_ha_2 Gratuidade Não Regimental': 0, 'set_qp_ha_3 Convênio': 0, 'set_qp_ha_9 Pago por Pessoa Fisica ou Empresa': 0, 'out_qp_ha_1 Gratuidade Regimental': 0, 'out_qp_ha_2 Gratuidade Não Regimental': 0, 'out_qp_ha_3 Convênio': 0, 'out_qp_ha_9 Pago por Pessoa Fisica ou Empresa': 0, 'nov_qp_ha_1 Gratuidade Regimental': 0, 'nov_qp_ha_2 Gratuidade Não Regimental': 0, 'nov_qp_ha_3 Convênio': 0, 'nov_qp_ha_9 Pago por Pessoa Fisica ou Empresa': 0, 'dez_qp_ha_1 Gratuidade Regimental': 0, 'dez_qp_ha_2 Gratuidade Não Regimental': 0, 'dez_qp_ha_3 Convênio': 0, 'dez_qp_ha_9 Pago por Pessoa Fisica ou Empresa': 0}


#CONCLUINTES

{'jan_qp_con_1 Gratuidade Regimental': 0, 'jan_qp_con_2 Gratuidade Não Regimental': 0, 'jan_qp_con_3 Convênio': 0, 'jan_qp_con_9 Pago por Pessoa Fisica ou Empresa': 0, 'fev_qp_con_1 Gratuidade Regimental': 0, 'fev_qp_con_2 Gratuidade Não Regimental': 0, 'fev_qp_con_3 Convênio': 0, 'fev_qp_con_9 Pago por Pessoa Fisica ou Empresa': 0, 'mar_qp_con_1 Gratuidade Regimental': 0, 'mar_qp_con_2 Gratuidade Não Regimental': 0, 'mar_qp_con_3 Convênio': 0, 'mar_qp_con_9 Pago por Pessoa Fisica ou Empresa': 0, 'abr_qp_con_1 Gratuidade Regimental': 0, 'abr_qp_con_2 Gratuidade Não Regimental': 0, 'abr_qp_con_3 Convênio': 0, 'abr_qp_con_9 Pago por Pessoa Fisica ou Empresa': 0, 'mai_qp_con_1 Gratuidade Regimental': 0, 'mai_qp_con_2 Gratuidade Não Regimental': 0, 'mai_qp_con_3 Convênio': 0, 'mai_qp_con_9 Pago por Pessoa Fisica ou Empresa': 0, 'jun_qp_con_1 Gratuidade Regimental': 0, 'jun_qp_con_2 Gratuidade Não Regimental': 0, 'jun_qp_con_3 Convênio': 0, 'jun_qp_con_9 Pago por Pessoa Fisica ou Empresa': 0, 'jul_qp_con_1 Gratuidade Regimental': 0, 'jul_qp_con_2 Gratuidade Não Regimental': 0, 'jul_qp_con_3 Convênio': 0, 'jul_qp_con_9 Pago por Pessoa Fisica ou Empresa': 0, 'ago_qp_con_1 Gratuidade Regimental': 0, 'ago_qp_con_2 Gratuidade Não Regimental': 0, 'ago_qp_con_3 Convênio': 0, 'ago_qp_con_9 Pago por Pessoa Fisica ou Empresa': 0, 'set_qp_con_1 Gratuidade Regimental': 0, 'set_qp_con_2 Gratuidade Não Regimental': 0, 'set_qp_con_3 Convênio': 0, 'set_qp_con_9 Pago por Pessoa Fisica ou Empresa': 0, 'out_qp_con_1 Gratuidade Regimental': 0, 'out_qp_con_2 Gratuidade Não Regimental': 0, 'out_qp_con_3 Convênio': 0, 'out_qp_con_9 Pago por Pessoa Fisica ou Empresa': 0, 'nov_qp_con_1 Gratuidade Regimental': 0, 'nov_qp_con_2 Gratuidade Não Regimental': 0, 'nov_qp_con_3 Convênio': 0, 'nov_qp_con_9 Pago por Pessoa Fisica ou Empresa': 0, 'dez_qp_con_1 Gratuidade Regimental': 0, 'dez_qp_con_2 Gratuidade Não Regimental': 0, 'dez_qp_con_3 Convênio': 0, 'dez_qp_con_9 Pago por Pessoa Fisica ou Empresa': 0}


#Evadidos

{'jan_qp_eva_1 Gratuidade Regimental': 0, 'jan_qp_eva_2 Gratuidade Não Regimental': 0, 'jan_qp_eva_3 Convênio': 0, 'jan_qp_eva_9 Pago por Pessoa Fisica ou Empresa': 0, 'fev_qp_eva_1 Gratuidade Regimental': 1, 'fev_qp_eva_2 Gratuidade Não Regimental': 0, 'fev_qp_eva_3 Convênio': 0, 'fev_qp_eva_9 Pago por Pessoa Fisica ou Empresa': 3, 'mar_qp_eva_1 Gratuidade Regimental': 1, 'mar_qp_eva_2 Gratuidade Não Regimental': 0, 'mar_qp_eva_3 Convênio': 0, 'mar_qp_eva_9 Pago por Pessoa Fisica ou Empresa': 1, 'abr_qp_eva_1 Gratuidade Regimental': 0, 'abr_qp_eva_2 Gratuidade Não Regimental': 0, 'abr_qp_eva_3 Convênio': 0, 'abr_qp_eva_9 Pago por Pessoa Fisica ou Empresa': 0, 'mai_qp_eva_1 Gratuidade Regimental': 0, 'mai_qp_eva_2 Gratuidade Não Regimental': 0, 'mai_qp_eva_3 Convênio': 0, 'mai_qp_eva_9 Pago por Pessoa Fisica ou Empresa': 0, 'jun_qp_eva_1 Gratuidade Regimental': 0, 'jun_qp_eva_2 Gratuidade Não Regimental': 0, 'jun_qp_eva_3 Convênio': 0, 'jun_qp_eva_9 Pago por Pessoa Fisica ou Empresa': 0, 'jul_qp_eva_1 Gratuidade Regimental': 0, 'jul_qp_eva_2 Gratuidade Não Regimental': 0, 'jul_qp_eva_3 Convênio': 0, 'jul_qp_eva_9 Pago por Pessoa Fisica ou Empresa': 0, 'ago_qp_eva_1 Gratuidade Regimental': 0, 'ago_qp_eva_2 Gratuidade Não Regimental': 0, 'ago_qp_eva_3 Convênio': 0, 'ago_qp_eva_9 Pago por Pessoa Fisica ou Empresa': 0, 'set_qp_eva_1 Gratuidade Regimental': 0, 'set_qp_eva_2 Gratuidade Não Regimental': 0, 'set_qp_eva_3 Convênio': 0, 'set_qp_eva_9 Pago por Pessoa Fisica ou Empresa': 0, 'out_qp_eva_1 Gratuidade Regimental': 0, 'out_qp_eva_2 Gratuidade Não Regimental': 0, 'out_qp_eva_3 Convênio': 0, 'out_qp_eva_9 Pago por Pessoa Fisica ou Empresa': 0, 'nov_qp_eva_1 Gratuidade Regimental': 0, 'nov_qp_eva_2 Gratuidade Não Regimental': 0, 'nov_qp_eva_3 Convênio': 0, 'nov_qp_eva_9 Pago por Pessoa Fisica ou Empresa': 0, 'dez_qp_eva_1 Gratuidade Regimental': 0, 'dez_qp_eva_2 Gratuidade Não Regimental': 0, 'dez_qp_eva_3 Convênio': 0, 'dez_qp_eva_9 Pago por Pessoa Fisica ou Empresa': 0}





from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebPageElements:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_css_with_nth_child_and_id(self, child_number, id_value):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({child_number}) > [id='{id_value}'].indicador"))
        )

    def find_element_by_id(self, id_value):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, id_value))
        )

    def find_element_by_class_name(self, class_name):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, class_name))
        )

    def find_element_by_xpath(self, xpath):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

# Função para iterar sobre os meses e realizar a lógica
def iterar_sobre_meses(nav):
    page_elements = WebPageElements(nav)
    meses = ["Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    for index, mes in enumerate(meses, start=5):  # Começa do índice 5 (correspondente a Fevereiro)
        mat_c = page_elements.find_element_by_css_with_nth_child_and_id(index, "5033")
        mat_c.click()

        mat_c_id = page_elements.find_element_by_id("5033")
        mat_c_popover = page_elements.find_element_by_class_name("popover-content")
        mat_c_send = page_elements.find_element_by_xpath("(//input[@type='text'])[8]")

        mat_c_send.send_keys(str(mat_QP[f'{mes}_qp_mat_9 Pago por Pessoa Fisica ou Empresa']))

# Exemplo de uso:
iterar_sobre_meses(nav)


from web_page_elements import WebPageElements


#Janeiro
#Fevereiro
#Marco
#Abril
#Maio
#Junho
#Julho
#Agosto
#Setembro
#Outubro
#Novembro
#Dezembro
