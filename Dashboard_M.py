import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Remuneração", layout="wide")

# Dados
dados = {
    "Categoria": ["A", "B", "C", "D"],
    "EP_Mín": [1086.20, 1763.19, 1889.50, 2984.04],
    "EP_Med": [1556.40, 2216.62, 2401.41, 4254.70],
    "EP_Máx": [2078.98, 2788.89, 2593.73, 6558.53],
    "IP_Mín": [900.00, 1050.00, 1550.00, 3173.42],
    "IP_Med": [1002.50, 1182.50, 2086.96, 3948.40],
    "IP_Máx": [1105.00, 1315.00, 2623.92, 4723.37],
    "CP_Mín": [892.19, 1300.00, 2089.83, 2800.00],
    "CP_Med": [1003.04, 1458.62, 2340.84, 3500.00],
    "CP_Máx": [1113.90, 1617.23, 2591.84, 4200.00],
}
df = pd.DataFrame(dados)

# Interface
st.title("📊 Dashboard Interativo: Remuneração Pública (2024)")

st.sidebar.header("🔧 Filtros")

entidades = ["EP", "IP", "CP"]
tipos_salario = ["Mín", "Med", "Máx"]
categorias = ["A", "B", "C", "D"]

# Filtros interativos
entidade_selecionada = st.sidebar.selectbox("Entidade", entidades)
tipo_salario = st.sidebar.radio("Tipo de salário", tipos_salario)
categorias_selecionadas = st.sidebar.multiselect("Categorias", categorias, default=categorias)

# Preparar dados
coluna = f"{entidade_selecionada}_{tipo_salario}"
df_filtrado = df[df["Categoria"].isin(categorias_selecionadas)]

# Gráfico de barra para uma entidade
st.subheader(f"📌 Salário {tipo_salario} por categoria - {entidade_selecionada}")
fig1, ax1 = plt.subplots(figsize=(6, 3))
ax1.bar(df_filtrado["Categoria"], df_filtrado[coluna], color="skyblue")
ax1.set_ylabel("Salário (€)")
ax1.set_xlabel("Categoria")
ax1.set_title(f"Salários {tipo_salario} - {entidade_selecionada}")
ax1.grid(True)
st.pyplot(fig1)

st.markdown("---")

# Comparação entre entidades
st.subheader("📈 Comparação entre Entidades")

col1, col2 = st.columns(2)
with col1:
    ent1 = st.selectbox("Escolhe a 1ª entidade", entidades, key="ent1")
with col2:
    ent2 = st.selectbox("Escolhe a 2ª entidade", entidades, key="ent2")

tipo_comp = st.radio("Tipo de salário para comparar", tipos_salario, horizontal=True)

coluna1 = f"{ent1}_{tipo_comp}"
coluna2 = f"{ent2}_{tipo_comp}"

fig2, ax2 = plt.subplots(figsize=(6, 3))
ax2.plot(df["Categoria"], df[coluna1], label=f"{ent1} - {tipo_comp}", marker="o")
ax2.plot(df["Categoria"], df[coluna2], label=f"{ent2} - {tipo_comp}", marker="o")
ax2.set_ylabel("Salário (€)")
ax2.set_xlabel("Categoria")
ax2.set_title(f"Comparação: {ent1} vs {ent2} ({tipo_comp})")
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)


