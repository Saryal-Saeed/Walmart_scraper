import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
import regex as re
import json


payload={}
headers = {
  'authority': 'www.walmart.com',
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'cookie': 'AID=wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1680629130393; ACID=06dfba9c-8d8b-4948-aef5-fb6173322bf0; hasACID=true; assortmentStoreId=3081; hasLocData=1; vtc=e53P9nN4TgKx46-IidusZg; _pxhd=c9f119ac89514cd45729c512bac0c25183ced7b10d455a1d455eaf6187ffe17f:b2a1ee9c-d30d-11ed-92e5-636343625079; adblocked=false; _pxvid=b2a1ee9c-d30d-11ed-92e5-636343625079; TBV=7; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjp0cnVlLCJzdG9yZVNlbGVjdGlvblR5cGUiOiJERUZBVUxURUQiLCJwaWNrdXAiOnsibm9kZUlkIjoiMzA4MSIsInRpbWVzdGFtcCI6MTY4MDYyOTEzMDQyN30sInNoaXBwaW5nQWRkcmVzcyI6eyJ0aW1lc3RhbXAiOjE2ODA2MjkxMzA0MjcsInR5cGUiOiJwYXJ0aWFsLWxvY2F0aW9uIiwiZ2lmdEFkZHJlc3MiOmZhbHNlLCJwb3N0YWxDb2RlIjoiOTU4MjkiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJkZWxpdmVyeVN0b3JlTGlzdCI6W3sibm9kZUlkIjoiMzA4MSIsInR5cGUiOiJERUxJVkVSWSIsInN0b3JlU2VsZWN0aW9uVHlwZSI6IkRFRkFVTFRFRCJ9XX0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjgwNjI5MTMwNDI3LCJiYXNlIjoiOTU4MjkifSwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOjA2ZGZiYTljLThkOGItNDk0OC1hZWY1LWZiNjE3MzMyMmJmMCJ9; dimensionData=757; _gcl_au=1.1.933014234.1681311557; bstc=RHjUK0LzOcHSI3E4QeKJfs; mobileweb=0; xptc=assortmentStoreId%2B3081; xpa=10hNA|1bHX2|456qm|5T7w_|6mVys|7AiHj|A5Ih6|AaLnz|BB1yD|D8jju|DckjW|HNply|I63vb|JeH5W|MRAaL|No0Ca|O_W3W|Onkhp|S-7Vu|VG72V|X_0sV|YnYws|ZLvCF|Zmb6E|btMCR|ce_CN|fLj07|jJAPh|kHCgj|lPtmn|ohl01|omGZ5|pXoyW|tRgKW|u5Y8n|vx67L; exp-ck=10hNA11bHX215T7w_36mVys17AiHj1A5Ih63AaLnz1D8jju1DckjW1X_0sV3YnYws4ZLvCF1ce_CN1jJAPh2lPtmn1ohl011pXoyW1u5Y8n1vx67L1; xpkdw=1; pxcts=a943949e-d942-11ed-ae50-6f475a58637a; _pxff_cfp=1; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; auth=MTAyOTYyMDE4GZnmyOeN6R5r0EUI3HijqvpMqfyIasUWLeZm9eu32LwnANA6awbjWGvLLXvXV%2FMQhb92aLg%2B3NNEXuLBDPz2ZEMPJj3lP8SSxIpeuog4VDp1uR590YVl1n3hfdfH5%2Ftz767wuZloTfhm7Wk2Kcjygiq0nmGVz3wI1IrcfVbuZ14zv8jNCdymXWOcA5krBHqBcmoa%2BMtg7SXN7qWtEmnIWsROROWz05yj8gJHPRUYO%2B4UMk70P8glgOEpLOprhDfMDCcb9mgycy9jtT1uIyOBHdGZlpcviaAM4RKodIU%2F06agoroZouKuMm163RL3qs%2Banjun39TnyJEU1gh69tF1Wn204pGWrARRh%2FenqT9gVvQwE7PUXN7AWSvwcZA%2FCt7n3YjUMocf2K93JFH01U2HCJE5WBBdZBCyKnCQAR7o6eg%3D; xpm=1%2B1681311584%2Be53P9nN4TgKx46-IidusZg~%2B0; locDataV3=eyJpc0RlZmF1bHRlZCI6dHJ1ZSwiaXNFeHBsaWNpdCI6ZmFsc2UsImludGVudCI6IlNISVBQSU5HIiwicGlja3VwIjpbeyJidUlkIjoiMCIsIm5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiOTU4MjkiLCJhZGRyZXNzTGluZTEiOiI4OTE1IEdlcmJlciBSb2FkIiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5NTgyOS0wMDAwIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozOC40ODI2NzcsImxvbmdpdHVkZSI6LTEyMS4zNjkwMjZ9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIzMDgxIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9DVVJCU0lERSIsIlBJQ0tVUF9JTlNUT1JFIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozOC40NzQ2LCJsb25naXR1ZGUiOi0xMjEuMzQzOCwicG9zdGFsQ29kZSI6Ijk1ODI5IiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJQSUNLVVBfQ1VSQlNJREUiLCJQSUNLVVBfSU5TVE9SRSJdLCJpbnRlbnQiOiJQSUNLVVAifSwiaW5zdG9yZSI6ZmFsc2UsImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMzA4MSIsImRpc3BsYXlOYW1lIjoiU2FjcmFtZW50byBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5NTgyOSIsImFkZHJlc3NMaW5lMSI6Ijg5MTUgR2VyYmVyIFJvYWQiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6Ijk1ODI5LTAwMDAifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjM4LjQ4MjY3NywibG9uZ2l0dWRlIjotMTIxLjM2OTAyNn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsImFjY2Vzc1BvaW50cyI6W3siYWNjZXNzVHlwZSI6IkRFTElWRVJZX0FERFJFU1MifV0sImh1Yk5vZGVJZCI6IjMwODEiLCJpc0V4cHJlc3NEZWxpdmVyeU9ubHkiOmZhbHNlLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJERUxJVkVSWV9BRERSRVNTIl19LCJyZWZyZXNoQXQiOjE2ODEzMTE4ODc3NjYsInZhbGlkYXRlS2V5IjoicHJvZDp2MjowNmRmYmE5Yy04ZDhiLTQ5NDgtYWVmNS1mYjYxNzMzMjJiZjAifQ%3D%3D; _astc=b63de9c34af28547e494ead7e09b42ee; _uetsid=9925b040d94211edba1a6372978667df; _uetvid=99264540d94211edaf7dc73fa27df5f0; wmlh=b81da24d28452bff93b3d8976700d3788714e4c8fb30e3ab08089832c196d448; bm_mi=ADA21BBF7364FEA6EC77536021B7D68E~YAAQPZ4QAramWlyHAQAAPjP8dRPE5O7ZI9FmhFT6bWpxPCc8ywzrBEsTS7b3R76C4ssCBTDHg7q/CbxZIsBeCgf5In3ZceEDkwOb/2fKnrWbHocAkDmiuGiusiXZsey4V8Un7p/JZnW2qGdElIF3cTnDLHvy5vxPgvnnpzFjnbm4JAfYI56tLNgkK5SelLsmNUL/RbqkY1jGLho3PbvMImKG968v8jKna07EMNOMhZRSqwRA/wH9JlLtcIXGUtzvJ9+zS/rQtaX0VshISXU52CgeQMvayPF1I07zKqOzg7SSy6zzWlaBfOGWO0fnKr/Y7FI7VrI=~1; xptwj=rq:4c6cfa18e1c987f1d8cd:NtOdCan/069znawr+IqmjcOiR0d2SVQf+T9o3XztDH3Az/4t6ixW5rOVWWBWHzBSxDMyVsKcRG6o84JpUD1TtqCEI6hIxhFNAEftixNls0S872gvISsCs5RwwvTDQSaITUARoftOrlpof/+F9cRNkWDq4VJhCg==; akavpau_p2=1681312289~id=8b380a4b236e37bbcd24218aa93a449a; bm_sv=FADAA63E9A43EC8A6208A2D008BEA16B~YAAQPZ4QAmOnWlyHAQAAEWv8dRNrsLWrPzY/Bx1Kv3ljSbFpK3byODnCY6xaJ76jvzz0FYPf82UW2MmxQpfc6DcUzBEo19TOhNoSgCI/pSIxz65XN7dgpns1JqIADsnr/y8e/HlZIBd/NH7bTWEDTfu3w25Nd2NLuaJhfX9oOZJVaxwWX4MQjYD48E9VXnEE2YxOpbMyvOWaqZJMueexSdVfbxMahR6F8swYQDNpZwhrMZPoA25qVM+3ek9DxItWcx8=~1; ak_bmsc=F4E91448AE9A3270CC09F0FBBC627F66~000000000000000000000000000000~YAAQPZ4QAoKnWlyHAQAAMnX8dRMtEQwzZ9lBtjbOGFEp3aCSWKQx9wIvtORvnSY9M63myczSfWz+KVYOcbgYkPEP0/vzK0sY68sW/wNmeVdrdC66aXuPyyHwfG1i8JVkOY1NfdTCylYYcrk+bE0GXqS4RoVjXRKtAPtYgKTCygk1V6z7AoGblkxAna4iem9wFfQHgTdvbKTqK8JcTAy6ifrVbCdPL64zU1lwrk+vA6Tgj5S3OprCKrj14wFikbucsWGNslSwnFD69WJiXhRrjntdLYGRx1pPnX5EAgcZWD+EU0Pr22/49KbRMWfUs3veb9rcxuivaNqEK126cauVRBLoz+zUWTE8S9KUIyurIsklJoM0GTXtgJUtvIedyUQwadZM5OXdr/GAIAwwa0YBO86kjUUYapqXOzLFrj1P7mUFAnHSnpE=; _px3=4db625bd95f8f57d510c86c2f947def5fdf4158f2c894174e2543a66e5567bf5:ctRuTxfgwC6+2qMhDnH4g+X7T5ef7enPW/UoNe1M5Gv+dW9mv6idQeQphdlUu+Ib0czGY0aiTf7JcgInI2Y0vQ==:1000:ku8P4isO5ojxbQijbCuviAISkBO3FCU3kr6H0hDgnwMZh/35MCbp6EXUEO4KQWoEWX9nCkLhE99gJRcjZh19KYQKnTvGe/tLEL6Vx1J9gLhw0kVFtWVKPt1Yu6ZKh4hxajQy5HI+kYLGOoCa4kfHqlDTMPzTnzTsv01aW81x7DogWAkpFIG7aWIA9kra66FfC1jkIE5jO0X0K7USlEnjvQ==; _pxde=3e784b2d68bebcdc0d8c0c5ca2b7e3fdfd483f7db438bbe3e4cf8f5dd56eef28:eyJ0aW1lc3RhbXAiOjE2ODEzMTE3MDIwODN9; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1681311703000@firstcreate:1680629130393"; xptwg=874791797:1D283BDEC81E8C0:4A7BA2F:F6B10394:22EBD70C:7DC0C10:; TS012768cf=01419f1d62626b6f2224421b2a08656b2bde6e8c7af8e901ccaaa52a57d8bd358f10ef1183a3b7fb7342cde4b492f640f699e8429b; TS01a90220=01419f1d62626b6f2224421b2a08656b2bde6e8c7af8e901ccaaa52a57d8bd358f10ef1183a3b7fb7342cde4b492f640f699e8429b; TS2a5e0c5c027=0820e3fdc4ab200014bda87a3a89a77ff2ddac8c8249c232c73647971a527a4acc9a07525229a0ba081fc559f71130008a206463facbc4d543eb14ac1766f24769bb8b27ec9b359e7acef42f3c12b98638f9f76ebdfe3b297fef4bb8025f625d; TS01a90220=014dff5a5d4bc0ee89e5256d3747bc4f760e2930c463fbf854fe418f168928e32d90333e8b0538d39d0069353149a23fede297e357; bstc=RHjUK0LzOcHSI3E4QeKJfs; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1681311765000@firstcreate:1680629130393"; exp-ck=10hNA11bHX215T7w_36mVys17AiHj1A5Ih63AaLnz1D8jju1DckjW1X_0sV3YnYws4ZLvCF1ce_CN1jJAPh2lPtmn1ohl011pXoyW1u5Y8n1vx67L1; mobileweb=0; vtc=e53P9nN4TgKx46-IidusZg; xpa=10hNA|1bHX2|456qm|5T7w_|6mVys|7AiHj|A5Ih6|AaLnz|BB1yD|D8jju|DckjW|HNply|I63vb|JeH5W|MRAaL|No0Ca|O_W3W|Onkhp|S-7Vu|VG72V|X_0sV|YnYws|ZLvCF|Zmb6E|btMCR|ce_CN|fLj07|jJAPh|kHCgj|lPtmn|ohl01|omGZ5|pXoyW|tRgKW|u5Y8n|vx67L; xpm=1%2B1681311584%2Be53P9nN4TgKx46-IidusZg~%2B0; xptc=assortmentStoreId%2B3081; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xptwg=131483448:17D873E76A0ED20:3CEA078:CB3CB42D:174B26F0:D32ED7B5:; xptwj=rq:62a0ba89c586f9cac72b:RwcAsOj85c+/AbvSLC/QUJlUWgXsPaW4K+nL2zgeEkvoqE8OYnVHo5vW1K8E9pkI6201lWyrcO+H1zE33MVBRj1WAi7RGh4dFj6/sTl65nBAHhw4CUjEjN8RM7ts8fj1gDXcy1KAhgWROK1iwu3jwCuNSw==; TS012768cf=014dff5a5d4bc0ee89e5256d3747bc4f760e2930c463fbf854fe418f168928e32d90333e8b0538d39d0069353149a23fede297e357; TS2a5e0c5c027=085ea3cd67ab200087fcd614d1d95d2b98ec6c612cbe72035529e27cfdeaba48d4f5c981d7a654a40885e2607b1130004533332e6a9db3bbb6d6195d933e2e29b630b5dedb1a15a3986996f56f9c16a198c627842faa4cada634947a49097cc8; akavpau_p2=1681312365~id=be50e87ca6ef4714684d8301839b5628',
  'device_profile_ref_id': 'b6RfPDtffdWcGmHHemQ1gbS124H6vvKZzEts',
  'referer': 'https://www.walmart.com/search?cat_id=0&query=grocery&page=2&affinityOverride=store_led',
  'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'traceparent': '00-160a42db7cf55135c40cb9f91631ac6b-035934637f2b385c-00',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
  'wm_mp': 'true',
  'wm_page_url': 'https://www.walmart.com/search?cat_id=0&query=grocery&page=2&affinityOverride=store_led',
  'wm_qos.correlation_id': '2lsAZQDFU21OxgX57hALVn0c152PQXTfgo4l',
  'x-apollo-operation-name': 'Search',
  'x-enable-server-timing': '1',
  'x-latency-trace': '1',
  'x-o-bu': 'WALMART-US',
  'x-o-ccm': 'server',
  'x-o-correlation-id': '2lsAZQDFU21OxgX57hALVn0c152PQXTfgo4l',
  'x-o-gql-query': 'query Search',
  'x-o-mart': 'B2C',
  'x-o-platform': 'rweb',
  'x-o-platform-version': 'main-1.62.0-4093f9-0411T1851',
  'x-o-segment': 'oaoh'
}

PN = []
USITM = []
ID = []
URLS = []
PRICE = []
output = []
links = []


for page in range(1):
    url = f"https://www.walmart.com/orchestra/snb/graphql/Search/7a8656160a83166719c22e01473ee3b89afb0b1ed1f774b984035590e69d625f/search?variables=%7B%22id%22%3A%22%22%2C%22affinityOverride%22%3A%22store_led%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22grocery%22%2C%22page%22%3A{page}%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%220%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22grocery%22%2C%22cat_id%22%3A%220%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22fitmentFieldParams%22%3A%7B%22powerSportEnabled%22%3Atrue%7D%2C%22fitmentSearchParams%22%3A%7B%22id%22%3A%22%22%2C%22affinityOverride%22%3A%22store_led%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22grocery%22%2C%22page%22%3A{page}%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%220%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22grocery%22%2C%22cat_id%22%3A%220%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22cat_id%22%3A%220%22%2C%22_be_shelf_id%22%3A%22%22%7D%2C%22enableFashionTopNav%22%3Afalse%2C%22enableRelatedSearches%22%3Afalse%2C%22enablePortableFacets%22%3Atrue%2C%22enableFacetCount%22%3Atrue%2C%22fetchMarquee%22%3Atrue%2C%22fetchSkyline%22%3Atrue%2C%22fetchGallery%22%3Afalse%2C%22fetchSbaTop%22%3Atrue%2C%22tenant%22%3A%22WM_GLASS%22%2C%22enableFlattenedFitment%22%3Atrue%2C%22pageType%22%3A%22SearchPage%22%7D"
    r = requests.request("GET", url, headers=headers)
    data = json.loads(r.text)

    for items in data['data']['search']['searchResult']['itemStacks'][0]['itemsV2']:
        try:
            ProductName = (items['name'])
            id = items['id']
            USitemID = items['usItemId']
            Urls = "https://www.walmart.com/" + (items['canonicalUrl'])
            price = items['priceInfo']['currentPrice']["priceString"]
            time.sleep(0.25)
            print('storing data')
            PN.append(ProductName)
            ID.append(id)
            USITM.append(USitemID)
            URLS.append(Urls)
            PRICE.append(price)
            links.append(Urls)
        except:
            pass

df2 = pd.DataFrame(links)
link = df2.to_csv('links.csv')

api_key = '2FY54CHXZI9O65KBDSJ8L9NFWC8VNK6Q53UPOXYPIPZ2JDEIXFMT0UNLAR1KLX5GVGWG6S1558XUY23I'

upc_codes = []
for item in links:
    url = item
    params = {
        'api_key': api_key,
        'url': url,
        'premium_proxy': True,
        'js_snippets': [
            '''
            window.onload = function() {
                window.scrollTo(0,document.body.scrollHeight);
                setTimeout(function() {
                    var scriptTag = document.querySelector('script[type="application/json"]');
                    if (scriptTag !== null) {
                        var upcMatch = scriptTag.innerHTML.match(/"upc":\s*"(\d+)"/);
                        if (upcMatch !== null) {
                            var upc = upcMatch[1];
                            console.log("Fetching UPC:", upc);
                            upc_codes.append(upc);
                        } else {
                            console.log("UPC not found");
                            upc_codes.append("UPC not found");
                        }
                    } else {
                        console.log("No script tag with type 'application/json' found.");
                    }
                }, 1000); // wait 1 second for the script tag to load
            }
            '''
        ]
    }

    response = requests.get('https://app.scrapingbee.com/api/v1/', params=params)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")

    # The script tag is loaded by JavaScript, so we don't need to find it using BeautifulSoup

    # The UPC code is already extracted by the JavaScript snippet, so we don't need to use a regular expression to find it

    # We can print the list of UPC codes or do whatever we want with them
    print(upc_codes)

#df = pd.DataFrame({'Product': PN, 'ID': ID, 'UsItemNO': USITM, 'URLS': URLS, 'PRICE': PRICE, 'UPC': upc_codes})

#final = df.to_csv('new_groceries.csv')
