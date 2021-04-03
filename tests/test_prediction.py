import numpy as np
from app import app
import pytest

PORT = '5000'

@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_prediction(client):
    json_payload = {
        'CHAS': {'0': 0},
        'RM': {'0': 6.575},
        'TAX': {'0': 296.0},
        'PTRATIO': {'0': 15.3},
        'B': {'0': 396.9},
        'LSTAT': {'0': 4.98},
        }
    r = client.post('predict', json=json_payload)
    #r = requests.post('http://localhost:{}/predict'.format(PORT), json=)
    #print(r['prediction'][0])
    prediction = r.get_json()['prediction'][0]
    print(prediction)
    np.testing.assert_almost_equal(prediction, 20.353731, decimal=3)


if __name__ == '__main__':
    test_prediction()
