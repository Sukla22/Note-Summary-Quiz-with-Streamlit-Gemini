import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_generator
from PIL import Image

st.title("Generate Your Note Summary and Quiz")
st.markdown("Upload upto 3 images to generate Note Summary and Quiz")
st.divider()

#Images
with st.sidebar:
    st.header("Controls")

    images = st.file_uploader(
        "Upload the photoes of your note",
        type = ["jpg","png","jpeg"],
        accept_multiple_files = True
    )
    pil_image = []
    for img in images:
        pil_img = Image.open(img)
        pil_image.append(pil_img)

    if images:
        if len(images) > 3:
            st.error("You can upload maximum 3 images")
        else:
            st.subheader("Your Uploaded Images")
            col = st.columns(len(images))

            
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)

#Difficulty Level

    selected_option = st.selectbox("Enter the difficulty level",
                               ("Easy","Medium","Hard"),
                               index = None)

    pressed = st.button("Generate Note Summary and Quiz", type = "secondary")
#Error handling
if pressed:
    if not images:
        st.error("You must upload at least 1 image")
    if not selected_option:
        st.error("You must select a difficulty level")

    if images and selected_option:
        #Note
        with st.container(border=True):
            st.subheader("Note Summary")
            with st.spinner("Your note is generating..."):
                generated_notes = note_generator(pil_image)
                st.markdown(generated_notes)

        #Audio Transcription
        with st.container(border=True):
            st.subheader("Audio Transcription")

            with st.spinner("Your audio is generating..."):
             
             #clearing markdown 
             generated_notes = generated_notes.replace("#","")
             generated_notes = generated_notes.replace("*","")
             generated_notes = generated_notes.replace("-","")
             generated_notes = generated_notes.replace("`","")
             generated_notes = generated_notes.replace("+","")
             generated_notes = generated_notes.replace("_","")
             audio_transcript = audio_transcription(generated_notes)
             st.audio(audio_transcript)

        #Quiz Generation
        with st.container(border=True):
            st.subheader(f"Generated Quizzes({selected_option})") 
            with st.spinner("Your quizzes is generating..."):
                quizzes = quiz_generator(pil_image, selected_option)
                st.text(quizzes)