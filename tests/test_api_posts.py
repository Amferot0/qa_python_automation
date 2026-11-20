import allure

@allure.title("Создание поста")
def test_created_post(api):
    create_response = api.create_post({
        "title": "test",
        "body": "body",
        "userId": 1,
    })
    assert create_response.status_code == 201
    assert "id" in create_response.json()


@allure.title("Обновление поста")
def test_update_post(api):
    # Обновляем существующий пост (id=1)
    update_response = api.update_post(1, {
        "id": 1,
        "title": "updated",
        "body": "updated body",
        "userId": 1,
    })
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "updated"