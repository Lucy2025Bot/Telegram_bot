# Aviator Telegram Bot

## Features
- Predicts Aviator rounds
- Supports webhook for fast response
- Runs 24/7 on Render

## Setup

### 1. Create a Telegram Bot
1. Go to [@BotFather](https://t.me/BotFather) on Telegram.
2. Send `/newbot` and follow the instructions.
3. Copy the **BOT_TOKEN** you receive.

### 2. Create Environment Variables
For local development, create a `.env` file:
```
BOT_TOKEN=your_new_bot_token_here
WEBHOOK_URL=https://telegram-bot-wbt3.onrender.com/webhook
```
For **Render**, manually add environment variables:
- **Key:** `BOT_TOKEN` → **Value:** *(your bot token)*
- **Key:** `WEBHOOK_URL` → **Value:** `https://telegram-bot-wbt3.onrender.com/webhook`

### 3. Deploy on Render
1. Push your bot files to GitHub.
2. Connect your GitHub repo to Render.
3. Set the **start command** as:
   ```
   ./start.sh
   ```

### 4. Fix Port Issue (If Any)
Modify `start.sh` to:
```
uvicorn bot:app --host 0.0.0.0 --port $PORT
```
Then restart your bot.

### 5. Set Webhook
1. Delete old webhook:
```
https://api.telegram.org/botYOUR_NEW_BOT_TOKEN/deleteWebhook
```
2. Set new webhook:
```
https://api.telegram.org/botYOUR_NEW_BOT_TOKEN/setWebhook?url=https://telegram-bot-wbt3.onrender.com/webhook
```

### 6. Test Your Bot
Send `/start` in Telegram to check if it responds.
