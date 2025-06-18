#!/usr/bin/env bash


set -euo pipefail   # quit on error, unset var, or pipe fail

# arg check
[[ $# -eq 1 ]] || { echo "Usage: $0 <git-tag>" >&2; exit 1; }
TAG=$1

CONTAINER="cutthroat-site"
LIVE_DIR=$(pwd)

# make sure container exists
docker inspect "$CONTAINER" >/dev/null 2>&1 || {
  echo "No container named $CONTAINER" >&2; exit 1; }

# scratch spac, self-cleans on exit
TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT

# grab code for the given tag
git clone --depth 1 --branch "$TAG" \
  https://github.com/cutthroat-systems/cutthroat-site "$TMP_DIR"

# swap it in
docker stop "$CONTAINER"
rsync -a --delete --exclude deploy.sh "$TMP_DIR"/ "$LIVE_DIR"/
docker start "$CONTAINER"

echo "Yur $TAG has been deployed to $CONTAINER pardner!"
