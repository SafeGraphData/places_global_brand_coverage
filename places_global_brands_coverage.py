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

top_1000_brands_df =  top_1000_brands_df[[x.isnumeric() for x in top_1000_brands_df['NAICS Code']]].reset_index().drop("index", axis=1)


brands_by_country_df = (
    read_from_gsheets("Countries")
    .assign(**{"Distinct brands": lambda df: df["Distinct brands"].astype(int)})
    [["iso_country_code", "country", "Distinct brands"]]
    .sort_values("Distinct brands", ascending=False)
    .rename(columns={"iso_country_code": "Country Code", "country": "Country Name"})
    [["Country Name", "Country Code", "Distinct brands"]]
    .reset_index(drop=True)
)


country_list = st.selectbox("Country Name:", [""] + brands_by_country_df['Country Name'].tolist())

brand_tab1, brand_tab2 = st.tabs(["Top 1,000 Brands", "Brand Count By Country"])


with brand_tab1:
    if country_list:
        top_1000_brands_styled = (
            top_1000_brands_df[top_1000_brands_df['Country Name List'].str.contains(country_list)]
            .style.apply(lambda x: ['background-color: #D7E8ED' if i % 2 == 0 else '' for i in range(len(x))], axis=0)
        )

        st.dataframe(top_1000_brands_styled, use_container_width=True, hide_index=True)
    else:
        top_1000_brands_styled = (
            top_1000_brands_df
            .style.apply(lambda x: ['background-color: #D7E8ED' if i % 2 == 0 else '' for i in range(len(x))], axis=0)
        )
        st.dataframe(top_1000_brands_styled, use_container_width=True, hide_index=True)

with brand_tab2:
    if country_list:
        brands_by_country_df_styled = (
            brands_by_country_df[brands_by_country_df['Country Name'].str.contains(country_list)].style
            .apply(lambda x: ['background-color: #D7E8ED' if i%2==0 else '' for i in range(len(x))], axis=0)
            .format({"Distinct brands": "{:,.0f}"})
        )
    else:
         brands_by_country_df_styled = (
            brands_by_country_df.style
            .apply(lambda x: ['background-color: #D7E8ED' if i%2==0 else '' for i in range(len(x))], axis=0)
            .format({"Distinct brands": "{:,.0f}"})
        )

    st.dataframe(brands_by_country_df_styled, use_container_width=True, hide_index=True)



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

css = '''
<style>
section.main > div:has(~ footer ) {
    padding-top: 0px;
    padding-bottom: 0px;
}

[data-testid="ScrollToBottomContainer"] {
    overflow: hidden;
}
</style>
'''

st.markdown(css, unsafe_allow_html=True)

# Keep-alive comment: 2025-04-25 16:18:37.950591
# Keep-alive comment: 2025-04-26 00:24:12.828928
# Keep-alive comment: 2025-04-26 11:24:07.389392
# Keep-alive comment: 2025-04-26 22:23:06.519246
# Keep-alive comment: 2025-04-27 09:23:37.715242
# Keep-alive comment: 2025-04-27 20:23:32.639353
# Keep-alive comment: 2025-04-28 07:24:03.256985
# Keep-alive comment: 2025-04-28 18:24:23.076343
# Keep-alive comment: 2025-04-29 05:23:52.377801
# Keep-alive comment: 2025-04-29 16:24:37.142056
# Keep-alive comment: 2025-04-30 03:23:27.261153
# Keep-alive comment: 2025-04-30 14:23:55.838895
# Keep-alive comment: 2025-05-01 01:24:06.801721
# Keep-alive comment: 2025-05-01 12:23:38.247708
# Keep-alive comment: 2025-05-01 23:23:11.238856
# Keep-alive comment: 2025-05-02 10:23:57.267968
# Keep-alive comment: 2025-05-02 21:23:08.530627
# Keep-alive comment: 2025-05-03 08:23:33.033074
# Keep-alive comment: 2025-05-03 19:23:51.166219
# Keep-alive comment: 2025-05-04 06:23:56.827744
# Keep-alive comment: 2025-05-04 17:23:05.685570
# Keep-alive comment: 2025-05-05 04:24:16.558378
# Keep-alive comment: 2025-05-05 15:23:35.766989
# Keep-alive comment: 2025-05-06 02:24:26.639971
# Keep-alive comment: 2025-05-06 13:23:28.462725
# Keep-alive comment: 2025-05-07 00:23:27.183118
# Keep-alive comment: 2025-05-07 11:23:39.960005
# Keep-alive comment: 2025-05-07 22:23:38.284060
# Keep-alive comment: 2025-05-08 09:23:40.446156
# Keep-alive comment: 2025-05-08 20:23:39.361566
# Keep-alive comment: 2025-05-09 07:23:48.959223
# Keep-alive comment: 2025-05-09 18:24:01.340965
# Keep-alive comment: 2025-05-10 05:23:44.696459
# Keep-alive comment: 2025-05-10 16:23:30.185155
# Keep-alive comment: 2025-05-11 03:23:30.465755
# Keep-alive comment: 2025-05-11 14:23:22.175231
# Keep-alive comment: 2025-05-12 01:23:27.607162