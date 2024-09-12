import sqlite3
import streamlit as st
import base64

# Function to convert file to Base64 and insert student data with resume stored as BLOB
def insert_student_blob(name, contact_number, join_date, course, resume_file):
    try:
        # Read the resume file as binary data
        resume_data = resume_file.read()
        
        # Encode the binary data to Base64
        resume_base64 = base64.b64encode(resume_data)
        
        # Connect to the database
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        
        # SQL query to insert data into the students table
        insert_query = """
        INSERT INTO students (name, contact_number, join_date, course, resume)
        VALUES (?, ?, ?, ?, ?);
        """
        
        # Execute the query
        cursor.execute(insert_query, (name, contact_number, join_date, course, resume_base64))
        connection.commit()
        
        st.write("Student data inserted successfully!")
        
    except Exception as e:
        st.write(f"An error occurred: {e}")
        
    finally:
        cursor.close()
        connection.close()

# Streamlit UI
def main():
    st.title("Insert Student Data")
    
    with st.form(key='student_form'):
        name = st.text_input("Name")
        contact_number = st.text_input("Contact Number")
        join_date = st.date_input("Join Date")
        course = st.text_input("Course")
        resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
        
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            if resume_file is not None:
                insert_student_blob(name, contact_number, join_date, course, resume_file)
            else:
                st.write("Please upload a resume file.")

if __name__ == "__main__":
    main()
