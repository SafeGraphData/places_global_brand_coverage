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
# Keep-alive comment: 2025-07-27 03:22:57.115930
# Keep-alive comment: 2025-07-27 14:22:47.183568
# Keep-alive comment: 2025-07-28 01:23:08.770750
# Keep-alive comment: 2025-07-28 12:23:04.209267
# Keep-alive comment: 2025-07-28 23:23:02.080906
# Keep-alive comment: 2025-07-29 10:22:37.795123
# Keep-alive comment: 2025-07-29 21:23:07.855529
# Keep-alive comment: 2025-07-30 08:23:04.117256
# Keep-alive comment: 2025-07-30 19:23:12.877656
# Keep-alive comment: 2025-07-31 06:23:17.321118
# Keep-alive comment: 2025-07-31 17:23:03.114516
# Keep-alive comment: 2025-08-01 04:23:00.818940
# Keep-alive comment: 2025-08-01 15:23:12.794997
# Keep-alive comment: 2025-08-02 02:22:56.267795
# Keep-alive comment: 2025-08-02 13:23:07.208273
# Keep-alive comment: 2025-08-03 00:23:02.551525
# Keep-alive comment: 2025-08-03 11:23:07.782968
# Keep-alive comment: 2025-08-03 22:23:02.487852
# Keep-alive comment: 2025-08-04 09:22:59.842564
# Keep-alive comment: 2025-08-04 20:23:04.924457
# Keep-alive comment: 2025-08-05 07:23:07.463621
# Keep-alive comment: 2025-08-05 18:23:08.697987
# Keep-alive comment: 2025-08-06 05:23:02.283380
# Keep-alive comment: 2025-08-06 16:24:53.607004
# Keep-alive comment: 2025-08-07 03:23:06.576722
# Keep-alive comment: 2025-08-07 14:23:09.117966
# Keep-alive comment: 2025-08-08 01:22:57.274357
# Keep-alive comment: 2025-08-08 12:23:08.686701
# Keep-alive comment: 2025-08-08 23:23:08.800012
# Keep-alive comment: 2025-08-09 10:23:02.106425
# Keep-alive comment: 2025-08-09 21:23:24.332837
# Keep-alive comment: 2025-08-10 08:23:08.186193
# Keep-alive comment: 2025-08-10 19:23:08.042685
# Keep-alive comment: 2025-08-11 06:23:02.700967
# Keep-alive comment: 2025-08-11 17:23:08.942738
# Keep-alive comment: 2025-08-12 04:23:08.792824
# Keep-alive comment: 2025-08-12 15:23:00.768442
# Keep-alive comment: 2025-08-13 02:23:08.347178
# Keep-alive comment: 2025-08-13 13:23:06.132422
# Keep-alive comment: 2025-08-14 00:23:01.476240
# Keep-alive comment: 2025-08-14 11:23:09.915999
# Keep-alive comment: 2025-08-14 22:23:02.956086
# Keep-alive comment: 2025-08-15 09:23:02.618364
# Keep-alive comment: 2025-08-15 20:22:52.249432
# Keep-alive comment: 2025-08-16 07:23:16.588370
# Keep-alive comment: 2025-08-16 18:23:03.259962
# Keep-alive comment: 2025-08-17 05:23:06.134957
# Keep-alive comment: 2025-08-17 16:23:01.368538
# Keep-alive comment: 2025-08-18 03:23:03.341574
# Keep-alive comment: 2025-08-18 14:23:04.723565
# Keep-alive comment: 2025-08-19 01:23:03.043367
# Keep-alive comment: 2025-08-19 12:23:09.434340
# Keep-alive comment: 2025-08-19 23:23:30.216904
# Keep-alive comment: 2025-08-20 10:23:05.538066
# Keep-alive comment: 2025-08-20 21:23:08.126693
# Keep-alive comment: 2025-08-21 08:23:04.870764
# Keep-alive comment: 2025-08-21 19:23:09.639258
# Keep-alive comment: 2025-08-22 06:23:08.305099
# Keep-alive comment: 2025-08-22 17:23:03.510295
# Keep-alive comment: 2025-08-23 04:23:12.262705
# Keep-alive comment: 2025-08-23 15:23:01.673863
# Keep-alive comment: 2025-08-24 02:23:01.495081
# Keep-alive comment: 2025-08-24 13:23:02.671749
# Keep-alive comment: 2025-08-25 00:23:08.925237
# Keep-alive comment: 2025-08-25 11:23:08.564474
# Keep-alive comment: 2025-08-25 22:23:03.260568
# Keep-alive comment: 2025-08-26 09:23:04.867286
# Keep-alive comment: 2025-08-26 20:23:08.849117
# Keep-alive comment: 2025-08-27 07:23:13.527431
# Keep-alive comment: 2025-08-27 18:22:43.269728
# Keep-alive comment: 2025-08-28 05:23:13.848299
# Keep-alive comment: 2025-08-28 16:23:03.698727
# Keep-alive comment: 2025-08-29 03:22:47.113678
# Keep-alive comment: 2025-08-29 14:22:54.528486
# Keep-alive comment: 2025-08-30 01:22:52.225059
# Keep-alive comment: 2025-08-30 12:22:47.865114
# Keep-alive comment: 2025-08-30 23:22:51.401063
# Keep-alive comment: 2025-08-31 10:22:47.463848
# Keep-alive comment: 2025-08-31 21:22:58.915745
# Keep-alive comment: 2025-09-01 08:23:02.663065
# Keep-alive comment: 2025-09-01 19:22:58.990744
# Keep-alive comment: 2025-09-02 06:22:48.486788
# Keep-alive comment: 2025-09-02 17:22:59.552824
# Keep-alive comment: 2025-09-03 04:22:51.579395
# Keep-alive comment: 2025-09-03 15:22:55.004890
# Keep-alive comment: 2025-09-04 02:22:56.423023
# Keep-alive comment: 2025-09-04 13:23:07.306209
# Keep-alive comment: 2025-09-05 00:22:47.720444
# Keep-alive comment: 2025-09-05 11:22:43.942334
# Keep-alive comment: 2025-09-05 22:22:52.815393
# Keep-alive comment: 2025-09-06 09:22:48.346172
# Keep-alive comment: 2025-09-06 20:22:47.779415
# Keep-alive comment: 2025-09-07 07:22:53.065593
# Keep-alive comment: 2025-09-07 18:22:52.957322
# Keep-alive comment: 2025-09-08 05:22:49.120869
# Keep-alive comment: 2025-09-08 16:22:55.846506
# Keep-alive comment: 2025-09-09 03:23:19.730410
# Keep-alive comment: 2025-09-09 14:22:55.587567
# Keep-alive comment: 2025-09-10 01:22:47.030441
# Keep-alive comment: 2025-09-10 12:23:00.000057
# Keep-alive comment: 2025-09-10 23:22:48.097491
# Keep-alive comment: 2025-09-11 10:22:51.100845
# Keep-alive comment: 2025-09-11 21:22:48.110049
# Keep-alive comment: 2025-09-12 08:23:03.632669
# Keep-alive comment: 2025-09-12 19:22:53.884604
# Keep-alive comment: 2025-09-13 06:22:41.315365
# Keep-alive comment: 2025-09-13 17:22:47.826569
# Keep-alive comment: 2025-09-14 04:22:38.019527
# Keep-alive comment: 2025-09-14 15:22:49.519613
# Keep-alive comment: 2025-09-15 02:22:47.259232
# Keep-alive comment: 2025-09-15 13:22:50.479978
# Keep-alive comment: 2025-09-16 00:22:48.297628
# Keep-alive comment: 2025-09-16 11:22:53.837078
# Keep-alive comment: 2025-09-16 22:22:47.653288
# Keep-alive comment: 2025-09-17 09:22:50.715023
# Keep-alive comment: 2025-09-17 20:22:59.977408
# Keep-alive comment: 2025-09-18 07:22:55.388133
# Keep-alive comment: 2025-09-18 18:22:55.184809
# Keep-alive comment: 2025-09-19 05:22:49.314408
# Keep-alive comment: 2025-09-19 16:23:24.456342
# Keep-alive comment: 2025-09-20 03:22:52.726213
# Keep-alive comment: 2025-09-20 14:22:54.449141
# Keep-alive comment: 2025-09-21 01:22:53.892729
# Keep-alive comment: 2025-09-21 12:22:54.278032
# Keep-alive comment: 2025-09-21 23:22:49.078891
# Keep-alive comment: 2025-09-22 10:22:52.295958
# Keep-alive comment: 2025-09-22 21:22:48.607670
# Keep-alive comment: 2025-09-23 08:22:51.267182
# Keep-alive comment: 2025-09-23 19:22:56.779502
# Keep-alive comment: 2025-09-24 06:22:49.358178
# Keep-alive comment: 2025-09-24 17:22:55.845884
# Keep-alive comment: 2025-09-25 04:25:06.620411
# Keep-alive comment: 2025-09-25 15:23:00.088391
# Keep-alive comment: 2025-09-26 02:22:55.014091
# Keep-alive comment: 2025-09-26 13:22:59.164129
# Keep-alive comment: 2025-09-26 19:31:26.454168
# Keep-alive comment: 2025-09-27 05:31:30.871656
# Keep-alive comment: 2025-09-27 15:31:26.046230
# Keep-alive comment: 2025-09-28 01:31:29.995866
# Keep-alive comment: 2025-09-28 11:31:31.396564
# Keep-alive comment: 2025-09-28 21:31:30.831555
# Keep-alive comment: 2025-09-29 07:31:37.442883
# Keep-alive comment: 2025-09-29 17:31:46.645988
# Keep-alive comment: 2025-09-30 03:31:25.270674
# Keep-alive comment: 2025-09-30 13:31:32.658462
# Keep-alive comment: 2025-09-30 23:31:50.088958
# Keep-alive comment: 2025-10-01 09:31:58.721755
# Keep-alive comment: 2025-10-01 19:31:31.639752
# Keep-alive comment: 2025-10-02 05:31:59.120461
# Keep-alive comment: 2025-10-02 15:31:57.454214
# Keep-alive comment: 2025-10-03 01:31:30.191518
# Keep-alive comment: 2025-10-03 11:31:51.416795
# Keep-alive comment: 2025-10-03 21:31:26.088777
# Keep-alive comment: 2025-10-04 07:31:25.250422
# Keep-alive comment: 2025-10-04 17:31:35.968062
# Keep-alive comment: 2025-10-05 03:31:29.730723
# Keep-alive comment: 2025-10-05 13:31:34.644185
# Keep-alive comment: 2025-10-05 23:31:55.626376
# Keep-alive comment: 2025-10-06 09:32:01.540299
# Keep-alive comment: 2025-10-06 19:31:35.174866
# Keep-alive comment: 2025-10-07 05:31:32.813157
# Keep-alive comment: 2025-10-07 15:31:54.812655
# Keep-alive comment: 2025-10-08 01:31:30.736970
# Keep-alive comment: 2025-10-08 11:31:32.750002
# Keep-alive comment: 2025-10-08 21:31:31.854756
# Keep-alive comment: 2025-10-09 07:31:35.092851
# Keep-alive comment: 2025-10-09 17:31:34.993601
# Keep-alive comment: 2025-10-10 03:31:21.196008
# Keep-alive comment: 2025-10-10 13:31:13.692290
# Keep-alive comment: 2025-10-10 23:31:25.803433
# Keep-alive comment: 2025-10-11 09:31:31.233496
# Keep-alive comment: 2025-10-11 19:31:25.033253
# Keep-alive comment: 2025-10-12 05:31:28.358458
# Keep-alive comment: 2025-10-12 15:31:34.157173
# Keep-alive comment: 2025-10-13 01:31:27.451076
# Keep-alive comment: 2025-10-13 11:31:59.349457
# Keep-alive comment: 2025-10-13 21:31:21.776886
# Keep-alive comment: 2025-10-14 07:31:26.221055
# Keep-alive comment: 2025-10-14 17:31:29.183232
# Keep-alive comment: 2025-10-15 03:31:26.092478
# Keep-alive comment: 2025-10-15 13:31:29.395353
# Keep-alive comment: 2025-10-15 23:31:32.153440
# Keep-alive comment: 2025-10-16 09:31:28.740444
# Keep-alive comment: 2025-10-16 19:31:34.650099
# Keep-alive comment: 2025-10-17 05:31:32.691453
# Keep-alive comment: 2025-10-17 15:31:49.697589
# Keep-alive comment: 2025-10-18 01:31:27.018871
# Keep-alive comment: 2025-10-18 11:31:51.619044
# Keep-alive comment: 2025-10-18 21:32:01.078816
# Keep-alive comment: 2025-10-19 07:31:20.838775
# Keep-alive comment: 2025-10-19 17:31:56.136429
# Keep-alive comment: 2025-10-20 03:31:54.772718
# Keep-alive comment: 2025-10-20 13:31:34.264345
# Keep-alive comment: 2025-10-20 23:31:27.124011
# Keep-alive comment: 2025-10-21 09:31:33.413315
# Keep-alive comment: 2025-10-21 19:33:34.956869
# Keep-alive comment: 2025-10-22 05:31:28.235603
# Keep-alive comment: 2025-10-22 15:32:34.241357
# Keep-alive comment: 2025-10-23 01:31:28.421632
# Keep-alive comment: 2025-10-23 11:31:40.081979
# Keep-alive comment: 2025-10-23 21:31:29.453653
# Keep-alive comment: 2025-10-24 07:32:48.806636
# Keep-alive comment: 2025-10-24 17:31:38.533949
# Keep-alive comment: 2025-10-25 03:31:31.520249
# Keep-alive comment: 2025-10-25 13:31:55.101438
# Keep-alive comment: 2025-10-25 23:31:27.708834
# Keep-alive comment: 2025-10-26 09:31:20.766448
# Keep-alive comment: 2025-10-26 19:31:58.006552
# Keep-alive comment: 2025-10-27 05:31:37.997357
# Keep-alive comment: 2025-10-27 15:31:54.866210
# Keep-alive comment: 2025-10-28 01:31:30.796061
# Keep-alive comment: 2025-10-28 11:31:33.575063
# Keep-alive comment: 2025-10-28 21:31:21.756807
# Keep-alive comment: 2025-10-29 07:31:28.418624
# Keep-alive comment: 2025-10-29 17:31:37.900321
# Keep-alive comment: 2025-10-30 03:31:27.971165
# Keep-alive comment: 2025-10-30 13:31:59.920960
# Keep-alive comment: 2025-10-30 23:31:33.087520
# Keep-alive comment: 2025-10-31 09:32:47.804051
# Keep-alive comment: 2025-10-31 19:31:22.860527
# Keep-alive comment: 2025-11-01 05:31:31.527129
# Keep-alive comment: 2025-11-01 15:31:20.132640
# Keep-alive comment: 2025-11-02 01:31:32.301040
# Keep-alive comment: 2025-11-02 11:31:33.330286
# Keep-alive comment: 2025-11-02 21:31:47.387020
# Keep-alive comment: 2025-11-03 07:31:29.088411
# Keep-alive comment: 2025-11-03 17:31:34.837977
# Keep-alive comment: 2025-11-04 03:31:32.440790
# Keep-alive comment: 2025-11-04 13:32:00.796278
# Keep-alive comment: 2025-11-04 23:31:52.364132
# Keep-alive comment: 2025-11-05 09:32:04.295559
# Keep-alive comment: 2025-11-05 19:31:32.999679
# Keep-alive comment: 2025-11-06 05:32:02.628882
# Keep-alive comment: 2025-11-06 15:31:46.528961
# Keep-alive comment: 2025-11-07 01:31:30.531953
# Keep-alive comment: 2025-11-07 11:31:36.567315
# Keep-alive comment: 2025-11-07 21:31:34.530631
# Keep-alive comment: 2025-11-08 07:31:21.476414
# Keep-alive comment: 2025-11-08 17:31:37.050444
# Keep-alive comment: 2025-11-09 03:32:11.271648
# Keep-alive comment: 2025-11-09 13:31:32.926906
# Keep-alive comment: 2025-11-09 23:31:22.759534
# Keep-alive comment: 2025-11-10 09:31:29.900134
# Keep-alive comment: 2025-11-10 19:31:45.018095
# Keep-alive comment: 2025-11-11 05:31:29.397057
# Keep-alive comment: 2025-11-11 15:31:28.252078
# Keep-alive comment: 2025-11-12 01:31:34.587719
# Keep-alive comment: 2025-11-12 11:31:38.104384
# Keep-alive comment: 2025-11-12 21:31:54.826333
# Keep-alive comment: 2025-11-13 07:31:18.334919
# Keep-alive comment: 2025-11-13 17:31:29.563543
# Keep-alive comment: 2025-11-14 03:31:35.616392
# Keep-alive comment: 2025-11-14 13:31:56.566071
# Keep-alive comment: 2025-11-14 23:31:28.095343
# Keep-alive comment: 2025-11-15 09:31:31.307474
# Keep-alive comment: 2025-11-15 19:31:36.838832
# Keep-alive comment: 2025-11-16 05:31:28.661115
# Keep-alive comment: 2025-11-16 15:31:32.972866
# Keep-alive comment: 2025-11-17 01:31:23.199438
# Keep-alive comment: 2025-11-17 11:31:56.476059
# Keep-alive comment: 2025-11-17 21:31:25.518363
# Keep-alive comment: 2025-11-18 07:31:27.993377
# Keep-alive comment: 2025-11-18 17:31:28.900877
# Keep-alive comment: 2025-11-19 03:31:31.366180
# Keep-alive comment: 2025-11-19 13:31:24.678582
# Keep-alive comment: 2025-11-19 23:31:25.922179
# Keep-alive comment: 2025-11-20 09:31:33.816412
# Keep-alive comment: 2025-11-20 19:33:23.172166
# Keep-alive comment: 2025-11-21 05:31:28.741613
# Keep-alive comment: 2025-11-21 15:31:34.253391
# Keep-alive comment: 2025-11-22 01:31:37.114834
# Keep-alive comment: 2025-11-22 11:31:21.930146
# Keep-alive comment: 2025-11-22 21:31:33.245818
# Keep-alive comment: 2025-11-23 07:31:33.993398
# Keep-alive comment: 2025-11-23 17:31:36.877610
# Keep-alive comment: 2025-11-24 03:31:27.440763
# Keep-alive comment: 2025-11-24 13:31:25.041802
# Keep-alive comment: 2025-11-24 23:31:34.770726
# Keep-alive comment: 2025-11-25 09:31:56.486926