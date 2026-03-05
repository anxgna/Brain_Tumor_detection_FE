import gradio as gr


# Import local modules
from config.settings import APP_TITLE, APP_DESCRIPTION, THEME_PRIMARY_HUE, THEME_SECONDARY_HUE
from app.api_client import predict_tumor
from app.utils import format_prediction_result

# Custom CSS for a "cute" aesthetic
CUTE_CSS = """
/* Background gradient */
body {
    background: linear-gradient(135deg, #fff0f5 0%, #ffe4e1 100%);
    font-family: 'Quicksand', 'Nunito', sans-serif !important;
}

/* Rounded, soft containers */
.gradio-container {
    background: rgba(255, 255, 255, 0.9) !important;
    border-radius: 20px !important;
    box-shadow: 0 10px 30px rgba(255, 182, 193, 0.3) !important;
    padding: 30px !important;
    margin-top: 20px !important;
    margin-bottom: 20px !important;
}

/* Playful Markdown headings */
.prose h1 {
    color: #ff69b4 !important; /* Hot Pink */
    text-align: center;
    font-size: 2.5em !important;
    text-shadow: 2px 2px 5px rgba(255, 105, 180, 0.2);
}

.prose p {
    color: #555555 !important;
    font-size: 1.1em !important;
    text-align: center;
    line-height: 1.6;
}

/* Enhance Image upload box */
.image-container {
    border: 3px dashed #ffb6c1 !important; /* Light Pink border */
    border-radius: 15px !important;
    background-color: #fffafa !important; /* Snow */
    transition: all 0.3s ease;
}

.image-container:hover {
    border-color: #ff69b4 !important;
    background-color: #fff0f5 !important; /* Lavender Blush */
}

/* Style the Predict button */
button.primary {
    background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%) !important;
    color: white !important;
    font-weight: bold !important;
    font-size: 1.2em !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 15px 30px !important;
    box-shadow: 0 5px 15px rgba(255, 154, 158, 0.4) !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}

button.primary:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 8px 20px rgba(255, 154, 158, 0.6) !important;
}

button.primary:active {
    transform: scale(0.95) !important;
}

/* Output styling */
.label-component {
    font-size: 1.3em !important;
    color: #ff1493 !important; /* Deep Pink */
    border-radius: 12px !important;
    background: #ffe4e1 !important; 
    padding: 10px !important;
    border: 2px solid #ffb6c1 !important;
}
"""

def process_image(image_filepath):
    """
    Handler function for the Detect button click.
    """
    if image_filepath is None:
        return "Please upload an image first! 🥺", "", ""
        
    result = predict_tumor(image_filepath)
    return format_prediction_result(result)

def build_app():
    """
    Constructs the Gradio Application.
    """
    theme = gr.themes.Soft(
        primary_hue=THEME_PRIMARY_HUE,
        secondary_hue=THEME_SECONDARY_HUE,
        font=[gr.themes.GoogleFont("Quicksand"), "Arial", "sans-serif"]
    )
    
    with gr.Blocks(theme=theme, css=CUTE_CSS, title="Cute Brain Tumor Detector") as demo:
        
        gr.Markdown(f"# {APP_TITLE}")
        gr.Markdown(APP_DESCRIPTION)
        
        with gr.Row():
            with gr.Column(scale=1):
                image_input = gr.Image(type="filepath", label="Upload MRI Scan 🖼️", elem_classes="image-container")
                predict_btn = gr.Button("Detect Tumor 🔍✨", variant="primary")
            
            with gr.Column(scale=1):
                diagnosis_output = gr.Markdown(label="Diagnosis Status", value="Awaiting your image... 🌸")
                confidence_output = gr.HTML(label="Confidence Score")
                status_output = gr.HTML(label="Recommendation / Status")
                
                # We can also add a placeholder for future cute animations or tips
                gr.Markdown("---")
                gr.Markdown("*Tip: Make sure the MRI is clear and centered for the best results! 💡*")
                
        # Link button click to function
        predict_btn.click(
            fn=process_image,
            inputs=image_input,
            outputs=[diagnosis_output, confidence_output, status_output]
        )
        
    return demo

if __name__ == "__main__":
    # Ensure event loop handles async calls gracefully
    app = build_app()
    app.launch(server_name="0.0.0.0", server_port=7860, show_api=False)
