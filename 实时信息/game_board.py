import requests
import json

cookies = {
    'qgqp_b_id': 'bbab04bb75eb4ff7d0ac80095f74c2ae',
    'emshistory': '%5B%22%E4%BB%BB%E5%A4%A9%E5%A0%82%22%2C%22%E6%B8%B8%E6%88%8F%22%5D',
    'websitepoptg_api_time': '1734286731603',
    'HAList': 'ty-1-600519-%u8D35%u5DDE%u8305%u53F0%2Cty-90-BK1046-%u6E38%u620F%2Cty-1-603986-%u5146%u6613%u521B%u65B0%2Cty-0-300795-%u7C73%u5965%u4F1A%u5C55%2Cty-90-BK0486-%u6587%u5316%u4F20%u5A92%2Cty-1-603258-%u7535%u9B42%u7F51%u7EDC%2Cty-0-300280-%u7D2B%u5929%u79D1%u6280%2Cty-1-600892-%u5927%u665F%u6587%u5316%2Cty-0-300113-%u987A%u7F51%u79D1%u6280%2Cty-1-600633-%u6D59%u6570%u6587%u5316',
    'st_si': '14539794737348',
    'st_pvi': '04649914865772',
    'st_sp': '2024-05-07%2000%3A19%3A07',
    'st_inirUrl': 'https%3A%2F%2Fwww.bing.com%2F',
    'st_sn': '1',
    'st_psi': '20241217012050763-113200301321-5175609964',
    'st_asi': 'delete',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'qgqp_b_id=bbab04bb75eb4ff7d0ac80095f74c2ae; emshistory=%5B%22%E4%BB%BB%E5%A4%A9%E5%A0%82%22%2C%22%E6%B8%B8%E6%88%8F%22%5D; websitepoptg_api_time=1734286731603; HAList=ty-1-600519-%u8D35%u5DDE%u8305%u53F0%2Cty-90-BK1046-%u6E38%u620F%2Cty-1-603986-%u5146%u6613%u521B%u65B0%2Cty-0-300795-%u7C73%u5965%u4F1A%u5C55%2Cty-90-BK0486-%u6587%u5316%u4F20%u5A92%2Cty-1-603258-%u7535%u9B42%u7F51%u7EDC%2Cty-0-300280-%u7D2B%u5929%u79D1%u6280%2Cty-1-600892-%u5927%u665F%u6587%u5316%2Cty-0-300113-%u987A%u7F51%u79D1%u6280%2Cty-1-600633-%u6D59%u6570%u6587%u5316; st_si=14539794737348; st_pvi=04649914865772; st_sp=2024-05-07%2000%3A19%3A07; st_inirUrl=https%3A%2F%2Fwww.bing.com%2F; st_sn=1; st_psi=20241217012050763-113200301321-5175609964; st_asi=delete',
    'Referer': 'https://quote.eastmoney.com/center/boardlist.html',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response1 = requests.get('https://75.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112405163559613566906_1734369677755&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&dect=1&wbp2u=|0|0|0|web&fid=f3&fs=b:BK1046+f:!50&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f45&_=1734369677756', cookies=cookies, headers=headers)
response2 = requests.get('https://54.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112403762781731857183_1734390159818&pn=1&pz=100&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&dect=1&wbp2u=|0|0|0|web&fid=f3&fs=b:BK1036+f:!50&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f45&_=1734390159819', cookies=cookies, headers=headers)
response_str2 = response2.text
def get_sector_data(stock_sector: str):
    def extract_data_dict(response_str):
        start_index = response_str.find('(')
        end_index = response_str.rfind(')')
        if start_index != -1 and end_index != -1:
            json_str = response_str[start_index+1:end_index]
            return json.loads(json_str)
        return None

    def get_stock_codes(response_str) -> list:
        data_dict = extract_data_dict(response_str)
        stock_info_list = data_dict['data']['diff']
        res = []
        for stock_info in stock_info_list:
            res.append(stock_info['f12'])   
        return res
    
    url = f'https://54.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112403762781731857183_1734390159818&pn=1&pz=100&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&dect=1&wbp2u=|0|0|0|web&fid=f3&fs=b:{stock_sector}+f:!50&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f45&_=1734390159819'
    response = requests.get(url, cookies=cookies, headers=headers)
    response_str = response.text
    print(get_stock_codes(response_str))

get_sector_data('BK0972')