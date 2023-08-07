# Este arquivo é parte do programa Map&MEC
# Map&MEC é um software livre; você pode redistribuí-lo e/ou
# modificá-lo sob os termos da Licença Pública Geral GNU como publicada
# pela Free Software Foundation; na versão 3 da Licença, ou
# (a seu critério) qualquer versão posterior.
#
# Este programa é distribuído na esperança de que possa ser útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
# a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para mais detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU junto
# com este programa. Se não, veja <http://www.gnu.org/licenses/>.


import base64
import streamlit as st
import pandas as pd
from funcoes import *  # Garantir que funcoes.py esteja no mesmo diretório ou no PYTHONPATH

# Layout principal do aplicativo
st.sidebar.title("Menu")
selected_option = st.sidebar.radio("Selecione uma opção:", ["Processador de Dados", "Tutorial download SIGA"])

st.sidebar.markdown("###### Atenção, após baixar o arquivo observe que nem todas as informação estão completas.")
st.sidebar.markdown("###### Esta aplicação ainda esta em desenvolvimento e pode ser melhorada. Se você puder contrubuir, entre em contato: arana@ufpr.br")
if selected_option == "Processador de Dados":
    # Título da página
    st.title("🌐 Map&MEC 📈")
    st.subheader("Processador de Dados dos Docentes para planilha do MEC")
    # Texto explicativo
    st.write("Bem-vindo(a) à aplicação de processamento de dados dos docentes!")
    st.write("Esta ferramenta foi projetada para facilitar a organização e consolidação dos dados dos docentes da UFPR, extraídos do SIGA e da PROGEPE.")
    # Introdução
    st.subheader("Siga as instruções para utilizar a aplicação")
    st.write("1️⃣ Faça o download dos dados do SIGA: Os usuários devem fazer upload de um arquivo CSV com dados dos docentes extraídos diretamente do SIGA. Veja o tutorial no Menu \"Tutorial download SIGA\"")
    st.write("2️⃣ Faça o upload dos dados do SIGA em \"Processador de Dados\": A aplicação processará automaticamente os dados, fazendo comparações, removendo duplicatas e estruturando-os conforme os padrões da planilha do INEP.")
    st.write("3️⃣ Faça o download dos Dados Processados: Após o processamento, o usuário poderá baixar o arquivo em formato Excel, que estará pronto para ser utilizado em outros sistemas ou para análise.")

    uploaded_file = st.file_uploader("👉Carregue o arquivo CSV com os dados dos docentes extraídos do SIGA.", type="csv")
    st.write("🚨Lembre-se de adicionar todas as colunas.")
    if uploaded_file is not None:
        output = process_file(uploaded_file)
        if output:
            b64 = base64.b64encode(output.getvalue()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="Dados_docentes_MEC-ok.xlsx">Baixar arquivo Excel</a>'
        st.markdown(href, unsafe_allow_html=True)

        #st.markdown(get_download_link("DADOS_MEC/Dados_docentes_MEC-ok.xlsx", "Dados_docentes_MEC-ok.xlsx"), unsafe_allow_html=True)

    st.write("⚠️Esta aplicação não armazena nenhum dos dados carregados após a sessão terminar.")
    st.write("👍A privacidade e a integridade dos seus dados são nossa prioridade.")


else:  # selected_option == "Tutorial"
    show_tutorial()

# Logo do curso
logo_curso_path = "IMAGEM/LOGO_CARTO.png"
# Logo do UFPR
logo_ufpr_path = "IMAGEM/LOGO_UFPR.png"

# Colocar as duas imagens lado a lado
col1, col2 = st.sidebar.columns(2)

# Inserir a primeira imagem na primeira coluna
col1.image(logo_curso_path, use_column_width=True)

# Inserir a segunda imagem na segunda coluna
col2.image(logo_ufpr_path, use_column_width=True)

st.sidebar.markdown("###### 👨‍💻 Developed by: Prof. Dr. Daniel Arana, Map&Ação")
st.sidebar.markdown("###### GNU GENERAL PUBLIC LICENSE - V3")