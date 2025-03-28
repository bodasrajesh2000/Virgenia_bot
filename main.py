from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/product")
async def get_product(request: Request):
    return JSONResponse({
        "fulfillment_response": {
            "messages": [{"text": {"text": ["We offer T-shirts, Longsleeves, CDs, Digital Albums, and Tour Movies."]}}]
        }
    })

@app.post("/price")
async def get_price(request: Request):
    return JSONResponse({
        "fulfillment_response": {
            "messages": [{"text": {"text": ["A T-shirt costs $25, and a Longsleeve is $30. CDs are $10."]}}]
        }
    })

@app.post("/confirmation")
async def confirm_order(request: Request):
    body = await request.json()
    # (Optional) parse values from request to log or use
    return JSONResponse({
        "fulfillment_response": {
            "messages": [{"text": {"text": ["Your order has been placed successfully! Rock on 🤘"]}}]
        }
    })
