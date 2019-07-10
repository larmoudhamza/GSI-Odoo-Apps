# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from openerp import models
from openerp.osv import fields, osv

class PricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    _columns = {
        'date_start':fields.date('Date de debut', required=True, help="....", copy=True),
        'date_end':fields.date('Date de fin', required=True, help="....", copy=True),
	}
  