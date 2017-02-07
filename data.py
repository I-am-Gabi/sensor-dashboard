import time, requests
from random import randint

# http://smartmetropolis-dashboard.herokuapp.com/update
def run():
    r = requests.post("http://localhost:5000/update",
                      data={'sensor1': randint(1, 100), 'sensor2': randint(1, 100), 'sensor3': randint(1, 100),
                            'sensor4': randint(1, 100)})
    print(r.status_code, r.reason)


if __name__ == "__main__":
    while True:
        run()
        time.sleep(5)
