#!/bin/bash
## Running PandaUserbot

terakhir () {
    echo "
    
=+---------------------------------------------------------+=
꧁༺ Panda Userbot ༻꧂
Copyright (C) 2021 PandaX_Userbot
Powered By @diemmmmmmmmmm with Telegram
=+---------------------------------------------------------+=
    "
}

_start_all () {
    terakhir
    python3 ../installer/updater.py ../requirements.txt requirements.txt
    python3 -m userbot
}

_start_all
