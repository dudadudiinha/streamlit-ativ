import streamlit as st
from view import View
import time

class AgendarServicoUI:
    def main():
        st.header("Agendar Serviço")
        prof = View.profissional_listar()
        if len(prof) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            profissional = st.selectbox("Informe o profissional", prof)
            horarios = View.horario_agendar_horario(profissional.get_id())
            if len(horarios) == 0:
                st.write("Nenhum horário disponível")
            else:
                opcoes = []
                for h in horarios:
                    servico = View.servico_listar_id(h.get_id_servico())
                    if servico:
                        descricao = servico.get_descricao()
                    else:
                        descricao = "Serviço não definido"
                    opcoes.append(f"{h.get_id()} | {h.get_data().strftime('%d/%m/%Y %H:%M')} | {descricao}")
                opcao_escolhida = st.selectbox("Selecione o horário disponível:", opcoes, label_visibility="collapsed")
                if st.button("Agendar"):
                    indice = opcoes.index(opcao_escolhida)
                    horario = horarios[indice]
                    View.horario_atualizar(horario.get_id(), horario.get_data(), False, st.session_state["usuario_id"], horario.get_id_servico(), profissional.get_id())
                    st.success("Horário agendado com sucesso")
                    time.sleep(4)
                    st.rerun()
