#!/bin/bash
cd ~/botdor || { echo "❌ Folder ~/botdor tidak ditemukan"; exit 1; }
nohup python3 bot.py &
echo "✅ Bot berhasil dijalankan di background."
