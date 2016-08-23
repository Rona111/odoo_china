# _*_ coding: utf-8 _*_
import string
from openerp import models, fields, api


class Website(models.Model):
    _inherit = "website"

    social_sina = fields.Char('Sina Account')
    social_weixin_qrcode = fields.Char('Weixin QR Code', help="微信公众号二维码图片在服务器上的路径。")

    baidu_map_AK = fields.Char(help="百度地图的访问授权。可以在这里申请 http://lbsyun.baidu.com/apiconsole/key")
