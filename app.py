from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('Medical_file.pkl', 'rb'))


@app.route('/', methods=['GET', 'POST'])
def homepage():
  return render_template('prediction.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    features = [x for x in request.form.values()]
    features1 = features[1:6]

    features1[0] = int(features1[0])
    features1[4] = float(features1[4])
    
    
    print(features)
    print(features1)
    
    if features1[1] == 'M':
      features1[1] = 1
    else:
      features1[1] = 0

    if features1[2] == 'HIGH':
      features1[2] = 0
    elif features1[2] == 'LOW':
      features1[2] = 1
    else:
      features1[2] = 2

    if features1[3] == 'HIGH':
      features1[3] = 0
    else:
      features1[3] = 1
    print(features1)
    
    prediction = model.predict([features1])
    output = prediction[0]
    
    if output == 0:
      output = 'drugA'
    elif output == 1:
      output = 'drugB'
    elif output == 2:
      output = 'drugC'
    elif output == 3:
      output = 'drugX'
    else:
      output = 'drugY'
  
    return render_template('prediction.html', prediction_text='The medicine he should take is {}'.format(output))

if __name__ == '__main__':
  app.run(port = 8000)