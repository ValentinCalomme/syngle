# This script is meant to install poetry and to configure it
# such that the virtual environment is created in the root folder
# of the project

if ! type "poetry" > /dev/null;
then

    echo "Install poetry"
    python -m pip install -U poetry
fi

echo "Configure poetry"
python -m poetry config virtualenvs.create true
python -m poetry config virtualenvs.in-project true
