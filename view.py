from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO

class View:
    def cliente_listar():
        return ClienteDAO.listar()
    
    def cliente_inserir(nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(cliente)

    def cliente_atualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(cliente)

    def cliente_excluir(id):
        ClienteDAO.excluir(id)

    def servico_listar():
        return ServicoDAO.listar()
    
    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)

    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)

    def servico_excluir(id):
        ServicoDAO.excluir(id)