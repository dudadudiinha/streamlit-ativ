import streamlit as st
import pandas as pd
import time
from datetime import datetime
from view import View

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir", "Concluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()
        with tab5: ManterHorarioUI.concluir()

    def formatar_horario(h):
        cliente = View.cliente_listar_id(h.get_id_cliente())
        servico = View.servico_listar_id(h.get_id_servico())
        profissional = View.profissional_listar_id(h.get_id_profissional())
        cliente_str = cliente.get_nome() if cliente else "Sem cliente"
        servico_str = servico.get_descricao() if servico else "Sem serviço"
        prof_str = profissional.get_nome() if profissional else "Sem prof."
        return f"{h.get_data().strftime('%d/%m/%Y %H:%M')} | {cliente_str} | {servico_str} | {prof_str}"

    def selectbox_horario(texto, horarios):
        opcoes_formatadas = []
        for h in horarios:
            texto_formatado = ManterHorarioUI.formatar_horario(h)
            opcoes_formatadas.append(texto_formatado)
        opcao_selecionada = st.selectbox(texto, opcoes_formatadas, label_visibility="collapsed")
        indice_selecionado = opcoes_formatadas.index(opcao_selecionada)
        return horarios[indice_selecionado]

    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            list_dic = []
            for obj in horarios:
                cliente = View.cliente_listar_id(obj.get_id_cliente())
                servico = View.servico_listar_id(obj.get_id_servico())
                profissional = View.profissional_listar_id(obj.get_id_profissional())
                if cliente != None: 
                    cliente = cliente.get_nome()
                if servico != None: 
                    servico = servico.get_descricao()
                if profissional != None: 
                    profissional = profissional.get_nome()
                list_dic.append({"id": obj.get_id(), "data": obj.get_data().strftime("%d/%m/%Y %H:%M"), "confirmado": obj.get_confirmado(), "cliente": cliente, "serviço": servico, "profissional": profissional})
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        clientes = View.cliente_listar() 
        servicos = View.servico_listar() 
        profissionais = View.profissional_listar()
        data = st.text_input("Informe a data e horário do serviço", datetime.now().strftime("%d/%m/%Y %H:%M")) 
        confirmado = st.checkbox("Confirmado")
        cliente = st.selectbox("Informe o cliente", clientes, index=None) 
        servico = st.selectbox("Informe o serviço", servicos, index=None) 
        profissional = st.selectbox("Informe o profissional", profissionais, index=None) 
        if st.button("Inserir"): 
            if profissional == None or cliente == None or servico == None:
                st.error("Nenhum campo pode estar vazio")
                return
            id_cliente = 0
            id_servico = 0
            id_profissional = 0
            if cliente != None: 
                id_cliente = cliente.get_id() 
            if servico != None: 
                id_servico = servico.get_id() 
            if profissional != None: 
                id_profissional = profissional.get_id() 
            try:
                View.horario_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissional) 
                st.success("Horário inserido com sucesso") 
                time.sleep(4)
                st.rerun()
            except ValueError as e:
                if "unconverted data remains" in str(e) or "does not match format" in str(e):
                    st.error("O formato da data está incorreto. Use exatamente DD/MM/AAAA HH:MM")
                else: st.error(f"{e}")

    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            clientes = View.cliente_listar() 
            servicos = View.servico_listar() 
            profissionais = View.profissional_listar()
            op = ManterHorarioUI.selectbox_horario("Atualização de horários", horarios)
            data = st.text_input("Informe a nova data e horário do serviço", op.get_data().strftime("%d/%m/%Y %H:%M")) 
            confirmado = st.checkbox("Nova confirmação", op.get_confirmado())
            id_cliente = None if op.get_id_cliente() in [0, None] else op.get_id_cliente()
            id_servico = None if op.get_id_servico() in [0, None] else op.get_id_servico()
            id_profissional = None if op.get_id_profissional() in [0, None] else op.get_id_profissional()
            cliente = st.selectbox("Informe o novo cliente", clientes, next((i for i, c in enumerate(clientes) if c.get_id() == id_cliente), None)) 
            servico = st.selectbox("Informe o novo serviço", servicos, next((i for i, s in enumerate(servicos) if s.get_id() == id_servico), None)) 
            profissional = st.selectbox("Informe o novo profissional", profissionais, next((i for i, p in enumerate(profissionais) if p.get_id() == id_profissional), None)) 
            if st.button("Atualizar"): 
                id_cliente = None 
                id_servico = None 
                id_profissional = None
                if cliente != None: id_cliente = cliente.get_id()
                if servico != None: id_servico = servico.get_id()
                if profissional != None: id_profissional = profissional.get_id()
                try:
                    View.horario_atualizar(op.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissional)
                    st.success("Horário atualizado com sucesso")
                    time.sleep(4)
                    st.rerun()
                except ValueError as e:
                    if "unconverted data remains" in str(e) or "does not match format" in str(e):
                        st.error("O formato da data está incorreto. Use exatamente DD/MM/AAAA HH:MM")
                    else: st.error(f"{e}")

    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            op = ManterHorarioUI.selectbox_horario("Exclusão de horários", horarios)
            if st.button("Excluir"):
                try:
                    View.horario_excluir(op.get_id())
                    st.success("Horário excluído com sucesso")
                    time.sleep(4)
                    st.rerun()
                except ValueError as e:
                    st.error(f"{e}")

    @staticmethod
    def concluir():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
            return
        opcoes = []
        for h in horarios:
            if h.get_confirmado() and not h.get_concluido() and h.get_data() < datetime.now():
                opcoes.append(h)
        if len(opcoes) == 0:
            st.info("Nenhum atendimento pendente de conclusão")
            return
        op = ManterHorarioUI.selectbox_horario("Conclusão de horários", opcoes)
        if st.button("Concluir"):
            try:
                View.horario_concluir(op.get_id())
                st.success("Atendimento concluído com sucesso")
                time.sleep(4)
                st.rerun()
            except ValueError as e:
                st.error(f"{e}")