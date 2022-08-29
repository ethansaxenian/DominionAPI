import requests

from core.config import get_settings

settings = get_settings()

if not settings.RENDER_SERVICE_ID or not settings.RENDER_DEPLOY_KEY:
    print("Deploy failed: missing service ID or deploy key")

else:
    requests.post(
        f"https://api.render.com/v1/services/{settings.RENDER_SERVICE_ID}/deploys",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {settings.RENDER_DEPLOY_KEY}",
        },
    )
