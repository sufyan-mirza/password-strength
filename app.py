import re
import streamlit as st

st.title("Password Strength Meter")
st.write("Here you can create a password and check the strength of Password")

def check_password_strength(password):
    score=0
    feedback=[]

    if len(password) >=8:
        score += 1
    else:
        feedback.append("your password length should be 8 character")
    
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score += 1
    else:
        feedback.apppend("your password contain both UPPERCASE and LOWERCASE")

    if re.search(r"/d" , password):
        score +=1 
    else:
        feedback.append("your password contain number")
    if re.search(r"[!@#$%^&*?]" , password):
        score +=1
    else:
        feedback.append("your password should contain special character")  


    if score==4:
        st.success("your password is strong")
    elif score==3:
        st.info("your password is moderate")
    else:
        st.error("you password is weak")        


    if feedback:
        with st.expander("improve your password"):
            for item in feedback:
                st.write(item)           

password=st.text_input("enter your password" , type="password", help="improve the password")

if st.button("check strength"):
        if password:
            check_password_strength(password)
        else:
            st.warning("write password")    