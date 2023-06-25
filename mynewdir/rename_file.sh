#!/bin/bash

for file in *.txt; do
  name=$(basename "$file" .txt)
  echo mv "$file" "$name.tx"
done
