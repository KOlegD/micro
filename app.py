import os

from flask import Flask, request, jsonify
import pickle as p

app = Flask(__name__)
# modelfile = 'knnpickle_file'
# model = p.load(open(modelfile, 'rb'))


@app.route('/', methods=['POST'])
def makecalc():
    # data = request.get_json()
    # prediction = model.predict(data)
    # flower = ['Setosa', 'Versicolor', 'Virginica']
    prediction ='234'
        # flower[int(prediction)]
    return jsonify(prediction)


if __name__ == '__main__':
    # app.run(port=5000, host='127.0.0.1')
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
