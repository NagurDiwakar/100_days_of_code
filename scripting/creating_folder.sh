#!/usr/bin/env bash
# Description: This script creates a folder if it doesn't already exist.

Folder_NAME="my_new_folder"

if [-Z "$Folder_NAME" ]; then
  echo "Folder name is empty. Please provide a valid folder name."
  exit 1
fi

if [ ! -d "$Folder_NAME" ]; then
  mkdir "$Folder_NAME"
  cd "$Folder_NAME"
  touch README.md
  echo "hi my name is diwakar" > README.md
  echo "Folder '$Folder_NAME' and 'README.md' created successfully."
else
  echo "Folder '$Folder_NAME' already exists."
fi
