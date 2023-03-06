import streamlit as st
from deta import Deta

st.set_page_config(
    page_title="Admin | Deoldify",
    # page_icon=im,
    layout="wide",
)

hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}
.css-14xtw13 e8zbici0{
    visibility:hidden;
}
footer{
    visibility:hidden;
}
</style>
"""

st.markdown(hide_menu, unsafe_allow_html=True)

######################### Frontend UI of the Application #########################

# App Title Name
st.title("Image Deoldify Parameters")

################## Backend Logic of the Application #####################

#  !Database Key !Important
# a0vvxqkjjrd_UEZCetnYYiHbrAEFyCjeXjSKUbCbQp4W

deta = Deta('a0fah3x7pzr_7sQZMjTVUoamdmKjzdFq6XMwxT395f7E')
db = deta.Base('image-deoldify')

def getItem():
    return db.fetch().items


st.sidebar.title("Login")
username = st.sidebar.text_input("Enter the Username")
password = st.sidebar.text_input("Enter the Password")

submit = st.sidebar.button("Login")

dataBase = getItem()
if username == dataBase[2]['username'] and password == dataBase[2]['password']:
    st.sidebar.success("Login Success")

    with st.form("my_form"):
        
        st.write("Change the text")
        english = st.text_input("Enter the content in English",value=dataBase[0]["english"])
        dutch = st.text_input("Enter the content in Dutch",value=dataBase[0]["dutch"])
        french = st.text_input("Enter the content in French",value=dataBase[0]["french"])
        german = st.text_input("Enter the content in German",value=dataBase[0]["german"])
        spanish = st.text_input("Enter the content in Spanish",value=dataBase[0]["spanish"])
        
        # Admin Panel Parameters
        secretKey = st.text_input("Enter the Secret Key",value=dataBase[1]['secretKey'])
        username = st.text_input("Enter the Username",value=dataBase[2]["username"])
        password = st.text_input("Enter the Password",value=dataBase[2]['password'])
        apiKey = st.text_input("Enter the New API Key",value=dataBase[3]['apiKey'])

        submitted = st.form_submit_button("Submit")
        # submitted = st.button("Submit")
        if submitted:
            # changing the password for admin
            db.put({
                'key':'tadmin',
                'username':username,
                'password':password
            })

            #changing language content
            db.put({
                "key":"language",
                "english":english,
                "spanish":spanish,
                "german":german,
                "dutch":dutch,
                "french":french
            })

            # for changing the secret key
            db.put({
                "key":"secret",
                "secretKey":secretKey
            })

            # For changing the API key
            db.put({
                "key": "zkey",
                "apiKey": apiKey
            })
            
            st.success("Values are Set for User Model")

elif username == '' and password == '':
    st.sidebar.warning("Enter the Username and Password")

else:
    st.sidebar.error("Inncorrect Login Details")