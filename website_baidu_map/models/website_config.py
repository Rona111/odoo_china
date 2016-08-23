# _*_ coding: utf-8 _*_
from openerp import models, fields


class WebsiteConfig(models.TransientModel):
    _inherit = "website.config.settings"

    baidu_map_AK = fields.Char(related="website_id.baidu_map_AK", string="Baidu map AK",
                               help="百度地图的访问授权。可以在这里申请 http://lbsyun.baidu.com/apiconsole/key")

