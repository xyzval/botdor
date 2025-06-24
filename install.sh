#!/bin/bash
apt update && apt install -y python3 python3-pip git

# Clone repo tanpa folder bot
rm -rf botdor
git clone https://github.com/xyzval/botdor.git
cd botdor

# Langsung install di root
pip3 install -r requirements.txt
nohup python3 bot.py &
echo "Bot berhasil dijalankan di latar belakang."
