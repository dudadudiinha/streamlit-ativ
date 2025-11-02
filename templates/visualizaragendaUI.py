import streamlit as st
from view import View 
import pandas as pd

class VisualizarAgendaUI:
    def main():
        st.header("Minha Agenda")
        id_profissional = st.session_state["usuario_id"]
        horarioss = View.horario_filtrar_profissional(id_profissional)
        if len(horarioss) == 0:
            st.write("Ainda não há horários cadastrados na agenda")
            return
        lista = []
        for h in horarioss:
            cliente_nome = "Disponível"
            if h.get_id_cliente() != None:
                cliente = View.cliente_listar_id(h.get_id_cliente()) 
                if cliente:
                    cliente_nome = cliente.get_nome()
            servico_nome = "Nenhum"
            if h.get_id_servico() != None:
                servico = View.servico_listar_id(h.get_id_servico())
                if servico:
                    servico_nome = servico.get_descricao()
            lista.append({"id": h.get_id(), "data": h.get_data().strftime("%d/%m/%Y %H:%M"), "confirmado": h.get_confirmado(), "cliente": cliente_nome, "serviço": servico_nome})
        if len(lista) > 0:
            df = pd.DataFrame(lista)
            st.dataframe(df, use_container_width=True)
        else:
            st.write("Nenhum horário encontrado")