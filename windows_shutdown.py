import os
import time
import subprocess
from datetime import datetime, timedelta

def check_and_shutdown():

    # 바탕화면 경로 설정 -> 사용자 텍스트 파일 경로에 따라 수정이 필요(같은 디렉토리로 PATH 설정)
    # 해당 디렉토리인 windows_shutdown 에 endTime 위치시킴
    # desktop_path = "C:\\freshway\\endTime.txt"
    desktop_path = "endTime.txt"

    
    while True:
        try:
            # 텍스트 파일 읽기
            with open(desktop_path, 'r') as file:
                shutdown_time = file.read().strip()

            # 설정된 종료 시간 파싱
            shutdown_dt = datetime.strptime(shutdown_time, '%H:%M')
            now = datetime.now()
            shutdown_dt = datetime.combine(now.date(), shutdown_dt.time())

            # 현재 시간이 종료 시간 이후면 다음 날로 설정
            if now >= shutdown_dt:
                shutdown_dt += timedelta(days=1)

            # 종료 시간까지 남은 시간 계산
            remaining_seconds = (shutdown_dt - now).total_seconds()

            print(f"Current time: {now}")
            print(f"Scheduled shutdown time: {shutdown_dt}")
            print(f"Remaining seconds until shutdown: {remaining_seconds}")

            if remaining_seconds <= 120:  # 설정된 종료 시간이 2분 이내일 경우
                try:
                # 설정된 종료 시간에 PC 종료
                    print(f"Shutting down at {shutdown_dt.strftime('%Y-%m-%d %H:%M:%S')}")
                    subprocess.run(["shutdown", "/s", "/t", f"{int(remaining_seconds)}"], check=True)
                except subprocess.CalledProcessError as e:
                    if "1190" in str(e):
                        print("A shutdown has already been scheduled.")
                        break  # 이미 예약된 종료가 있으면 반복 종료
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(120)  # 다음 체크까지 2분 대기

if __name__ == "__main__":
    check_and_shutdown()