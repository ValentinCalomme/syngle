# This script pushes code to master, updates the docs website and pushes
# to pypi

sh bin/build.sh

UPSTREAM=${1:-'@{u}'}
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")
BASE=$(git merge-base @ "$UPSTREAM")

if [ $LOCAL = $REMOTE ]; then

    python -m mkdocs gh-deploy

    poetry publish

elif [ $LOCAL = $BASE ]; then
    echo "The local branch is behind the remote."
elif [ $REMOTE = $BASE ]; then
    echo "The local branch is ahead of the remote, please push first."
else
    echo "The local and remote branch have diverged, please fix that first."
fi
