import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import altair as alt




st.set_page_config(
    page_title="Risk Management",
    page_icon="📈",
)



# Add custom CSS for print view
st.markdown(
    """
    <style>
    @media print {
        .stPlotlyChart {
            height: 100% !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.title('Comparison')
st.sidebar.title("Risk Management Project 📈 Designed by: @Karim Ben Khaled")


# read initial risk data and select the first column
if "uploaded_file1" in st.session_state and "uploaded_file" in st.session_state:

    initial_risk = st.session_state["uploaded_file"]
    initial_risk1 = pd.read_csv(initial_risk)

    note1 = initial_risk1.iloc[:, -1]
    risques = initial_risk1.iloc[:, 0]

    # read mitigation data and select the last column
    mitigation = st.session_state["uploaded_file1"]
    mitigation1 = pd.read_csv(mitigation)

    note2 = mitigation1.iloc[:, -1]

    # create a new DataFrame by combining the two columns
    df = pd.concat([risques, note1, note2], axis=1)
    df.columns = ["Risques", "Note1", "Note2"]

    file_container = st.expander("Check your uploaded .csv")
    initial_risk.seek(0)
    file_container.write(initial_risk1)

    file_container1 = st.expander("Check your uploaded .csv")
    mitigation.seek(0)
    file_container1.write(mitigation1)


    st.title("Compare Intial Risk and Risk Mitigation")
    fig = go.Figure(data=[
    go.Bar(name='Initial Risk', x=df['Risques'], y=df['Note1']),
    go.Bar(name='Risk Mitigation',     x=df['Risques'], y=df['Note2'])])
    st.plotly_chart(fig)

    bar_chart = alt.Chart(df).mark_bar().encode(
        x='Note1',
        x2='Note2',
        y='Risques',

        color=alt.Color('Note1', legend=None),
        tooltip=['Risques', 'Note1', 'Note2']
    ).properties(
        title='Comparison of Initial Score and Mitigation Score for each Risk'
    ).interactive()

    st.altair_chart(bar_chart, use_container_width=True)

else:
    st.info(
        "Upload the .csv files to get started"
    )
