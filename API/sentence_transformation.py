from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Load the model (this can take some time)
model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route('/embeddings', methods=['POST'])
def get_embeddings():
    # Get the data from the POST request.
    data = request.get_json()

    if not data or 'sentences' not in data:
        return jsonify({'error': 'No sentences provided'}), 400

    # Get the list of sentences from the request's body
    sentences = data['sentences']

    # Check if the input is valid
    if not isinstance(sentences, list):
        return jsonify({'error': 'Sentences should be a list'}), 400

    # Generate embeddings
    embeddings = model.encode(sentences)

    # Convert embeddings to list of lists (as numpy arrays are not JSON serializable)
    embeddings_list = embeddings.tolist()

    # Return the embeddings as a JSON object
    return jsonify({'embeddings': embeddings_list})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)