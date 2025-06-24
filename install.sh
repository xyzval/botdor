#!/bin/bash
# Update sistem dan install dependensi
apt update && apt install -y python3 python3-pip git

# Clone repository GitHub
rm -rf botdor
git clone https://github.com/xyzval/botdor.git
cd botdor/bot

# Install requirements dan jalankan bot
pip3 install -r requirements.txt
nohup python3 bot.py &

echo "Bot berhasil dijalankan di latar belakang."
