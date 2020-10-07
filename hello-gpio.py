from flask import Flask, render_template  # 플라스크 라이브러리 불러오기
import datetime      
import RPi.GPIO as GPIO                     # 시간 라이브러리
app = Flask(__name__)                     # 플라스크 객체 만들기

GPIO.setmode(GIPO.BCM) #BCM 모드

@app.route("/")   # <변수>
def hello(): 
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M")
    templateData = {   #딕션너리 변수
        'title' : "안녕하세요!", 
        'time' : time
    }
    return render_template('main.html', **templateData) # 딕셔너리 안에 있는 templateData 변수를 전달
#    return render_template('index.html', name = username)

@app.route("/<pin>") # <변수>
def readPin():
    try:
        GPIC.setup(int(pin), GPIO.IN)
        if GPIO.input(int(pin)) == True:
            response = "핀 넘버"+pin+"은 HIGH"
        else:
            response = "핀 넘버"+pin+"은 LOW"
    except:
        response = "핀을 읽는데 문제가 있음"+pin+"번 핀"
    templateData = {
        'pin' : "핀상태" + pin,
        'response' : response
    }             
    return render_template('pin.html', **templataDate)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

