from fastapi import FastAPI, HTTPException
from app.models import get_model, predict

app = FastAPI(title="GENUIE ML Server")

# Simple health check endpoint
@app.get("/")
def read_root():
    return {"message": "GENUIE Multi-Model Server is running"}

# Main prediction endpoint for any model
@app.post("/predict/{model_id}")
async def model_predict(model_id: str, input_data: dict):
    # Step 1: Try to load the model (it will be cached)
    model = get_model(model_id)
    if model is None:
        raise HTTPException(status_code=404, detail=f"Model '{model_id}' not found")
    
    # Step 2: Make a prediction
    try:
        result = predict(model, input_data)
        return {"model_id": model_id, "result": result, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

# Endpoint to list available models
@app.get("/models")
def list_models():
    # This would read from your model registry
    return {"available_models": ["model_1", "model_2", "model_3"]}
