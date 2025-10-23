import streamlit as st
from view import View 
import pandas as pd

class VisualizarAgendaUI:
    def main():
        st.header("Minha Agenda")
        if "usuario_id" not in st.session_state:
            st.error("Erro: Profissional não está logado")
            return
        id_profissional = st.session_state["usuario_id"]
        horarioss = View.horario_filtrar_profissional(id_profissional)
        if len(horarioss) == 0:
            st.write("Ainda não há horários cadastrados na agenda")
            return
        lista_formatada = []
        for h in horarioss:
            cliente_nome = "Disponível"
            if h.get_id_cliente() is not None:
                cliente = View.cliente_listar_id(h.get_id_cliente()) 
                if cliente:
                    cliente_nome = cliente.get_nome()
            servico_nome = "Nenhum"
            if h.get_id_servico() is not None:
                servico = View.servico_listar_id(h.get_id_servico())
                if servico:
                    servico_nome = servico.get_descricao()
            lista_formatada.append({"Data": h.get_data().strftime("%d/%m/%Y %H:%M"), "Confirmado": "Sim" if h.get_confirmado() else "Não", "Cliente": cliente_nome, "Serviço": servico_nome,"ID_Horario": h.get_id()})
        if len(lista_formatada) > 0:
            df = pd.DataFrame(lista_formatada)
            st.dataframe(df, use_container_width=True)
        else:
            st.write("Nenhum horário encontrado")