#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-23 17:55:52

import begin
import uvicorn
from server.config import AppConfig
import server.main

@begin.start
def main(arg1 = None):
    conf = uvicorn.Config(
            app="server.main:app",
            host="localhost",
            port=8000,
            log_level="debug"
        )
    server = uvicorn.Server(conf)
    server.run()

