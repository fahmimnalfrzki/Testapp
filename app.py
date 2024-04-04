import streamlit as st
import eda
import prediction

# st.sidebar.markdown("### AtaPP")
# st.sidebar.markdown(
#         """
#         <div style="text-align:center; margin-bottom: 30px;">
#             <img src="D:\Bootcamp\Phase 2\Final Project\AtaPP.png" alt="Logo" width="500">
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
page = st.sidebar.selectbox(label="Choose Menu", options=["HOME", "EDA", "PREDICTION"])

if page == 'HOME':
    st.image('Logo.png')
    st.write("### FINAL PROJECT")
    st.write("### FTDS-RMT-028")
    st.write("### Group 2")
    st.markdown("<hr/>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center'>Meet our Nakama</h2>", unsafe_allow_html=True)

    # Custom CSS for the LinkedIn buttons
    button_css = """
    <style>
    .linkedin-btn {
        display: inline-block;
        background: #005db5;
        color: #F26634;
        padding: 10px 15px;
        margin: 10px 0px;
        border-radius: 5px;
        text-decoration: none;
        font-size: 14px;
        text-align: center;
        vertical-align: middle;
    }
    </style>
    """
    def linkedin_button(profile_url, button_text="LinkedIn Profile"):
        return f'<a href="{profile_url}" target="_blank" class="linkedin-btn">{button_text}</a>'
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image('5.png')
        st.markdown(linkedin_button("https://www.linkedin.com/in/kelvin-rizky-novsa-situmorang-00552820a/"), unsafe_allow_html=True)
    
    with col2:
        st.image('2.png')
        st.markdown(linkedin_button("https://www.linkedin.com/in/mhafizjuliant/"), unsafe_allow_html=True)
    
    with col3:
        st.image('3.png')
        st.markdown(linkedin_button("https://www.linkedin.com/in/nailinafarah/"), unsafe_allow_html=True)
    
    with col4:
        st.image('4.png')
        st.markdown(linkedin_button("https://www.linkedin.com/in/rian-girianom/"), unsafe_allow_html=True)

elif page == "EDA":
    eda.run()
else:
    prediction.run()
    