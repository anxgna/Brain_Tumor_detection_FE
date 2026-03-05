import string
from config.settings import ERROR_BACKEND_OFFLINE, ERROR_INVALID_IMAGE

def format_prediction_result(result: dict) -> tuple[str, str, str]:
    """
    Formats the JSON response from the backend intro clear, cute outputs.
    Returns: (Diagnosis Text, Confidence HTML, Overall Status HTML)
    """
    if "error" in result:
        err_type = result["error"]
        if err_type == "backend_offline":
            return ERROR_BACKEND_OFFLINE, "", ""
        return "An unknown error occurred during prediction. 😢", "", ""
        
    prediction = result.get("prediction", "Unknown")
    confidence = result.get("confidence", 0.0)
    
    # Format confidence as a percentage
    conf_percentage = f"{confidence * 100:.1f}%"
    
    if prediction.lower() == "tumor":
        diagnosis_text = "🚨 **Tumor Detected!** 🚨"
        confidence_html = f"<div style='color: #ff4d4d; font-size: 20px; font-weight: bold;'>Confidence: {conf_percentage}</div>"
        status_html = "<div style='padding: 15px; border-radius: 10px; background-color: #ffe6e6; border: 2px solid #ff4d4d; text-align: center;'><strong>Oh no! Our model detected a potential tumor. Please consult a doctor for a professional diagnosis. 🏥💖</strong></div>"
    else:
        diagnosis_text = "✨ **No Tumor Detected!** ✨"
        confidence_html = f"<div style='color: #4CAF50; font-size: 20px; font-weight: bold;'>Confidence: {conf_percentage}</div>"
        status_html = "<div style='padding: 15px; border-radius: 10px; background-color: #e6ffe6; border: 2px solid #4CAF50; text-align: center;'><strong>Great news! Our model did not detect any tumor. Stay healthy! 🌸🍏</strong></div>"
        
    return diagnosis_text, confidence_html, status_html
