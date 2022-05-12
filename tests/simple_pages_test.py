"""
This tests the homepage and extra information pages on the nav bar
"""


def test_index(client):
    """ This ensures that the Index page gets the correct HTML response of status code 200 """
    response = client.get("/")
    assert response.status_code == 200


def test_git_page(client):
    """ This ensures that the Git page gets the correct HTML response of status code 200 """
    response = client.get("/page1")
    assert response.status_code == 200


def test_docker_page(client):
    """ This ensures that the Docker page gets the correct HTML response of status code 200 """
    response = client.get("/page2")
    assert response.status_code == 200


def test_pnf_page(client):
    """ This ensures that the Python/Flask page gets correct HTML response of status code 200 """
    response = client.get("/page3")
    assert response.status_code == 200


def test_cicd_page(client):
    """ This ensures that the CICD page gets the correct HTML response of status code 200 """
    response = client.get("/page4")
    assert response.status_code == 200


def test_oop_page(client):
    """This ensures that the OOP page gets the correct HTML response of status code 200"""
    response = client.get("/page5")
    assert response.status_code == 200


def test_aaa_page(client):
    """This ensures that the AAA page gets the correct HTML response of status code 200"""
    response = client.get("/page6")
    assert response.status_code == 200


def test_solid_page(client):
    """This ensures that the SOLID page gets the correct HTML response of status code 200"""
    response = client.get("/page7")
    assert response.status_code == 200


def test_pylint_page(client):
    """ This ensures that the Pylint page gets the correct HTML response of status code 200 """
    response = client.get("/page9")
    assert response.status_code == 200
