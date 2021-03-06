# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class POSFrontConfiguration(models.Model):
    _name = 'posfront.configuration'

    name = fields.Char(required=True, help='Name of this POS front configuration')
    api_key = fields.Text(string='API key', required=True, help='API key used to connect the mobile device')

    @api.model
    def send(self,config_id,data):
        config = self.env['posfront.configuration'].sudo().search([('id','=',config_id)])
        #print 'Sending ' + data + ' to ' + 'ebmerchant_posfront_mobile_'+config.api_key
        self.env['bus.bus'].sendone('ebmerchant_posfront_mobile_'+config.api_key, data)


class PosConfig(models.Model):
    _inherit = "pos.config"
    posfront_config_id = fields.Many2one('posfront.configuration', string='Pos front configuration', help='The configuration of POS front')

