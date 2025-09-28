from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO
from datetime import datetime

class View:
    def cliente_inserir(nome, email, fone):
        c = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(c)

    def cliente_listar():
        return ClienteDAO.listar()

    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(c)

    def cliente_excluir(id):
        ClienteDAO.excluir(id)

    def servico_inserir(descricao, valor):
        s = Servico(0, descricao, valor)
        ServicoDAO.inserir(s)

    def servico_listar():
        return ServicoDAO.listar()

    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)

    def servico_atualizar(id, descricao, valor):
        s = Servico(id, descricao, valor)
        ServicoDAO.atualizar(s)

    def servico_excluir(id):
        ServicoDAO.excluir(id)
        
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        h = Horario(0, data, confirmado, id_cliente, id_servico, id_profissional)
        HorarioDAO.inserir(h)

    def horario_listar():
        return HorarioDAO.listar()

    def horario_listar_id(id):
        return HorarioDAO.listar_id(id)
        
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        h = Horario(id, data, confirmado, id_cliente, id_servico, id_profissional)
        HorarioDAO.atualizar(h)

    def horario_excluir(id):
        HorarioDAO.excluir(id)

    def profissional_inserir(nome, especialidade, conselho):
        p = Horario(0, nome, especialidade, conselho)
        ProfissionalDAO.inserir(p)

    def profissional_listar():
        return ProfissionalDAO.listar()

    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)
    
    def profissional_atualizar(id, nome, especialidade, conselho):
        p = Profissional(id, nome, especialidade, conselho)
        ProfissionalDAO.atualizar(p)

    def profissional_excluir(id):
        ProfissionalDAO.excluir(id)