from flask import Flask, request, jsonify, render_template
from bike_rental.pipeline.prediction import PredictionPipeline

app = Flask(__name__)
pipeline = PredictionPipeline()

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON input
        data = request.json

        # Make prediction
        prediction = pipeline.predict(data)

        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
