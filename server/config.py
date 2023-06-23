import os

class Config():
    origins = [ 
        "http://localhost",
        "http://localhost:9800",
        "http://plaza.local",
        "http://plaza.local:9800",
        "http://piedmont",
        "http://piedmont:9800",
    ]
    host = os.environ["LOCAL_IP"]
    port = 9890


