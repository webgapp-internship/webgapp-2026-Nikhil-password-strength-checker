def check_password_strength(password):
    
    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%&" for char in password)
    
    
    score = sum([length, has_upper, has_lower, has_digit, has_special])
    
   
    feedback = []
    if not length: feedback.append("at least 8 characters")
    if not has_upper: feedback.append("one uppercase letter")
    if not has_lower: feedback.append("one lowercase letter")
    if not has_digit: feedback.append("one number")
    if not has_special: feedback.append("one special symbol (@#$ %&!)")
    
    
    if score == 5: strength = "Very Strong"
    elif score >= 3: strength = "Strong"
    elif score == 2: strength = "Moderate"
    else: strength = "Weak"
    
    return strength, feedback


user_password = input("Enter your password: ")
strength, feedback = check_password_strength(user_password)

print(f"\nPassword Strength: {strength}")
if feedback:
    print(f"To improve, add: {', '.join(feedback)}.")