from fastapi import FastAPI, File, UploadFile
import google.generativeai as genai

# Configure Gemini client
genai.configure(api_key="YOUR_GEMINI_API_KEY")

app = FastAPI()

@app.post("/summarize")
async def summarize(file: UploadFile = File(...)):
    # Read and decode uploaded text file
    text = (await file.read()).decode()

    # Initialize the Gemini model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Generate summary
    response = model.generate_content(f"Summarize the following text:\n\n{text}")

    # Return the result
    return {"summary": response.text}
