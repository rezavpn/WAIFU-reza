class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = 1463920223
    sudo_users = "1683587530", "5254260722", "6747049506", "5539507956", "6915699640", "1463920223","1666459894"
    GROUP_ID = "-1002032751462"
    TOKEN = "6815163005:AAEnQXDqju9C-jRV7x7GyQSmL3bqqt03JDk"
    mongo_url = "mongodb+srv://reza:reza@rezavpn.0n5u13c.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/ff59826943869e919a58d.jpg"]
    SUPPORT_CHAT = "Origanimegc"
    UPDATE_CHAT = "risuenoofc"
    BOT_USERNAME = "Origanime_H_W_GuessBot"
    OWNER_BOT = "reza01345"
    CHARA_CHANNEL_ID = "-1002119942993"
    api_id = "2170226"
    api_hash = "ed1412c738a861fbda7f1a7aa2b7b43b"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
