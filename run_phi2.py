from src.generator_phi2 import AcceptanceTestGenerator

if __name__ == "__main__":
    feature = "As a user, I want to be able to log in using my phone number and OTP verification so that I can access my account securely."
    generator = AcceptanceTestGenerator()
    test_script = generator.generate(feature)

    print("\nGenerated Acceptance Test Script (Phi-2):\n")
    print(test_script)

    with open("outputs/acceptance_test_phi2.txt", "w") as f:
        f.write(test_script)
