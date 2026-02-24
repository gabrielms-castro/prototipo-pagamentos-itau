from src.config import PV, TOKEN
from src.entities.environment import Environment
from src.entities.store import Store
from src.entities.erede import eRede


def main():
    store = Store(PV, TOKEN, Environment.sandbox())

    access_token = eRede(store).get_access_token()
    print(access_token)



if __name__ == "__main__":
    main()