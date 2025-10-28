import streamlit as st
from view import View
import time

class PerfilProfissionalUI:
    def main():
        st.header("Meus Dados")
        op = View.profissional_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome(), key="nomePC")
        especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade(), key="especialidadePC")
        conselho = st.text_input("Informe o novo conselho", op.get_conselho(), key="conselhoPC")
        email = st.text_input("Informe o novo e-mail", op.get_email(), key="emailPC")
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password", key="senhaPC")
        if st.button("Atualizar",key="atualizarPC"):
            id = op.get_id()
            try:
                View.profissional_atualizar(id, nome, especialidade, conselho, email, senha)
                st.success("Profissinal atualizado com sucesso")
            except ValueError as e:
                st.error(f"{e}")