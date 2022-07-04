#!/bin/bash
echo $"#/bin/sh\nblack .\n" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

python3 -m pip install -r requirements.txt
python3 -m pip install -e .