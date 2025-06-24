#!/usr/bin/env bash
# chmod +x ./update.sh

set -euo pipefail   # quit on error, unset var, or pipe fail

# arg check
if [[ $# -gt 1 ]]; then
 echo "Usage: $0 <git-tag>" >&2; exit 1;
elif [[ $# -eq 1 ]]; then
  TAG=$1
else
  TAG="main"
fi

CONTAINER="cutthroat-site"
LIVE_DIR=$(pwd)

# make sure container exists
docker inspect "$CONTAINER" >/dev/null 2>&1 || {
  echo "No container named $CONTAINER" >&2; exit 1; }

# scratch space, self-cleans on exit
TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT

# grab code for the given tag
git clone -q --depth 1 --branch "$TAG" \
  https://github.com/cutthroat-systems/cutthroat-site "$TMP_DIR"

# swap it in
docker stop "$CONTAINER" >/dev/null
rsync -a --delete --exclude deploy.sh "$TMP_DIR"/ "$LIVE_DIR"/
docker start "$CONTAINER" >/dev/null

echo "Yur tag '$TAG' has been deployed to yur container '$CONTAINER' pardner!"
