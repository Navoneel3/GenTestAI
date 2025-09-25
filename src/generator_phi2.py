from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

class AcceptanceTestGenerator:
    def __init__(self, model_name="microsoft/phi-2", device="auto"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map=device
        )
        self.pipeline = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=150
        )

    def generate(self, feature_description: str) -> str:
        prompt = f"""
You are a test automation assistant. Write an acceptance test in Gherkin syntax for the following mobile app feature:

Feature: {feature_description}
"""
        output = self.pipeline(prompt)[0]['generated_text']
        result = output[len(prompt):].strip()
        return f"Feature: {feature_description}\n" + result
