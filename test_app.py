import pytest
from app import app

@pytest.fixture
def client():
    """Crea un cliente de prueba para la aplicación Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """
    Test 1: Verifica que la página principal responda con status 200
    """
    response = client.get('/')
    assert response.status_code == 200, "La página principal debe retornar código 200"

def test_home_page_content(client):
    """
    Test 2: Verifica que el contenido de la página sea correcto
    """
    response = client.get('/')
    assert b"Hola Mundo desde Flask" in response.data, "El contenido debe incluir el mensaje de bienvenida"

def test_response_type(client):
    """
    Test 3: Verifica que el tipo de contenido sea text/html
    """
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8', "El tipo de contenido debe ser HTML"

def test_404_error(client):
    """
    Test 4: Verifica que las rutas no existentes retornen 404
    """
    response = client.get('/ruta-inexistente')
    assert response.status_code == 404, "Las rutas no existentes deben retornar código 404"

def test_method_not_allowed(client):
    """
    Test 5: Verifica que métodos no permitidos retornen error adecuado
    """
    response = client.post('/')
    assert response.status_code == 405, "POST en la ruta principal debe retornar 405 (Method Not Allowed)"

def test_app_configuration():
    """
    Test 6: Verifica que la aplicación esté configurada correctamente
    """
    assert app is not None, "La aplicación Flask debe estar inicializada"
    assert app.name == 'app', "El nombre de la aplicación debe ser 'app'"

def test_response_not_empty(client):
    """
    Test 7: Verifica que la respuesta no esté vacía
    """
    response = client.get('/')
    assert len(response.data) > 0, "La respuesta no debe estar vacía"

def test_utf8_encoding(client):
    """
    Test 8: Verifica que la respuesta soporte caracteres UTF-8 (español)
    """
    response = client.get('/')
    text = response.data.decode('utf-8')
    assert '¡' in text and 'ó' in text, "Debe soportar caracteres especiales del español"