import serial
import re  # 정규 표현식 사용
import webbrowser  # 웹 브라우저 열기


# 아두이노와 연결된 포트와 속도 설정
arduino = serial.Serial(port='COM14', baudrate=9600, timeout=1)  # 포트 이름은 환경에 맞게 변경

try:
    while True:
        # 아두이노로부터 데이터 읽기
        data = arduino.readline().decode('utf-8').strip()
        if data.startswith("RESULT:"):  # RESULT: 로 시작하는 데이터만 처리
            result = data.split("RESULT: ")[1]  # RESULT: 뒤의 값만 추출
            print(f"받은 데이터: {result}")
            # URL 형식 정리 (정규식으로 URL 추출)
            url_match = re.search(r"https?://[^\s]+", result)  # URL 패턴 매칭
            if url_match:
                url = url_match.group()  # 매칭된 URL 추출
                print(f"추출된 URL: {url}")

                # 웹 브라우저에서 열기
                webbrowser.open(url)
                print("URL을 웹 브라우저에서 열었습니다.")
            else:
                print("URL이 포함되어 있지 않습니다.")
except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    arduino.close()  # 포트 닫기