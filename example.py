"""simple test module"""


import autoui
from autoui.inputs import Slider, TextBox, Number


def test(name):
    """simple test function"""
    return name


screen = autoui.Screen(func=test,
    inputs=[
        TextBox(lines=3, label="Text"),
        Number(label="Number"),
        Slider(label="slide here", minimum=0, maximum=100, step=5)
    ],
    outputs=['']
)
screen.run(debug=True)
