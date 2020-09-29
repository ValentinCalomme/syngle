# This script pushes code to master, updates the docs website and pushes
# to pypi

sh bin/build.sh

if git diff-index --quiet master --; then

    git push origin master

    python -m mkdocs gh-deploy

    poetry publish --build

else
    echo "Please commit all changes before committing."
fi
