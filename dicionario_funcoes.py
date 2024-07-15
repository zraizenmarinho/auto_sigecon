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
    # Clicando na célula correspondente ao mês
    mat_ipd_bolsa_mes = WebDriverWait(nav, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"td:nth-child({5 + i}) > [id='5073'].indicador"))
    )
    mat_ipd_bolsa_mes.click()

    mat_ipd_bolsa_mes = WebDriverWait(nav, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"))
    )

    # Montando a chave correta para acessar os dados
    chave_dado = f"{mes}_inicia_distan_mat_2 Gratuidade Não Regimental"
    
    # Acessando os dados de matrículas
    mat_iniciacao_distancia_bolsa = dados['iniciacao']['distancia']['matriculas'].get(chave_dado, 0)

    mat_ipd_bolsa_mes.send_keys(str(mat_iniciacao_distancia_bolsa))
    mat_ipd_bolsa_mes.send_keys(Keys.ENTER)

