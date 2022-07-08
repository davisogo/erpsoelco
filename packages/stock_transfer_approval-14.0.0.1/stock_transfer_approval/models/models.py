# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
class stock_location(models.Model):
    _inherit = 'stock.location'
    manager_id=fields.Many2one('res.users')

class stock_transfer_approval(models.Model):
    _inherit = 'stock.picking'
    show_validate_btn=fields.Boolean(compute='_compute_show_validate_btn',store=False)
    
    manager_activity_id=fields.Many2one('mail.activity')
    @api.depends('state','location_dest_id','location_dest_id.manager_id')
    def _compute_show_validate_btn(self):
        for picking in self:
            if(picking.location_dest_id):
                manager=picking.location_dest_id.manager_id
                if(manager):
                    if(manager.id==self.env.user.id):
                        picking.show_validate_btn=True
                    else:
                        picking.show_validate_btn=False
                else:
                    picking.show_validate_btn=True
            else:
                picking.show_validate_btn=False

    state=fields.Selection(selection_add=[('waiting_approval','Waiting Approval')])
    is_internal_transfer=fields.Boolean(compute='_compute_is_internal_transfer',store=True)
    def send_approval(self):
        if(self.location_dest_id.manager_id):
            activity=self.env['mail.activity'].sudo().create({'res_id':self.id,'res_model_id':self.env['ir.model'].search([('model','=','stock.picking')]).id,'activity_type_id':self.env.ref('mail.mail_activity_data_todo').id,'date_deadline':fields.Date.today()+timedelta(days=1),'user_id':self.location_dest_id.manager_id.id})
            self.manager_activity_id=activity.id
        self.state='waiting_approval'
    
    def write(self,vals):
        print('wruititii')
        print('wruititii')
        print('wruititii')
        print('wruititii')
        print('wruititii')
        print('wruititii')
        print(vals)
        res = super(stock_transfer_approval, self).write(vals)
        if('date_done' in vals):
            print(self.state)
            print(self.state)
            print(self.state)
            if(self.state=='done'):
                self.manager_activity_id.action_done()

    @api.depends('picking_type_id','state','picking_type_id.code')
    def _compute_is_internal_transfer(self):
        for r in self:
            if(r.picking_type_id.code=='internal'):
                r.is_internal_transfer=True
                # r.update({'is_internal_transfer':True})
            else:
                # r.update({'is_internal_transfer':False})
                r.is_internal_transfer=False
    hide_approval=fields.Boolean(compute='_compute_hide_approval',store=True)
    @api.depends('picking_type_id','picking_type_id.code','state')
    def _compute_hide_approval(self):
        for r in self:
            if(r.picking_type_id.code=='internal' and r.state=='waiting_approval'):
                r.hide_approval=True
            else:
                r.hide_approval=False
#     _description = 'stock_transfer_approval.stock_transfer_approval'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
