from dotenv import load_dotenv
import os

load_dotenv()

# all .env keys
tripadvisor_token = os.getenv("TRIADVISOR_TOKEN")

# ui config
app_name = os.getenv("APP_NAME")
bg_color = f"#{os.getenv("BG_COLOR")}"
logo_color_yellow=f"#{os.getenv("LOGO_COLOR_YELLOW")}"