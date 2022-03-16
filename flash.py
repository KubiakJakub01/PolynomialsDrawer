from flask import Flask, render_template
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from wielomian import Wielomian
from flask import request
from flask import redirect, session

app = Flask(__name__)

app.secret_key = 'qwerty'


@app.route('/')
def input():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def input_post():
    stopien = request.form['stopien']
    x_min = request.form['x_min']
    x_max = request.form['x_max']
    stopien = int(stopien)
    session['stopien'] = stopien
    session['x_min'] = int(x_min)
    session['x_max'] = int(x_max)
    session['wspolczyniki_zmienne'] = [('x^'+ str(x)) for x in range(0,stopien+1)]
    return redirect('input_2')

@app.route('/input_2', methods=['GET'])
def input_2():
    wspolczyniki_zmienne = session.get('wspolczyniki_zmienne')
    return render_template('input_2.html', wspolczyniki_zmienne=wspolczyniki_zmienne)

@app.route('/input_2', methods=['POST'])
def input_2_post():
    wspolczyniki = []
    w = session.get('wspolczyniki_zmienne')
    for x in w:
        wspolczyniki.insert(0,float(request.form[x]))

    session['wspolczyniki'] = wspolczyniki

    return redirect('plot')

@app.route('/plot')
def plot_png():
    wielomian = Wielomian(session.get('wspolczyniki'), session.get('x_min'), session.get('x_max'))
    #wielomian = Wielomian([2,-3,-1],-3,3)
    fig = wielomian.plot()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run()