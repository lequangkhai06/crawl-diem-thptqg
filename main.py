import requests
import pandas as pd
import json


def get_score(key, result):
    return float(result.get(key, 0) or 0)


config_path = 'config.json'
with open(config_path, "r") as file:
    data = json.load(file)

SBDS = [f"{data['cityCode']}00{id:04}" for id in range(
    data['minRange'], data['maxRange'])]
year = data['year']
all_main_info = []
file_name = data['fileName']

for SBD in SBDS:
    print(f">> [ĐANG XỬ LÝ] SBD: {SBD:<12}")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    api_url = f"https://diemthi.vnanet.vn/Home/SearchBySobaodanh?code={SBD}&nam={year}"
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if 'result' in data and data['result']:
            result = data['result'][0]
            code = result['Code']

            toan = get_score('Toan', result)
            vatli = get_score('VatLi', result)
            hoahoc = get_score('HoaHoc', result)
            ngoaingu = get_score('NgoaiNgu', result)
            nguvan = get_score('NguVan', result)
            diali = get_score('DiaLi', result)
            lichsu = get_score('LichSu', result)
            sinhhoc = get_score('SinhHoc', result)
            khxh = get_score('KHXH', result)
            khtn = get_score('KHTN', result)
            gdcd = get_score('GDCD', result)

            main_info = {
                'SBD': code,
                'Toán': toan,
                'Ngữ Văn': nguvan,
                'Ngoại Ngữ': ngoaingu,
                'Vật Lí': vatli,
                'Hoá Học': hoahoc,
                'Sinh Học': sinhhoc,
                'KHTN': khtn,
                'Địa Lí': diali,
                'Lịch Sử': lichsu,
                'GDCD': gdcd,
                'KHXH': khxh,
                'A00': toan + vatli + hoahoc,
                'A01': toan + vatli + ngoaingu,
                'B00': toan + hoahoc + sinhhoc,
                'D01': toan + nguvan + ngoaingu,
                'C00': nguvan + diali + lichsu
            }
            all_main_info.append(main_info)
            print(f">> [THÀNH CÔNG] SBD: {SBD:<12}")
        else:
            print(f">> [KHÔNG TÌM THẤY] SBD: {SBD:<12}")
    else:
        print(f">> [LỖI] Mã lỗi {response.status_code:<4} SBD: {SBD:<12}")
        print(response.text)

main_df = pd.DataFrame(all_main_info)

with pd.ExcelWriter(file_name+'.xlsx') as writer:
    main_df.to_excel(writer, sheet_name='MainInfo', index=False)

print(f">> [HOÀN THÀNH] Dữ liệu đã được ghi lại vào file '{file_name}.xlsx'")
