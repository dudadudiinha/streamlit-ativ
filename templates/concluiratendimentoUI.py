import streamlit as st
import time
from datetime import datetime
from view import View

class ConcluirAtendimentoUI:
    def main():
        st.header("Concluir Atendimentos")
        id_profissional = st.session_state["usuario_id"]
        horarios = []
        for h in View.horario_listar():
            if h.get_id_profissional() == id_profissional and h.get_confirmado() and not h.get_concluido() and h.get_data() <= datetime.now():
                horarios.append(h)
        if len(horarios) == 0:
            st.info("Nenhum atendimento pendente de conclusão")
            return
        opcoes = []
        for h in horarios:
            cliente = View.cliente_listar_id(h.get_id_cliente())
            servico = View.servico_listar_id(h.get_id_servico())
            cliente_nome = cliente.get_nome() if cliente else "Cliente não encontrado"
            servico_desc = servico.get_descricao() if servico else "Serviço não encontrado"
            texto_opcao = (f"{h.get_data().strftime('%d/%m/%Y %H:%M')} | "f"Cliente: {cliente_nome} | "f"Serviço: {servico_desc}")
            opcoes.append(texto_opcao)
        st.write("Selecione o atendimento para concluir:")
        opcao_selecionada = st.selectbox("Atendimento Pendente", options=opcoes, label_visibility="collapsed")
        if st.button("Concluir"):
            try:
                indice_selecionado = opcoes.index(opcao_selecionada)
                horario_a_concluir = horarios[indice_selecionado]
                View.horario_concluir(horario_a_concluir.get_id())
                st.success("Atendimento concluído com sucesso")
                time.sleep(4)
                st.rerun()
            except ValueError as e:
                st.error(f"{e}")
