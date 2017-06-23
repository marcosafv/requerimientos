from openerp import models, fields, api
from openerp.report import report_sxw


class report_invoice_print(report_sxw.rml_parse):
    def __init__(self,cr,uid,name,context):
        super(report_invoice_print, self).__init__(cr,uid,name,context)

class reports_invoice_print(models.AbstractModel):
    _name = "report.loc_invoice_print.softnetco_client"
    _inherit = "report.abstract_report"
    _template = "loc_invoice_print.softnetco_client"
    _wrapped_report_class = report_invoice_print