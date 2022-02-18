"""Module contains all of the available input components"""


class Input:
    """parent for all input components"""

    def serialize(self) -> dict:
        """
        converts input object to dictionary

        returns:
            (dict): dictionary containing input configuration
        """
        return {"component": self.__class__.__name__}


class TextBox(Input):
    """
    TextBox component
    """
    def __init__(self, lines: int = 1, label: str = "", placeholder: str = ""):
        """
        Parameters:
            lines (int): number of input lines
            label (str): label to be displyed on component
            placeholder (str): placeholder text
        """
        self.lines = lines
        self.label = label
        self.placeholder = placeholder

    def serialize(self):
        return {
            "lines": self.lines,
            "label": self.label,
            "placeholder": self.placeholder,
            **super().serialize()
        }


class Number(Input):
    """
    Numeric input component
    """
    def __init__(self, label: str = "", placehoder: str = ""):
        """
        Parameters:
            label (str): label to be displyed on component
            placeholder (str): placeholder text
        """
        self.label = label
        self.placeholder = placehoder

    def serialize(self):
        return {
            "label": self.label,
            "placeholder": self.placeholder,
            **super().serialize()
        }


class Slider(Input):
    """Slider component"""
    def __init__(self, label: str = '', minimum: float = 0, maximum: float = 10, step: int = 1):
        """
        Parameters:
            label (str): label to be displyed on component
            minimum (float): minimum value for slider
            maximum (float): maximum value for slider
            step (int): step to take between slider values
        """
        self.label = label
        self.minimum = minimum
        self.maximum = maximum
        self.step = step

    def serialize(self):
        return {
            "label": self.label,
            "minimum": self.minimum,
            "maximum": self.maximum,
            "step": self.step,
            **super().serialize()
        }
