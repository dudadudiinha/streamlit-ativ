import json
from models.dao import DAO
from datetime import datetime

class Profissional:
    def __init__(self, id, nome, especialidade, conselho, email, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
        self.set_email(email)
        self.set_senha(senha)
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
    def set_email(self, email): 
        if email == "": raise ValueError("E-mail não pode ser vazio.")
        self.__email = email
    def set_senha(self, senha): 
        if senha == "": raise ValueError("Senha não pode ser vazia.")
        self.__senha = senha

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_especialidade(self):
        return self.__especialidade
    def get_conselho(self):
        return self.__conselho
    def get_email(self): 
        return self.__email
    def get_senha(self): 
        return self.__senha

    def __str__(self):
        return f"{self.get_id()} - {self.get_nome()}"

    def to_json(self):
        return {"id": self.__id, "nome": self.__nome, "especialidade": self.__especialidade, "conselho": self.__conselho, "email":self.__email, "senha": self.__senha}

    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["especialidade"], dic["conselho"], dic["email"], dic["senha"])

class ProfissionalDAO(DAO):

    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("profissionais.json", mode="r") as arquivo:
                profissionais_json = json.load(arquivo)
                for obj in profissionais_json:
                    p = Profissional.from_json(obj)
                    cls._objetos.append(p)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("profissionais.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default=Profissional.to_json)