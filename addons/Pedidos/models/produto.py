from odoo import models, fields
from odoo import api


class Produto(models.Model):
    _name = 'pedidos.produto'
    _description = 'Produto'

    nome_produto = fields.Char(string='Nome do Produto')
    descricao = fields.Text(string='Descrição')
    valor_unitario = fields.Float(string='Valor Unitário')
    pedido_ids = fields.Many2many(comodel_name='pedidos.pedido', string='Pedidos', relation='pedidos_pedido_produto_rel', column1='produto_id', column2='pedido_id')

    @api.onchange('nome_produto')
    def _onchange_nome_produto(self):
        if self.nome_produto:
            produto = self.env['pedidos.produto'].search([('nome_produto', '=', self.nome_produto)])
            if produto:
                self.descricao = produto.descricao
            else:
                self.descricao = ''

    @api.model
    def name_get(self):
        result = []
        for produto in self:
            name = produto.nome_produto
            result.append((produto.id, name))
        return result