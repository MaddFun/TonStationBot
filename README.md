TonStation bot. 

**Donation TON: UQCz2QU1r-z966MDfv1o_6pcrFSV-hKZfNOFcTFrXkO0hsP8**

## [Settings]
|        Settings         |                                      Description                                       |
|:-----------------------:|:--------------------------------------------------------------------------------------:|
|  **API_ID**             |        Your Telegram API ID (integer)                                                  |
|  **API_HASH**           |        Your Telegram API Hash (string)                                                 |
| **AUTO_FARM**        | Auto farm (True / False)     |
| **AUTO_QUESTS**  | Auto quests (True / False)    |
|  **FAKE_USERAGENT**     |        Use a fake user agent for sessions (True / False)                               |
| **USE_RANDOM_DELAY_IN_RUN** | Whether to use random delay at startup (True / False)                              |
| **RANDOM_DELAY_IN_RUN** |        Random delay at startup (e.g. [0, 15])                                          |
| **USE_PROXY_FROM_FILE** |        Whether to use a proxy from the `bot/config/proxies.txt` file (True / False)    |


# Installation
```shell
git clone https://github.com/consolko/TonStation_bot.git
cd TonStation_bot
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Here you must specify your API_ID and API_HASH, the rest is taken by default
python3 main.py
```

You can also use arguments for quick start, for example:
```shell
~/TonStation_bot >>> python3 main.py --action (1/2)
# Or
~/TonStation_bot >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```
