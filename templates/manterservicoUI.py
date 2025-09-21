import streamlit as st
import pandas as pd
import time
from view import View

class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()
    
    def listar():
        servicos = View.servico_listar()
        if len(servicos) == 0: 
            st.write("Nenhum serviço cadastrado")
        else:
            list_dic = []
            for s in servicos: list_dic.append(s.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe a descrição")
        valor = st.number_input("Informe o valor", format="%.2f")
        if st.button("Inserir"):
            View.servico_inserir(descricao, valor)
            st.success("Serviço inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        View.servico_atualizar()

    def excluir():
        View.servico_excluir()