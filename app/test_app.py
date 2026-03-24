from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_browse():
    client = app.test_client()
    response = client.get("/browse")
    assert response.status_code == 200


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "OK"


def test_info():
    client = app.test_client()
    response = client.get("/info")
    assert response.status_code == 200
    data = response.get_json()
    assert data["project"] == "SoundWave DevOps Cloud Project"


def test_api_playlists():
    client = app.test_client()
    response = client.get("/api/playlists")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "title" in data[0]


def test_api_albums():
    client = app.test_client()
    response = client.get("/api/albums")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "artist" in data[0]


def test_api_songs():
    client = app.test_client()
    response = client.get("/api/songs")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "title" in data[0]


def test_api_player_playlist():
    client = app.test_client()
    response = client.get("/api/player/playlists/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["title"] == "Chill Vibes"
    assert "audio_url" in data


def test_api_search():
    client = app.test_client()
    response = client.get("/api/search?q=billie")
    assert response.status_code == 200
    data = response.get_json()
    assert "albums" in data
    assert "songs" in data