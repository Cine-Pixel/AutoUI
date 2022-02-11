from typing import Callable

from .inputs import Input
from .backend import app


class Screen:
    def __init__(self, func: Callable, inputs: list[Input], outputs: list[str]):
        self.func = func
        self.inputs = inputs
        self.outputs = outputs
    
    def run(self) -> None:
        # Start flask app
        app.func = self.func
        app.run()
