import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-pro")

with st.sidebar:
    st.title("Rhymeweaver")
    st.write("Invoking the magic of poetry, this name alludes to the application's ability to craft intricate rhymes that dance off the page.")
    st.write('With an intuitive user interface and a user-friendly design, this web application invites users to embark on a creative odyssey. By simply providing a few details about the individual, such as their name, interests, and passions, the application harnesses the transformative power of Gemini Pro to generate a personalized poem. Whether it"s a heartfelt tribute to a loved one, a celebration of personal achievements, or a reflective exploration of lifes complexities, the application adapts to the users preferences, producing poems that resonate with authenticity and emotional depth.')

# Call the model and print the response.
st.title("Rhymeweaver")
aoi = ["Reading","Exercising","Listening to music","Watching movies","Playing video games","Traveling","Cooking","Gardening","Photography","Art and crafts","DIY projects","Learning new skills",
    "Meditation","Spending time with friends and family","Volunteering","Technology","Science",
    "History","Politics","Economics","Philosophy","Psychology","Sociology","Art","Music","Literature","Film","Fashion","Travel","Food and drink","Health and wellness","Sports","Current events"]

col1, col2, col3 = st.columns(3)
with col1:
    name = st.text_input('Name')
    age = st.text_input('Age')
    interest = st.multiselect('Area of interest',options=aoi)
    others = st.text_input('Other interest (if any)',placeholder='separated by comma')
with col2:
    state = st.text_input('State ')
    country = st.text_input('Country ')
    profession = st.text_input('Kaam kya karte ho')
    fav_show_movie = st.text_input('Favourite Show and movies',placeholder='separated by comma')
with col3:
    fav_songs = st.text_input('Favourite songs/singers/genres',placeholder='separated by comma')
    gender = st.selectbox('Gender',options=['Male','Female'])
    language = st.selectbox('Poem ka language',['English','Hindi'])

contents = 'A person whose name is '+name+'. Gender is '+gender+'. Age is '+age+'. Area of interest are '+",".join(interest)
contents += '. Lives in state of '+state+' located in country '+country+'.'
contents += 'Profession is '+profession+'. Favourite show and movies are '+fav_show_movie+'. And Favourite songs/singers/genres are '+fav_songs+'.'
contents += 'Write a high quality rhyming poem about 100 lines describing the person which will be a masterpiece when read by a user . Language of the poem would be'+language+'.'

a = st.button('Generate')
if a:
    with st.spinner('Wait for it'):
        gemini = genai.GenerativeModel(model_name=model)
        response = gemini.generate_content(contents,stream=False)
        st.text_area(label ="",value=response.text,height=500)
    st.success('Done')
