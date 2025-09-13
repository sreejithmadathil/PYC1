import streamlit as st
from streamlit_option_menu import option_menu

# Import your app pages (make sure these files exist)
import home, trending, account, your, about

st.set_page_config(
    page_title="Multi Page App",
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Menu ',
                options=['Home', 'Account', 'Trending', 'Your Posts', 'About'],
                icons=['house-fill', 'person-circle', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "3!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "15px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "2px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        # Call the relevant page function based on the selected menu item
        if app == "Home":
            home.app()
        elif app == "Account":
            account.app()
        elif app == "Trending":
            trending.app()
        elif app == "Your Posts":
            your.app()
        elif app == "About":
            about.app()
        elif app == "Buy_me_a_coffee":
            # You can handle the Buy me a coffee page here if needed
            st.write("Support me on Buy Me A Coffee!")

# Initialize and run the app
if __name__ == '__main__':
    app = MultiApp()
    app.run()
