import pandas as pd
import openpyxl
import numpy as np
import si_janeiro
import pandas as pd

# SENAI TAGUATINGA INICIAÇÃO PROFISSIONAL PRESENCIAl #################################################################

def obter_matriculas_por_tipo_jan(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_matriculas_jan(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin(mes_referencia)
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin(anos_referencia)
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento
            
            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan]

            return len(base_filtrada)
    
    matriculas_por_tipo = MatriculasPorTipoFinanciamento(file_path)

    #Janeiro Ajustar o mes de referencia do relatorio atual

    jan_ip_mat_regi = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', '12024', ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '1 Gratuidade Regimental')
    jan_ip_mat_bolsa = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial','12024', ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '2 Gratuidade Não Regimental')
    jan_ip_mat_convenio = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial','12024', ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '3 Convênio')
    jan_ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial','12024', ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '9 Pago por Pessoa Fisica ou Empresa')


    return {
            "jan_ip_mat_regi": jan_ip_mat_regi,
            "jan_ip_mat_bolsa": jan_ip,
            "jan_ip_mat_convenio": jan_ip_mat_convenio,
            "jan_ip_mat_n_gratuita": jan_ip_mat_n_gratuita
    
    }

def obter_matriculas_por_tipo(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_matriculas(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin([mes_referencia])
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin([anos_referencia])
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan]

            #tipo_de_dados = base_filtrada.dtypes 

            #print(tipo_de_dados)

            return  len(base_filtrada)
        
            
        
    matriculas_por_tipo_g = MatriculasPorTipoFinanciamento(file_path)

    meses = {
        'fev': '2',
        'mar': '3',
        'abr': '4',
        'mai': '5',
        'jun': '6',
        'jul': '7',
        'ago': '8',
        'set': '9',
        'out': '10',
        'nov': '11',
        'dez': '12'
    }
    
    resultados_mat = {}
    
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_ip_mat_{tipo_financiamento}"
            resultados_mat[chave_resultado] = matriculas_por_tipo_g.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', '32024', mes_referencia,'2024', tipo_financiamento)
            
    
    return resultados_mat


def obter_concluintes_por_tipo(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_concluintes(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento,tipo_situacao):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin([mes_referencia])
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin([anos_referencia])
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento
            filtro_situa = self.data['SITUACAO_MATRICULA'] == tipo_situacao

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan & filtro_situa]

            #tipo_de_dados = base_filtrada.dtypes 

            #print(tipo_de_dados)

            return  len(base_filtrada)
        
            
        
    concluintes_por_tipo = MatriculasPorTipoFinanciamento(file_path)

    meses = {

        'jan': '1',
        'fev': '2',
        'mar': '3',
        'abr': '4',
        'mai': '5',
        'jun': '6',
        'jul': '7',
        'ago': '8',
        'set': '9',
        'out': '10',
        'nov': '11',
        'dez': '12'
    }
    
    resultados_conc = {}
    
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_ip_con_{tipo_financiamento}"
            resultados_conc[chave_resultado] = concluintes_por_tipo.contar_concluintes('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', '32024', mes_referencia,'2024', tipo_financiamento,'2 Concluída')
            
    
    return resultados_conc


def obter_evasao_por_tipo(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_evadidos(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento,tipo_situacao):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin([mes_referencia])
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin([anos_referencia])
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento
            filtro_situa = self.data['SITUACAO_MATRICULA'] == tipo_situacao

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan & filtro_situa]

            #tipo_de_dados = base_filtrada.dtypes 

            #print(tipo_de_dados)

            return  len(base_filtrada)
        
            
        
    evadidos_por_tipo = MatriculasPorTipoFinanciamento(file_path)

    meses = {
        'jan': '1',
        'fev': '2',
        'mar': '3',
        'abr': '4',
        'mai': '5',
        'jun': '6',
        'jul': '7',
        'ago': '8',
        'set': '9',
        'out': '10',
        'nov': '11',
        'dez': '12'
    }
    
    resultados_eva = {}
    
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_ip_eva_{tipo_financiamento}"
            resultados_eva[chave_resultado] = evadidos_por_tipo.contar_evadidos('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', '32024', mes_referencia,'2024', tipo_financiamento, '4 Evadida')
            
    
    return resultados_eva


#########################################################################################################################################################
#########################################################################################################################################################


# SENAI TAGUATINGA INICIAÇÃO PROFISSIONAL A DISTANCIA ################################################################

def obter_matriculas_IPD_TAG_jan(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_matriculas_jan(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin(mes_referencia)
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin(anos_referencia)
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento
            
            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan]

            return len(base_filtrada)
    
    matriculas_por_tipo = MatriculasPorTipoFinanciamento(file_path)

    #Janeiro Ajustar o mes de referencia do relatorio atual

    jan_ip_mat_regi = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '2 A distância', '12024', ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '1 Gratuidade Regimental')
    jan_ip_mat_bolsa = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '2 A distância','12024', ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '2 Gratuidade Não Regimental')
    jan_ip_mat_convenio = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '2 A distância','12024', ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '3 Convênio')
    jan_ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '2 A distância','12024', ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '9 Pago por Pessoa Fisica ou Empresa')


    return {
            "jan_ipd_mat_regi": jan_ip_mat_regi,
            "jan_ipd_mat_bolsa": jan_ip_mat_bolsa,
            "jan_ipd_mat_convenio": jan_ip_mat_convenio,
            "jan_ipd_mat_n_gratuita": jan_ip_mat_n_gratuita
    
    }

def obter_matriculas_IPD_TAG(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_matriculas(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin([mes_referencia])
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin([anos_referencia])
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan]

            #tipo_de_dados = base_filtrada.dtypes 

            #print(tipo_de_dados)

            return  len(base_filtrada)
        
            
        
    matriculas_por_tipo_g = MatriculasPorTipoFinanciamento(file_path)

    meses = {
        'fev': '2',
        'mar': '3',
        'abr': '4',
        'mai': '5',
        'jun': '6',
        'jul': '7',
        'ago': '8',
        'set': '9',
        'out': '10',
        'nov': '11',
        'dez': '12'
    }
    
    resultados_mat = {}
    
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_ipd_mat_{tipo_financiamento}"
            resultados_mat[chave_resultado] = matriculas_por_tipo_g.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '2 A distância', '32024', mes_referencia,'2024', tipo_financiamento)
            
    
    return resultados_mat


def obter_concluintes_IPD_TAG(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_concluintes(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento,tipo_situacao):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin([mes_referencia])
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin([anos_referencia])
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento
            filtro_situa = self.data['SITUACAO_MATRICULA'] == tipo_situacao

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan & filtro_situa]

            #tipo_de_dados = base_filtrada.dtypes 

            #print(tipo_de_dados)

            return  len(base_filtrada)
        
            
        
    concluintes_por_tipo = MatriculasPorTipoFinanciamento(file_path)

    meses = {

        'jan': '1',
        'fev': '2',
        'mar': '3',
        'abr': '4',
        'mai': '5',
        'jun': '6',
        'jul': '7',
        'ago': '8',
        'set': '9',
        'out': '10',
        'nov': '11',
        'dez': '12'
    }
    
    resultados_conc = {}
    
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_ipd_con_{tipo_financiamento}"
            resultados_conc[chave_resultado] = concluintes_por_tipo.contar_concluintes('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '2 A distância', '32024', mes_referencia,'2024', tipo_financiamento,'2 Concluída')
            
    
    return resultados_conc


def  obter_evasao_IPD_TAG(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_evadidos(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento,tipo_situacao):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin([mes_referencia])
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin([anos_referencia])
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento
            filtro_situa = self.data['SITUACAO_MATRICULA'] == tipo_situacao

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan & filtro_situa]

            #tipo_de_dados = base_filtrada.dtypes 

            #print(tipo_de_dados)

            return  len(base_filtrada)
        
            
        
    evadidos_por_tipo = MatriculasPorTipoFinanciamento(file_path)

    meses = {
        'jan': '1',
        'fev': '2',
        'mar': '3',
        'abr': '4',
        'mai': '5',
        'jun': '6',
        'jul': '7',
        'ago': '8',
        'set': '9',
        'out': '10',
        'nov': '11',
        'dez': '12'
    }
    
    resultados_eva = {}
    
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_ipd_eva_{tipo_financiamento}"
            resultados_eva[chave_resultado] = evadidos_por_tipo.contar_evadidos('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '2 A distância', '32024', mes_referencia,'2024', tipo_financiamento, '4 Evadida')
            
    
    return resultados_eva


# SENAI TAGUATINGA APRENDIZAGEM INDUSTRIAL PRESENCIAL ################################################################


def obter_matriculas_AP_TAG_jan(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_matriculas_jan(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin(mes_referencia)
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin(anos_referencia)
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento
            
            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan]

            return len(base_filtrada)
    
    matriculas_por_tipo = MatriculasPorTipoFinanciamento(file_path)

    #Janeiro Ajustar o mes de referencia do relatorio atual

    jan_ap_mat_regi = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '1 Presencial', '12024', ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '1 Gratuidade Regimental')
    jan_ap_mat_bolsa = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '1 Presencial','12024', ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '2 Gratuidade Não Regimental')
    jan_ap_mat_convenio = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '1 Presencial','12024', ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '3 Convênio')
    jan_ap_mat_n_gratuita = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '1 Presencial','12024', ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '9 Pago por Pessoa Fisica ou Empresa')


    return {
            "jan_ip_mat_regi": jan_ap_mat_regi,
            "jan_ip_mat_bolsa": jan_ap_mat_bolsa,
            "jan_ip_mat_convenio": jan_ap_mat_convenio,
            "jan_ip_mat_n_gratuita": jan_ap_mat_n_gratuita
    
    }

def obter_matriculas_AP_TAG(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_matriculas(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin([mes_referencia])
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin([anos_referencia])
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan]

            #tipo_de_dados = base_filtrada.dtypes 

            #print(tipo_de_dados)

            return  len(base_filtrada)
        
            
        
    matriculas_por_tipo_g = MatriculasPorTipoFinanciamento(file_path)

    meses = {
        'fev': '2',
        'mar': '3',
        'abr': '4',
        'mai': '5',
        'jun': '6',
        'jul': '7',
        'ago': '8',
        'set': '9',
        'out': '10',
        'nov': '11',
        'dez': '12'
    }
    
    resultados_mat = {}
    
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_ap_mat_{tipo_financiamento}"
            resultados_mat[chave_resultado] = matriculas_por_tipo_g.contar_matriculas('1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '1 Presencial', '32024', mes_referencia,'2024', tipo_financiamento)
            
    
    return resultados_mat

def obter_concluintes_AP_TAG(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_concluintes(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento,tipo_situacao):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin([mes_referencia])
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin([anos_referencia])
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento
            filtro_situa = self.data['SITUACAO_MATRICULA'] == tipo_situacao

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan & filtro_situa]

            #tipo_de_dados = base_filtrada.dtypes 

            #print(tipo_de_dados)

            return  len(base_filtrada)
        
            
        
    concluintes_por_tipo = MatriculasPorTipoFinanciamento(file_path)

    meses = {

        'jan': '1',
        'fev': '2',
        'mar': '3',
        'abr': '4',
        'mai': '5',
        'jun': '6',
        'jul': '7',
        'ago': '8',
        'set': '9',
        'out': '10',
        'nov': '11',
        'dez': '12'
    }
    
    resultados_conc = {}
    
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_ap_con_{tipo_financiamento}"
            resultados_conc[chave_resultado] = concluintes_por_tipo.contar_concluintes('1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '1 Presencial', '32024', mes_referencia,'2024', tipo_financiamento,'2 Concluída')
            
    
    return resultados_conc

def obter_evasao_AP_TAG(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_evadidos(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento,tipo_situacao):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin([mes_rela])
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin([mes_referencia])
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin([anos_referencia])
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento
            filtro_situa = self.data['SITUACAO_MATRICULA'] == tipo_situacao

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan & filtro_situa]

            #tipo_de_dados = base_filtrada.dtypes 

            #print(tipo_de_dados)

            return  len(base_filtrada)
        
            
        
    evadidos_por_tipo = MatriculasPorTipoFinanciamento(file_path)

    meses = {
        'jan': '1',
        'fev': '2',
        'mar': '3',
        'abr': '4',
        'mai': '5',
        'jun': '6',
        'jul': '7',
        'ago': '8',
        'set': '9',
        'out': '10',
        'nov': '11',
        'dez': '12'
    }
    
    resultados_eva = {}
    
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_ap_eva_{tipo_financiamento}"
            resultados_eva[chave_resultado] = evadidos_por_tipo.contar_evadidos('1117376 SENAI Taguatinga', '11 Aprendizagem Industrial básica', '1 Presencial', '32024', mes_referencia,'2024', tipo_financiamento, '4 Evadida')
            
    
    return resultados_eva
