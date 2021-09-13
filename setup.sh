#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt 

line="*/1 * * * * $(pwd)/.venv/bin/python update_profile.py"
(crontab -u $(whoami) -l; echo "$line" ) | crontab -u $(whoami) -

