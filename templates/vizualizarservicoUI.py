import streamlit as st
from view import View
import pandas as pd

class VizualizarServicoUI:
    def main():
        st.header("Meus Serviços")
        dic = []
        horarios = View.horario_servicos(st.session_state["usuario_id"])
        for h in horarios:
            cliente = View.cliente_listar_id(h.get_id_cliente())
            servico = View.servico_listar_id(h.get_id_servico())
            profissional = View.profissional_listar_id(h.get_id_profissional())
            if cliente != None: cliente = cliente.get_nome()
            if servico != None: servico = servico.get_descricao()
            if profissional != None: profissional = profissional.get_nome()
            dic.append({"id": h.get_id(), "data": h.get_data(), "confirmado": h.get_confirmado(), "servico": servico, "profissional": profissional})
        if dic:
            df = pd.DataFrame(dic)
            st.dataframe(df) 