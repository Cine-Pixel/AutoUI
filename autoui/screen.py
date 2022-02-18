"""Module contains main Screen class which"""

from typing import Callable

from .inputs import Input
from .backend import app


class Screen:
    """Handles creation of UI based on inputs list and outputs list"""
    def __init__(self, func: Callable, inputs: list[Input], outputs: list[str]):
        """
        Parameters:
            func (Callable): function which should run on input values
            inputs (list[Input]): list of input components
            outputs (list[Output]): list of output components
            debug (bool): should app run in debug mode or not
        """
        self.func = func
        self.inputs = inputs
        self.outputs = outputs

    def run(self, debug: bool = False) -> None:
        """creates flask app which bulds UI"""
        app.func = self.func
        app.input_config = self.get_input_config()
        app.run(debug=debug)

    def get_input_config(self) -> list[dict]:
        """converts all input fields into dictionary"""
        config = []
        for inp in self.inputs:
            config.append(inp.serialize())
        return config
