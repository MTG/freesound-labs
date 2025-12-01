#!/bin/env bash

if [ -z "$1" ]; then
    echo "Usage: $0 <output_directory>"
    exit 1
fi

mkdir -p $1
git clone https://github.com/MTG/freesound-labs.git
pushd freesound-labs
# The docker image that we use will force-run as the `jekyll` user, even if we exexute as root.
# jekyll tries to create this directory, but because the current directory is owned by root it will fail
# however, the runner script will chown this directory to the `jekyll` user if it already exists, so create it here
# TODO: Or, we could just run everything as the `jekyll` user.
mkdir -p _site

jekyll build
cp -r _site/* $1

popd
