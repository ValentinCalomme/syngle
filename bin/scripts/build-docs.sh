# This script builds the documentation

echo "### Build documentation via mkdocs ###"

python -m mkdocs build

cp ./docs/index.md ./README.md
