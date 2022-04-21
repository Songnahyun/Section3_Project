#csv파일에 들어있는 데이터를 sqlite DB에 저장하기2

import csv
import sqlite3

#[1]csv파일 읽기-->open()사용-->csv.reader()메서드 사용하여 한 줄씩 읽기.
fileName="DATA_1.csv"
file=open(fileName,"r")
reader=csv.reader(file)

#[2]DB연결 및 커서 객체 생성
conn = sqlite3.connect("/Users/songnahyun/Section3_Project/cosmetics.db")
cur = conn.cursor()

#테이블 생성
cur.execute("DROP TABLE IF EXISTS cosmetics;")
cur.execute("""
                CREATE TABLE IF NOT EXISTS cosmetics(Name TEXT, brand TEXT, ratings TEXT, 
                volume TEXT, price TEXT, category TEXT, Age TEXT,
                type TEXT, gender TEXT, rating TEXT, recommend TEXT);
            """)

#[3]순회하면서 할 일 처리.
arr = []

for row in reader:
    # print(row)
    arr.append(row)
    
for row in arr:
    strSQL = "INSERT INTO cosmetics(Name, brand, ratings, volume, price, category, Age, type, gender, rating, recommend)values(?,?,?,?,?,?,?,?,?,?,?)"
    cur.execute(strSQL,(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))

conn.commit()

print('-'*100)
print('CSV파일의 데이터가 DB에 입력되었습니다.')

cur.close()
conn.close()