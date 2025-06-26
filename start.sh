#!/bin/bash
cd "$(dirname "$0")"
nohup python3 bot.py &
echo "✅ Bot berhasil dijalankan di latar belakang."
