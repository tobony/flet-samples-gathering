from flet import (
    flet,
    Page,
    Container,
    Column,
    LinearGradient,
    Row,
)

from controls.navigation import Navigation
from controls.landing import Landing
from controls.content import MainContent


def FletUI(page: Page):
    def PageResize(e):
        if page.width <= 760:
            # NAVBAR FUNCTIONS: show/hide the different navbars (sidebar and top bar)
            _main_content_area.controls[0].controls[1].visible = False
            _main_content_area.controls[0].controls[1].update()

            # PADDING: show/hide the far right padding area to center the main content area
            _main_content_area.controls[0].controls[3].visible = False
            _main_content_area.controls[0].controls[3].update()

            # NAVBAR FUNCTIONS: show/hide the different navbars (sidebar and top bar)
            _navigation.controls[0].visible = True
            _navigation.update()

        else:
            _main_content_area.controls[0].controls[1].visible = True
            _main_content_area.controls[0].controls[1].update()

            _main_content_area.controls[0].controls[3].visible = True
            _main_content_area.controls[0].controls[3].update()

            _navigation.controls[0].visible = False
            _navigation.update()

    # COLUMN: add other controls to this main column
    _main_column_ = Column(scroll="auto")

    # NAVIGATION: pop-up navigation buttons when width is SMALL
    _navigation = Navigation(False)

    # LANDING: TITLE and SUBTITLE of the LANDING PAGE
    _landing = Landing()

    # MAIN CONTENT AREA: serves the main area with all the generated ocntent plus routing
    _main_content_area = MainContent()

    # MAIN COLUMN: append the above modules to the main column to display accordingly
    _main_column_.controls.append(_navigation)
    _main_column_.controls.append(_landing)
    _main_column_.controls.append(_main_content_area)

    # MAIN CONTAINER: returns the main container for all other controls. Includes the custom background.
    _main_container_ = Container(
        margin=-10,
        height=page.height,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#1f2937", "#111827"],
        ),
        expand=True,
        content=_main_column_,
    )

    # MAIN ROOT: setting up the MAIN PAGE
    page.title = "Flet UI"
    page.add(_main_container_)
    page.on_resize = PageResize
    page.update()


if __name__ == "__main__":
    flet.app(target=FletUI)
