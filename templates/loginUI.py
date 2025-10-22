import streamlit as st
from view import View

class LoginUI:
    def main():
        st.header("Logar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha)
            p = View.profissional_autenticar(email, senha)

            if c:
                st.session_state["usuario_tipo"] = "cliente"
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.session_state["categoria_usuario"] = "cliente"
                st.rerun()
            elif p:
                st.session_state["usuario_tipo"] = "profissional"
                st.session_state["usuario_id"] = p["id"]
                st.session_state["usuario_nome"] = p["nome"]
                st.session_state["categoria_usuario"] = "profissional"
                st.rerun()
            else:
                st.write("E-mail ou senha inválidos")