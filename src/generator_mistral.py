import os
from pathlib import Path
from transformers import AutoTokenizer, pipeline
from auto_gptq import AutoGPTQForCausalLM

class AcceptanceTestGenerator:
    def __init__(self, model_name="TheBloke/Mistral-7B-Instruct-v0.1-GPTQ", device="cuda:0"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
        self.model = AutoGPTQForCausalLM.from_quantized(
            model_name,
            use_safetensors=True,
            trust_remote_code=True,
            device=device
        )
        self.pipeline = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=200
        )

    def generate(self, feature_description: str) -> str:
        prompt = f"""
You are a test automation assistant. Write an acceptance test in Gherkin syntax for the following mobile app feature:

Feature: {feature_description}
"""
        output = self.pipeline(prompt)[0]['generated_text']
        result = output[len(prompt):].strip()
        return f"Feature: {feature_description}\n" + result
