import streamlit as st
import sqlite3 as sqlite
 
col1, col2 = st.columns(2)

with col1:
    st.header("IZEON INNOVATIVE PVT LTD")
    st.write("Log In to your account")
    st.write("To continue where you left off, please enter your details")
    
   
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")  # Mask the password input

    
    if st.button("Login", use_container_width=True, type="primary"):
        if username == "" or password == "":
            st.write("Please fill in both fields")
        else:
            try:
                connection = sqlite.connect("data.db")
                cursor = connection.cursor()
                
               
                cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
                user = cursor.fetchone()
                if user:
                    st.write("Login successful!")
                else:
                    st.write("Invalid email or password")
                
                cursor.close()
                connection.close()
            except Exception as e:
                st.write(f"An error occurred: {e}")


with col2:
    st.image("images/login.png")