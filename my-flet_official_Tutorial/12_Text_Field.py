import flet
from flet import Page, TextField


def main(page: Page):
    text_input = TextField()

    page.controls.append(text_input)
    page.update()


# flet.app(target=main)
flet.app(target=main, port=8080, view=flet.WEB_BROWSER)
