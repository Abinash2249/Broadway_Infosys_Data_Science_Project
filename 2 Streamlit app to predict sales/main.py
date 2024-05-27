import pickle
import streamlit as st

with open("lr_model.pickle", "rb") as file:
    lr_model = pickle.load(file)

st.title("Sales prediction APP")

tv = st.text_input("Enter TV advertising expenditure: ")

if st.button("Submit"):
    try: 
        y_pred = lr_model.predict([[float(tv)]])
        st.write(f"The expected sales is: {y_pred[0]}")
    except:
        st.error("Please enter a valid number for TV advertising expenditure.")
 