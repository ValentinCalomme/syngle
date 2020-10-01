# This script builds the documentation

echo "### Build documentation via mkdocs ###"

python -m mkdocs build

echo "### Generate badges ###"

python -m pytest
coverage-badge -o docs/assets/coverage.svg

python -m docstr-coverage --badge docs/assets/docstr-coverage.svg

echo "### Update README.md to follow docs/index.md ###"

cp ./docs/index.md ./README.md
