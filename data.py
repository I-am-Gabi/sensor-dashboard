import time, requests
from random import randint


def run():
    r = requests.post("http://smartmetropolis-dashboard.herokuapp.com/update",
                      data={'sensor1': randint(1, 100), 'sensor2': randint(1, 100), 'sensor3': randint(1, 100),
                            'sensor4': randint(1, 100)})
    print(r.status_code, r.reason)


if __name__ == "__main__":
    while True:
        run()
        time.sleep(5)
