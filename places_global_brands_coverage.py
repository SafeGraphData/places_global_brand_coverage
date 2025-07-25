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
# Keep-alive comment: 2025-05-12 12:23:58.122811
# Keep-alive comment: 2025-05-12 23:23:31.144761
# Keep-alive comment: 2025-05-13 10:24:32.215062
# Keep-alive comment: 2025-05-13 21:23:32.162225
# Keep-alive comment: 2025-05-14 08:23:59.930514
# Keep-alive comment: 2025-05-14 19:23:57.285127
# Keep-alive comment: 2025-05-15 06:23:58.853447
# Keep-alive comment: 2025-05-15 17:24:28.491073
# Keep-alive comment: 2025-05-16 04:23:43.774482
# Keep-alive comment: 2025-05-16 15:22:46.727825
# Keep-alive comment: 2025-05-17 02:23:04.928198
# Keep-alive comment: 2025-05-17 13:23:48.261657
# Keep-alive comment: 2025-05-18 00:23:03.123509
# Keep-alive comment: 2025-05-18 11:23:31.395071
# Keep-alive comment: 2025-05-18 22:23:28.845371
# Keep-alive comment: 2025-05-19 20:23:04.157549
# Keep-alive comment: 2025-05-20 07:23:20.391178
# Keep-alive comment: 2025-05-20 18:24:32.431178
# Keep-alive comment: 2025-05-21 05:23:04.028779
# Keep-alive comment: 2025-05-21 16:23:13.412472
# Keep-alive comment: 2025-05-22 03:23:07.717065
# Keep-alive comment: 2025-05-22 14:23:11.856066
# Keep-alive comment: 2025-05-23 01:23:10.397305
# Keep-alive comment: 2025-05-23 12:23:10.117506
# Keep-alive comment: 2025-05-23 23:23:13.897347
# Keep-alive comment: 2025-05-24 10:23:11.544420
# Keep-alive comment: 2025-05-24 21:23:08.359946
# Keep-alive comment: 2025-05-25 08:23:09.075927
# Keep-alive comment: 2025-05-25 19:23:14.038249
# Keep-alive comment: 2025-05-26 06:22:59.215270
# Keep-alive comment: 2025-05-26 17:23:03.509520
# Keep-alive comment: 2025-05-27 04:23:09.221857
# Keep-alive comment: 2025-05-27 15:23:13.802310
# Keep-alive comment: 2025-05-28 02:23:23.484987
# Keep-alive comment: 2025-05-28 13:23:14.215075
# Keep-alive comment: 2025-05-29 00:23:07.060199
# Keep-alive comment: 2025-05-29 11:23:02.346440
# Keep-alive comment: 2025-05-29 22:23:16.713965
# Keep-alive comment: 2025-05-30 09:23:01.956536
# Keep-alive comment: 2025-05-30 20:23:02.837920
# Keep-alive comment: 2025-05-31 07:23:14.844939
# Keep-alive comment: 2025-05-31 18:23:09.281695
# Keep-alive comment: 2025-06-01 05:23:09.103034
# Keep-alive comment: 2025-06-01 16:23:21.506161
# Keep-alive comment: 2025-06-02 03:23:22.985549
# Keep-alive comment: 2025-06-02 14:23:14.213618
# Keep-alive comment: 2025-06-03 01:23:04.224915
# Keep-alive comment: 2025-06-03 12:23:19.099826
# Keep-alive comment: 2025-06-03 23:23:15.077237
# Keep-alive comment: 2025-06-04 10:23:14.155368
# Keep-alive comment: 2025-06-04 21:22:53.136995
# Keep-alive comment: 2025-06-05 08:23:16.381062
# Keep-alive comment: 2025-06-05 19:23:06.636259
# Keep-alive comment: 2025-06-06 06:23:04.120443
# Keep-alive comment: 2025-06-06 17:22:47.381049
# Keep-alive comment: 2025-06-07 04:22:49.134026
# Keep-alive comment: 2025-06-07 15:22:58.313817
# Keep-alive comment: 2025-06-08 02:23:03.407320
# Keep-alive comment: 2025-06-08 13:23:05.145448
# Keep-alive comment: 2025-06-09 00:22:47.515950
# Keep-alive comment: 2025-06-09 11:23:02.442587
# Keep-alive comment: 2025-06-09 22:23:11.124743
# Keep-alive comment: 2025-06-10 09:23:14.377439
# Keep-alive comment: 2025-06-10 20:23:07.023773
# Keep-alive comment: 2025-06-11 07:23:08.068829
# Keep-alive comment: 2025-06-11 18:24:56.988449
# Keep-alive comment: 2025-06-12 05:23:05.276726
# Keep-alive comment: 2025-06-12 16:23:08.730302
# Keep-alive comment: 2025-06-13 03:23:09.671255
# Keep-alive comment: 2025-06-13 14:22:59.046502
# Keep-alive comment: 2025-06-14 01:23:19.049858
# Keep-alive comment: 2025-06-14 12:23:05.682224
# Keep-alive comment: 2025-06-14 23:22:57.044563
# Keep-alive comment: 2025-06-15 10:22:43.972562
# Keep-alive comment: 2025-06-15 21:23:17.607727
# Keep-alive comment: 2025-06-16 08:23:14.837598
# Keep-alive comment: 2025-06-16 19:22:58.732494
# Keep-alive comment: 2025-06-17 06:23:35.513403
# Keep-alive comment: 2025-06-17 17:23:03.582491
# Keep-alive comment: 2025-06-18 04:23:09.534224
# Keep-alive comment: 2025-06-18 15:23:09.656073
# Keep-alive comment: 2025-06-19 02:23:07.252295
# Keep-alive comment: 2025-06-19 13:23:07.310723
# Keep-alive comment: 2025-06-20 00:23:03.662389
# Keep-alive comment: 2025-06-20 11:23:52.991972
# Keep-alive comment: 2025-06-20 22:23:12.464586
# Keep-alive comment: 2025-06-21 09:22:57.668981
# Keep-alive comment: 2025-06-21 20:23:09.838534
# Keep-alive comment: 2025-06-22 07:23:02.658853
# Keep-alive comment: 2025-06-22 18:22:53.675609
# Keep-alive comment: 2025-06-23 05:23:09.824767
# Keep-alive comment: 2025-06-23 16:23:03.387316
# Keep-alive comment: 2025-06-24 03:23:09.803591
# Keep-alive comment: 2025-06-24 14:22:49.671958
# Keep-alive comment: 2025-06-25 01:22:43.332256
# Keep-alive comment: 2025-06-25 12:23:05.768594
# Keep-alive comment: 2025-06-25 23:23:07.882043
# Keep-alive comment: 2025-06-26 10:23:15.486790
# Keep-alive comment: 2025-06-26 21:24:40.083743
# Keep-alive comment: 2025-06-27 08:23:08.597045
# Keep-alive comment: 2025-06-27 19:23:05.224802
# Keep-alive comment: 2025-06-28 06:23:12.003663
# Keep-alive comment: 2025-06-28 17:23:02.159163
# Keep-alive comment: 2025-06-29 04:22:51.687511
# Keep-alive comment: 2025-06-29 15:22:41.679315
# Keep-alive comment: 2025-06-30 02:23:03.102840
# Keep-alive comment: 2025-06-30 13:22:45.631890
# Keep-alive comment: 2025-07-01 00:24:49.442064
# Keep-alive comment: 2025-07-01 11:23:05.313221
# Keep-alive comment: 2025-07-01 22:23:09.011072
# Keep-alive comment: 2025-07-02 09:23:03.054340
# Keep-alive comment: 2025-07-02 20:24:52.342854
# Keep-alive comment: 2025-07-03 07:23:17.713378
# Keep-alive comment: 2025-07-03 18:22:43.923398
# Keep-alive comment: 2025-07-04 05:23:06.180819
# Keep-alive comment: 2025-07-04 16:23:02.202457
# Keep-alive comment: 2025-07-05 03:23:01.295175
# Keep-alive comment: 2025-07-05 14:23:06.105966
# Keep-alive comment: 2025-07-06 01:23:04.275013
# Keep-alive comment: 2025-07-06 12:23:00.664747
# Keep-alive comment: 2025-07-06 23:23:02.335280
# Keep-alive comment: 2025-07-07 10:23:03.210845
# Keep-alive comment: 2025-07-07 21:23:02.192502
# Keep-alive comment: 2025-07-08 08:23:06.626329
# Keep-alive comment: 2025-07-08 19:23:02.777399
# Keep-alive comment: 2025-07-09 06:23:13.300764
# Keep-alive comment: 2025-07-09 17:23:46.749622
# Keep-alive comment: 2025-07-10 04:23:01.780299
# Keep-alive comment: 2025-07-10 15:23:08.121386
# Keep-alive comment: 2025-07-11 02:23:00.957282
# Keep-alive comment: 2025-07-11 13:23:01.913070
# Keep-alive comment: 2025-07-12 00:22:47.753718
# Keep-alive comment: 2025-07-12 11:23:05.801174
# Keep-alive comment: 2025-07-12 22:23:01.930920
# Keep-alive comment: 2025-07-13 09:23:01.629827
# Keep-alive comment: 2025-07-13 20:22:46.447521
# Keep-alive comment: 2025-07-14 07:22:59.612751
# Keep-alive comment: 2025-07-14 18:23:22.632751
# Keep-alive comment: 2025-07-15 05:23:12.799045
# Keep-alive comment: 2025-07-15 16:23:07.289356
# Keep-alive comment: 2025-07-16 03:23:06.488921
# Keep-alive comment: 2025-07-16 14:23:07.956517
# Keep-alive comment: 2025-07-17 01:23:01.953929
# Keep-alive comment: 2025-07-17 12:23:08.681542
# Keep-alive comment: 2025-07-17 23:22:59.968702
# Keep-alive comment: 2025-07-18 10:23:22.302327
# Keep-alive comment: 2025-07-18 21:23:01.787064
# Keep-alive comment: 2025-07-19 08:23:41.866627
# Keep-alive comment: 2025-07-19 19:22:46.768722
# Keep-alive comment: 2025-07-20 06:23:11.073721
# Keep-alive comment: 2025-07-20 17:23:17.308069
# Keep-alive comment: 2025-07-21 04:23:12.147936
# Keep-alive comment: 2025-07-21 15:22:59.199827
# Keep-alive comment: 2025-07-22 02:23:21.394637
# Keep-alive comment: 2025-07-22 13:23:35.273022
# Keep-alive comment: 2025-07-23 00:23:08.407308
# Keep-alive comment: 2025-07-23 11:22:58.636821
# Keep-alive comment: 2025-07-23 22:23:01.152009
# Keep-alive comment: 2025-07-24 09:23:18.154962
# Keep-alive comment: 2025-07-24 20:23:03.446411
# Keep-alive comment: 2025-07-25 07:22:58.381380
# Keep-alive comment: 2025-07-25 18:23:03.500241
# Keep-alive comment: 2025-07-26 05:22:56.796161
# Keep-alive comment: 2025-07-26 16:23:01.731084