!pip install transformers accelerate torch
from google.colab import drive

# Mount Google Drive
import os
from pathlib import Path

drive.mount('/content/drive')
drive_path = "/content/drive/MyDrive/AcceptanceTestOutputs"
os.makedirs(drive_path, exist_ok=True)

# Import necessary libraries
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

# Load Phi-2 model from Hugging Face (public model)
model_name = "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# Create a pipeline
llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=150)

# Function to generate acceptance test script using Phi-2
def generate_acceptance_test_script(feature_description):
    prompt = f"""
You are a test automation assistant. Write an acceptance test in Gherkin syntax for the following mobile app feature:

Feature: {feature_description}
"""
    output = llm_pipeline(prompt)[0]['generated_text']
    result = output[len(prompt):].strip()
    return f"Feature: {feature_description}\n" + result

# Example feature description
feature_description = "As a user, I want to be able to log in using my phone number and OTP verification so that I can access my account securely."

# Generate the acceptance test script
acceptance_test_script = generate_acceptance_test_script(feature_description)
print("\nGenerated Acceptance Test Script:\n")
print(acceptance_test_script)

# Save to file in Google Drive
file_path = Path(drive_path) / "acceptance_test_script_phi2.txt"
with open(file_path, "w") as f:
    f.write(acceptance_test_script)

print(f"\nTest script saved to: {file_path}")
