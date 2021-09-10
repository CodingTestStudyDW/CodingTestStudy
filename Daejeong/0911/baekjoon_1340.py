# 1차 파싱
month, day, year, time = input().split()
# 1차 파싱 결과 => int형
day = int(day[:-1])
year = int(year)
# 2차 파싱
hour, minute = map(int, time.split(':'))

# 월 이름, 월별 일수 초기화
month_list = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
month_date_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 윤년일때, 2월달 날짜 변경
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    month_date_list[1] = 29
# 당해 총 분 연산
year_minutes = sum(month_date_list) * 1440
# 월을 숫자로 반환
month_num = month_list.index(month)
# 분 + 시간 * 60 + (전월까지 합산일 + 당월 일) * 1440
total_minutes = minute + (hour * 60) + ((sum(month_date_list[:month_num]) + day-1) * 1440)
# 현재까지 진행된 시간 / 1년 총 분 * 100 = 현재 진행도
print(total_minutes / year_minutes * 100)