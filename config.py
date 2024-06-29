#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7213198715:AAHeL-v3G2957kmjihTnKYsYi94DITLUHJw")
    API_ID = int(os.environ.get("API_ID", "15958423"))
    API_HASH = os.environ.get("API_HASH", "0f38f0c37cec744bccb074b5180e37b0")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7213198715")
