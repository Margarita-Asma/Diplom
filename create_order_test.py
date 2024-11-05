# Маргарита Кулишова, 23-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def positive_assert(track):
    get_order_response = sender_stand_request.get_order(track)

    assert get_order_response.status_code == 200

def test_get_order():
    order_body = data.order_body
    create_order_response = sender_stand_request.post_new_order(order_body)
    track = create_order_response.json()["track"]

    positive_assert(track)