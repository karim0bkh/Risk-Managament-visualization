import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Risk Management",
    page_icon="📈",
    )

st.title('Initial Risk')
st.sidebar.title("Risk Management Project 📈 Designed by: @Karim Ben Khaled")

if "uploaded_file" in st.session_state:
    uploaded_file = st.session_state["uploaded_file"]
    file_container = st.expander("Check your uploaded .csv")
    shows = pd.read_csv(uploaded_file)
    uploaded_file.seek(0)
    file_container.write(shows)

    # generate the six different charts
    st.subheader("Chart 1: Histogram")
    fig6 = px.histogram(shows, x='Risques', y='Note' )
    st.plotly_chart(fig6, use_container_width=True)

    st.subheader("Chart 2: Stacked Bar chart")
    fig2 = px.bar(shows, x='Probabilite', y='Note', color='Risques', barmode='stack')
    st.plotly_chart(fig2, use_container_width=True)

    # Display the next two charts in the same row
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Chart 3: Line plot")
        fig3 = px.line(shows, x='Risques', y='Note')
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        st.subheader("Chart 4: Area plot")
        fig4 = px.area(shows, x='Risques', y='Note')
        st.plotly_chart(fig4, use_container_width=True)

    # Display the last two charts in separate rows
    st.subheader("Chart 5: Scatter plot")
    fig1 = px.scatter(shows, x='Risques', y='Note')
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Chart 6: Box plot")
    fig5 = px.box(shows, x='Risques', y='Note')
    st.plotly_chart(fig5, use_container_width=True)



else:
    st.info("Upload a .csv file in the initial risk section to get started")
