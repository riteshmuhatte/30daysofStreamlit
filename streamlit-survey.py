import streamlit_survey as ss
import streamlit as st

survey = ss.StreamlitSurvey()
st.header("Experimenting Survey Using Streamlit")
survey.text_input("Name:", id="Q1")
st.write("Have you watched the Day to Day Productivity video ??")
watched = survey.radio("watched_st", options=["NA", "Yes", "No"], horizontal=True,label_visibility="collapsed", id="Q2")

if watched == "Yes":
 st.write("Congratulations on the progress!!!")
 st.write("What do you think about the topics that were discussed?")
 survey.select_slider(
    "Scale:", options=["Super Boring", "Boring", "Meh!!", "Good", "Awesome"],
    label_visibility="collapsed", id="Q3"
 )
elif watched == "No":
 st.write("Now is the time...Watch it!!")
 st.write("Are you going to ever watch it ??")
 guilty = survey.radio("guilty", options=["NA", "Yes", "No"], horizontal=True, label_visibility="collapsed", id="Q4")

 if guilty == "Yes":
  st.write("You are on the right Path!!")
 elif guilty == "No":
  st.write("Bhagwan apka bhala kare !")

json = survey.to_json()
#st.json(json)
