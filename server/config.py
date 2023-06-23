import os

class AppConfig():
    origins = [ 
        "http://localhost",
        "http://localhost:9800",
        "http://plaza.local",
        "http://plaza.local:9800",
        "http://piedmont",
        "http://piedmont:9800",
    ]
    apikey = "468abfab24174c0aac31ef08069b6520"

    class Server():
        host = os.environ["LOCAL_IP"]
        port = 9890

    class Client():
        host = os.environ["LOCAL_IP"]
        port = 9800

