import requests
import re

cookies = {
    'UOR': 'www.google.com,weibo.com,www.google.com',
    'SINAGLOBAL': '9834865993733.826.1720930879405',
    'SUB': '_2AkMQB1bVf8NxqwFRmf4TyGPrbY5xywDEieKmW6cOJRMxHRl-yT9kqmoFtRB6O4d4OliQ2a8L4XQ8jdJxXyJytQbi2Tok',
    'SUBP': '0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFv.5SKjGzLrRC0QiqX.AkJ',
    '_s_tentry': 'passport.weibo.com',
    'Apache': '793987105539.6019.1734072803468',
    'ULV': '1734072803474:2:1:1:793987105539.6019.1734072803468:1720930879425',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'UOR=www.google.com,weibo.com,www.google.com; SINAGLOBAL=9834865993733.826.1720930879405; SUB=_2AkMQB1bVf8NxqwFRmf4TyGPrbY5xywDEieKmW6cOJRMxHRl-yT9kqmoFtRB6O4d4OliQ2a8L4XQ8jdJxXyJytQbi2Tok; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFv.5SKjGzLrRC0QiqX.AkJ; _s_tentry=passport.weibo.com; Apache=793987105539.6019.1734072803468; ULV=1734072803474:2:1:1:793987105539.6019.1734072803468:1720930879425',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

params = {
    'cate': 'realtimehot',
}

def getTopKeyWords50() -> list:
    '''返回微博实时top50热搜关键词'''
    response = requests.get('https://s.weibo.com/top/summary', params=params, cookies=cookies, headers=headers)
    response_str = response.text

    # 正则表达式模式，用于匹配"_blank">和</a>之间的内容
    pattern = re.compile(r'_blank">(.*?)</a>')

    # 使用 findall 方法查找所有匹配的内容
    result = pattern.findall(response_str)
    if result:
        return(result[0:49])
    else: 
        print(response_str)
        raise ValueError('出问题了，返回报文中未找到目标字段')

if __name__ == '__main__':
    print(getTopKeyWords50())