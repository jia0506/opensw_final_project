import pandas as pd
import matplotlib.pyplot as plt

def organ_month(df):
    text = '2020-01'
    sum = 0
    for index, i in enumerate(df["일자"]):
        if text != i[:7]:
            new_data = {'일자': text, '계(명)': sum}
            df = df.append(new_data, ignore_index=True)
            text = i[:7]
            sum = 0

        else:
            sum += df["계(명)"][index]
    return df

pd.set_option('display.max_row', None)
pd.set_option('display.max_columns', None)

musical = pd.read_csv("data\\공연 기간별 통계_월별.csv")
covid19_generation = pd.read_csv("data\\코로나바이러스감염증-19_확진환자_발생현황_211213_발생별.csv")
covid19_gender = pd.read_csv("data\\코로나바이러스감염증-19_확진환자_발생현황_211213_성별.csv")

covid19_male = covid19_gender.loc[:, '일자':'남성(명)']
covid19_female = covid19_gender.loc[:, ['일자', '여성(명)']]

covid19_female.rename(columns={'여성(명)':'계(명)'},inplace=True)
covid19_male.rename(columns={'남성(명)':'계(명)'},inplace=True)

covid19_male=organ_month(covid19_male)
covid19_female=organ_month(covid19_female)

musical["순수익"] = musical["매출액"] / musical["공연건수"]

print(covid19_gender)

covid19_generation = organ_month(covid19_generation)
covid19_generation = covid19_generation.iloc[694:, 0:2]



def graph(df):
    plt.rc('font', family='Malgun Gothic')
    plt.rc('axes', unicode_minus=False)

    ax = plt.gca()
    musical.iloc[12:35].plot(kind='line', x='기간', y='순수익', ax=ax)
    df.plot(kind='line', x='일자', y='계(명)', ax=ax)
    plt.title('코로나 추이별 뮤지컬 예매율')
    plt.show()


graph(covid19_generation)
graph(covid19_male)
graph(covid19_female)
