# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import frappe
import json

es_base_url = "http://localhost:9200"
index = "vue_storefront_catalog"


def sync_product():
    # retrieve and update product or add new product to index
    # https://www.elastic.co/guide/en/elasticsearch/reference/5.6/docs-index_.html

    endpoint = "{es_base_url}/{index}/product/{id}".format(
        es_base_url=es_base_url, index=index, id=355)
    response = requests.get(endpoint, )

    product = frappe._dict(response.json()["_source"])
    description = "Modified in erpnext" + \
        product["description"]

    data = {"description": description}

    response = requests.put(endpoint, data=json.dumps(data), headers={"Content-Type": "application/json"}
                            )

    return response.json()
