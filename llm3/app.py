import streamlit as st

# Define the pages
main_page = st.Page("main.py", title="Main Page", icon="🎈")
page_1 = st.Page("p1.py", title="Page 1", icon="🎈")
page_2 = st.Page("p2.py", title="Page 2", icon="🎈")
page_3 = st.Page("p3.py", title="Page 3", icon="🎈")
page_4 = st.Page("p4.py", title="Page 4", icon="🎈")
page_5 = st.Page("p5.py", title="Page 5", icon="🎈")
page_6 = st.Page("p6.py", title="Page 6", icon="🎈")
page_7 = st.Page("p7.py", title="Page 7", icon="❄️")
page_8 = st.Page("p8.py", title="Page 8", icon="❄️")
page_9 = st.Page("p9.py", title="Page 9", icon="❄️")
page_10 = st.Page("p10.py", title="Page 10", icon="❄️")
page_11 = st.Page("p11.py", title="Page 11", icon="❄️")
page_12 = st.Page("p12.py", title="Page 12", icon="❄️")
page_13 = st.Page("p13.py", title="Page 13", icon="❄️")
page_14 = st.Page("p14.py", title="Page 14", icon="❄️")



# Set up navigation
page = st.navigation([main_page, page_1, page_2, page_3,page_4,page_5, page_6,page_7,page_8,page_9,page_10,
                      page_11, page_12,page_13,page_14])

# Run the selected page
page.run()