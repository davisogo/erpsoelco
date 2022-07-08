# -*- coding: utf-8 -*-
# from odoo import http


# class StockTransferApproval(http.Controller):
#     @http.route('/stock_transfer_approval/stock_transfer_approval/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_transfer_approval/stock_transfer_approval/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_transfer_approval.listing', {
#             'root': '/stock_transfer_approval/stock_transfer_approval',
#             'objects': http.request.env['stock_transfer_approval.stock_transfer_approval'].search([]),
#         })

#     @http.route('/stock_transfer_approval/stock_transfer_approval/objects/<model("stock_transfer_approval.stock_transfer_approval"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_transfer_approval.object', {
#             'object': obj
#         })
