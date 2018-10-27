from flask import Flask, render_template
from GoatLight import GoatLight

app = Flask(__name__)

goat_light = GoatLight()


@app.route('/')
def hello_world():
    return render_template("goatlight.html")


@app.route('/light_on', methods=['POST'])
def light_on():
    goat_light.turn_on()
    return "ok"


@app.route('/light_off', methods=['POST'])
def light_off():
    goat_light.turn_off()
    return "ok"


if __name__ == '__main__':
    app.run()
