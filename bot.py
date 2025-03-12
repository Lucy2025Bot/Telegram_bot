import logging
import httpx
from fastapi import FastAPI, Request, BackgroundTasks
from config import BOT_TOKEN, WEBHOOK_URL

# Telegram API URL
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

# FastAPI app
app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/")
def home():
    return {"status": "Aviator Bot is Running!"}

@app.post("/webhook")
async def webhook(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "").lower()

        if text == "/start":
            background_tasks.add_task(send_message, chat_id, "Welcome to the Aviator Predictor Bot! Use /predict to get predictions.")
        elif text == "/predict":
            prediction = "Next round: High chance of 2x+ multiplier!"
            background_tasks.add_task(send_message, chat_id, prediction)

    return {"status": "ok"}

async def send_message(chat_id, text):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"{TELEGRAM_API}/sendMessage", json={"chat_id": chat_id, "text": text})
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            logging.error(f"Error sending message: {e.response.text}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
