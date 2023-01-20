import streamlit as st
import pandas as pd
from problem import CarGroupProblem

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

students_df = pd.DataFrame()
cars_df = pd.DataFrame()
solution_df = pd.DataFrame()

st.title("学生の乗車グループ分け問題")

with st.sidebar:
    students_file = st.file_uploader("学生データ：", type={"csv", "txt"})
    if students_file is not None:
        students_df = pd.read_csv(students_file)

    cars_file = st.file_uploader("車データ：", type={"csv", "txt"})
    if cars_file is not None:
        cars_df = pd.read_csv(cars_file)

# 最適化実行
if all([students_df is not None, cars_df is not None]):
    try:
        solution_df = CarGroupProblem(students_df, cars_df).solve()
        if solution_df.empty:
            st.write("ファイルの内容が間違っています。")
        else:
            st.dataframe(solution_df, width=300, height=720)
    # except KeyError('student_id'):
    #     st.write("学生データをアップロードして下さい。")
    # except KeyError('car_id'):
    #     st.write("車データをアップロードして下さい。")
    except:
        pass
        # st.write(f'ERROR')
else:
    solution_df = pd.DataFrame()

if not solution_df.empty:
    csv = convert_df(solution_df)
    st.sidebar.download_button(
        label="CSVダウンロード",
        data=csv,
        file_name='solution.csv',
        mime='text/csv',
    )
