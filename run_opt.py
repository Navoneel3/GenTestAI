from src.generator_opt import AcceptanceTestGeneratorOPT

if __name__ == "__main__":
    feature = "As a user, I want to be able to log in using my phone number and OTP verification so that I can access my account securely."
    generator = AcceptanceTestGeneratorOPT()
    test_script = generator.generate(feature)

    print("\nGenerated Acceptance Test Script (OPT):\n")
    print(test_script)

    with open("outputs/acceptance_test_opt.txt", "w") as f:
        f.write(test_script)
