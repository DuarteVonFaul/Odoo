from odoo import models, fields
from odoo import api
from .produto import Produto


class Pedido(models.Model):
    _name = 'pedidos.pedido'
    _description = 'Pedidos de Clientes'
    
    nome_cliente = fields.Char('Nome do Cliente')
    data_pedido = fields.Date('Data do Pedido')
    status_pedido = fields.Selection([
        ('aberto', 'Aberto'),
        ('em_processo', 'Em Processo'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ], 'Status do Pedido')
    produtos = fields.One2many('pedidos.produto', 'pedido', 'Produtos')


