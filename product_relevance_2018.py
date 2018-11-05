import pandas as pd

df = pd.read_csv("./produto_vendas_visitas.txt", sep=';', names=["id_product","qtd_sales","qtd_visits"])

df = df.groupby("id_product", as_index=False).agg({"qtd_sales":"sum","qtd_visits":"sum"})

def calc_score_sales(row):
    # 2 * qtd_sales + qtd_visits
    return 2 * row[1] + row[2]

df["score"] = df.apply(calc_score_sales, axis=1)

df = df[["id_product","score"]].copy()

df.sort_values(["score"], inplace=True, ascending=False)

df.to_csv("./saida_product_rev_2018", index=False)

