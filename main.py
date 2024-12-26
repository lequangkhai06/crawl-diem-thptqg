import requests
import pandas as pd

SBDS = [f'6300{id:04}' for id in range(1, 7502)]
year = 2024
all_main_info = []
all_group_info = []

for SBD in SBDS:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    api_url = 'https://diemthi.vnanet.vn/Home/SearchBySobaodanh?code=' + \
        str(SBD)+'&nam='+str(year)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
        # {
        #     "result": [
        #         {
        #             "CityCode": "63",
        #             "CityArea": null,
        #             "Code": "63000012",
        #             "Toan": "4.00",
        #             "NguVan": "5.25",
        #             "NgoaiNgu": "2.80",
        #             "VatLi": "",
        #             "HoaHoc": "",
        #             "SinhHoc": "",
        #             "KHTN": "",
        #             "DiaLi": "7.25",
        #             "LichSu": "8.50",
        #             "GDCD": "8.00",
        #             "KHXH": "7.92",
        #             "ResultGroup": "",
        #             "Result": ""
        #         }
        #     ]
        # }
        if data['result']:
            result = data['result'][0]
            main_info = {
                'SBD': result['Code'],
                'Toan': result['Toan'],
                'NguVan': result['NguVan'],
                'NgoaiNgu': result['NgoaiNgu'],
                'VatLi': result['VatLi'],
                'HoaHoc': result['HoaHoc'],
                'SinhHoc': result['SinhHoc'],
                'KHTN': result['KHTN'],
                'DiaLi': result['DiaLi'],
                'LichSu': result['LichSu'],
                'GDCD': result['GDCD'],
                'KHXH': result['KHXH'],
            }
            all_main_info.append(main_info)

    else:
        print(
            f'Có lỗi xảy ra {response.status_code} SBD {SBD}')
        print(response.text)

main_df = pd.DataFrame(all_main_info)
group_df = pd.DataFrame(all_group_info)

with pd.ExcelWriter('DIEMTHITHPTQG2024.xlsx') as writer:
    main_df.to_excel(writer, sheet_name='MainInfo', index=False)
    group_df.to_excel(writer, sheet_name='ListGroup', index=False)

print('Dữ liệu đã được ghi lại vào file DIEMTHITHPTQG2024.xlsx')
