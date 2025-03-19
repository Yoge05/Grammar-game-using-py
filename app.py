from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='../frontend')
CORS(app)

# Simple stories data
stories = [
    # Level 1 - Basic Grammar
    {
        "id": 1,
        "level": 1,
        "title": "The Magic Garden 🌸",
        "text": "Once upon a time, there was a beautiful garden where flowers danced in the wind. The garden was magical, and it's flowers could talk.",
        "errors": [
            {"original": "where flowers", "corrected": "where the flowers"},
            {"original": "it's", "corrected": "its"}
        ]
    },
    # Level 2 - Multiple Error Types
    {
        "id": 2,
        "level": 2,
        "title": "The Clever Fox 🦊",
        "text": "The fox were very clever. He seen a crow with cheese in it's beak. The crow were sitting in they're tree.",
        "errors": [
            {"original": "were", "corrected": "was"},
            {"original": "seen", "corrected": "saw"},
            {"original": "it's", "corrected": "its"},
            {"original": "they're", "corrected": "their"}
        ]
    },
    # Level 3 - Complex Sentences
    {
        "id": 3,
        "level": 3,
        "title": "Space Mission 🚀",
        "text": "Despite the astronauts extensive training, they wasn't prepared for what they discovered. The alien artifact, which were floating in space, emitted strange signals, but none of the crew was able to decoded them. Each of the team members have tried they're best to understand it's purpose.",
        "errors": [
            {"original": "astronauts extensive", "corrected": "astronauts' extensive"},
            {"original": "wasn't", "corrected": "weren't"},
            {"original": "were floating", "corrected": "was floating"},
            {"original": "decoded", "corrected": "decode"},
            {"original": "have tried", "corrected": "had tried"},
            {"original": "they're", "corrected": "their"},
            {"original": "it's", "corrected": "its"}
        ]
    },
    # Level 4 - Advanced Grammar
    {
        "id": 4,
        "level": 4,
        "title": "Time Travel Mystery 🕰️",
        "text": "The scientist whom developed the time machine have made several mistakes in their calculations. If they would have checked more carefully, they might of prevented the paradox. Neither the equipment or the backup systems was functioning properly, and everyone except the lead researcher were unable to understood what went wrong.",
        "errors": [
            {"original": "whom developed", "corrected": "who developed"},
            {"original": "have made", "corrected": "had made"},
            {"original": "would have", "corrected": "had"},
            {"original": "might of", "corrected": "might have"},
            {"original": "or", "corrected": "nor"},
            {"original": "was functioning", "corrected": "were functioning"},
            {"original": "were unable", "corrected": "was unable"},
            {"original": "understood", "corrected": "understand"}
        ]
    },
    # Level 5 - Expert Challenge
    {
        "id": 5,
        "level": 5,
        "title": "Literary Conference 📚",
        "text": "The panel of experts, along with the keynote speaker, were scheduled to arrive the next day, but neither of them have confirmed their attendance yet. The manuscripts, which the committee is reviewing, needs to be properly catalogued, and its essential that each document are handled with care. The data suggests that many of the texts dates back to ancient times, and every one of these manuscripts require special preservation techniques.",
        "errors": [
            {"original": "were scheduled", "corrected": "was scheduled"},
            {"original": "have confirmed", "corrected": "had confirmed"},
            {"original": "needs", "corrected": "need"},
            {"original": "its essential", "corrected": "it's essential"},
            {"original": "are handled", "corrected": "is handled"},
            {"original": "dates", "corrected": "date"},
            {"original": "require", "corrected": "requires"}
        ]
    }
]

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/stories')
def get_stories():
    return jsonify(stories)

if __name__ == '__main__':
    print("\n=== Grammar Quest Game ===")
    print("1. Open http://localhost:5001 in your browser")
    print("2. Click 'Start Game' to begin")
    print("3. Press Ctrl+C to stop the server")
    print("========================\n")
    app.run(port=5001, debug=True) 