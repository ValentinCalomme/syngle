# This script builds the documentation

echo -e "\n### Build documentation via mkdocs ###\n"

python -m mkdocs build

echo -e "\n### Generate badges ###\n"

python -m pytest
coverage-badge -o docs/assets/coverage.svg

python -m docstr-coverage --badge docs/assets/docstr-coverage.svg

echo -e "\n### Update README.md to follow docs/index.md ###\n"

cp ./docs/index.md ./README.md
