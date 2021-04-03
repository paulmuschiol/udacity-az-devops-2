import requests
import numpy as np

PORT = '5000'


def test_prediction():
    r = requests.post('http://localhost:{}/predict'.format(PORT), json={
        'CHAS': {'0': 0},
        'RM': {'0': 6.575},
        'TAX': {'0': 296.0},
        'PTRATIO': {'0': 15.3},
        'B': {'0': 396.9},
        'LSTAT': {'0': 4.98},
        })
    prediction = r.json()['prediction'][0]
    print(prediction)
    np.testing.assert_almost_equal(prediction, 20.353731, decimal=3)


if __name__ == '__main__':
    test_prediction()
