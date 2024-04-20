from flask import Flask, render_template, request
import re
from Logics import find_information

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("MainWebLayout.html")


@app.route('/', methods=['post', 'get'])
def info():
    phone_number = ''
    operator = ''
    region = ''
    inn = ''
    error = ''

    if request.method == 'POST':

        telephone = request.form.get('input')
        telephone_mask = re.compile("89[0-9]{9}")

        if telephone_mask.match(telephone):

            phone_number = telephone
            info_list = find_information(telephone)

            if info_list != 0:

                operator = info_list[0] if len(info_list[0]) > 1 else "-------"

                if len(info_list[2]) > 1:
                    region = info_list[2]
                elif len(info_list[1]) > 1:
                    region = info_list[1]
                else:
                    region = "-------"

                inn = info_list[3] if len(info_list[3]) > 1 else "-------"

            else:
                error = 'Такого номера телефона не существует! Попробуйте еще раз.'

        else:
            error = 'Неправильно введен номер телефона. Попробуйте еще раз.'

    return render_template('MainWebLayout.html', number=phone_number, operator=operator, region=region, inn=inn,
                           error=error)


if __name__ == "__main__":
    app.run(debug=True)