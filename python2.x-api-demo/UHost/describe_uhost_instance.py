#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
import json
from utils import ApiClient
from config import * 

if __name__=='__main__':
    arg_length = len(sys.argv)
    ApiClient = ApiClient(base_url, public_key, private_key)
    Parameters = {
            "Action":"DescribeUHostInstance",
            "Region":"cn-north-03",
            }
    response = ApiClient.get("/", Parameters)
    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))

