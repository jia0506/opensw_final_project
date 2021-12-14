import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_row', None)
pd.set_option('display.max_columns', None)

musical = pd.read_csv("data\\공연 기간별 통계_월별.csv")
covid19_generation = pd.read_csv("data\\코로나바이러스감염증-19_확진환자_발생현황_211213_확진자 수.csv")
covid19_gender = pd.read_csv("data\\코로나바이러스감염증-19_확진환자_발생현황_211213_성별 별.csv")
covid19_area = pd.read_csv("data\\코로나바이러스감염증-19_확진환자_발생현황_211213_지역별2.csv")

covid19_male = covid19_gender.loc[:, ['일자', '남성(명)']]
covid19_female = covid19_gender.loc[:, ['일자', '여성(명)']]

covid19_area1 = covid19_area.loc[:, ['일자', '서울']]
covid19_area2 = covid19_area.loc[:, ['일자', '부산']]
covid19_area3 = covid19_area.loc[:, ['일자', '대전']]
covid19_area4 = covid19_area.loc[:, ['일자', '전북']]
covid19_area5 = covid19_area.loc[:, ['일자', '제주']]

covid19_female.rename(columns={'여성(명)':'계(명)'},inplace=True)
covid19_male.rename(columns={'남성(명)':'계(명)'},inplace=True)

covid19_area1.rename(columns={'서울':'계(명)'},inplace=True)
covid19_area2.rename(columns={'부산':'계(명)'},inplace=True)
covid19_area3.rename(columns={'대전':'계(명)'},inplace=True)
covid19_area4.rename(columns={'전북':'계(명)'},inplace=True)
covid19_area5.rename(columns={'제주':'계(명)'},inplace=True)

def organ_month(df, date):
    text = '2020-01'
    sum = 0
    for index, i in enumerate(df["일자"]):
        if text != i[:date]:
            new_data = {'일자': text, '계(명)': sum}
            df = df.append(new_data, ignore_index=True)
            text = i[:date]
            sum = 0
        else:
            sum += df["계(명)"][index]
    return df

covid19_male = organ_month(covid19_male, 7)
covid19_female = organ_month(covid19_female, 7)

covid19_area1 = organ_month(covid19_area1, 7)
covid19_area2 = organ_month(covid19_area2, 7)
covid19_area3 = organ_month(covid19_area3, 7)
covid19_area4 = organ_month(covid19_area4, 7)
covid19_area5 = organ_month(covid19_area5, 7)

covid19_generation = organ_month(covid19_generation, 7)

musical["평균수익"] = musical["매출액"] / musical["공연건수"]

covid19_generation.rename(columns={'계(명)':'확진자 수(명)'},inplace=True)
covid19_female.rename(columns={'계(명)':'여성 확진자 수(명)'},inplace=True)
covid19_male.rename(columns={'계(명)':'남성 확진자 수(명)'},inplace=True)

covid19_area1.rename(columns={'계(명)': '서울 확진자 수'},inplace=True)
covid19_area2.rename(columns={'계(명)': '부산 확진자 수'},inplace=True)
covid19_area3.rename(columns={'계(명)': '대전 확진자 수'},inplace=True)
covid19_area4.rename(columns={'계(명)': '전북 확진자 수'},inplace=True)
covid19_area5.rename(columns={'계(명)': '제주 확진자 수'},inplace=True)

covid19_generation = covid19_generation.iloc[694:, 0:2]
covid19_female = covid19_female.iloc[694:, 0:2]
covid19_male = covid19_male.iloc[694:, 0:2]

covid19_area1 = covid19_area1.iloc[694:, 0:2]
covid19_area2 = covid19_area2.iloc[694:, 0:2]
covid19_area3 = covid19_area3.iloc[694:, 0:2]
covid19_area4 = covid19_area4.iloc[694:, 0:2]
covid19_area5 = covid19_area5.iloc[694:, 0:2]

plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)

fig, ax = plt.subplots()
musical.iloc[12:35].plot(kind='line', x='기간', y='평균수익', ax=ax)
covid19_generation.plot(kind='line', x='일자', y='확진자 수(명)', ax=ax)
plt.title('코로나 확진자 추이별 뮤지컬 예매율')

fig, ax = plt.subplots()
musical.iloc[12:35].plot(kind='line', x='기간', y='평균수익', ax=ax)
covid19_female.plot(kind='line', x='일자', y='여성 확진자 수(명)', ax=ax)
covid19_male.plot(kind='line', x='일자', y='남성 확진자 수(명)', ax=ax)
plt.title('코로나 성별 별 확진자 추이별 뮤지컬 예매율')

fig, ax = plt.subplots()
musical.iloc[12:35].drop(['공연건수','상연횟수','매출액','예매수','개막편수'],axis=1).plot(kind='line', x='기간', y='평균수익', ax=ax)
covid19_area1.plot(kind='line', x='일자', y='서울 확진자 수', ax=ax)
covid19_area2.plot(kind='line', x='일자', y='부산 확진자 수', ax=ax)
covid19_area3.plot(kind='line', x='일자', y='대전 확진자 수', ax=ax)
covid19_area4.plot(kind='line', x='일자', y='전북 확진자 수', ax=ax)
covid19_area5.plot(kind='line', x='일자', y='제주 확진자 수', ax=ax)
plt.legend()
plt.title('코로나 지역별 확진자 추이별 뮤지컬 예매율')

plt.show()
