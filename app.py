import streamlit as st
import string
import random
import re


# title
st.title("🚀 Assignment 2")
st.title("🔒 Password Strength Meter 🔑")


# Create Password
def generate_password(length):
    characters = string.digits + string.ascii_letters + "!@#$%^&*"
    return "".join(random.choice(characters) for i in range (length))


# Common ones
def check_password_strength(password):
    score = 0
    common_Passwords = ["12345", "abc1234", "password"]
    if password in common_Passwords:
        return "❌ This password is too commmon. Choose a more unique one.", "Weak"
    

# Generate Password
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🌀 Password should be atleast 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🌀 Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🌀 Add atleast one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🌀 Include atleast one special character (!@#$%^&*).")


# Return Password Strength
    if score == 4:
        return "✅ Strong Password!", "Strong"
    elif score == 3:
        return "⚠ Moderate Password - Consider adding more security features.", "Moderate"
    else:
        return "/n".join(feedback),"Weak"


check_password = st.text_input("Enter your password:",type="password") 
if st.button("Check Strength"):
    if check_password:
        result , strength = check_password_strength(check_password)
        if strength == "Strong":
            st.success(result)
            st.snow()
        elif strength == "Moderate":
            st.warning(result)
        else:
            st.error("Weak Password - Improve it using these tips:")
            for tip in result.split("/n"):
                st.write(tip)        
    else:
        st.warning("Please enter a password")
    

# Suggestion
password_length = st.number_input("Enter the length of password", min_value=8,max_value=20, value=10 )
if st.button("Generate Password"):
    password = generate_password(password_length)
    st.success(f"{password}")