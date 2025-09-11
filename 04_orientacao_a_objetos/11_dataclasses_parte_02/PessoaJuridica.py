import Pessoa
from dataclasses import dataclass

@dataclass
class PessoaJuridica(Pessoa.Pessoa):
    razao_social: str
    nome_fantasia: str
    cnpj: str
  
    
    def __str__(self):
        return f"{'-'*20} Dados da empresa: {'-'*20}\n\nRazão Social: {self.razao_social}\nNome Fantasia: {self.nome_fantasia}\nCNPJ: {self.cnpj}\nTelefone: {self.telefone}\nEndereço: {self.endereco}\nE-mail: {self.email}\n"
