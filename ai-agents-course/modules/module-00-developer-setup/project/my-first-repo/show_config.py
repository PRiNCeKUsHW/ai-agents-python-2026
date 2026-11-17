"""show_config.py: read settings from .env without putting secrets in code."""

import os

from dotenv import load_dotenv

load_dotenv()  # copies KEY=value lines from .env into os.environ

app_name = os.environ.get("APP_NAME", "my-app")
debug = os.environ.get("DEBUG", "false").lower() == "true"
api_key = os.environ.get("API_KEY", "")

print(f"App name : {app_name}")
print(f"Debug    : {debug}")
# Never print a secret. Show only that it exists and how long it is.
if api_key:
    print(f"API key  : set ({len(api_key)} characters, value hidden)")
else:
    print("API key  : NOT SET")
