#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:56:39 2023

@author: jak
"""

def dict_from_row(row):
    return {desc[0]: value for desc, value in zip(row.cursor_description, row)}