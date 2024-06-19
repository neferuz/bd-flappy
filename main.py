from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class TelegramMessage(BaseModel):
    update_id: int
    message: dict

@app.post("/webhook")
async def handle_webhook(message: TelegramMessage):
    # Обработка сообщения
    print(message)
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)