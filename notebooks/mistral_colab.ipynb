# Install required packages
!pip install transformers accelerate auto-gptq
from google.colab import drive

# Mount Google Drive
import os
from pathlib import Path

drive.mount('/content/drive')
drive_path = "/content/drive/MyDrive/AcceptanceTestOutputs"
os.makedirs(drive_path, exist_ok=True)

# Import necessary libraries
from transformers import AutoTokenizer, pipeline
from auto_gptq import AutoGPTQForCausalLM
import torch

# Load 4-bit quantized Mistral-7B-Instruct model
model_name = "TheBloke/Mistral-7B-Instruct-v0.1-GPTQ"

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoGPTQForCausalLM.from_quantized(
    model_name,
    use_safetensors=True,
    trust_remote_code=True,
    device="cuda:0"
)

# Create a pipeline
llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=200)

# Function to generate acceptance test script using Mistral-7B-Instruct (4-bit)
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
file_path = Path(drive_path) / "acceptance_test_script_mistral.txt"
with open(file_path, "w") as f:
    f.write(acceptance_test_script)

print(f"\nTest script saved to: {file_path}")
