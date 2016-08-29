# _*_ coding: utf-8 _*_
import string
from openerp import models, fields, api


class Website(models.Model):
    _inherit = "website"

    baidu_map_AK = fields.Char(
        help="You can get access to baidu map,use this url: http://lbsyun.baidu.com/apiconsole/key")
