#!/bin/bash

VER=$(date +"%Y%m%dt%H%M%S")
while true; do
    read -p "Promote to PRODUCTION (yes/n)? " yn
    case $yn in
        yes ) gcloud app deploy app.yaml --project=passepartout --version=$VER; git tag $VER; break;;
        [Nn]* ) gcloud app deploy app.yaml --project=passepartout --version=$VER --no-promote; git tag $VER; break;;
        * ) echo "Please answer yes or no.";;
    esac
done