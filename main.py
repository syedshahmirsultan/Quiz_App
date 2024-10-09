import streamlit as st

st.title("Shahmir Quiz App")
st.write("           ")

mcqs1:str = st.radio("What is the capital city of Australia?",["Sydney","Canberra","Brisbane","Melbourne"])
st.write("        ")
mcqs2:str = st.radio("What is the capital city of Brazil?",["São Paulo","Rio de Janeiro","Brasília","Salvador"])
st.write("           ")
mcqs3 :str = st.radio("What is the capital city of Pakistan?",["Islamabad","Karachi","Lahore","Multan"])
st.write('           ')
mcqs4:str = st.radio("What is the capital city of Japan?",["Osaka","Tokyo","Kyoto","Hiroshima"])
st.write("        ")
mcqs5:str = st.radio("What is the capital city of South Africa?",["Cape Town","Johannesburg","Durban","Pretoria"])

marks:int = 0

# This if logic is for mcqs1
if mcqs1:
    if mcqs1 == "Canberra":
        marks+=1
    else:
        pass
    
# This if logic is for mcqs2
if mcqs2:
    if mcqs2 == "Brasília":
        marks+= 1
    else:
        pass
 
# This if logic is for mcqs3 
if mcqs3:
    if mcqs3== "Islamabad":
        marks+=1
    else:
        pass
    
# This if logic is for mcqs4
if mcqs4:
    if mcqs4 == "Tokyo":
        marks+=1
    else:
        pass
    
# This if logic is for mcqs5
if mcqs5:
    if mcqs5 == "Pretoria":
        marks+=1
    else:
        pass
    
st.write("      ")
total :int = 5
result = (marks/total) *100
# User will click on this button to get Result
if (st.button("Result")):
    st.write(f" Result = {result} %")
    st.write("      ")
    if marks >= 3:
        st.success("Congratulations! You have passed the quiz")
    else:
        st.error("You have failed the quiz ! ")