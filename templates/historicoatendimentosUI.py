import streamlit as st
import pandas as pd
from view import View

class HistoricoAtendimentosUI:
    def main():
        st.header("Histórico de Atendimentos")
        if "usuario_tipo" not in st.session_state:
            st.error("Usuário não identificado")
            return
        id_usuario = st.session_state["usuario_id"]
        tipo = st.session_state["usuario_tipo"]
        historico = View.historico(id_usuario, tipo)
        if len(historico) == 0:
            st.info("Nenhum atendimento concluído encontrado")
            return
        dados = [] 
        for h in historico:
            cliente = View.cliente_listar_id(h.get_id_cliente())
            servico = View.servico_listar_id(h.get_id_servico())
            profissional = View.profissional_listar_id(h.get_id_profissional())
            if cliente: nome_cliente = cliente.get_nome()
            else: nome_cliente = ""
            if profissional: nome_profissional = profissional.get_nome()
            else: nome_profissional = ""
            if servico: nome_servico = servico.get_descricao()
            else: nome_servico = ""
            dados.append({"Data": h.get_data().strftime("%d/%m/%Y %H:%M"), "Cliente": nome_cliente, "Profissional": nome_profissional, "Serviço": nome_servico})
        st.dataframe(pd.DataFrame(dados))
