import json
from datetime import datetime

class Profissional:
    def __init__(self, id, nome, especialidade, conselho):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)

    def set_id(self, id):
        if id < 0: raise ValueError("ID não pode ser negativo.")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio.")
        self.__nome = nome
    def set_especialidade(self, especialidade):
        if especialidade == "": raise ValueError("especialidade não pode ser vazia.")
        self.__especialidade = especialidade
    def set_conselho(self, conselho):
        if conselho == "": raise ValueError("conselho não pode ser vazio.")
        self.__conselho = conselho

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_especialidade(self):
        return self.__especialidade
    def get_conselho(self):
        return self.__conselho

    def __str__(self):
        return f"{self.get_id()} - {self.get_nome()}"

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "especialidade": self.__especialidade,
            "conselho": self.__conselho
        }

    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["especialidade"], dic["conselho"])

class ProfissionalDAO:
    __profissionais = []

    @classmethod
    def abrir(cls):
        cls.__profissionais = []
        try:
            with open("profissionais.json", mode="r") as arquivo:
                profissionais_json = json.load(arquivo)
                for obj in profissionais_json:
                    p = Profissional.from_json(obj)
                    cls.__profissionais.append(p)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("profissionais.json", mode="w") as arquivo:
            json.dump(cls.__profissionais, arquivo, default=Profissional.to_json)

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for profissional in cls.__profissionais:
            if profissional.get_id() > id:
                id = profissional.get_id()
        obj.set_id(id + 1)
        cls.__profissionais.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__profissionais

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for profissional in cls.__profissionais:
            if profissional.get_id() == id:
                return profissional
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__profissionais.remove(aux)
            cls.__profissionais.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        aux = cls.listar_id(id)
        if aux != None:
            cls.__profissionais.remove(aux)
            cls.salvar()