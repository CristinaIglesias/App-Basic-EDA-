import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

from streamlit_lottie import st_lottie
import requests
import json


def load_lottiefile(filepath: str):
    with open(filepath, "r")as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottiefile("bigdata.json")
lottie_Big_data = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_qp1q7mct.json")

st_lottie (
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    renderer="svg",
    height=None,
    width=None,
    key=None
)


with st.sidebar.header("Upload your input CSV file"):
    uploaded_file = st.sidebar.file_uploader(
        "Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""[Example CSV input file](https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/automotive_data.csv)
""")

st.header("**EDA Streamlit Python App**")

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header("**Input Dataframe**")
    st.write(df)
    st.write("---")
    st.header("**Pandas Profiling Report**")
    st_profile_report(pr)
else:
    st.info("Awaiting for CSV file to be uploaded.")
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
