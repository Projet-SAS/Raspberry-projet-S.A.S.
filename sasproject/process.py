#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""docstring for connection

"""


class Process(object):
    """"""
    def __init__(self):
        print("[Process] data core launching..")
        pass

    def decompose(self, data_in):
        """Docstrings for decompose (func)
        input data : 'begin type1:data1_data2_data3\ttype2:data1_data2_data3\t[...] end'
        output data : [[['type1'], [data1, data2, data3], ['type2"], [data1, data2, ... ]]]
        """
        if data_in.startswith("begin", beg=0, end=7) and \
                data_in.startswith("end", beg=(len(data_in)-5), end=len(data_in)):
            data_in = data_in.strip("begin ")
            data_in = data_in.strip(" end")
            table = data_in.split('\t')

            i = 0
            for row in table:
                table[i] = row.split(':')
                i2 = 0
                for col in table[i]:
                    table[i][i2] = col.split('_')
                    i2 += 1
                    pass
                i += 1
                pass

            return table

        pass

    def setsql(self, data_in):
        """transform our table to be use by th database
        we admits our input data get the pattern : [[['type1'], [data1, data2, data3], ['type2"], [data1, data2, ... ]]]
        """
        sql = []
        sql[0] = "INSERT INTO %r VALUES (%r, %r, %r)" % \
                 (data_in[0][0][0], data_in[0][1][0], data_in[0][1][1], data_in[0][1][2])
        sql[1] = "INSERT INTO %r VALUES (%r, %r, %r)" % \
                 (data_in[0][0][0], data_in[0][1][0], data_in[0][1][1], data_in[0][1][2])
        sql[2] = "INSERT INTO %r VALUES (%r, %r, %r)" % \
                 (data_in[0][0][0], data_in[0][1][0], data_in[0][1][1], data_in[0][1][2])
        return sql

        pass

    def readsql(self, data_sql):
        """process sql to be more readable"""
        return data_sql

    def core_choice(self, actual_data, wanted_data):
        """"""
        if actual_data != wanted_data:
            print("we need modifications")
            pass
        pass
