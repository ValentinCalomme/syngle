# This script is meant to install poetry and to configure it
# such that the virtual environment is created in the root folder
# of the project

if ! type "poetry" > /dev/null;
then

    echo -e "\n### Install poetry ###\n"
    python -m pip install -U poetry

fi

echo -e "\n### Configure poetry ###\n"
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true
