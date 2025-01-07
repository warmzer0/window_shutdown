# window_shutdown
윈도우 컴퓨터 종료 프로그램

• **기능:** 

동일 루트에 저장된 텍스트 파일에 저장된 시간을 읽어, 해당 시간에 윈도우 PC를 종료하는 프로그램(텍스트 파일을 읽는 주기는 2분)

윈도우 환경이고  GUI가 없는 Daemon 형태의 프로그램

<.py를 .exe로 변환 방법>

1. pyinstaller 설치

pip install pyinstaller

1. 실행파일 만들기

( 1번째 경우 - 터미널창 숨기지 않고 실행 ) 

pyinstaller --onefile windows_shutdown.py

( 2번째 경우 - 터미널창 숨겨서 실행 ) 

pyinstaller --noconsole --onefile windows_shutdown.py
