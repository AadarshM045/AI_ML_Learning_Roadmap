import string


def check_password(password):        # ✅ renamed
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Use at least 8 characters")

    if any(char in string.ascii_lowercase for char in password):
        score += 1
    else:
        feedback.append("❌ Add a LOWERCASE letter")     # ✅ "a" not "an"

    if any(char in string.ascii_uppercase for char in password):
        score += 1
    else:
        feedback.append("❌ Add an UPPERCASE letter")

    if any(char in string.digits for char in password):
        score += 1
    else:
        feedback.append("❌ Add a number")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("❌ Add a special character (!@#$...)")

    return score, feedback


def get_strength(score):
    if score == 5:
        return "🟢 Very Strong"
    elif score == 4:
        return "🟡 Strong"
    elif score == 3:
        return "🟠 Medium"
    elif score == 2:
        return "🔴 Weak"
    else:
        return "💀 Very Weak"


def main():
    print("🔐 Password Strength Checker")
    print("-" * 30)

    password = input("Enter a password to check: ")

    score, feedback = check_password(password)   # ✅ renamed
    strength = get_strength(score)

    print(f"Score    : {score}/5")
    print(f"Strength : {strength}")

    if feedback:
        print("\nTo improve your password:")
        for tip in feedback:
            print(tip)
    else:
        print("\n✅ Perfect! Your password passes all checks.")


if __name__ == "__main__":
    main()
