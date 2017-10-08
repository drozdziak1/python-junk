#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
import time

from datetime import datetime

path = "./intraQuarter"


def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path + "/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]
    # print(stock_list)

    for stock_dir in stock_list[1:]:
        stock_files = os.listdir(stock_dir)
        import pdb
        pdb.set_trace()
        ticker = stock_dir.split("/")[1]

        if len(stock_files) > 0:
            for file in stock_files:
                date_stamp = datetime.strptime(file, "%Y%m%d%H%M%S.html")
                unix_time = time.mktime(date_stamp.timetuple())

                full_file_path = stock_dir + '/' + file

                source = open(full_file_path).read()

                value = source.split(
                    gather + ":</td><td class=\"yfnc_tabledata1\">"
                )[1].split(
                        "</td>"
                        )[0]

                print(ticker + ":", value)

                time.sleep(1)


Key_Stats()
