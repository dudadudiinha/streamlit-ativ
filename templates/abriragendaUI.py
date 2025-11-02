import streamlit as st
from view import View 
from datetime import datetime, timedelta
import time

class AbrirAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")
        data = st.text_input("Informe a data no formato dd/mm/aaaa", "10/10/2025")
        hora_inicio = st.text_input("Informe o horário inicial no formato HH:MM", "10:10")
        hora_fim = st.text_input("Informe o horário final no formato HH:MM", "11:10")
        intervalo = st.text_input("Informe o intervalo entre os horários (min)", "10")
        servicos = View.servico_listar()
        servico_selecionado = st.selectbox("Selecione o serviço qiue será prestado", servicos, index=None)
        if st.button("Abrir Agenda"):
            try:
                intervalo_min = int(intervalo)
            except ValueError:
                st.error("O intervalo deve ser um número inteiro")
                return
            if intervalo_min < 5:
                st.error("O intervalo deve ser de no mínimo 5 minutos")
                return
            if servico_selecionado == None:
                st.error("A seleção de um serviço é obrigatória")
                return
            try:
                id_profissional = st.session_state["usuario_id"]
                id_servico = servico_selecionado.get_id()
                intervalo_delta = timedelta(minutes=intervalo_min)
                horario_atual = datetime.strptime(f"{data} {hora_inicio}", "%d/%m/%Y %H:%M")
                horario_final = datetime.strptime(f"{data} {hora_fim}", "%d/%m/%Y %H:%M") 
                horarios_inseridos = 0
                while horario_atual < horario_final:
                    View.horario_inserir(horario_atual, False, None, id_servico, id_profissional)
                    horario_atual += intervalo_delta
                    horarios_inseridos += 1
                if horarios_inseridos > 0:
                    st.success(f"{horarios_inseridos} horários inseridos com sucesso")
                    time.sleep(4) 
                    st.rerun()
                else:
                    st.warning("Nenhum horário foi inserido")
            except ValueError as e:
                if "unconverted data remains" in str(e) or "does not match format" in str(e):
                    st.error("O formato da data está incorreto. Use exatamente DD/MM/AAAA HH:MM")
                else: st.error(f"{e}")