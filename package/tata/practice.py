import streamlit as st 
import pandas as pd
##st.title("THis is file creates for only of practice and the all codes are need to be debugged and tested before they are going to be deployed")
##st.subheader("Student perforamnce dashboard")
st.set_page_config(page_title="Student Performance Dashboard", page_icon=":bar_chart:", layout="centered")
st.title("Student Performance Dashboard"    )
st.header("Enter Student Deatils")
name = st.text_input("Enter Student Name")
roll_no = st.text_input("Enter Roll Number")
m1 = st.number_input("Maths Marks",0,100)
beee = st.number_input("BEEE marks", 0,100)
vlsi = st.number_input("VLSI Marks",0,100)

st.snow()
st.write("Code is like humor. When you have to explain it,")
st.text("Code is like humor. When you have to explain it,")
st.page_config(page_title="LPA Predictor", page_icon=":computer:", layout="centered")



if "data" not in st.session_state:
    st.session_state.data = []

def calculte_grade(Percenatge):
    if Percenatge >= 75:
        return "A"
    elif Percenatge >= 60:
        return "B"
    elif Percenatge >= 45:
        return "c"
    else:
        return "FAIL"

if st.button("ADD Student"):
    total = m1 +beee+vlsi
    Percenatge = round((total/300)*100,2    )
    greade = calculte_grade(Percenatge)

    st.session_state.data.append({
        "Name": name,
        "Roll No" : roll_no,
        "Maths": m1,
        "BEEE": beee,
        "VLSI": vlsi,    
        "Total": total,
        "Percentage": Percenatge,
        "Grade": greade
    })
    st.success(f"Stduent {name} added successfully")
st.header("Stduend data")

if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df)

else :
    st.info("No student data available. Please add student details.")
st.warning("This is a practice application. Data will not be saved permanently.")
st.video("https://www.youtube.com/embed/dp2OYt_2O9E")
