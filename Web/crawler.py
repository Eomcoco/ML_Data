import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import pandas as pd
from sqlalchemy import create_engine

# ChromeDriver 경로 설정
CHROMEDRIVER_PATH = 'C:/Users/yi260/Downloads/chromedriver-win64/chromedriver.exe'

# Selenium WebDriver 설정
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 브라우저 창을 띄우지 않음
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# URL 설정
url = 'https://finance.naver.com/item/sise_day.naver?code=207940'
driver.get(url)

# 페이지 로딩 대기
time.sleep(2)

# HTML 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 테이블 데이터 추출
table = soup.find("table", class_="type2")
rows = table.find_all("tr")

# 데이터 저장 준비
data = []

for row in rows:
    cols = row.find_all("td")
    cols = [col.text.strip().replace('\n', '').replace('\t', '') for col in cols]  # \n 및 \t 제거
    if len(cols) == 7:  # 데이터가 있는 행만 저장
        data.append(cols)

driver.quit()

# CSV 파일로 저장
csv_file = 'C:/django_proj/webcrawling/daily_prices.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # 헤더 추가
    writer.writerow(['날짜', '종가', '전일 대비', '시가', '고가', '저가', '거래량'])
    # 데이터 추가
    writer.writerows(data)

print(f"데이터가 {csv_file}에 저장되었습니다.")


import pandas as pd
from sqlalchemy import create_engine

# MySQL 연결 설정
db_user = 'root'
db_password = 'adminkiki'
db_host = 'localhost'
db_name = 'finance_data'

# SQLAlchemy 엔진 생성
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

# UTF-8로 CSV 파일 읽기
csv_file = 'C:/django_proj/webcrawling/daily_prices.csv'
df = pd.read_csv(csv_file, encoding='utf-8')

# 데이터 삽입
try:
    with engine.connect() as conn:
        df.to_sql('daily_prices', con=conn, if_exists='append', index=False)
        print("CSV 데이터를 MySQL에 성공적으로 삽입했습니다!")
except Exception as e:
    print(f"데이터 삽입 중 오류가 발생했습니다: {e}")




