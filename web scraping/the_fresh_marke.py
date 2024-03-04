import requests
import pandas as pd

cookie = "osano_consentmanager_uuid=5e929f12-6acb-4a47-948f-b285d4a07718; osano_consentmanager=nhlRWC5VU21N6PPCCNiQnFSnQTX6mE46mug_pl7qD9MqnLTJv0dUre9ABeTxqgDyhpbzUKOy-PtZ6rlkHV_jegFIKZrtEqpk3jARyLgk2TOxs3TVzLd_VmlHj4-XTrwUz-6GW1v9G6vZFLH9xEG38N_JYJDIr5jfUCCOY_ahkuLLezg0tPr4IpAvqxl5QU-bZDUX7kd_qIwIAEejtRvJB4sWhCIHhi_mroZU0XQs_qFdYmeFxrvsclN8TpJj7LES4V_YxDhuSEnv1Als17PYvERFo_2ap6L040IQTQ==; _gcl_au=1.1.1269454524.1706692881; fw_se={%22value%22:%22fws2.7c2a8f7c-7d43-40c1-97cf-850318df2990.1.1706692881159%22%2C%22createTime%22:%222024-01-31T09:21:21.159Z%22}; _gid=GA1.2.336423086.1706692882; _fbp=fb.1.1706692882578.1649999801; _pin_unauth=dWlkPU9HVmxPR000T1dFdE1XSmhPQzAwWlRFMExXSTVOemd0WW1VNFl6UTFZMk0xWm1VMQ; _uetsid=19569dc0c01a11ee9aea3d666a32bd8d; _uetvid=19573f90c01a11eeac847b3e93947304; fw_chid={%22value%22:%22N7A4N3b%22%2C%22createTime%22:%222024-01-31T09:22:04.335Z%22}; _ga_EMDXDP2N4W=GS1.2.1706692882.1.1.1706692926.16.0.0; __cf_bm=8dn.TkHMo.qN741Ipqgf9KWY2paFU_yFDuV5SqopDMA-1706692927-1-AdNhZx4Ou+EgqvyGhy4TjNDkOO28bIQ8yvSwSvTsdi/heG3E8RudHODCN+ASlZ/mNH4JoBheqIGhnRH392e0hZg=; _gat=1; ajs_anonymous_id=31eefc9a-e571-4017-98f8-dd336353c56a; __stripe_mid=4bb9cbf2-29ad-476d-8b77-f6145492714cdd801b; __stripe_sid=fd8ef4b7-60b9-40b1-92e7-742ae8c13e41286ccc; session-prd-tfm=.eJxNyctygjAAQNF_ydo6hhod2PmMYSSILzQbBjCUBAMMwWrS6b_XZRd3c-4PSIqO6xJ4RXrXfACSlncqrXndA6_vHm_RXGvR1EnfVLwGHuDGLzOci1D45GQJpMJ3h2-EuXM272zu3L-zu9uyBZkQGYyC41xdnchujzMTxkFP8V5SMxqzZSm3Ma0YZorJm6KYisAQTeqzZRe_SONIhPJkqM0htSu0Xfglw7DN_n-FYIafmqj1I3MQymIX5oZMbhsfssNTpPF6RGTzonbmUFmZ8EhQEQ0vHztejeevmqZdtG42-93rCyewvSoTIow-g2I3PsfL1QkFYAAemneJuAEPOdMpmkL39w9ZS2h1.GJui_A.PvPq1v3VFKEchuj4AOxyFM6-YCg; fw_utm={%22value%22:%22{}%22%2C%22createTime%22:%222024-01-31T09:23:08.351Z%22}; fw_uid={%22value%22:%22353d241f-e478-4dd0-ba81-c510c97ebda5%22%2C%22createTime%22:%222024-01-31T09:23:08.370Z%22}; _gat_UA-000000000-1=1; _dd_s=rum=0&expire=1706693888825; _ga=GA1.1.573062806.1706692882; _ga_2NZ40CS25B=GS1.1.1706692882.1.1.1706692989.16.0.0"

HEADERS = {

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie    

}

# seachinput = input("enter the items to search :")

df_jaz_mart=pd.read_excel("jazil_mart.xlsx",sheet_name="Sheet1")

for i in range(0,len(df_jaz_mart)):
    searchinput=df_jaz_mart.loc[i]['name']


URL =f"https://shop.thefreshmarket.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=60&offset=0&page=1&prophetScorer=frequency&sort=rank&allow_autocorrect=true&search_is_autocomplete=false&search_provider=ic&search_term={searchinput}&secondary_results=true&unified_search_shadow_test_enabled=false"

#URL ="https://shop.thefreshmarket.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=5&offset=0&page=1&prophetScorer=frequency&sort=rank&allow_autocorrect=true&search_is_autocomplete=false&search_provider=ic&search_term=apple&secondary_results=true&unified_search_shadow_test_enabled=false"


responses = requests.get(URL,headers=HEADERS)
data = responses.json()

items = data['items']

df_items = pd.DataFrame(items)
df_clean = df_items[['name','base_price','display_uom','average_weight']]

# df_clean.to_csv("items.csv",index=False)
# df_clean.to_json("items.json",index=False)
# df_clean.to_html("items.html",index=False)
# df_clean.to_excel("items.xlsx",index=False)

# for i in range(61):
#     print(f"name :{data['items'][i]['name']}, price ${data['items'][i]['base_price']}")

df_clean.to_excel("tfm.xlsx",index=False)
