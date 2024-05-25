from dotenv import load_dotenv
import os

load_dotenv()

# all .env keys



tripadvisor_token = os.getenv("TRIADVISOR_TOKEN")

app_name = os.getenv("APP_NAME")

bgColor = os.getenv("BG_COLOR")
bg_color = f"{bgColor}"

logoColorYellow = os.getenv("LOGO_COLOR_YELLOW")
logo_color_yellow = f"{logoColorYellow}"