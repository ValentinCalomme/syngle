# This script builds the documentation

python -m mkdocs build

cp ./docs/index.md ./README.md
