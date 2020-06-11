# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RevisedSaleOrderLine(models.Model):
    _name = 'saleorderline.revised'
    _rec_name = 'line_custom_id'
    _description = 'Revised Sale Order Line'
    
    line_custom_id = fields.Many2one(
        'saleorder.revised',
        string='Revised Line',
    )

    product_id_rev = fields.Many2one(
        'product.product',
        string='Product',
    )
    # layout_category_id_rev = fields.Many2one(
    #     'sale.layout_category',
    #     string='Section',
    # )
    name_rev = fields.Char(
        string='Description',
    )
    qty_rev = fields.Char(
        string='Ordered Quantity',
    )
    uom_rev = fields.Many2one(
#        'product.uom',
        'uom.uom',
        string='Unit of Measure',
    )
    price_rev = fields.Float(
        string='Price Unit',
    )
    discount_rev = fields.Float(
        string='Discount(%)',
    )
    subtotal_rev = fields.Float(
        string='Subtotal',
    )
    total_rev = fields.Float(
        string='Total',
    )
    currency_id = fields.Many2one(
        "res.currency", 
        related='line_custom_id.sale_order_id.order_line.currency_id', 
        string="Currency",
        store=True,
    )
    sale_person_line_id = fields.Many2one(
        'res.users',
        string='Sales Person',
        related='line_custom_id.sale_order_id.user_id',
        store=True,
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
