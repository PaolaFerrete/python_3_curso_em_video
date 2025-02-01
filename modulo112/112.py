from modulo112.utilidadescv import moeda
from modulo112.utilidadescv import dados

p = dados.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 20, 12)