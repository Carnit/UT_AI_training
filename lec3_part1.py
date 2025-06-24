import string
from typing import Dict

vault: Dict[str, str] = {}

def is_strong(password: str) -> bool:
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    return len(password) > 8 and has_upper and has_lower and has_digit and has_special


def classify_strength(password: str) -> str:
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])

    if length >= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >= 3:
        return "Medium"
    else:
        return "Weak"


def add_credential() -> None:
    site: str = input("Enter site/app name: ").strip()
    password: str = input("Enter password: ").strip()
    vault[site] = password
    print(f"Credential added for {site}")


def view_credentials() -> None:
    if not vault:
        print("No credentials stored.")
        return
    print("\nStored Credentials:")
    for site, pwd in vault.items():
        print(f"- {site}: {pwd}")
    print()


def delete_credential() -> None:
    site: str = input("Enter site/app name to delete: ").strip()
    if site in vault:
        del vault[site]
        print(f"Credential deleted for {site}")
    else:
        print("No such credential found.")


def analyze_passwords() -> None:
    if not vault:
        print("No credentials to analyze.")
        return

    print("\nPassword Strength Analysis:")
    for site, pwd in vault.items():
        strength = classify_strength(pwd)
        print(f"- {site}: {strength}")

    strong_passwords = list(filter(lambda p: is_strong(p), vault.values()))
    print(f"\nStrong Passwords Count: {len(strong_passwords)}")


def menu() -> None:
    while True:
        print("\n=== Password Vault Menu ===")
        print("1. Add New Credential")
        print("2. View Credentials")
        print("3. Delete a Credential")
        print("4. Analyze Password Strength")
        print("5. Exit")
        choice: str = input("Choose an option (1-5): ")

        if choice == "1":
            add_credential()
        elif choice == "2":
            view_credentials()
        elif choice == "3":
            delete_credential()
        elif choice == "4":
            analyze_passwords()
        elif choice == "5":
            print("Exiting Password Vault. Stay safe!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
