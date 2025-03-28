from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

# Static place recommendations
places_by_city = {
    "richmond": [
        "Virginia Museum of Fine Arts",
        "Lewis Ginter Botanical Garden",
        "Maymont Park"
    ],
    "norfolk": [
        "Fort Norfolk",
        "MacArthur Memorial",
        "Norfolk Botanical Garden"
    ],
    "charlottesville": [
        "Monticello",
        "University of Virginia Rotunda",
        "Downtown Mall"
    ],
    "default": [
        "Colonial Williamsburg",
        "Blue Ridge Parkway",
        "Shenandoah National Park"
    ]
}

@app.post("/placesWebhook")
async def places_webhook(request: Request):
    body = await request.json()
    parameters = body.get("sessionInfo", {}).get("parameters", {})
    city = parameters.get("location", "").lower()

    place_list = places_by_city.get(city, places_by_city["default"])
    places_text = "\n- " + "\n- ".join(place_list)

    response = {
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": [
                            f"Here are some great places to visit in {city.title() if city else 'Virginia'}:{places_text}"
                        ]
                    }
                }
            ]
        }
    }
    return response

# To run locally
# uvicorn filename:app --reload --port 8000
