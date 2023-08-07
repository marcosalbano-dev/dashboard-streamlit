import pandas as pd
from conexao import conn

cursor = conn.cursor()

# LISTAGEM CADASTRADOS
cursor.execute(
    """SELECT DISTINCT ON (l.id) l.id AS id, terr.nom_territorio, m.nome AS nome_municipio, l.numero AS lote, l.proprietario AS proprietario,  
        COALESCE(l.cpf, l.cnpj) AS cpf_cnpj, l.nome AS nome_imovel, sj.nome AS situacao_juridica, l.sncr AS sncr, l.area AS area_medida
        FROM sige.lotes l
        JOIN ibge.municipios m ON l.municipio_id = m.id
        JOIN nom.territorio_mun tm ON tm.cod_mun = m.id
        JOIN nom.territorios terr ON terr.cod_territorio = tm.cod_territorio
        JOIN sige.situacoes_juridicas sj ON sj.id = l.situacao_juridica_id
        WHERE l.projeto_especial = false"""
)
listagem_cadastrados = cursor.fetchall()
df_listagem_cadastrados = pd.DataFrame(listagem_cadastrados, columns=['ID', 'TERRITÓRIO', 'MUNICÍPIO', 'LOTE', 'PROPRIETÁRIO', 'CPF_CNPJ', 'IMÓVEL', 'SITUAÇÃO JURÍDICA', 'SNCR', 'ÁREA'])

# # LISTAGEM TITULADOS
cursor.execute(
    """SELECT DISTINCT ON (l.id) l.id AS id, terr.nom_territorio, m.nome AS nome_municipio, l.numero AS lote, t.numero_titulo, l.proprietario AS proprietario,  
        COALESCE(l.cpf, l.cnpj) AS cpf_cnpj, l.nome AS nome_imovel, sj.nome AS situacao_juridica, l.sncr AS sncr,  l.area AS area_medida
        FROM sige.titulos t
        JOIN sige.lotes l ON l.id = t.lote_id
        JOIN ibge.municipios m ON m.id = l.municipio_id
        JOIN nom.territorio_mun tm ON tm.cod_mun = m.id
        JOIN nom.territorios terr ON terr.cod_territorio = tm.cod_territorio
        JOIN sige.situacoes_juridicas sj ON sj.id = l.situacao_juridica_id
        WHERE l.projeto_especial = false AND t.flag_cancelamento <> 'S' AND m.uf = 'CE'
    """
)
listagem_titulados = cursor.fetchall()
df_listagem_titulados = pd.DataFrame(listagem_titulados, columns=['ID', 'TERRITÓRIO', 'MUNICÍPIO', 'LOTE', 'TÍTULO', 'PROPRIETÁRIO', 'CPF_CNPJ', 'IMÓVEL', 'SITUAÇÃO JURÍDICA', 'SNCR', 'ÁREA'])

# # TOTAL CADASTRADOS POR TERRITÓRIO
# cursor.execute(
#     """SELECT x.nom_territorio, count(x.id) AS total_cadastrados FROM (
#         SELECT DISTINCT ON (l.id) l.id, m.nome AS nome_municipio_cadastrados, terr.nom_territorio
#         FROM sige.lotes l
#         JOIN ibge.municipios m ON l.municipio_id = m.id
#         JOIN nom.territorio_mun tm ON tm.cod_mun = m.id
#         JOIN nom.territorios terr ON terr.cod_territorio = tm.cod_territorio
#         JOIN sige.situacoes_juridicas sj ON sj.id = l.situacao_juridica_id
#         WHERE l.projeto_especial = false
#     ) x GROUP BY nom_territorio ORDER BY nom_territorio"""
# )
# total_cadastrados_por_territorio = cursor.fetchall()
# df_total_cadastrados_territorio = pd.DataFrame(total_cadastrados_por_territorio, columns=['TERRITÓRIO', 'TOTAL'])
# df_total_cadastrados_territorio['TOTAL'] = df_total_cadastrados_territorio['TOTAL'].astype(str)

# TOTAL CADASTRADOS POR MUNICÍPIO
# cursor.execute(
#     """SELECT x.nome_municipio_cadastrados, count(x.id) AS total_cadastrados FROM (
#         SELECT DISTINCT ON (l.id) l.id, m.nome AS nome_municipio_cadastrados, terr.nom_territorio
#         FROM sige.lotes l
#         JOIN ibge.municipios m ON l.municipio_id = m.id
#         JOIN nom.territorio_mun tm ON tm.cod_mun = m.id
#         JOIN nom.territorios terr ON terr.cod_territorio = tm.cod_territorio
#         JOIN sige.situacoes_juridicas sj ON sj.id = l.situacao_juridica_id
#         WHERE l.projeto_especial = false
#     ) x GROUP BY nome_municipio_cadastrados ORDER BY nome_municipio_cadastrados"""
# )
# total_cadastrados_por_municipio = cursor.fetchall()
# df_total_cadastrados_por_municipio = pd.DataFrame(total_cadastrados_por_municipio, columns=['TERRITÓRIO', 'TOTAL'])
# # df_total_cadastrados_por_municipio['TOTAL'] = df_total_cadastrados_por_municipio['TOTAL'].astype(str)


# # TOTAL TITULADOS
# cursor.execute(
#     """SELECT x.nom_territorio, count(x.id) AS total_titulados FROM (
#         SELECT DISTINCT ON (l.id) l.id, m.nome AS nome_municipio, terr.nom_territorio 
#         FROM sige.titulos t 
#         JOIN sige.lotes l ON l.id = t.lote_id 
#         JOIN ibge.municipios m ON m.id = l.municipio_id 
#         JOIN nom.territorio_mun tm ON tm.cod_mun = m.id
#         JOIN nom.territorios terr ON terr.cod_territorio = tm.cod_territorio
#         JOIN sige.situacoes_juridicas sj ON sj.id = l.situacao_juridica_id 
#         WHERE l.projeto_especial = false AND t.flag_cancelamento <> 'S'
#     ) x GROUP BY nom_territorio ORDER BY nom_territorio"""
# )
# total_titulados_por_territorio = cursor.fetchall()
# df_total_titulados_por_territorio = pd.DataFrame(total_titulados_por_territorio, columns=['TERRITÓRIO', 'TOTAL'])
# # df_total_titulados['TOTAL'] = df_total_titulados['TOTAL'].astype(str)
# # df_total_titulados['TOTAL'] = df_total_titulados['TOTAL'].str.replace(',', '')

# # # TOTAL MEDIDOS
# # cursor.execute(
# #     """SELECT x.nom_territorio, count(x.id) AS total_medidos FROM (
# #         SELECT DISTINCT ON (l.id) l.id, m.nome AS nome_municipio, terr.nom_territorio
# #         FROM sige.lotes l
# #         JOIN public.grafica g ON g.cod_mun = l.municipio_id AND g.cod_campo = l.numero
# #         JOIN ibge.municipios m ON l.municipio_id = m.id
# #         JOIN nom.territorio_mun tm ON tm.cod_mun = m.id
# #         JOIN nom.territorios terr ON terr.cod_territorio = tm.cod_territorio
# #         JOIN sige.situacoes_juridicas sj ON sj.id = l.situacao_juridica_id
# #         WHERE l.projeto_especial = false 
# #         ) x GROUP BY nom_territorio ORDER BY nom_territorio
# #     """
# #     )
# # total_medidos = cursor.fetchall()
# # df_total_medidos = pd.DataFrame(total_medidos, columns=['TERRITÓRIO', 'TOTAL'])
# # df_total_medidos['TOTAL'] = df_total_medidos['TOTAL'].astype(str)
# # # df_total_medidos['TOTAL'] = df_total_medidos['TOTAL'].str.replace('.', ',')


# # # TOTAL POSSES
# cursor.execute(
#     """SELECT x.nom_territorio, count(x.id) AS total_posses FROM ( 
#         SELECT DISTINCT ON (l.id) l.id, m.nome AS nome_municipio, terr.nom_territorio 
#         FROM sige.lotes l 
#         JOIN ibge.municipios m ON m.id = l.municipio_id
#         JOIN nom.territorio_mun tm ON tm.cod_mun = m.id
#         JOIN nom.territorios terr ON terr.cod_territorio = tm.cod_territorio
#         WHERE l.projeto_especial = false AND l.situacao_juridica_id = 1 
#         ) AS x GROUP BY nom_territorio ORDER BY nom_territorio
#     """
#     )
# total_posses = cursor.fetchall()
# df_total_posses = pd.DataFrame(total_posses, columns=['TERRITÓRIO', 'TOTAL'])
# # df_total_posses['TOTAL'] = df_total_posses['TOTAL'].astype(str)
# # df_total_posses['TOTAL'] = df_total_posses['TOTAL'].str.replace('.', ',')


# # # TOTAL POSSES A JUSTO TÍTULO
# cursor.execute(
#     """SELECT x.nom_territorio, count(x.id) AS total_justo_titulo FROM ( 
#         SELECT DISTINCT ON (l.id) l.id, m.nome AS nome_municipio, terr.nom_territorio 
#         FROM sige.lotes l 
#         JOIN ibge.municipios m ON m.id = l.municipio_id
#         JOIN nom.territorio_mun tm ON tm.cod_mun = m.id
#         JOIN nom.territorios terr ON terr.cod_territorio = tm.cod_territorio
#         WHERE l.projeto_especial = false AND l.situacao_juridica_id = 2 
#         ) AS x GROUP BY nom_territorio ORDER BY nom_territorio
#     """
#     )
# total_justo_titulo = cursor.fetchall()
# df_total_justo_titulo = pd.DataFrame(total_justo_titulo, columns=['TERRITÓRIO', 'TOTAL'])

# df_total_justo_titulo['TOTAL'] = df_total_justo_titulo['TOTAL'].astype(str)
# # # df_total_justo_titulo['TOTAL'] = df_total_justo_titulo['TOTAL'].str.replace('.', ',')

# # # TOTAL DOMÍNIOS
# cursor.execute(
#     """SELECT x.nom_territorio, count(x.id) AS total_dominios FROM ( 
#         SELECT DISTINCT ON (l.id) l.id, m.nome AS nome_municipio, terr.nom_territorio 
#         FROM sige.lotes l 
#         JOIN ibge.municipios m ON m.id = l.municipio_id
#         JOIN nom.territorio_mun tm ON tm.cod_mun = m.id
#         JOIN nom.territorios terr ON terr.cod_territorio = tm.cod_territorio
#         WHERE l.projeto_especial = false AND l.situacao_juridica_id = 3 
#         ) AS x GROUP BY nom_territorio ORDER BY nom_territorio
#     """
#     )
# total_dominios = cursor.fetchall()
# df_total_dominios = pd.DataFrame(total_dominios, columns=['TERRITÓRIO', 'TOTAL'])
# # df_total_dominios['TOTAL'] = df_total_dominios['TOTAL'].astype(str)
# # # df_total_dominios['TOTAL'] = df_total_dominios['TOTAL'].str.replace('.', ',')

# # # TOTAL INDEFINIDOS
# cursor.execute(
#     """SELECT x.nom_territorio, count(x.id) AS total_indefinidos FROM ( 
#         SELECT DISTINCT ON (l.id) l.id, m.nome AS nome_municipio, terr.nom_territorio 
#         FROM sige.lotes l 
#         JOIN ibge.municipios m ON m.id = l.municipio_id
#         JOIN nom.territorio_mun tm ON tm.cod_mun = m.id
#         JOIN nom.territorios terr ON terr.cod_territorio = tm.cod_territorio
#         WHERE l.projeto_especial = false AND l.situacao_juridica_id = 99 
#         ) AS x GROUP BY nom_territorio ORDER BY nom_territorio
#     """
#     )
# total_indefinidos = cursor.fetchall()
# df_total_indefinidos = pd.DataFrame(total_indefinidos, columns=['TERRITÓRIO', 'TOTAL'])
# # df_total_indefinidos['TOTAL'] = df_total_indefinidos['TOTAL'].astype(str)
# # # df_total_indefinidos['TOTAL'] = df_total_indefinidos['TOTAL'].str.replace('.', ',')





    

     
