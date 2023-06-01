from odoo import models, fields
from odoo import api
from .produto import Produto


class ProdutoQuant():
    ...

class Pedido(models.Model):
    _name = 'pedidos.pedido'
    _description = 'Pedido'

    STATUS_PEDIDO = [
        ('aberto', 'Aberto'),
        ('em_processo', 'Em Processo'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]

    nome_cliente = fields.Char(string='Nome do Cliente')
    data_pedido = fields.Date(string='Data do Pedido')
    status_pedido = fields.Selection(selection=STATUS_PEDIDO, string='Status do Pedido')
    produtos = fields.Many2many(comodel_name='pedidos.produto', string='Produtos', relation='pedidos_pedido_produto_rel', column1='pedido_id', column2='produto_id')

    valor_total = fields.Float(compute='_compute_valor_total', string='Valor Total')

    @api.depends('produtos', 'produtos.valor_unitario')
    def _compute_valor_total(self):
        for pedido in self:
            pedido.valor_total = sum(p.valor_unitario for p in pedido.produtos)

    def add_produto(self):
        produto_form = self.env.ref('pedidos.produto_form_view')
        return {
            'name': 'Adicionar Produto',
            'view_mode': 'form',
            'res_model': 'pedidos.produto',
            'target': 'new',
            'views': [(produto_form.id, 'form')],
            'context': {
                'default_pedido_id': self.id,
            },
        }