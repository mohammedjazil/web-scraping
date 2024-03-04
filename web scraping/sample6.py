import requests
import pandas as pd

cookie = "_gcl_au=1.1.684392445.1707114544; _fbp=fb.1.1707114547149.995837642; BVBRANDID=d9fff814-4c32-46c2-acf2-f5d805b32089; _pin_unauth=dWlkPU9HVmxPR000T1dFdE1XSmhPQzAwWlRFMExXSTVOemd0WW1VNFl6UTFZMk0xWm1VMQ; loyaltyID=undefined; ajs_anonymous_id=73a84f33-dfcd-4813-846c-6fab8a1460fa; __stripe_mid=1dcb03fd-b1e8-427c-914c-681915063bd3ae9391; _pin_unauth=dWlkPU9HVmxPR000T1dFdE1XSmhPQzAwWlRFMExXSTVOemd0WW1VNFl6UTFZMk0xWm1VMQ; ajs_anonymous_id=73a84f33-dfcd-4813-846c-6fab8a1460fa; _gid=GA1.2.53983315.1707209227; BVBRANDSID=5f36997c-1e07-4d55-bdce-a7626742410e; __cf_bm=KShjl1H2HDpFIwIV.wepZOt.iZoMNp6Fyz3qF._1gVY-1707209242-1-ATSDOulZgx0KMgMNHByXAIoySXUC/Sm3yQK836sz7at/cPgJKHv93SWe8Tm6JdegatKVijPKrWOP/QFhSTN1FtQ=; __stripe_sid=b060ecc3-49a4-4314-bf28-36b64df8dbf38c8c02; _gat_UA-47434162-1=1; _dd_s=rum=0&expire=1707210340694; session-sprouts=.eJwdjstygjAARf8la8cBlI6wc4DWMCSoPCJuGCShhEekBFTo9N9LO3PP5mzu-QZp0TNZArPIGslWIO1Y32aCiQGYQz8uRjIp-V2kw71mApiATW55-8i5z10YzVDF3DXWi1RzLZ4W5lxrHrfG6K4WfIMt3FyruERhU3ok2SCSDNh2ZhwoOp5p5ZFzheZEQwQq2Ia6H0AJRTxfL26RkRP3K6j49h_O1g-ePCHnISP6_9dFa2pYdSMlL-lZS1RrjIyoD3pB3BfniZJIwrYp6dKBwvyJZ-eFw_3kH5R1vdvXt_sEqe4dH0eqxF8s-jxkxfvWtiyxOaGgc05GmFQEghUYJetTToGpbXfL1J3x8wvc52kh.GKOEYw.6l9L175IFq58HA0dO0WQZu840Gg; _ga_LPZ816BHL5=GS1.1.1707209227.3.1.1707209443.40.0.0; _ga=GA1.2.2029369197.1707114547; _uetsid=57c3aa40c4cc11eea0851dfa3f0ac873; _uetvid=60e99530c3f011ee8694fbc781e7dc02"

HEADERS = {

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie    

}

URL= "https://shop.sprouts.com/api/v2/categories/store/2"

responses = requests.get(URL,headers=HEADERS)
data = responses.json()
print(data['items'])