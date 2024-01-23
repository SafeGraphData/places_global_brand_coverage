import streamlit as st
from read_data import read_from_gsheets
import altair as alt
from datetime import datetime, timedelta
import pandas as pd
import streamlit.components.v1 as components



st.set_page_config(
    page_title="Places Summary Statistics - Global Brand Coverage",
    layout="wide"
)
#### Global Brand Coverage #### 
top_1000_brands_df = (
    read_from_gsheets("Top 1000 brands")
    [["primary_brand", "naics_code", "safegraph_category", "country_code_list", "country_name_list"]]
    .sort_values("primary_brand", ascending=True)
    .reset_index(drop=True)
    .rename(columns={"primary_brand": "Brand name", "naics_code": "NAICS Code", "safegraph_category": "SafeGraph Category", "country_code_list": "Country Code", "country_name_list": "Country Name List"})
    #.style.apply(lambda x: ['background-color: #D7E8ED' if i % 2 == 0 else '' for i in range(len(x))], axis=0)
)

top_1000_brands_df =  top_1000_brands_df[[x.isnumeric() for x in top_1000_brands_df['NAICS Code']]].reset_index()

top_1000_brands_styled = (
    top_1000_brands_df
    .style.apply(lambda x: ['background-color: #D7E8ED' if i % 2 == 0 else '' for i in range(len(x))], axis=0)
)

brands_by_country_df = (
    read_from_gsheets("Countries")
    .assign(**{"Distinct brands": lambda df: df["Distinct brands"].astype(int)})
    [["iso_country_code", "country", "Distinct brands"]]
    .sort_values("Distinct brands", ascending=False)
    .rename(columns={"iso_country_code": "Country Code", "country": "Country Name"})
    [["Country Name", "Country Code", "Distinct brands"]]
    .reset_index(drop=True)
)

brands_by_country_df_styled = (
    brands_by_country_df.style
    .apply(lambda x: ['background-color: #D7E8ED' if i%2==0 else '' for i in range(len(x))], axis=0)
    .format({"Distinct brands": "{:,.0f}"})
)

brand_tab1, brand_tab2 = st.tabs(["Top 1,000 Brands", "Brand Count By Country"])

with brand_tab1:
    st.dataframe(top_1000_brands_styled, use_container_width=True)

with brand_tab2:
    st.dataframe(brands_by_country_df_styled, use_container_width=True)


hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
