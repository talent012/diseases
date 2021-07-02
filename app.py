from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model= pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/predict', methods= ['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

if __name__ == '__main__':
        app.run()
