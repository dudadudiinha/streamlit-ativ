from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
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
        c = Cliente(id, "a", "b", "c")
        ClienteDAO.excluir(c)

    def servico_inserir(descricao, valor, duracao):
        s = Servico(0, descricao, valor, duracao)
        ServicoDAO.inserir(s)

    def servico_listar():
        return ServicoDAO.listar()

    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)

    def servico_atualizar(id, descricao, valor, duracao):
        s = Servico(id, descricao, valor, duracao)
        ServicoDAO.atualizar(s)

    def servico_excluir(id):
        s = Servico(id, "", 0, 0)
        ServicoDAO.excluir(s)
        
    def horario_inserir(data, confirmado, id_cliente, id_servico):
        h = Horario(0, data, confirmado, id_cliente, id_servico)
        HorarioDAO.inserir(h)

    def horario_listar():
        return HorarioDAO.listar()

    def horario_listar_id(id):
        return HorarioDAO.listar_id(id)
        
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        h = Horario(id, data, confirmado, id_cliente, id_servico)
        HorarioDAO.atualizar(h)

    def horario_excluir(id):
        h = Horario(id, datetime.now(), False, 0, 0)
        HorarioDAO.excluir(h)