# _*_ coding: utf-8 _*_
from openerp import models, fields


class WebsiteConfig(models.TransientModel):
    _inherit = "website.config.settings"

    baidu_map_AK = fields.Char(related="website_id.baidu_map_AK", string="Baidu map AK",
                               help="You can get access to baidu map,use this url: http://lbsyun.baidu.com/apiconsole/key")

