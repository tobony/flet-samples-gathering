echo venv/ > .gitignore
python -m venv venv

@REM cd venv
./venv/Scripts/activate.sh
python -m pip install flet
pip install -r requirements.txt