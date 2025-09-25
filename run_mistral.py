from src.generator import AcceptanceTestGenerator

if __name__ == "__main__":
    feature = "As a user, I want to be able to log in using my phone number and OTP verification so that I can access my account securely."
    generator = AcceptanceTestGenerator()
    test_script = generator.generate(feature)

    print("\nGenerated Acceptance Test Script:\n")
    print(test_script)

    # Save output
    with open("outputs/sample_acceptance_test.txt", "w") as f:
        f.write(test_script)
