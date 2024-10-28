from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.constrains('account_id', 'analytic_distribution')
    def _check_analytic_account(self):
        for line in self:
            account_code = line.account_id.code
            if (account_code.startswith('41') or account_code.startswith('51')) and not line.analytic_distribution:
                raise ValidationError("Please enter the analytic field to post the journal entries .")
