import json

class Servico:
    def __init__(self, id, descricao, valor):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)

    def set_id(self, id):
        if id < 0: raise ValueError("ID não pode ser negativo.")
        self.__id = id
    def set_descricao(self, descricao): 
        if descricao == "": raise ValueError("Descrição não pode ser vazia.")
        self.__descricao = descricao
    def set_valor(self, valor): 
        if valor < 0: raise ValueError("Valor não pode ser negativo.")
        self.__valor = valor
    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - R${self.__valor:.2f}"

    def to_json(self):
        return {"id": self.__id, "descricao": self.__descricao, "valor": self.__valor}
    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])
    
class ServicoDAO:
    __servicos = []

    @classmethod
    def abrir(cls):
        cls.__servicos = []
        try:
            with open("servicos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
            for dic in list_dic:
                s = Servico.from_json(dic)
                cls.__servicos.append(s)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo:
            json.dump(cls.__servicos, arquivo, default = Servico.to_json)

    @classmethod
    def inserir(cls, s):
        cls.abrir()
        id = 0
        for obj in cls.__objetos:
            if obj.get_id() > id:
                id = obj.get_id()
        obj.set_id(id+1)
        cls.__servicos.append(s)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__servicos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for s in cls.__servicos:
            if s.get_id() == id:
                return s
        return None
    
    @classmethod
    def atualizar(cls, s):
        obj = cls.listar_id(s.get_id())
        if obj != None:
            cls.__servicos.remove(obj)
            cls.__append(s)
            cls.salvar()

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        obj_remover = None
        for obj in cls.__servicos:
            if obj.get_id() == id:
                obj_remover = obj
                break 
        if obj_remover: 
            cls.__servicos.remove(obj_remover)
            cls.salvar()