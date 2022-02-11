NUMBER_TYPE = 'number'
TEXT_TYPE = 'text'


class Input:
    pass

class TextBox(Input):
    def __init__(self, lines: int = 1, label: str = "", numeric: bool = False):
        self.lines = lines
        self.label = label
        if numeric:
            self.type = NUMBER_TYPE
        else:
            self.type = TEXT_TYPE
