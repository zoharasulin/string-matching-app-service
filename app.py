

from flask import Flask, request, render_template

from func_string_matching import StringMatching

 

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

 

@app.route('/string-matching', methods=['GET', 'POST'])

def string_matching():

    if request.method == 'POST':

        try:

            input1 = request.form['input1']

            input2 = request.form['input2']

            print(f"received:imput1={input1},input2={input2}")

            result = StringMatching(input1, input2)

            return render_template('result.html', result=result)

        except:

            return render_template('error.html', message="invalid request error")

    else:

        # Handle GET request (optional)

        return render_template('index.html')

 

@app.route('/string-matching/health-check')

def health():

    return 'OK'

 

if __name__ == '__main__':

    app.run(debug=True, port=5000)
