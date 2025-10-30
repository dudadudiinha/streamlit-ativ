from datetime import datetime
from models.dao import DAO
import json

class Horario:
    def __init__(self, id, data, confirmado=False, id_cliente=0, id_servico=None, id_profissional=0):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(confirmado)
        self.set_id_cliente(id_cliente)
        self.set_id_servico(id_servico)
        self.set_id_profissional(id_profissional)

    def set_id(self, id): 
        if id < 0: raise ValueError("ID não pode ser negativo.")
        self.__id = id
    def set_data(self, data):
        if data.year < datetime.today().year: raise ValueError("O ano não pode ser menor que o ano atual.")
        self.__data = data
    def set_confirmado(self, confirmado):
        self.__confirmado = confirmado
    def set_id_cliente(self, id_cliente): 
        if id_cliente is not None and id_cliente < 0: raise ValueError("O ID do cliente não pode ser negativo.")
        self.__id_cliente = id_cliente
    def set_id_servico(self, id_servico): 
        if id_servico is not None and id_servico < 0: raise ValueError("O ID do serviço não pode ser negativo.")
        self.__id_servico = id_servico
    def set_id_profissional(self, id_profissional):
        if id_profissional < 0: raise ValueError("O ID do profissional não pode ser negativo.")
        self.__id_profissional = id_profissional

    def get_id(self): 
        return self.__id
    def get_data(self): 
        return self.__data
    def get_confirmado(self): 
        return self.__confirmado
    def get_id_cliente(self): 
        return self.__id_cliente
    def get_id_servico(self): 
        return self.__id_servico
    def get_id_profissional(self):
        return self.__id_profissional
    
    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__confirmado}"
        
    def to_json(self):
        return {"id": self.__id, "data": self.__data.strftime("%d/%m/%Y %H:%M"), "confirmado": self.__confirmado, "id_cliente": self.__id_cliente, "id_servico": self.__id_servico, "id_profissional": self.__id_profissional}
    
    @staticmethod
    def from_json(dic):
        horario = Horario(dic["id"], datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"))
        horario.set_confirmado(dic["confirmado"])
        horario.set_id_cliente(dic["id_cliente"])
        horario.set_id_servico(dic["id_servico"])
        horario.set_id_profissional(dic["id_profissional"])
        return horario
class HorarioDAO(DAO):

    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("horarios.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
            for dic in list_dic:
                h = Horario.from_json(dic)
                cls._objetos.append(h)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("horarios.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Horario.to_json)