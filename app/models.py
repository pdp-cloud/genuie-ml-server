import sys
from functools import lru_cache

# In-memory cache for loaded models
MODEL_CACHE = {}

# Try to import tensorflow, but don't fail if it's not installed
try:
    import tensorflow as tf
    TENSORFLOW_AVAILABLE = True
    print("✓ TensorFlow is available")
except ImportError:
    TENSORFLOW_AVAILABLE = False
    print("⚠ TensorFlow is not available - running in demo mode")

@lru_cache(maxsize=7)  # Cache for up to 7 models
def get_model(model_id: str):
    """
    Loads a TensorFlow SavedModel from disk.
    For now, it returns a placeholder. Replace with actual loading logic.
    """
    if model_id not in MODEL_CACHE:
        # PLACEHOLDER: In a real setup, you would load from ./models/{model_id}/
        # Example: model = tf.saved_model.load(f"./models/{model_id}")
        print(f"Loading model: {model_id}")
        
        # For demonstration, create a simple dummy model
        # REPLACE THIS with actual tf.saved_model.load() for your real models
        class DummyModel:
            def __call__(self, inputs):
                # Simulate a simple prediction
                if isinstance(inputs, list):
                    return {"prediction": sum(inputs), "status": "demo_mode"}
                else:
                    return {"prediction": inputs * 2, "status": "demo_mode"}
        
        MODEL_CACHE[model_id] = DummyModel()
    
    return MODEL_CACHE.get(model_id)

def predict(model, input_data: dict):
    """
    Runs prediction using the loaded model.
    Adapt this function based on your model's expected input format.
    """
    # Extract features from input_data dictionary
    # This is a simple example - adjust for your model's needs
    features = input_data.get("features", [])
    
    # Convert to format your model expects (e.g., TensorFlow tensor)
    # For the dummy model, we just pass the features directly
    prediction = model(features)
    
    return prediction
