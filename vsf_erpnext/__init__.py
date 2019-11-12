# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__version__ = '0.0.1'
import frappe
from erpnext.shopping_cart.cart import _get_cart_quotation
from erpnext.shopping_cart.doctype.shopping_cart_settings.shopping_cart_settings \
    import get_shopping_cart_settings, show_quantity_in_website
from erpnext.utilities.product import get_price, get_qty_in_stock
from erpnext.shopping_cart import product_info


def patch_method(obj, method, override):
    # https://github.com/DigiThinkIT/frappe_utils/blob/master/monkey.py
    """Monkey Patch helper. Will override an object's method with a custome one"""
    orig = getattr(obj, method)
    if hasattr(orig, "monkeypatched") and orig.monkeypatched == override:
        return

    override.patched_method = orig

    def __fn(*args, **kwargs):
        return override(*args, **kwargs)
    __fn.monkeypatched = override

    setattr(obj, method, __fn)


def get_product_info_for_website(item_code):
    # custom implementation
    print("""
    
    
    =
    overriden get_product_info_for_website
    =


    """)

    # original
    cart_settings = get_shopping_cart_settings()
    if not cart_settings.enabled:
        return frappe._dict()

    cart_quotation = _get_cart_quotation()

    price = get_price(
        item_code,
        cart_quotation.selling_price_list,
        cart_settings.default_customer_group,
        cart_settings.company
    )

    stock_status = get_qty_in_stock(item_code, "website_warehouse")

    product_info = {
        "price": price,
        "stock_qty": stock_status.stock_qty,
        "in_stock": stock_status.in_stock if stock_status.is_stock_item else 1,
        "qty": 0,
        "uom": frappe.db.get_value("Item", item_code, "stock_uom"),
        "show_stock_qty": show_quantity_in_website(),
        "sales_uom": frappe.db.get_value("Item", item_code, "sales_uom")
    }

    if product_info["price"]:
        if frappe.session.user != "Guest":
            item = cart_quotation.get({"item_code": item_code})
            if item:
                product_info["qty"] = item[0].qty

    return frappe._dict({
        "product_info": product_info,
        "cart_settings": cart_settings
    })


# patch_method(product_info,
#              "get_product_info_for_website", get_product_info_for_website)
