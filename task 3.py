import re

def check_password_strength(password):
    """
    Verify the strength of 'password' based on specific criteria.
    Returns a string indicating the strength level.
    """
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*()-+]", password) is None # Specific symbols check

    if not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error):
        return "Strong"
    else:
        # You can add logic for 'Moderate' or 'Weak' based on which conditions fail
        return "Weak or Moderate" 

# Example usage:
user_password = input("Enter your password: ")
strength = check_password_strength(user_password)
print(f"The password is {strength}.")