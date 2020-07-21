# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class CapacitacionReporte(models.TransientModel):
    _name = 'capacitacion.reporte'
    _description = 'Capacitacion Reporte'

    start_date = fields.Datetime(
        string='Start Date',
        required=True)
    end_date = fields.Datetime(
        string='End Date',
        required=True)

    def generar_reporte(self):
        # workorder_ids = self.env['maintenance.cp.workorder'].search([('create_date', '>=', self.start_date),
        #                                                              ('create_date', '<=', self.end_date),
        #                                                              ('company_id', '=', self.env.user.company_id.id)])
        # workorders = []
        #
        # # raise exceptions.UserError((result))
        #
        # for wo in workorder_ids:
        #     workorders.append(
        #         {
        #             'name': wo.name,
        #             'star': wo.start_date,
        #             'end': wo.end_date
        #         }
        #     )

        query = """
        select wo.name as name, wo.start_date as start, wo.end_date as end, us.login as create_uid
        from maintenance_cp_workorder as wo join res_users as us on (wo.create_uid=us.id)
        where wo.create_date >= %s and wo.create_date <= %s and wo.company_id = %s;
        """

        params = (self.start_date, self.end_date, self.env.user.company_id.id)

        self.env.cr.execute(query, params)

        result = self.env.cr.dictfetchall()

        datas = {
            'ids': self.ids,
            'model': self._name,
            'user':self.env.user,
            'workorders': result
        }

        # data, data_format = self.env.ref('capacitacion_reporte.report_capacitacion_reporte').render(self.id, data=datas)

        data = self.env.ref('capacitacion_reporte.report_capacitacion_reporte').report_action(self, data=datas)

        return data

class ReportC(models.AbstractModel):
    _name = 'report.capacitacion_reporte.report_capacitacion_reporte_view'

    @api.model
    def get_report_values(self, docids, data=None):
        # raise exceptions.UserError(_('Entra en report values %s' % (data)))

        docs = [data]
        # raise exceptions.UserError(_('Entra en report values %s' % (all_re)))

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'docs': docs,
        }








