import streamlit as st
import pandas as pd
import time
from view import View

class ManterProfissionalUI:
    @staticmethod
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    @staticmethod
    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: 
            st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for pro in profissionais: 
                p = pro.to_json()
                if "senha" in p:
                    del p["senha"]
                list_dic.append(p)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    
    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome")
        especialidade = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        email = st.text_input("Informe o email")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            try:
                View.profissional_inserir(nome, especialidade, conselho, email, senha)
                st.success("Profissional inserido com sucesso")
                time.sleep(4)
                st.rerun()
            except ValueError as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def atualizar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de Profissionais", profissionais)
            nome = st.text_input("Novo nome", op.get_nome())
            especialidade = st.text_input("Nova especialidade", op.get_especialidade())
            conselho = st.text_input("Novo conselho", op.get_conselho())
            email = st.text_input("Novo email", op.get_email())
            senha = st.text_input("Nova senha", op.get_senha(), type="password")
        if st.button("Atualizar"): 
            id = op.get_id()
            try:
                View.profissional_atualizar(id, nome, especialidade, conselho, email, senha)
                st.success("Profissional atualizado com sucesso")
                time.sleep(4)
                st.rerun()
            except ValueError as e:
                st.error(f"Erro: {e}")
    
    @staticmethod
    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de Profissionais", profissionais)
            if st.button("Excluir"):
                id = op.get_id()
                try:
                    View.profissional_excluir(id)
                    st.success("Profissional excluído com sucesso")
                    time.sleep(4)
                    st.rerun()
                except ValueError as e:
                    st.error(f"Erro: {e}")