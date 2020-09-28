# This script builds the documentation and the package wheels

cp README.md docs/index.md

mkdocs build

poetry build
