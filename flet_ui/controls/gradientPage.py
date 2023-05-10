""" Gradient Page Class """
from flet import (
    UserControl,
    ResponsiveRow,
    Container,
    alignment,
    LinearGradient,
    Column,
)
import random
from data import *
from views import CopyContent

_color_name_ = ColorName()
_color_number = ColorNumber()


class GradientPage(UserControl):
    def __init__(self, visibility):
        self.visibility = visibility
        super().__init__()

    def build(self):
        # COLOR COLUMN: stores all the color pallates in here
        self._color_col = Column(scroll="adaptive")

        # COLOR CONTIANER: puts all the pallets under one contianer and returns it to the main app
        self._color = Container(
            visible=self.visibility,
            content=self._color_col,
        )

        _color_state = True
        for row in range(60):
            _ = ResponsiveRow(run_spacing=10, alignment="center")
            __ = Container(content=_)
            self._color_col.controls.append(__)

            for column in range(4):
                _start = random.choice(_color_name_) + random.choice(_color_number)
                _end = random.choice(_color_name_) + random.choice(_color_number)

                while _color_state == True:
                    if _start != _end:
                        _color_state = False
                    else:
                        _start = random.choice(_color_name_) + random.choice(
                            _color_number
                        )
                        _end = random.choice(_color_name_) + random.choice(
                            _color_number
                        )
                else:
                    _gradient = Container(
                        bgcolor="white",
                        padding=40,
                        border_radius=12,
                        aspect_ratio=1,
                        col={"xs": 12, "sm": 6, "md": 6, "lg": 6, "xl": 3},
                        content=Container(
                            aspect_ratio=1,
                            border_radius=500,
                            gradient=LinearGradient(
                                begin=alignment.bottom_left,
                                end=alignment.top_right,
                                colors=[_start, _end],
                            ),
                            data=f"gradient=LinearGradient(begin=alignment.bottom_left, end=alignment.top_right, colors=['{_start}', '{_end}']),",
                            on_click=lambda e: CopyContent(e),
                        ),
                    )
                    _.controls.append(_gradient)

        return self._color
