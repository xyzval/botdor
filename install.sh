#!/bin/bash
# Update sistem dan install dependensi dasar
apt update && apt install -y python3 python3-pip git

# Hapus repo lama dan clone ulang dari GitHub
rm -rf botdor
git clone https://github.com/xyzval/botdor.git
cd botdor || exit

# Install dependensi Python dengan flag --break-system-packages (Python 3.12+)
pip3 install -r requirements.txt --break-system-packages

# Jalankan bot di background
nohup python3 bot.py &

echo "âœ… Bot berhasil dijalankan di latar belakang."
