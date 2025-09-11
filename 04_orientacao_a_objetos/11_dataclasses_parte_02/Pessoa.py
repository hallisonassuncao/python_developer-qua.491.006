from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Pessoa(ABC):
    email: str
    telefone: str
    endereco: str

