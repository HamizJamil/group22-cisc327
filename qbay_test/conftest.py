import os


def pytest_sessionstart():
    print('INITIALIZING ENVIRONMENT..')
    db_file = 'db.sqlite'
    if os.path.exists(db_file):
        os.remove(db_file)


def pytest_sessionfinish():
    pass