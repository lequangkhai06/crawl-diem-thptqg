import pandas as pd

file_path = 'diem_thi_2024_final.xlsx'

df = pd.read_excel(file_path, sheet_name='Sheet1')

df_sorted_A00 = df.sort_values(by='A00', ascending=False)
df_sorted_A00.to_excel('diem_thi_2024_sorted_A00.xlsx', index=False)

df_sorted_A01 = df.sort_values(by='A01', ascending=False)
df_sorted_A01.to_excel('diem_thi_2024_sorted_A01.xlsx', index=False)

df_sorted_D01 = df.sort_values(by='D01', ascending=False)
df_sorted_D01.to_excel('diem_thi_2024_sorted_D01.xlsx', index=False)

df_sorted_C00 = df.sort_values(by='C00', ascending=False)
df_sorted_C00.to_excel('diem_thi_2024_sorted_C00.xlsx', index=False)

print("Hoàn thành sắp xếp và lưu các tệp!")
