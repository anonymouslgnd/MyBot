from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 25769451
    API_HASH = ""
    # the name to display in your alive message
    ALIVE_NAME = "LegendBoy"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = ""
    # After cloning the repo and installing requirements do python3 telesetup.py an fill th this
    LEGEND_STRING = ""
    # create a new bot in @botfather and fill the following vales with bottoken
    BOT_TOKEN = ""
    # command handler
    HANDLER = "."
    # command hanler for sudo
    SUDO_HANDLER = "."
    # External plugins repo
    EXTERNAL_REPO = True
    EXTERNAL_REPOBRANCH = "main"
    UPSTREAM_REPO = "pro"
    VCMODE = False
    VC_SESSION = ""
    # Your City's TimeZone
    TZ = "Asia/Kolkata"
