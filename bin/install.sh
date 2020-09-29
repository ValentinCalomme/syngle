# This script installs the dependencies required to contribute to
# this project.

sh bin/scripts/poetry_setup.sh

echo "### Install packages via poetry ###"
python -m poetry update

echo "### Activate virtual environment ###"
source .venv/Scripts/activate

echo "### Install pre-commit hooks ###"
pre-commit install
