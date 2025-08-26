# introduction
"""
- This is 1 page portfolio website for Freelancing
"""

# libraries
import streamlit as st
import json
from streamlit_lottie import st_lottie


# page configuration
st.set_page_config(
    page_icon="🎓",
    page_title="Portfolio | Divit Chandel",
    initial_sidebar_state="expanded",
    layout="centered"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
    )
local_css("style/styles.css")

# sidebar section
with st.sidebar:
    st.logo("assets/images/small.png", size="large")


    with st.container(
            horizontal=True,
            horizontal_alignment="center"
        ):
        st.markdown(
            f"""
            <h1 style="text-align: center;">
            Welcome to <span style="color: #A78BFA; font-weight: bold;">My Dev. Portfolio </span>Website 🙏
            </h1>
            """, unsafe_allow_html=True
        )
        with st.container(vertical_alignment="center", height=500, horizontal_alignment="center", border=False):
            st.subheader("Please review My Website 🙏", width="content")
            selected = st.feedback("stars")
            if selected is not None:
                if selected > 3:
                    st.success("Thank you, Please rate our app on other platforms too")
                else:
                    st.warning("Rate our app something good otherwise you know you're being tracked of your location, "
                               "so yeah")
            st.write("`ℹ️ This rating system uses my self made .py Automation to nofify me on my discord1`")

# hero section
with st.container(key="hero_section"):
    lcol1, rcol2 = st.columns(2)
    with lcol1:
        st.subheader("👋 Hello")
        st.markdown("""<h2>I'm <span style="color: #A78BFA; font-weight: bold;">Divit Chandel</span> !</h2>""",
                    unsafe_allow_html=True)
        st.write("**SaaS Dev** & **Freelancer** Specializes in `AI API LLMS`, `AI Automations` w/ `python+n8n` inside "
                     "beautifil`streamlit` frontend. In my SaaSes (private) and Freelance projects.")
    with st.container(
        horizontal=True,
        horizontal_alignment="distribute",
        ):
        SOCIAL_MEDIA = {
            "YouTube": ["https://youtube.com/", ":material/youtube_activity:"],
            "LinkedIn": ["https://linkedin.com", ":material/info:"],
            "GitHub": ["https://github.com/divit-chandel/", ":material/folder_code:"],
            "X (Twitter)": ["https://x.com/casuallywater", ":material/close:"],
        }
        for index, (platform, (url, icon)) in enumerate(SOCIAL_MEDIA.items()):
            st.link_button(
                label=platform,
                url=url,
                icon=icon,
                use_container_width=True
            )

    @st.cache_resource
    def load_lottie_file(filepath: str):
        """

        :rtype: Any
        """
        with open(filepath, "r") as f:
            return json.load(f)

    with rcol2:
        # clean animation goes here
        st_lottie(
            load_lottie_file(
                "assets/animations/9th_lottie_anime.json"
            ),
            quality="high",
            key="faq_animation",
            height=250
        )

st.title(" ")

with st.container(key="text_areas"):
    tab1, tab2, tab3 = st.tabs(["💼 Skills & Talent", "🚀 Projects & Accomplishments", "✨ My Techstack"])

    with tab1:
        with st.container(border=True):
            choice1 = st.radio(
                "Select a section:",
                ["⚡️ What I Do", "🚧 Hard Skills", "🧸 Soft Skills"],
                horizontal=True
            )

            if choice1 == "⚡️ What I Do":
                st.write('\n')
                st.write("**⚡️ What I Do**")
                st.markdown(
                    """
                    - ✔️ I develop everything from backend logic to slick frontend all from python.  
                    - ✔️ I create Smart, data-driven applications with AI/ML API Integrations.  
                    - ✔️ I create dashboards to complete JS rivaling apps having so skill gaps.  
                    - ✔️ I do freelancing on many platforms and create my own Indie saas.  
                    """
                )

            elif choice1 == "🚧 Hard Skills":
                st.write('\n')
                st.write("**Hard Skills 🚧**")
                st.write(
                    """
                    - 👩‍💻 Programming: Python (OpenAI, Streamlit, etc.), CSS3, SQL  
                    - 🛩️ API Keys: OpenAI, OpenRouter, Langchain, n8n Integration  
                    - 📚 Modeling: Logistic regression, linear regression, decision trees  
                    - 🗄️ Databases: Supabase, MySQL, Notion  
                    """
                )

            elif choice1 == "🧸 Soft Skills":
                st.write('\n')
                st.write("**Soft Skills 🧸**")
                st.write(
                    """
                    - ⚡ Fast Learner: Quickly picks up new tools, frameworks, and concepts  
                    - ⏱️ Time Efficient: Gets things done fast without compromising quality  
                    - 🔍 Resourceful: Figures things out through hands-on exploration and experimentation  
                    - ❤️ Passionate: Deeply invested in work, bringing energy and care to every project  
                    """
                )

    with tab2:
        with st.container(border=True):
            PROJECTS = [
                "🏆 Complete Finance App with AI so you're always best at financial management",
                "🏆 AI learning & Quiz App from YouTube Videos transcription",
                "🏆 AI based nutritional app with camera as input so you're healthy",
                "🏆 AI based productivity app with all the features you need to be productive",
                "🏆 AI desk assistance AI voice LLM which works in your terminal",
            ]

            st.write('\n')
            st.subheader("🎓 Projects & Accomplishments")
            for project in PROJECTS:
                st.button(project, type="tertiary")

            st.warning(
                "Note: These are projects which I'm boutta monetize as \"SaaS\" "
                "so I can't link them or show a screenshot of them. "
                "You'll eventually find them when they're released.",
                icon="⚠️"
            )

    with tab3:
        with st.container(border=True):
            choice = st.radio(
                "Select an area:",
                ["Freelancing", "SaaS Dev"],
                horizontal=True
            )

            if choice == "Freelancing":
                st.markdown("""
                    ### 🚀 Freelancing
                    - **Core Skills:** Python for building AI-powered automations  
                    - **Integrations:** n8n to connect apps and services  
                    - **Delivery:** Fully-packaged solutions in Streamlit web apps  
                    - **Focus:** Making processes faster, smarter, and hands-off  
                    """)

            elif choice == "SaaS Dev":
                st.markdown("""
                    ### 👑 SaaS Development
                    - **Frontend:** Streamlit + Shadcn UI + custom elements  
                    - **Backend:** Python with AI integrations via **OpenRouter**, **OpenAI API**, and various models  
                    - **Database:** Supabase  
                    - **Integrations:** Google Auth, Stripe, PayPal  
                    - **Extra touch:** n8n for certain workflows  
                    - **Approach:** AI-first, built for performance, and designed to scale  
                    """)

st.header(" ")

# LLM for fyne shyt
with st.container(key="Real_LLM"):
    lcol2, rcol2 = st.columns(2)
    with lcol2:
        # clean animation goes here
        st_lottie(
            load_lottie_file(
                "assets/animations/7th_lottie_anime.json"
            ),
            quality="high",
            key="ai_animation",
            height=250
        )
        st.write("So, This is my personal assistant, ask him bout anything he cool. He's a near perfect idencal AI to "
                 "me. So yeah, you're talking to me!. You can see how I make my LLMs. Agents and Automations are kept "
                 "in here too. 😉")
        st.write(" ")
        st.write("👑 The AI API LLMs and Automation agents are my passion and I'm really experianced in makin em in my "
                 "SaaS apps.")
    with rcol2:
        ai_box = st.container(height=475)
        with ai_box:
            st.chat_message("assistant").write("**Hey! I'm Divit's personal assistant, You can talk to me instead of "
                                               "readin' portfolio!**")
        if prompt := st.chat_input():
            with ai_box:
                st.chat_message("user").write(prompt)
                st.chat_message("assistant").write(f"I'm really sorry, The API Costs is keeping me away to talk "
                                                   f"It'll be fixed sooner then you'd expect. You can contact me via "
                                                   f"the login form below 😔")

st.header(" ")

with st.container(key="contact"):
    lcol3, rcol3 = st.columns(2)
    with lcol3:
        st.markdown(
            f"""
            <form action="https://formsubmit.co/n6941401@gmail.com" method="POST">
                 <input type="hidden" name="_captcha" value="false">
                 <input type="text" name="name" placeholder="Your name" required>
                 <input type="email" name="email" placeholder="Your email" required>
                 <input type="text" name="_subject" placeholder="subject" required>
                 <textarea name="message" placeholder="Your message here"></textarea required>
                 <button type="submit">Submit Form</button>
            </form>
            """, unsafe_allow_html=True
        )
    with rcol3:
        st.success("`This mail system works with python automation, again I made with Formsubmit API and tell "
                 "me who messaged me using tihs app.`", icon="ℹ️")

        # clean animation goes here
        st_lottie(
            load_lottie_file(
                "assets/animations/5th_lottie_anime.json"
            ),
            quality="high",
            key="ask me",
            height=250
        )

