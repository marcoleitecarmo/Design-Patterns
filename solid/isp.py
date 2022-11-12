from abc import ABC, abstractmethod


class Cliente(ABC):
    @abstractmethod
    def get_cpf(self): pass
    @abstractmethod
    def get_cnpj(self): pass


class PessoaFisica(Cliente):
    def get_cpf(self):
        pass

    def get_cnpj(self):
        pass


class PessoaJuridica(Cliente):
    def get_cpf(self):
        pass

    def get_cnpj(self):
        pass
