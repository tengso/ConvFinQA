from io import StringIO

import streamlit as st
import pandas as pd
import json

st.write('hello')

case_id = 'Single_MRO/2007/page_134.pdf-1'


def print_case(case):
    pre_text = case['pre_text']
    pre_text = ''.join(pre_text)
    st.info(pre_text)

    table = case['table']
    cols = {}
    for col in table:
        cols[col[0]] = col[1:]

    table = pd.DataFrame(cols)

    st.dataframe(table)

    buff = StringIO()
    table.to_csv(buff, index=False)
    st.text(buff.getvalue())


with open('data/dev.json') as f:
    data = json.load(f)
    case = data[0]

    print_case(case)
    st.write(case)
