from dotenv import load_dotenv
import os

load_dotenv()

# all .env keys
tripadvisor_token = os.getenv("TRIADVISOR_TOKEN")