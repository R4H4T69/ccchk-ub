import os
import logging
import yaml

from telethon import TelegramClient
from telethon.sessions import StringSession


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)

CONFIG = yaml.load(open('config.yml', 'r'), Loader=yaml.SafeLoader)
API_ID = int(os.getenv('API_ID', CONFIG['25135353']))
API_HASH = os.getenv('API_HASH', CONFIG['744ef666a3409e3069cbe0e8e6ef30ba'])
DUMP_ID = os.getenv('DUMP_ID', CONFIG['-1002057654379'])
STRING_SESSION = os.getenv('STRING_SESSION', CONFIG['1BVtsOJEBu20w56yWzZw68t0o75q7BKeaydFcZ65WQhOAyYc3NxgJ3vOSg72BAY5tXK-zZ-igbBgP4dELH0K7gxH6yjWVWP6brbWerBGN1ytHPhr_jwEGZN8LSrHlhUHJyBVKwg_caLoWidI1RKVVanNrey54w2rD8b4OScxMQUunwVGl3jDN1S-Ty7wl5SDdpwspqbrK-ZW0X-XBrf3qpKJOVBOjpDzkfoYeQm4o9ppO-wD11zYCpL4WwmWleb5IZ9404k67GRYPpMF7K_PwRzTdnoy_xHGZp4MftgUkMFgjoSRUcDiH0oGfCck8qgarmOu62uYzdKg5t_tAgfuGcb0S8mcmCKY='])

Ubot = TelegramClient(StringSession(STRING_SESSION),
                      API_ID,
                      API_HASH,
                      auto_reconnect=False,
                      lang_code='en')
