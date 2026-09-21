def test_set_token_adds_header(api):
    api.set_token("secret123")
    assert api.session.headers["Authorization"] == "Bearer secret123"