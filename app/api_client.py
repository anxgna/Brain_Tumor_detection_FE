import requests
import logging
from config.settings import UPLOAD_ENDPOINT, PREDICT_ENDPOINT_BASE

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def predict_tumor(image_filepath: str) -> dict:
    """
    Takes an image file path from Gradio, sends it to the FastAPI backend, 
    and returns the predicted result in a dict format compatible with the cute UI.
    """
    try:
        # STEP 1: UPLOAD THE IMAGE
        with open(image_filepath, "rb") as file:
            import os
            import mimetypes
            
            filename = os.path.basename(image_filepath)
            mime_type, _ = mimetypes.guess_type(image_filepath)
            if not mime_type:
                mime_type = "image/jpeg"
                
            files = {"file": (filename, file, mime_type)}
            upload_response = requests.post(UPLOAD_ENDPOINT, files=files, timeout=30)
            
        if upload_response.status_code != 200:
            logger.error(f"Error uploading image: {upload_response.text}")
            return {"error": "http_error", "details": upload_response.text}
            
        upload_data = upload_response.json()
        scan_id = upload_data.get("scan_id")
        
        # STEP 2: TRIGGER PREDICTION
        predict_url = f"{PREDICT_ENDPOINT_BASE}?scan_id={scan_id}"
        predict_response = requests.post(predict_url, timeout=30)
        
        if predict_response.status_code != 200:
            logger.error(f"Error predicting scan: {predict_response.text}")
            return {"error": "http_error", "details": predict_response.text}
            
        return predict_response.json()
        
    except requests.exceptions.ConnectionError:
        logger.error("Could not connect to the backend server.")
        return {"error": "backend_offline"}
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return {"error": "unexpected_error", "details": str(e)}
