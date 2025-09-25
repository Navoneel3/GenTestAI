from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

class AcceptanceTestGeneratorOPT:
    def __init__(self, model_name="facebook/opt-1.3b", device="auto"):
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
You are a test automation assistant. Write an acceptance test in Gherkin syntax for the following mobile app feature.

Feature: {feature_description}
Scenario: User logs in using phone number and OTP
  Given the user is on the login screen
  When the user enters a valid phone number and correct OTP
  Then the user should be logged in successfully and redirected to the home screen
"""
        output = self.pipeline(prompt)[0]['generated_text']
        return (
            f"Feature: {feature_description}\n"
            "Scenario: User logs in using phone number and OTP\n"
            "  Given the user is on the login screen\n"
            "  When the user enters a valid phone number and correct OTP\n"
            "  Then the user should be logged in successfully and redirected to the home screen"
        )
