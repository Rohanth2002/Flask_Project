from flask import Flask, request, jsonify

server = Flask(__name__)

tweets = [
    {"tweet_id": 1, "content": "This is tweet 1"},
    {"tweet_id": 2, "content": "Another tweet here"},
]

@server.route('/tweet/<int:id>', methods=['GET'])
def retrieve_tweet(id):
    tweet = next((item for item in tweets if item['tweet_id'] == id), None)
    if tweet:
        return jsonify(tweet)
    else:
        return jsonify({"error": "Tweet not found"}), 404

@server.route('/add_tweet', methods=['POST'])
def add_tweet():
    try:
        new_content = request.get_json()
        if 'content' not in new_content:
            return jsonify({"error": "Missing content"}), 400

        new_id = len(tweets) + 1
        tweets.append({"tweet_id": new_id, "content": new_content['content']})

        return jsonify({"message": "New tweet added successfully"}), 201

    except Exception as error:
        return jsonify({"error": str(error)}), 400

if __name__ == "__main__":
    server.run(debug=True)
