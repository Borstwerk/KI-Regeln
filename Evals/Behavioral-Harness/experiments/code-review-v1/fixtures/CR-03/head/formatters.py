"""Neu eingefuehrte Formatter-Registry (im Auftrag nicht vorgesehen)."""


class FormatterRegistry:
    def __init__(self):
        self._formatters = {}

    def register(self, name, func):
        self._formatters[name] = func

    def get(self, name):
        return self._formatters[name]
