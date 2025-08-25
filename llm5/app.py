import streamlit as st

# Define the pages
main_page = st.Page("main.py", title="Main Page", icon="🎈")
page_1 = st.Page("p1.py", title="Page 1", icon="🎈")
page_2 = st.Page("p2.py", title="Page 2", icon="🎈")




# Set up navigation
page = st.navigation([main_page, page_1, page_2])

# Run the selected page
page.run()