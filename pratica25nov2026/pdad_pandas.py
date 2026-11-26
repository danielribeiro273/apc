import os
import pandas as pd
import numpy as np

# Garante que o Python procura os ficheiros na mesma pasta onde o script está guardado
if '__file__' in globals():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ==========================================
# ETAPA 1: Ler e Inspecionar os Arquivos
# ==========================================
print("--- ETAPA 1 ---")
# Leitura dos dois ficheiros CSV e do dicionário Excel:
mor = pd.read_csv("moradores.csv", sep=";", decimal=",", encoding="utf-8-sig", low_memory=False)
dom = pd.read_csv("domicilios.csv", sep=";", decimal=",", encoding="utf-8-sig", low_memory=False)
dic = pd.read_excel("dicionario.xlsx")

print("Dimensões Moradores (Linhas, Colunas):", mor.shape)
print("Dimensões Domicílios (Linhas, Colunas):", dom.shape)
print("\nColunas do arquivo de moradores:")
print(mor.columns.tolist())

# ==========================================
# ETAPA 2: Selecionar Colunas e Tratar Sentinelas
# ==========================================
print("\n--- ETAPA 2 ---")
cols = ["localidade", "idade_calculada", "id_genero", "escolaridade", "renda_ind", "peso_mor"]
m = mor[cols].copy()

# Tratamento dos códigos sentinela (99999 e 88888) na renda
m["renda_ind"] = m["renda_ind"].replace([99999, 88888], np.nan)

# Mapeamento do dicionário para escolaridade e género
escolaridade_nome = {
    1: "Sem instrução", 
    2: "Fundamental incompleto", 
    3: "Fundamental completo",
    4: "Médio incompleto", 
    5: "Médio completo", 
    6: "Superior incompleto",
    7: "Superior completo", 
    8: "Sem classificação"
}
genero_nome = {1: "Masculino", 2: "Feminino"}

m["escolaridade_txt"] = m["escolaridade"].map(escolaridade_nome)
m["genero_txt"] = m["id_genero"].map(genero_nome)

print("Quantidade de rendas ausentes/tratadas:", m["renda_ind"].isna().sum())

# ==========================================
# ETAPA 3: Filtrar Linhas
# ==========================================
print("\n--- ETAPA 3 ---")
adultos = m[m["idade_calculada"] >= 18].copy()
idosos = m[m["idade_calculada"] >= 60]
adultos_superior = m[(m["idade_calculada"] >= 18) & (m["escolaridade"] == 7)]

print("Total de moradores com 60 anos ou mais (Atv 3a):", len(idosos))
print("Total de adultos com Superior Completo (Atv 3b):", len(adultos_superior))

# Comparação com laço for (Atv 3c)
contagem_for = 0
for idade in m["idade_calculada"]:
    if idade >= 60:
        contagem_for += 1
print(f"Validação com laço 'for' (60+ anos): {contagem_for} moradores.")

# ==========================================
# ETAPA 4: Agrupar e Contar
# ==========================================
print("\n--- ETAPA 4 ---")
# 4a. Tabela cruzada por género e escolaridade
print("\n--- Contagem por Gênero e Escolaridade (Adultos) ---")
print(pd.crosstab(adultos["genero_txt"], adultos["escolaridade_txt"]))

# 4b. Renda média por nível de escolaridade
print("\n--- Renda média por nível de escolaridade ---")
print(adultos.groupby("escolaridade_txt")["renda_ind"].mean().sort_values(ascending=False))

# Resumo por RA (Localidade)
resumo = adultos.groupby("localidade").agg(
    moradores=("renda_ind", "size"),
    renda_media=("renda_ind", "mean"),
    renda_mediana=("renda_ind", "median")
)
print("\nResumo por RA (5 primeiras):")
print(resumo.head())

# ==========================================
# ETAPA 5: Usar o Peso Amostral
# ==========================================
print("\n--- ETAPA 5 ---")
# População estimada por RA
pop_ra = m.groupby("localidade")["peso_mor"].sum().sort_values(ascending=False)

# Renda média simples vs ponderada no DF
r = adultos.dropna(subset=["renda_ind"])
media_simples = adultos["renda_ind"].mean()
media_pond = (r["renda_ind"] * r["peso_mor"]).sum() / r["peso_mor"].sum()

print(f"Renda média simples (DF): R$ {media_simples:.2f}")
print(f"Renda média ponderada (DF): R$ {media_pond:.2f}")

# 5b. Renda ponderada por RA
def media_ponderada(df, coluna, peso):
    df_limpo = df.dropna(subset=[coluna])
    return (df_limpo[coluna] * df_limpo[peso]).sum() / df_limpo[peso].sum()

renda_pond_ra = adultos.groupby("localidade").apply(media_ponderada, coluna="renda_ind", peso="peso_mor")
print("\nRenda ponderada por RA (5 primeiras):")
print(renda_pond_ra.head())

# 5c. Percentual estimado de adultos com superior completo no DF (somando pesos)
peso_adultos_total = adultos["peso_mor"].sum()
peso_adultos_superior = adultos[adultos["escolaridade"] == 7]["peso_mor"].sum()
pct_superior = (peso_adultos_superior / peso_adultos_total) * 100
print(f"\nPercentual estimado de adultos com Superior Completo no DF: {pct_superior:.2f}%")

# ==========================================
# ETAPA 6: Juntar Moradores e Domicílios
# ==========================================
print("\n--- ETAPA 6 ---")
comum = list(set(mor.columns) & set(dom.columns))
print("Colunas em comum entre as tabelas:", comum)

# Define explicitamente a chave do domicílio (A01nficha) para a junção
chave_dom = "A01nficha"

junto = mor.merge(dom, on=chave_dom, how="left", validate="many_to_one")
print("Dimensões após a junção (Linhas, Colunas):", junto.shape)

# ==========================================
# ETAPA 7: Salvar o Resultado
# ==========================================
print("\n--- ETAPA 7 ---")
# 7a. Gerar a planilha pedida por RA: População Estimada, Renda Média Ponderada e % Superior Completo
planilha_final = m.groupby("localidade").agg(
    populacao_estimada=("peso_mor", "sum")
).reset_index()

# Incorpora Renda Média Ponderada
planilha_final = planilha_final.merge(
    renda_pond_ra.reset_index(name="renda_media_ponderada"),
    on="localidade", 
    how="left"
)

# Incorpora % de Adultos com Superior Completo por RA
def pct_sup_ra(df):
    ad = df[df["idade_calculada"] >= 18]
    if ad["peso_mor"].sum() == 0:
        return np.nan
    return (ad[ad["escolaridade"] == 7]["peso_mor"].sum() / ad["peso_mor"].sum()) * 100

pct_sup_df = m.groupby("localidade").apply(pct_sup_ra).reset_index(name="pct_superior_completo")
planilha_final = planilha_final.merge(pct_sup_df, on="localidade", how="left")

# Exportar ficheiros
planilha_final.to_excel("resultado_pdad.xlsx", index=False)
m.to_csv("moradores_limpo.csv", sep=";", decimal=",", index=False, encoding="utf-8-sig")

print("\nSucesso! Os ficheiros 'resultado_pdad.xlsx' e 'moradores_limpo.csv' foram gerados na tua pasta.")