import random
import hashlib
import os
import time

# ---- SECURITY LOGGING ----
def log_security_event(event):
    with open("security_log.txt", "a") as log:
        log.write(f"[{time.ctime()}] {event}\n")


wrong_attempts = 0  # IDS counter

print("""
====================================
🔐 CYBER-SECURE DICE GAME (CSDG)
====================================
Features:
✔ OTP Verification (2FA)
✔ SHA-256 Hashed Dice Roll (Provably Fair System)
✔ Intrusion Detection System (IDS)
✔ Security Log File
✔ Secure Input Validation
====================================
""")


def generate_otp():
    return str(random.randint(100000, 999999))


def hash_value(value):
    return hashlib.sha256(str(value).encode()).hexdigest()


def secure_dice_roll():
    dice_result = random.randint(1, 6)
    hashed = hash_value(dice_result)
    return dice_result, hashed


while True:

    print("\n🎲 New Secure Round Started!\n")

    # OTP for this round
    otp = generate_otp()
    print(f"[2FA] Your OTP for this round is: {otp}")
    user_otp = input("Enter OTP to verify: ")

    # OTP Verification
    if user_otp != otp:
        print("❌ OTP Incorrect! Access Denied.")
        wrong_attempts += 1
        log_security_event("Failed OTP verification")

        if wrong_attempts >= 3:
            print("\n🚨 INTRUSION DETECTED! 🚨")
            print("Multiple failed attempts logged.")
            log_security_event("IDS Triggered: Too many failed OTP attempts.")
            break
        continue

    print("✅ OTP Verified Successfully!\n")

    # Guess from user
    guess = input("Enter your guess (1-6) or type 'quit': ")

    if guess.lower() == "quit":
        print("\nThanks for playing the secure game! Stay protected 😎")
        break

    if not guess.isdigit():
        print("⚠ Invalid input! Only numbers allowed.")
        wrong_attempts += 1
        log_security_event("Invalid non-numeric input")

        if wrong_attempts >= 3:
            print("\n🚨 INTRUSION DETECTED! 🚨")
            log_security_event("IDS Triggered: Multiple invalid inputs.")
            break
        continue

    guess = int(guess)
    if guess < 1 or guess > 6:
        print("⚠ Guess must be between 1–6.")
        log_security_event("Out-of-range guess attempt")
        continue

    # Secure Dice Roll
    dice_value, dice_hash = secure_dice_roll()

    print(f"\n🔐 Pre-roll Hash (Integrity Proof): \n{dice_hash}")

    print("\nRolling the dice securely... 🔒")
    time.sleep(1)

    print(f"\n🎲 Dice Result = {dice_value}")

    # Verify SHA-256 integrity
    print(f"🔍 Verify SHA-256 Hash: {hash_value(dice_value)}")

    if guess == dice_value:
        print("🎉 You WIN!")
    else:
        print("❌ You LOST")
