# -*- extra stuff goes here -*-

from zope.i18nmessageid import MessageFactory

CanaimaPolicyMF = MessageFactory('canaima.policy')

GLOBALS = globals()

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
