import os
from flask import Flask, render_template, request
from src.pipeline.model_prediction_pipeline import PredictionPipeline

# First train the model
# try:
#     # run the command
#     os.system("python main.py")
# except Exception as e:
#     print("Training failed, Not done.")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        predictor = PredictionPipeline(text)
        label = predictor.predict_label()  
        if label == 1:
            label = "Large Language Model"
        elif label == 0:
            label = "Human"
        return render_template('index.html', result=label)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
