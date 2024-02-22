import streamlit as st

st.header("Experimenting Survey Using Streamlit")
st.text_input("Name:")
st.write("Have you watched the Day to Day Productivity video ??")
watched = st.radio("watched_st", options=["NA", "Yes", "No"], horizontal=True,label_visibility="collapsed")

if watched == "Yes":
 st.write("Congratulations on the progress!!!")
 st.write("What do you think about the topics that were discussed?")
 st.select_slider(
    "Scale:", options=["Super Boring", "Boring", "Meh!!", "Good", "Awesome"],
    label_visibility="collapsed"
 )
elif watched == "No":
 st.write("Now is the time...Watch it!!")
 st.write("Are you going to ever watch it ??")
 guilty = st.radio("guilty", options=["NA", "Yes", "No"], horizontal=True, label_visibility="collapsed")

 if guilty == "Yes":
  st.write("You are on the right Path!!")
 elif guilty == "No":
  st.write("Bhagwan apka bhala kare !")

#json = st.to_json()
#st.json(json)
