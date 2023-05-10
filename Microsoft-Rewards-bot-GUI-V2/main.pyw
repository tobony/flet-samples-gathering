import flet as ft
from pathlib import Path
from src.ui import UserInterface
from src.core import resource_path
import json


def main():
    if Path(resource_path("accounts.json", True)).exists():
        pass
    else:
        with open(resource_path("accounts.json", True), "w") as f:
            f.write(json.dumps([{"username": "Your Email", "password": "Your Password"}], indent=4))
    ft.app(target=UserInterface, assets_dir=resource_path("assets"))
    

if __name__ == "__main__":
    main()