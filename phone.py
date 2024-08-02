import pandas as pd
import re

df = pd.read_csv("phone.csv")

phone_column = df.columns[1]

def format_phone_number(phone):
    phone = str(phone)
    if re.match(r'^10\d{8}$', phone):
        formatted_phone = '010-' + phone[2:6] + '-' + phone[6:]
        return formatted_phone
    return phone

df[phone_column] = df[phone_column].astype(str).apply(format_phone_number)

df.to_csv('output1.csv', index=False)