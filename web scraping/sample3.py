import requests
import pandas as pd

competitor_list =[
        {
        'url':"https://shop.thefreshmarket.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=5&offset=0&page=1&prophetScorer=frequency&sort=rank&allow_autocorrect=true&search_is_autocomplete=false&search_provider=ic&search_term=",
        'cookie':"osano_consentmanager_uuid=5e929f12-6acb-4a47-948f-b285d4a07718; osano_consentmanager=nhlRWC5VU21N6PPCCNiQnFSnQTX6mE46mug_pl7qD9MqnLTJv0dUre9ABeTxqgDyhpbzUKOy-PtZ6rlkHV_jegFIKZrtEqpk3jARyLgk2TOxs3TVzLd_VmlHj4-XTrwUz-6GW1v9G6vZFLH9xEG38N_JYJDIr5jfUCCOY_ahkuLLezg0tPr4IpAvqxl5QU-bZDUX7kd_qIwIAEejtRvJB4sWhCIHhi_mroZU0XQs_qFdYmeFxrvsclN8TpJj7LES4V_YxDhuSEnv1Als17PYvERFo_2ap6L040IQTQ==; _gcl_au=1.1.1269454524.1706692881; fw_se={%22value%22:%22fws2.7c2a8f7c-7d43-40c1-97cf-850318df2990.1.1706692881159%22%2C%22createTime%22:%222024-01-31T09:21:21.159Z%22}; _gid=GA1.2.336423086.1706692882; _fbp=fb.1.1706692882578.1649999801; _pin_unauth=dWlkPU9HVmxPR000T1dFdE1XSmhPQzAwWlRFMExXSTVOemd0WW1VNFl6UTFZMk0xWm1VMQ; _uetsid=19569dc0c01a11ee9aea3d666a32bd8d; _uetvid=19573f90c01a11eeac847b3e93947304; fw_chid={%22value%22:%22N7A4N3b%22%2C%22createTime%22:%222024-01-31T09:22:04.335Z%22}; _ga_EMDXDP2N4W=GS1.2.1706692882.1.1.1706692926.16.0.0; __cf_bm=8dn.TkHMo.qN741Ipqgf9KWY2paFU_yFDuV5SqopDMA-1706692927-1-AdNhZx4Ou+EgqvyGhy4TjNDkOO28bIQ8yvSwSvTsdi/heG3E8RudHODCN+ASlZ/mNH4JoBheqIGhnRH392e0hZg=; _gat=1; ajs_anonymous_id=31eefc9a-e571-4017-98f8-dd336353c56a; __stripe_mid=4bb9cbf2-29ad-476d-8b77-f6145492714cdd801b; __stripe_sid=fd8ef4b7-60b9-40b1-92e7-742ae8c13e41286ccc; session-prd-tfm=.eJxNyctygjAAQNF_ydo6hhod2PmMYSSILzQbBjCUBAMMwWrS6b_XZRd3c-4PSIqO6xJ4RXrXfACSlncqrXndA6_vHm_RXGvR1EnfVLwGHuDGLzOci1D45GQJpMJ3h2-EuXM272zu3L-zu9uyBZkQGYyC41xdnchujzMTxkFP8V5SMxqzZSm3Ma0YZorJm6KYisAQTeqzZRe_SONIhPJkqM0htSu0Xfglw7DN_n-FYIafmqj1I3MQymIX5oZMbhsfssNTpPF6RGTzonbmUFmZ8EhQEQ0vHztejeevmqZdtG42-93rCyewvSoTIow-g2I3PsfL1QkFYAAemneJuAEPOdMpmkL39w9ZS2h1.GJui_A.PvPq1v3VFKEchuj4AOxyFM6-YCg; fw_utm={%22value%22:%22{}%22%2C%22createTime%22:%222024-01-31T09:23:08.351Z%22}; fw_uid={%22value%22:%22353d241f-e478-4dd0-ba81-c510c97ebda5%22%2C%22createTime%22:%222024-01-31T09:23:08.370Z%22}; _gat_UA-000000000-1=1; _dd_s=rum=0&expire=1706693888825; _ga=GA1.1.573062806.1706692882; _ga_2NZ40CS25B=GS1.1.1706692882.1.1.1706692989.16.0.0"
     },
    {
        'url':"https://shop.wegmans.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=60&offset=0&page=1&prophetScorer=frecency&sort=rank&allow_autocorrect=true&search_is_autocomplete=true&search_provider=ic&search_term=",
        'cookie':"__cf_bm=Z8bLvZQ6l.HJp3mYJfTiTtntyNRsh_991sRz1TPL_Y0-1707113802-1-AbtJD8hEiEL/Yg7xamTp8qrqdh5bv3nnNFNSjaMonVyDqbecOM/+5XJ+W+t8G+KFMFVZk6z6WVZxNfSHQTx/bRQ=; AMCVS_68B620B35350F1650A490D45%40AdobeOrg=1; kndctr_68B620B35350F1650A490D45_AdobeOrg_identity=CiY4MDUzNzA5NzIyNTA1MjU2NTQwMzYyNDU3OTk3MjEzODA3ODQ4MVIRCP7hpb_XMRgBKgRJTkQxMAPwAf7hpb_XMQ==; kndctr_68B620B35350F1650A490D45_AdobeOrg_cluster=ind1; _fbp=fb.1.1707113804398.1310641003; _pin_unauth=dWlkPU9HVmxPR000T1dFdE1XSmhPQzAwWlRFMExXSTVOemd0WW1VNFl6UTFZMk0xWm1VMQ; _gcl_au=1.1.762442444.1707113805; wfm.tracking.sessionStart=1707113804909; wfmStoreId=16; at_check=true; AMCV_68B620B35350F1650A490D45%40AdobeOrg=179643557%7CMCIDTS%7C19759%7CMCMID%7C80537097225052565403624579972138078481%7CMCAAMLH-1707718606%7C12%7CMCAAMB-1707718606%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1707121006s%7CNONE%7CMCSYNCSOP%7C411-19766%7CMCCIDH%7C0%7CvVersion%7C5.5.0; inRedirectGoldPanAudience=1; inRedirectYogurtAudience=1; ajs_anonymous_id=17424575-2cdc-4a00-9b44-6d6a94201f1b; wfm.tracking.s10=1; dotcomSearchId=c4d4458a-f275-45a7-8475-5ba98ffc443d; lux_uid=170711384700794657; wfm.tracking.x2p=1; sa-user-id=s%253A0-11fb6219-bcb6-5b55-6cce-2117a7964893.u417Suaqk0UIkJogLRkqE9rm1Zbg3oGH%252BZRzIQIrifo; sa-user-id-v2=s%253AEftiGby2W1VsziEXp5ZIkzEvxIg.1NH1fpuxpTQu%252B0sbglgKu8ECbY8nrOVrJHe%252Bw5PqSMQ; sa-user-id-v3=s%253AAQAKIDBXs133MqCZcxdQRnaQYcwgdDJ-VTbugywCLk-InUMSEAEYAyC4_PisBjABOgROQQ4MQgQ86QaL.H%252BhBC%252Bnn%252FV0tLyv9cZPBg2pVa5mwKZkFmH96PmS7A20; _pin_unauth=dWlkPU9HVmxPR000T1dFdE1XSmhPQzAwWlRFMExXSTVOemd0WW1VNFl6UTFZMk0xWm1VMQ; at_check=true; __stripe_mid=8b4e5716-8b8b-4012-8f31-fabb94c485bc2f9d85; __stripe_sid=e7a65e80-d640-44cc-966e-8d4c4fc2ac3573511c; ajs_anonymous_id=17424575-2cdc-4a00-9b44-6d6a94201f1b; s_gpv=Search%20Results:%20apple%20|%20Wegmans; session-prd-weg=.eJwdjstygjAARf8la8eBWGNlZ63aMCaMDwxhwyBESQRkCKhJp_9e2sXdnLs45xskl1boAniXtNRiBJJGtFVai7oDXtf2A9FCa3mvk-5-EzXwgDB-cd5kMpA-Di12qfTn4wG6GTyZYTaD5eNczpt4iRGuqCJwNaFs99oybrnFHd2sTHBwphxiuz2GhquPIlZrSRW35IA1rk82jvxLynYyUDuXfPLJ30fNU3K271I2_XdFsLxh1fQ5e-ntcoiq5r1g7iOPiAzqvclZqHFVFvnQQY7Zk9rVi9jrk0bOeB0HipsWrsNNs4DKOoHoeviOkD5bfiSz9CtGSRkX12gBRqDXok1kDry3qYNmCE1mP7_gv2sm.GKIPIQ.LcjVhrW5yRC3slMFqbho8rnLLQE; _uetsid=2301b1e0c3ee11ee9964cdc43e1a8073; _uetvid=23022dc0c3ee11ee838d136dcf19cf78; _dd_s=rum=0&expire=1707114790370; mbox=session#2812cd3fed6c4e62a240867eaaa99ada#1707115752|PC#2812cd3fed6c4e62a240867eaaa99ada.41_0#1770358666"
     },
    {
        'url':"https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=60&offset=0&search_provider=ic&search_term=",
        'cookie':"_gcl_au=1.1.684392445.1707114544; _gid=GA1.2.1032539318.1707114547; _fbp=fb.1.1707114547149.995837642; BVBRANDID=d9fff814-4c32-46c2-acf2-f5d805b32089; BVBRANDSID=b3f06b8a-ba77-429c-bfa7-b5d94c03983a; _pin_unauth=dWlkPU9HVmxPR000T1dFdE1XSmhPQzAwWlRFMExXSTVOemd0WW1VNFl6UTFZMk0xWm1VMQ; loyaltyID=undefined; __cf_bm=drdDCXLBGp22c8wclW8aYXF3F7MqcljC9GCdyHnb8Sk-1707115026-1-ARQOfufyyo3hJtx57lCnffyIutlgVQrRRdA3ykz3HuKS4bpjE0aA+l6foOHAt7B5Yx9XXpn/3PojZTOwdPW/hEM=; ajs_anonymous_id=73a84f33-dfcd-4813-846c-6fab8a1460fa; dotcomSearchId=dda0e649-7893-4b47-9d38-cef592fc8af2; _gat_UA-47434162-1=1; __stripe_mid=1dcb03fd-b1e8-427c-914c-681915063bd3ae9391; __stripe_sid=b7801e92-400a-4ac6-9cb6-72d8452084905ad788; _pin_unauth=dWlkPU9HVmxPR000T1dFdE1XSmhPQzAwWlRFMExXSTVOemd0WW1VNFl6UTFZMk0xWm1VMQ; ajs_anonymous_id=73a84f33-dfcd-4813-846c-6fab8a1460fa; session-sprouts=.eJwdjkFvgjAARv9Lz2YRxoxwU0BXpO3mkAIXglBDoSDSosKy_z625HuXd_neN0gvPZMlsC6ZkGwB0o71TdayVgFL9cNsJJOSX9tUXWvWAguw0SvP-5wT7sHTBDXMPfNlllquh-PMlOvifhZml9hwBattjZrThKdt5QcbIw5yhfdoSWytxI5X-0FSIUc0iRO_Jk0iiA0lbMMpibxLRj85qeCSOH-4Bvl68JgeVUbf_r8iXdSw6oaCPqVvz1GNOTCq3YsIcdIex4KeJGxEWcwdKMgfeHKfONiM5H35ciPIP6y2boxGzJ67bjzswsdhTwxJPpAbOlh10a2mRK2vYAEGyfqUF8DSjfU8bW3-_AIigGn6.GKITuQ.NMKoCVDpgwtUQmOXbC2yKTerpXE; _ga_LPZ816BHL5=GS1.1.1707114547.1.1.1707115066.30.0.0; _ga=GA1.2.2029369197.1707114547; _uetsid=60e971d0c3f011eea1a885bcac0afae3; _uetvid=60e99530c3f011ee8694fbc781e7dc02; _dd_s=rum=0&expire=1707115966509"
     }
]

searchterm ="Apple"
cookie=competitor_list[2]["cookie"]

HEADERS = {

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie    

}


URL = competitor_list[2]['url']+"apple"
responses=requests.get(URL,headers=HEADERS)
data = responses.json()
items=data.get('items')

for item in items:
    for category in item.get('categories'):
        if(category.get('name')=='Fruits'):
            if(searchterm in item.get('name')):
                print(item.get('name'))
        
    # if searchterm in item.get('name'):
    #     print(item.get('name'))