import sqlite3
import streamlit as st
import base64

def fetch_students():
    try:
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        
        query = "SELECT id, name, contact_number, join_date, course, resume FROM students"
        cursor.execute(query)
        
        students = cursor.fetchall()
        
        if not students:
            st.write("No student records found.")
        else:
            st.write("Student Details:")
            for student in students:
                student_id, name, contact_number, join_date, course, resume_base64 = student
                
                # Decode the Base64 resume data
                resume_data = base64.b64decode(resume_base64)
                
                st.write(f"ID: {student_id}")
                st.write(f"Name: {name}")
                st.write(f"Contact Number: {contact_number}")
                st.write(f"Join Date: {join_date}")
                st.write(f"Course: {course}")
                
                # Add a download button for the resume
                st.download_button(
                    label="Download Resume",
                    data=resume_data,
                    file_name=f"{name}_resume.pdf",
                    mime="application/octet-stream"
                )
                
                st.write("---")
        
    except Exception as e:
        st.write(f"An error occurred: {e}")
        
    finally:
        cursor.close()
        connection.close()

# Streamlit UI
def main():
    st.title("Fetch Student Data")
    
    # Call the function to fetch and display students
    fetch_students()

if __name__ == "__main__":
    main()
