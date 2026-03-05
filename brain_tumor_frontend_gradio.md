# Brain Tumor Detection System (Frontend Architecture - Gradio)

## 1. Overview

The frontend of the Brain Tumor Detection System is implemented using
**Gradio**, a Python-based UI framework designed for quickly building
interfaces for machine learning applications.

The Gradio interface allows users to:

-   Upload MRI brain scan images
-   Send the image to the FastAPI backend
-   Receive tumor prediction results
-   View confidence scores
-   Visualize the uploaded MRI scan

Gradio serves as the **user interface layer** that communicates with the
backend inference API.

------------------------------------------------------------------------

# 2. System Architecture

User (Browser) \| \| Gradio Interface \| \| FastAPI Backend API \| \| ML
Model + MySQL Database

The frontend does not directly interact with the ML model. All inference
requests are routed through the FastAPI backend.

------------------------------------------------------------------------

# 3. Tech Stack

Frontend Framework: Gradio\
Programming Language: Python\
HTTP Communication: Requests / HTTPX\
Backend API: FastAPI\
Data Format: JSON\
Image Handling: PIL / NumPy

------------------------------------------------------------------------

# 4. Project Folder Structure

brain-tumor-frontend/

app/ gradio_app.py api_client.py utils.py

assets/ logo.png sample_mri.png

config/ settings.py

requirements.txt

------------------------------------------------------------------------

# 5. UI Components

The Gradio UI will include the following components:

### Image Upload Component

Allows users to upload MRI scans.

Component:

gr.Image(type="pil")

Supported formats:

-   PNG
-   JPG
-   JPEG

------------------------------------------------------------------------

### Prediction Button

Triggers the prediction request to the FastAPI backend.

Component:

gr.Button("Detect Tumor")

------------------------------------------------------------------------

### Prediction Output

Displays the prediction label returned by the backend.

Component:

gr.Label()

Possible outputs:

-   Tumor Detected
-   No Tumor Detected

------------------------------------------------------------------------

### Confidence Score

Displays the model confidence percentage.

Component:

gr.Textbox()

Example output:

Confidence: 94.2%

------------------------------------------------------------------------

### MRI Preview

Displays the uploaded MRI scan.

Component:

gr.Image()

------------------------------------------------------------------------

# 6. Backend API Communication

The Gradio frontend sends the uploaded MRI image to the backend API.

Endpoint:

POST /predict

Request type:

multipart/form-data

Payload:

image: MRI scan file

Example request flow:

1.  User uploads MRI scan
2.  Image converted to bytes
3.  POST request sent to FastAPI
4.  Backend processes prediction
5.  JSON response returned

Example response:

{ "prediction": "Tumor", "confidence": 0.94 }

------------------------------------------------------------------------

# 7. API Client Module

The API client handles communication between Gradio and FastAPI.

Responsibilities:

-   Send HTTP requests
-   Handle responses
-   Manage errors

Example logic:

upload_image → send_request → receive_prediction → display_result

------------------------------------------------------------------------

# 8. Gradio Interface Layout

The UI layout will follow a simple vertical layout.

Title

Brain Tumor Detection using MRI

Components:

1.  Image Upload
2.  Detect Tumor Button
3.  MRI Preview
4.  Prediction Result
5.  Confidence Score

Layout Example:

Title \| Upload MRI \| \[Detect Tumor\] \| MRI Preview \| Prediction
Result \| Confidence Score

------------------------------------------------------------------------

# 9. Core Prediction Workflow

Step 1: User uploads MRI scan\
Step 2: Gradio captures image input\
Step 3: Image sent to FastAPI /predict endpoint\
Step 4: Backend runs preprocessing + model inference\
Step 5: Prediction returned as JSON\
Step 6: Gradio displays result to user

------------------------------------------------------------------------

# 10. Error Handling

Frontend handles the following errors:

Invalid image format

Server unavailable

Prediction failure

Network error

Example message:

"Unable to process MRI scan. Please try again."

------------------------------------------------------------------------

# 11. Performance Considerations

Optimizations include:

-   Compressing image before sending
-   Asynchronous API calls
-   Limiting upload size
-   Caching repeated predictions

------------------------------------------------------------------------

# 12. Deployment Options

Gradio interface can be deployed using:

Local development:

python gradio_app.py

Cloud platforms:

Hugging Face Spaces

Render

Docker container

Server deployment example:

gradio.launch(server_name="0.0.0.0", server_port=7860)

------------------------------------------------------------------------

# 13. Security Considerations

To ensure safe usage:

-   File type validation
-   Upload size limit
-   API authentication token
-   Rate limiting

------------------------------------------------------------------------

# 14. Example User Flow

User opens interface → Uploads MRI image → Clicks Detect Tumor → Backend
processes request → Prediction displayed

Example Output:

Prediction: Tumor Detected\
Confidence: 93.7%

or

Prediction: No Tumor\
Confidence: 97.4%

------------------------------------------------------------------------

# End of Frontend Architecture
