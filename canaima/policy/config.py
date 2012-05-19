# -*- coding: utf-8 -*-

"""
Contains constants used by setuphandler.py
"""

from canaima.policy import CanaimaPolicyMF as _

PROJECTNAME = 'canaima.policy'

PRODUCT_DEPENDENCIES = [
    'Products.CMFPlacefulWorkflow',
    ]

PACKAGE_DEPENDENCIES = [
    'canaima.aponwaotheme',
    ]

DEPENDENCIES = PRODUCT_DEPENDENCIES + PACKAGE_DEPENDENCIES

