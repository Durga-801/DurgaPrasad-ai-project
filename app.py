from google import genai
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Send request to the model
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain artificial intelligence in simple terms."
)

# Display the response
print(interaction.output_text)