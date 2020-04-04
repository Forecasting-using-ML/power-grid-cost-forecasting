#!/bin/bash
# run a notebook ($2) using a given Python executable ($1).
$1 -m jupyter nbconvert --ExecutePreprocessor.timeout=None --execute --inplace $2
