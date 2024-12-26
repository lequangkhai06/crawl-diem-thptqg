import pandas as pd

file_path = 'DIEMTHITHPTQG2024.xlsx'

df = pd.read_excel(file_path)

df_sorted_A00 = df.sort_values(by='A00', ascending=False)
df_sorted_A00.to_excel('DIEMTHITHPTQG2024_SORTED_A00.xlsx', index=False)

df_sorted_A01 = df.sort_values(by='A01', ascending=False)
df_sorted_A01.to_excel('DIEMTHITHPTQG2024_SORTED_A01.xlsx', index=False)

df_sorted_D01 = df.sort_values(by='D01', ascending=False)
df_sorted_D01.to_excel('DIEMTHITHPTQG2024_SORTED_D01.xlsx', index=False)

df_sorted_C00 = df.sort_values(by='C00', ascending=False)
df_sorted_C00.to_excel('DIEMTHITHPTQG2024_SORTED_C00.xlsx', index=False)

df_sorted_B00 = df.sort_values(by='B00', ascending=False)
df_sorted_B00.to_excel('DIEMTHITHPTQG2024_SORTED_B00.xlsx', index=False)

print(">> ĐÃ HOÀN THÀNH!")
