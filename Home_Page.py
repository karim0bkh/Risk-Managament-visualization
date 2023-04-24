import streamlit as st
import pandas as pd

###################################
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode

###################################

from functionforDownloadButtons import download_button

###################################

st.set_page_config(
    page_title="Risk Management",
    page_icon="📈",
    )
st.image("img.jpg", use_column_width=True , width=100)
st.title("Risk Management")
st.sidebar.title("Risk Management Project 📈 Designed by: \n @Karim Ben Khaled")

###################################initial risk###################################
st.subheader("Initial Risk -File Upload-")
c29, c30, c31 = st.columns([1, 6, 1])

with c30:

    uploaded_file = st.file_uploader(
        "",
        key="1",
        help="To activate 'wide mode', go to the hamburger menu > Settings > turn on 'wide mode'",
    )

    if uploaded_file is not None:
        st.session_state["uploaded_file"] = uploaded_file
        file_container = st.expander("Check your uploaded .csv")
        shows = pd.read_csv(uploaded_file)
        uploaded_file.seek(0)
        file_container.write(shows)
    elif "uploaded_file" in st.session_state:
        uploaded_file = st.session_state["uploaded_file"]
        file_container = st.expander("Check your uploaded .csv")
        shows = pd.read_csv(uploaded_file)
        uploaded_file.seek(0)
        file_container.write(shows)

    else:
        st.info(
            f"""
                👆 Upload a .csv file first. Sample to try: [Risk.csv](https://docs.google.com/spreadsheets/d/e/2PACX-1vSkEHC2_-EU93iL5T7q54tIA2fc4d3FIfC4xryA0MmedE_4BXxABM3-xVZ8yDNZK9YxpRANwAVYxngG/pub?output=xlsx)
                """
        )

        st.stop()

from st_aggrid import GridUpdateMode, DataReturnMode

gb = GridOptionsBuilder.from_dataframe(shows)
# enables pivoting on all columns, however i'd need to change ag grid to allow export of pivoted/grouped data, however it select/filters groups
gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
gb.configure_selection(selection_mode="multiple", use_checkbox=True)
gb.configure_side_bar()  # side_bar is clearly a typo :) should by sidebar
gridOptions = gb.build()

st.success(
    f"""
        💡 Tip! Hold the shift key when selecting rows to select multiple rows at once!
        """
)

response = AgGrid(
    shows,
    gridOptions=gridOptions,
    enable_enterprise_modules=True,
    update_mode=GridUpdateMode.MODEL_CHANGED,
    data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
    fit_columns_on_grid_load=False,
)

df = pd.DataFrame(response["selected_rows"])

st.subheader("Filtered data will appear below 👇 ")
st.text("")

st.table(df)

st.text("")

c29, c30, c31 = st.columns([1, 1, 2])

with c29:

    CSVButton = download_button(
        df,
        "File.csv",
        "Download to CSV",
    )

with c30:
    CSVButton = download_button(
        df,
        "File.txt",
        "Download to TXT",
    )

###################################mitigation risk###################################
st.subheader("Mitigation Risk -File Upload-")

c29, c30, c31 = st.columns([1, 6, 1])

with c30:

    uploaded_file1 = st.file_uploader(
        "",
        key="2",
        help="To activate 'wide mode', go to the hamburger menu > Settings > turn on 'wide mode'",
    )

    if uploaded_file1 is not None:
        st.session_state["uploaded_file1"] = uploaded_file1
        file_container = st.expander("Check your uploaded .csv")
        shows = pd.read_csv(uploaded_file1)
        uploaded_file1.seek(0)
        file_container.write(shows)
    elif "uploaded_file1" in st.session_state:
        uploaded_file = st.session_state["uploaded_file1"]
        file_container = st.expander("Check your uploaded .csv")
        shows = pd.read_csv(uploaded_file)
        uploaded_file.seek(0)
        file_container.write(shows)

    else:
        st.info(
            f"""
                👆 Upload a .csv file first. Sample to try: [Risk.csv](https://docs.google.com/spreadsheets/d/e/2PACX-1vSkEHC2_-EU93iL5T7q54tIA2fc4d3FIfC4xryA0MmedE_4BXxABM3-xVZ8yDNZK9YxpRANwAVYxngG/pub?output=xlsx)
                """
        )

        st.stop()

from st_aggrid import GridUpdateMode, DataReturnMode

gb = GridOptionsBuilder.from_dataframe(shows)
# enables pivoting on all columns, however i'd need to change ag grid to allow export of pivoted/grouped data, however it select/filters groups
gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
gb.configure_selection(selection_mode="multiple", use_checkbox=True)
gb.configure_side_bar()  # side_bar is clearly a typo :) should by sidebar
gridOptions = gb.build()

st.success(
    f"""
        💡 Tip! Hold the shift key when selecting rows to select multiple rows at once!
        """
)

response = AgGrid(
    shows,
    key="3",
    gridOptions=gridOptions,
    enable_enterprise_modules=True,
    update_mode=GridUpdateMode.MODEL_CHANGED,
    data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
    fit_columns_on_grid_load=False,
)

df = pd.DataFrame(response["selected_rows"])

st.subheader("Filtered data will appear below 👇 ")
st.text("")

st.table(df)

st.text("")

c29, c30, c31 = st.columns([1, 1, 2])

with c29:

    CSVButton = download_button(
        df,
        "File.csv",
        "Download to CSV",
    )

with c30:
    CSVButton = download_button(
        df,
        "File.txt",
        "Download to TXT",
    )
