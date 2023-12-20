from fastapi import FastAPI

from manager.alert_manager import handle_phone_button_alert


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello buttons 1.3"}


@app.get("/api/v1/alarms/phonebtn/{phonebtn_id}")
async def phonebtn_alert(phonebtn_id: str):
    print(f"phonebtn_id: {phonebtn_id}")
    handle_phone_button_alert(phonebtn_id)

    return {"mensaje": "alerta recibida", "phonebtn_id": phonebtn_id}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8060)
