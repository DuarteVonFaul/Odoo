from odoo import models, fields

class Produto(models.Model):
    _name = 'pedidos.produto'
    _description = 'Produtos'
    
    nome_produto = fields.Char('Nome do Produto')
    descricao = fields.Text('Descrição')
    preco_unitario = fields.Float('Preço Unitário')
    pedido = fields.Many2one('pedidos.pedido', 'Pedido')