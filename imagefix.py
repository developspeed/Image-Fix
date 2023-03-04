import streamlit as st
import replicate
import os

st.set_page_config(
    page_title="Image Process",
    # page_icon=im,
    layout="wide",
)
st.write("Click on > to Login")
hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}
.css-14xtw13 e8zbici0{
    visibility:hidden;
}
.css-j7qwjs e1fqkh3o7{
    visibility:hidden;
}
footer{
    visibility:hidden;
}
</style>
"""
 
st.markdown(hide_menu , unsafe_allow_html=True)


######################### Frontend UI of the Application #########################

# App Title Name
st.title("Image Processing")

key = st.sidebar.text_input("Enter the Security Key")
if key == 'image':
    st.sidebar.success("Welcome")
    # Initializing the database

    # Uploading image file
    image_file = st.file_uploader("Choose File")
    if image_file is not None:
        st.subheader("Input")
        st.image(image_file,width=500)

    ################## Backend Logic of the Application #####################


    # Setting the Environment of the application using the API token of Replicate from the database
    os.environ['REPLICATE_API_TOKEN'] = '62e15e6986072b8ec7ac3baa00efe8d9dd48872f'
    models = st.selectbox("Which Model you want to use",["Artistic","Stable"])
    st.markdown("Which model to use: Artistic has more vibrant color but may leave important parts of the image gray.Stable is better for nature scenery and is less prone to leaving gray human parts")
            
    render_factor = st.text_input("Render Factor",value="35")
    st.markdown("The default value of 35 has been carefully chosen and should work -ok- for most scenarios (but probably won't be the -best-). This determines resolution at which the color portion of the image is rendered. Lower resolution will render faster, and colors also tend to look more vibrant. Older and lower quality images in particular will generally benefit by lowering the render factor. Higher render factors are often better for higher quality images, but the colors may get slightly washed out.")

    if st.button("Submit"):
        if image_file is not None:
            
            st.warning("Working...")
            model = replicate.models.get("arielreplicate/deoldify_image")
            version = model.versions.get("0da600fab0c45a66211339f1c16b71345d22f26ef5fea3dca1bb90bb5711e950")

            # https://replicate.com/arielreplicate/deoldify_image/versions/0da600fab0c45a66211339f1c16b71345d22f26ef5fea3dca1bb90bb5711e950#input
            inputs = {
                # Path to an image
                'input_image': image_file,

                
                'model_name': models,

                
                'render_factor': int(render_factor),
            }

            try:
                # https://replicate.com/arielreplicate/deoldify_image/versions/0da600fab0c45a66211339f1c16b71345d22f26ef5fea3dca1bb90bb5711e950#output-schema
                output = version.predict(**inputs)

                # Showing the Output Image
                st.subheader("Output")
                st.image(output,width=500)
                st.write("Click on the below link to download the image")
                st.write(output)
                st.success("Done!")
            except Exception:
                st.error("There could be some error with API or Image.")

elif key == "":
    st.sidebar.warning("Enter the Secret Key")

else:
    st.sidebar.error("Incorrect Secret Key")
