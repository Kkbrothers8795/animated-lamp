import os


class Config:

    API_ID = 2532603
    API_HASH = "f565b00bbe3ad9c6748e39a3a71d16e7"
    BOT_TOKEN = "6600693083:AAFlLceUGrI_4o2JfxEfW-dmuwmoDhfUflU"
    SESSION_NAME = ":memory:"
    LOG_CHANNEL = "-1002046013717"
    DATABASE_URL = "mongodb+srv://user:user@cluster0.x3e1p.mongodb.net"
    AUTH_USERS = "754495556"
    MAX_PROCESSES_PER_USER = int(os.environ.get("MAX_PROCESSES_PER_USER", 2))
    MAX_TRIM_DURATION = int(os.environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = "-1002046013717"
    SLOW_SPEED_DELAY = int(os.environ.get("SLOW_SPEED_DELAY", 3))
    HOST = os.environ.get("HOST", "")
    TIMEOUT = int(os.environ.get("TIMEOUT", 60 * 30))
    DEBUG = bool(os.environ.get("DEBUG"))
    WORKER_COUNT = int(os.environ.get("WORKER_COUNT", 20))
    IAM_HEADER = os.environ.get("IAM_HEADER", "")

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
