import pandas as pd
import pyodbc
from sqlalchemy import create_engine
from si_janeiro_m_c_e import obter_matriculas_por_tipo_jan #
from si_janeiro_m_c_e import obter_matriculas_por_tipo #
from si_janeiro import obter_hora_por_tipo
from si_janeiro_m_c_e import obter_concluintes_por_tipo #
from si_janeiro_m_c_e import obter_evasao_por_tipo #
# Lendo os dados do Excel para um DataFrame do pandas
df = pd.read_excel('si_jan.xlsx')

dados_filtrados= obter_matriculas_por_tipo('si_jan.xlsx')
# Conectando ao SQL Server
server = 'SRV-DHW-01'
database = 'GPOG'
username = 'SISTEMAFIBRA\matheus.reck'
password = ''
driver = '{SQL Server}' # Isso depende do driver instalado, verifique a documentação do pyodbc para mais opções
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(conn_str)


# Salvando os dados do DataFrame no SQL Server
table_name = 'MATRICULA'  # Substitua 'nome_da_tabela' pelo nome da tabela no seu banco de dados
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={conn_str}')
df.to_sql(table_name, engine, index=False, if_exists='append')

print("Dados salvos no SQL Server com sucesso!")