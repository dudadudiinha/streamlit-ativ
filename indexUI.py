import streamlit as st
from templates.abrircontaUI import AbrirContaUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.agendarservicoUI import AgendarServicoUI
from templates.alterarsenhaUI import AlterarSenhaUI
from templates.concluiratendimentoUI import ConcluirAtendimentoUI
from templates.confirmarservicoUI import ConfirmarServicoUI
from templates.historicoatendimentosUI import HistoricoAtendimentosUI
from templates.loginUI import LoginUI
from templates.perfilclienteUI import PerfilClienteUI
from templates.perfilprofissionalUI import PerfilProfissionalUI
from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.visualizaragendaUI import VisualizarAgendaUI
from templates.vizualizarservicoUI import VizualizarServicoUI
from view import View

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Meus Serviços", "Histórico de Atendimentos"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()
        if op == "Meus Serviços": VizualizarServicoUI.main()
        if op == "Histórico de Atendimentos": HistoricoAtendimentosUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Abrir Minha Agenda", "Minha Agenda", "Confirmar Serviço", "Concluir Atendimentos", "Histórico de Atendimentos"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op == "Abrir Minha Agenda": AbrirAgendaUI.main()
        if op == "Minha Agenda": VisualizarAgendaUI.main()
        if op == "Confirmar Serviço": ConfirmarServicoUI.main()
        if op == "Concluir Atendimentos": ConcluirAtendimentoUI.main()
        if op == "Histórico de Atendimentos": HistoricoAtendimentosUI.main()

    def menu_admin(): 
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários","Cadastro de Profissionais", "Histórico de Atendimentos", "Alterar Senha"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Histórico de Atendimentos": HistoricoAtendimentosUI.main()
        if op == "Alterar Senha": AlterarSenhaUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " +
            st.session_state["usuario_nome"])
            if admin: 
                IndexUI.menu_admin()
            elif st.session_state["usuario_tipo"] == "profissional": 
                IndexUI.menu_profissional()
            else: 
                IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    def main():
        View.cliente_criar_admin()
        IndexUI.sidebar()

IndexUI.main()