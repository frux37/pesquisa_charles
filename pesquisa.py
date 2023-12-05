import numpy as np
#import matplotlib.pyplot as plt
import streamlit as st

# Função para calcular o tamanho da amostra
def calculate_sample_size(N, z=1.96, p=0.5, e=0.07):
    n = (z**2 * p * (1 - p) * N) / ((N - 1) * e**2 + z**2 * p * (1 - p))
    return int(np.ceil(n))  # Arredonda para o próximo número inteiro

# Interface do usuário com Streamlit
st.title("Tamanho da Amostra e Gráfico")

N = st.number_input("Tamanho da População (N):", min_value=1, step=1)

if st.button("Calcular Tamanho da Amostra"):
    sample_size = calculate_sample_size(N)
    st.write(f"Tamanho da Amostra Necessário: {sample_size}")

    # Gerar gráfico relacionado ao tamanho da amostra
    N_values = np.arange(1, N + 1)
    sample_sizes = [calculate_sample_size(N_val) for N_val in N_values]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(N_values, sample_sizes)
    ax.set_xlabel("Tamanho da População (N)")
    ax.set_ylabel("Tamanho da Amostra")
    ax.set_title("Relação entre Tamanho da População e Tamanho da Amostra")
    st.pyplot(fig)