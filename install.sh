#!/bin/bash
apt update && apt install -y python3 python3-pip git

rm -rf botdor
git clone https://github.com/xyzval/botdor.git
cd botdor

pip3 install -r requirements.txt
nohup python3 bot.py &

echo "Bot telah dijalankan di latar belakang."
