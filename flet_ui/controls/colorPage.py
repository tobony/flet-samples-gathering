""" Color Page Class """
from flet import UserControl, ResponsiveRow, Container, alignment, Text, padding, Column
from data import *
from views import CopyContent

_color_name_ = ColorName()
_color_number = ColorNumber()
_color_white_ = ColorWhite()


class Color(UserControl):
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

        # BLACK/WHITE ROW: seperate from the rest of the colors due to number differences
        _black_white = ResponsiveRow(
            run_spacing=10,
            alignment="center",
            vertical_alignment="center",
            controls=[
                Text("BLACK/WHITE", text_align="center"),
            ],
        )

        # BLACK/WHITE CONTAINER: gathers all 10 individule colors together for resizing purposes
        _white_container = Container(
            alignment=alignment.center,
            content=_black_white,
        )

        # append to the color column
        self._color_col.controls.append(_white_container)

        #
        for _color in _color_white_:
            _color_container = Container(
                border_radius=10,
                aspect_ratio=1.25,
                bgcolor=_color,
                col={"xs": 3.175, "sm": 2.25, "md": 2.25, "lg": 1, "xl": 1},
                tooltip=f"{_color}",
                data=_color,
                on_click=lambda e: CopyContent(e),
            )
            _black_white.controls.append(_color_container)

        for _color in _color_name_:
            _responsive_row = ResponsiveRow(
                run_spacing=10,
                controls=[Text(f"{_color.upper()}", text_align="center")],
                alignment="center",
                vertical_alignment="center",
            )
            _row_container = Container(content=_responsive_row)
            self._color_col.controls.append(_row_container)

            for _number in _color_number:
                __color = f"{_color}{_number}"
                _color_container = Container(
                    border_radius=10,
                    aspect_ratio=1.25,
                    col={"xs": 3.175, "sm": 2.25, "md": 2.25, "lg": 1, "xl": 1},
                    bgcolor=__color,
                    tooltip=f"{__color}",
                    data=__color,
                    on_click=lambda e: CopyContent(e),
                )

                _responsive_row.controls.append(_color_container)

        return self._color
