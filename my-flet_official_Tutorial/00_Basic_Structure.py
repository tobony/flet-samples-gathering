import flet
from flet import Page

def main(page: Page):
    pass

# flet.app(target=main, port=8080)
# flet.app(target=main, view=WEB_BROWSER, port=8080)
flet.app(target=main, port=8080, view=flet.WEB_BROWSER)

