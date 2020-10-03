# This script installs the dependencies required to contribute to
# this project.


echo -e "\n### Upgrade pip ###\n"
python -m pip install --upgrade pip

sh bin/scripts/poetry_setup.sh

echo -e "\n### Install packages via poetry ###\n"
poetry update

echo -e "\n### Activate virtual environment ###\n"
source .venv/Scripts/activate

echo -e "\n### Install pre-commit hooks ###\n"
pre-commit install
