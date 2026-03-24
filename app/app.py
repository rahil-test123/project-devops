from flask import Flask, jsonify, render_template, request, send_from_directory

app = Flask(__name__, template_folder="templates", static_folder="static")


playlists = [
    {
        "id": 1,
        "title": "Chill Vibes",
        "cover": "image/chillvibes.jpg",
        "first_song": "Keep The Rain",
        "audio_url": "/static/audio/keep_the_rain.mp3"
    },
    {
        "id": 2,
        "title": "Focus Mode",
        "cover": "image/focusmode.jpg",
        "first_song": "On The Nature Of Daylight",
        "audio_url": "/static/audio/on_the_nature_of_daylight.mp3"
    },
    {
        "id": 3,
        "title": "Party Time",
        "cover": "image/partytime.jpg",
        "first_song": "Sugar On My Tongue",
        "audio_url": "/static/audio/sugar_on_my_tongue.mp3"
    },
    {
        "id": 4,
        "title": "Late Night",
        "cover": "image/latenight.jpg",
        "first_song": "Male Fantasy",
        "audio_url": "/static/audio/male_fantasy.mp3"
    }
]

albums = [
    {
        "id": 1,
        "title": "Eternal Sunshine",
        "artist": "Ariana Grande",
        "cover": "image/eternalsunshine.jpg",
        "first_song": "intro (end of the world)"
    },
    {
        "id": 2,
        "title": "Happier Than Ever",
        "artist": "Billie Eilish",
        "cover": "image/happierthanever.jpg",
        "first_song": "Getting Older"
    },
    {
        "id": 3,
        "title": "Amir",
        "artist": "Tamino",
        "cover": "image/amir.jpg",
        "first_song": "Habibi"
    },
    {
        "id": 4,
        "title": "Ultraviolence",
        "artist": "Lana Del Rey",
        "cover": "image/ultraviolence.jpg",
        "first_song": "Cruel World"
    }
]

songs = [
    {
        "id": 1,
        "title": "House Song",
        "artist": "Searows",
        "cover": "image/housesong.jpg"
    },
    {
        "id": 2,
        "title": "WILDFLOWER",
        "artist": "Billie Eilish",
        "cover": "image/hitmehard.png"
    },
    {
        "id": 3,
        "title": "i love you",
        "artist": "Billie Eilish",
        "cover": "image/iloveyou.jpg"
    },
    {
        "id": 4,
        "title": "Strangers",
        "artist": "Ethel Cain",
        "cover": "image/strangers.jpg"
    }
]

top_albums = [
    {
        "title": "HIT ME HARD AND SOFT",
        "artist": "Billie Eilish",
        "cover": "image/hitmehard.png"
    },
    {
        "title": "OK Computer",
        "artist": "Radiohead",
        "cover": "image/Okcomputer.png"
    },
    {
        "title": "Good Riddance",
        "artist": "Gracie Abrams",
        "cover": "image/Goodriddance.png"
    }
]

top_artists = [
    {
        "name": "Billie Eilish",
        "genre": "Alternative Pop",
        "cover": "image/billieeilish.png"
    },
    {
        "name": "Deftones",
        "genre": "Alternative Metal",
        "cover": "image/deftones1.jpg"
    },
    {
        "name": "The Beatles",
        "genre": "Rock / Pop Rock",
        "cover": "image/beatles.jpg"
    }
]






@app.route("/")
def home():
    return render_template("index.html")


@app.route("/browse")
def browse():
    return render_template("page1.html")


@app.route("/page1.html")
def browse_legacy():
    return render_template("page1.html")




@app.route("/image/<path:filename>")
def serve_image(filename):
    return send_from_directory("static/image", filename)




@app.route("/api/playlists", methods=["GET"])
def get_playlists():
    return jsonify(playlists)


@app.route("/api/albums", methods=["GET"])
def get_albums():
    return jsonify(albums)


@app.route("/api/songs", methods=["GET"])
def get_songs():
    return jsonify(songs)


@app.route("/api/home", methods=["GET"])
def get_home_data():
    return jsonify({
        "top_albums": top_albums,
        "top_artists": top_artists
    })


@app.route("/api/player/<category>/<int:item_id>", methods=["GET"])
def get_player_item(category, item_id):
    source_map = {
        "playlists": playlists,
        "albums": albums,
        "songs": songs
    }

    if category not in source_map:
        return jsonify({"error": "Invalid category"}), 400

    item = next((x for x in source_map[category] if x["id"] == item_id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    if category == "playlists":
        payload = {
            "title": item["title"],
            "cover": item["cover"],
            "subtitle": item["first_song"],
            "audio_url": item.get("audio_url")
        }
    elif category == "albums":
        payload = {
            "title": item["title"],
            "cover": item["cover"],
            "subtitle": item["first_song"],
            "audio_url": None
        }
    else:  
        payload = {
            "title": item["title"],
            "cover": item["cover"],
            "subtitle": item["artist"],
            "audio_url": None
        }

    return jsonify(payload)


@app.route("/api/search", methods=["GET"])
def search():
    query = request.args.get("q", "").strip().lower()

    if not query:
        return jsonify({
            "query": query,
            "playlists": playlists,
            "albums": albums,
            "songs": songs
        })

    filtered_playlists = [
        p for p in playlists
        if query in p["title"].lower() or query in p["first_song"].lower()
    ]

    filtered_albums = [
        a for a in albums
        if query in a["title"].lower()
        or query in a["artist"].lower()
        or query in a["first_song"].lower()
    ]

    filtered_songs = [
        s for s in songs
        if query in s["title"].lower() or query in s["artist"].lower()
    ]

    return jsonify({
        "query": query,
        "playlists": filtered_playlists,
        "albums": filtered_albums,
        "songs": filtered_songs
    })




@app.route("/health")
def health():
    return jsonify({
        "status": "OK"
    })


@app.route("/info")
def info():
    return jsonify({
        "project": "SoundWave DevOps Cloud Project",
        "version": "2.1-demo",
        "frontend": True,
        "backend": "Flask",
        "features": [
            "Landing page",
            "Browse page",
            "Music playlists",
            "Albums",
            "Songs",
            "Search API",
            "Player API",
            "Audio playback for playlists"
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)