# GenTestAI
GenTestAI-Generative AI for mobile app acceptance testing.
This project generates acceptance test scripts in Gherkin syntax (.feature files) for mobile app features using Large Language Models (LLMs).
It supports multiple backends (Mistral-7B GPTQ, Phi-2, OPT-1.3B) and outputs Cucumber-ready scenarios with tags.

✨ Features
🔹 Generates .feature files directly from plain English feature descriptions.
🔹 Uses Hugging Face LLMs for text generation.
🔹 Adds Cucumber tags (@Login, @Positive, @Negative).
🔹 Supports multiple models:

Mistral-7B-Instruct (GPTQ, 4-bit)

Microsoft Phi-2

Facebook OPT-1.3B
⚙️ Installation

Clone the repository and install dependencies:
git clone https://github.com/Navoneel3/GenTestAI.git
cd GenTestAI
pip install -r requirements.txt

Use Cases
✅ Agile teams generating acceptance criteria quickly
✅ QA engineers writing Cucumber/Behave/SpecFlow tests automatically
✅ Students & researchers experimenting with LLMs for test automation

📚 Acknowledgments
Hugging Face Transformers
Cucumber
TheBloke’s GPTQ Models
Microsoft Phi-2
Facebook OPT Models

