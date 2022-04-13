import requests as r
import json
from bs4 import BeautifulSoup
import base64

req = r#.Session()
# req.headers.update({
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
# })

def get(url, options={}):
    response = req.get(url, params=options)
    # get status code
    status = response.status_code
    if (status == 200):
        return response
    else:
        url_base64 = base64.b64encode(url.encode('utf-8'))
        response = req.get("https://bypass.kato-rest.us/?q=" + url_base64.decode('utf-8'))
        # if "komikindo" in url:
        #     # url = url.replace("komikindo.id", "komikindo-id.translate.goog")
        #     # if "?" in url:
        #     #     response = req.get(url + "&_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=id", params=options)
        #     # else:
        #     #     response = req.get(url + "?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=id", params=options)
            
        #     return response
        
        # if "otakudesu" in url:
        #     url_base64 = base64.b64encode(url.encode('utf-8'))
        #     response = req.get("https://bypass.kato-rest.us/?q=" + url_base64.decode('utf-8'))
        #     # url = url.replace("otakudesu.site", "otakudesu-site.translate.goog")
        #     # if "?" in url:
        #     #     response = req.get(url + "&_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=id", params=options)
        #     # else:
        #     #     response = req.get(url + "?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=id", params=options)
            
        return response
        
def get_media_src(url):
    response = get(url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    
    src = None
    src1 = soup.find("source")
    src2 = data.split("sources: [")
    src3 = soup.find("iframe")
    if (src1):
        src = src1.get("src")
    elif (len(src2) > 1):
        src = src2[1].split("]")[0].split("'file':")[1].split("'")[1]
    elif (src3):
        src = src3.get("src")
    return src

def reverse_proxy(url):
    #decode base64
    url = base64.b64decode(url).decode('utf-8')

    #return as video
    response = req.get(url,)
    
    return response