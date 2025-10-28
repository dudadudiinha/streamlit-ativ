from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO
from datetime import datetime

class View:
    def validacao(email):
        for c in View.cliente_listar():
            if c.get_email() == email:
                raise ValueError("Esse e-mail já foi cadastrado")
        for p in View.profissional_listar():
            if p.get_email() == email:
                raise ValueError("Esse e-mail já foi cadastrado")
        if email == "admin":
            raise ValueError("Esse e-mail já foi cadastrado")
        
    def cliente_inserir(nome, email, fone, senha):
        View.validacao(email)
        c = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(c)

    def cliente_listar():
        r = ClienteDAO.listar()
        r.sort(key= lambda obj : obj.get_nome())
        return r

    def cliente_listar_id(id):
        for c in View.cliente_listar():
            if c.get_id() == id:
                return c 
        return None

    def cliente_atualizar(id, nome, email, fone, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_id() != id:
                raise ValueError("Outro cliente já foi cadastrado com esse e-mail")
        c = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(c)

    def cliente_excluir(id):
        cliente = View.cliente_listar_id(id)
        if cliente and cliente.get_email() == "admin":
            raise ValueError("O admin não pode ser excluído")
        for h in View.horario_listar():
            if h.get_id_cliente() == id:
                raise ValueError("Não é possível excluir um cliente com um horário agendado")
        ClienteDAO.excluir(id)

    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None

    def servico_inserir(descricao, valor):
        for obj in View.servico_listar():
            if obj.get_descricao() == descricao:
                raise ValueError("Serviço já cadastrado")
        s = Servico(0, descricao, valor)
        ServicoDAO.inserir(s)

    def servico_listar():
        r = ServicoDAO.listar()
        r.sort(key= lambda obj : obj.get_descricao())
        return r

    def servico_listar_id(id):
        for s in View.servico_listar():
            if s.get_id() == id:
                return s
        return None

    def servico_atualizar(id, descricao, valor):
        for obj in View.servico_listar():
            if obj.get_id() != id and obj.get_descricao() == descricao:
                raise ValueError("Essa descriçao já foi cadastrada em outro serviço")
        s = Servico(id, descricao, valor)
        ServicoDAO.atualizar(s)

    def servico_excluir(id):
        for h in View.horario_listar():
            if h.get_id_servico() == id:
                raise ValueError("Não é possível excluir um serviço com um horário agendado")
        ServicoDAO.excluir(id)
        
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        for h in View.horario_listar():
            if h.get_id_profissional() == id_profissional and h.get_data() == data:
                raise ValueError("Outro horário já foi cadastrado com essa data e hora para esse profissional")
        h = Horario(0, data, confirmado, id_cliente, id_servico, id_profissional)
        HorarioDAO.inserir(h)

    def horario_listar():
        r = HorarioDAO.listar()
        r.sort(key= lambda obj : obj.get_data())
        return r

    def horario_listar_id(id):
        return HorarioDAO.listar_id(id)
        
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        for h in View.horario_listar():
            if h.get_id_profissional() == id_profissional and h.get_data() == data and h.get_id() != id:
                raise ValueError("Outro horário já foi cadastrado com essa data e hora para esse profissional")
        h = Horario(id, data, confirmado, id_cliente, id_servico, id_profissional)
        HorarioDAO.atualizar(h)

    def horario_excluir(id):
        h = View.horario_listar_id(id)
        if h.get_id_cliente() is not None and h.get_id_cliente() != 0:
            raise ValueError("Não é possível excluir um horário que já foi agendado por um cliente.")
        HorarioDAO.excluir(id)

    def horario_filtrar_profissional(id_profissional):
        r=[]
        for h in View.horario_listar():
            if h.get_id_profissional() == id_profissional: 
                r.append(h)
        return r
    
    def horario_filtrar_cliente(id_cliente):
        r=[]
        for h in View.horario_listar():
            if h.get_id_cliente() == id_cliente:
                r.append(h)
        return r

    def horario_agendar_horario(id_profissional):
        r=[]
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key= lambda h :h.get_data())
        return r
    
    def horario_listar_nao_confirmados(id_profissional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_id_profissional() == id_profissional and h.get_id_cliente() is not None and h.get_confirmado() == False:                      
                r.append(h)
        r.sort(key=lambda x: x.get_data())
        return r
    
    def horario_servicos(id_cliente):
        r = []
        for h in View.horario_listar():
            if h.get_id_cliente() == id_cliente:
                r.append(h)
        r.sort(key=lambda h: h.get_data())
        return r

    def profissional_inserir(nome, especialidade, conselho, email, senha):
        View.validacao(email)
        p = Profissional(0, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.inserir(p)

    def profissional_listar():
        r = ProfissionalDAO.listar()
        r.sort(key= lambda obj : obj.get_nome())
        return r

    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)
    
    def profissional_atualizar(id, nome, especialidade, conselho, email, senha):
        for p in View.profissional_listar():
            if p.get_email() == email and p.get_id() != id:
                raise ValueError("Outro profissional já está cadastrado com esse e-mail")
        p = Profissional(id, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.atualizar(p)

    def profissional_excluir(id):
        for h in View.horario_listar():
            if h.get_id_profissional() == id:
                raise ValueError("Não é possível excluir um profissional com um horário agendado")
        ProfissionalDAO.excluir(id)

    def profissional_autenticar(email, senha):
        for c in View.profissional_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None