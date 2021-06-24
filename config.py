from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bot_token = os.environ.get("BOT_TOKEN")
shop_lenta_url = 'https://lenta.com/product/napitok-bezalkogolnyjj-red-bull-big-can-bolshaya-banka-toniz-energet-gaz-zhb-shvejjcariya-0473l-148381/'