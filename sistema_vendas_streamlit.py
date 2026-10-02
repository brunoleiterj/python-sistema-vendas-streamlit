import streamlit as st
import pandas as pd
import plotly.express as px

vendedores = ["Bruno", "Ethan", "Gab"]
produtos = ["Notebook", "Smartphone", "Headset"]
tabela_vendas = pd.read_csv("vendas.csv")


st.sidebar.write("Cadastrar Vendas")
st.write("# Sistema de Vendas")

data = st.sidebar.date_input('Data', min_value="today")
vendedor = st.sidebar.selectbox("Vendedor", vendedores)
produto = st.sidebar.selectbox("Produto", produtos)
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")

btn_cadastrar = st.sidebar.button("Cadastrar Venda")

if btn_cadastrar:
    if quantidade == 0 or valor == 0:
        st.warning("Venda com erro de preenchimento")
    else:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.success("Venda Cadastrada!")


st.write("## Cadastrar Vendas")
st.dataframe(tabela_vendas)

#id_venda = st.number_input("ID Venda", step=1)
#botao_pesquisar = st.button("Pesquisar")

botao_remover_ultima_venda = st.button("Remover última venda")

if botao_remover_ultima_venda:
    ultima_linha = tabela_vendas.index[-1]
    tabela_vendas = tabela_vendas.drop(ultima_linha)
    tabela_vendas.to_csv("vendas.csv", index=False)

st.write("## Vendas Cadastradas")

st.write("## Dashboard")
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}.")


grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)