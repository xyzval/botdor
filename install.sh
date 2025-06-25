#!/bin/bash
apt update && apt install -y python3 python3-pip git
rm -rf botdor
git clone https://github.com/xyzval/botdor.git
cd botdor || exit
pip3 install -r requirements.txt --break-system-packages
nohup python3 bot.py &
echo "✅ Bot berhasil dijalankan di latar belakang."
