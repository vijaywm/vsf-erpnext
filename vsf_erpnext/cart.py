# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from werkzeug.wrappers import Response
import frappe
import json
__version__ = '0.0.1'


@frappe.whitelist(allow_guest=True)
# api url: http://<site_name>/api/method/vsf_erpnext.cart.update?token=&cartId=
def update(token=None, cartId=None,):
    # https://github.com/DivanteLtd/vue-storefront-integration-sdk/blob/tutorial/sample-api-js/src/api/stock.js

    # doc = frappe.local.form_dict["cartItem"]
    # print(doc)

    result = {
        "code": 200,
        "result": {
            "item_id": 580,
            "product_id": 580,
            "stock_id": 1,
            "qty": 0,
            "is_in_stock": False,
            "is_qty_decimal": False,
            "show_default_notification_message": False,
            "use_config_min_qty": True,
            "min_qty": 0,
            "use_config_min_sale_qty": 1,
            "min_sale_qty": 1,
            "use_config_max_sale_qty": True,
            "max_sale_qty": 10000,
            "use_config_backorders": True,
            "backorders": 0,
            "use_config_notify_stock_qty": True,
            "notify_stock_qty": 1,
            "use_config_qty_increments": True,
            "qty_increments": 0,
            "use_config_enable_qty_inc": True,
            "enable_qty_increments": False,
            "use_config_manage_stock": True,
            "manage_stock": True,
            "low_stock_date": None,
            "is_decimal_divided": False,
            "stock_status_changed_auto": 0
        }
    }
    # frappe.response['content_type'] = 'application/json'

    # return Response(json.dumps({"code": 500, "result": "Item not found"}), status=200,
    #                 content_type="application/json", )

    return Response(json.dumps(result), status=200,
                    content_type="application/json", )


@frappe.whitelist(allow_guest=True)
def create(token=None):
    pass
