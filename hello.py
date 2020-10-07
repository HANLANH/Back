from flask import Flask, render_template  #플라스크 라이브러리 불러오기
app = Flask(__name__)    #플라스크 객체 만들기
import datetime  # 시간 라이브러리
#print(__name__)

@app.route("/<username>")   # <변수>
def hello(username = None):  # username값에 아무것도 넣지 않았을때 None을 넣는다
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M")
    templateData = {   #딕션너리 변수 / 변수가 많을시 아래 처럼 여러개의 변수를 지정하여 한번에 처리
        'name' : username, 
        'time' : time
    }
    return render_template('index.html', **templateData) # 딕셔너리 안에 있는 templateData 변수를 전달
#    return render_template('index.html', name = username)
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return "블로그 입니다!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

