# Archivo para pruebas de pytest
# Importamos el método que queremos probar (add)
# La prueba de pytest se puede realizar con el comando 'python -m pytest -v'
# También se puede iniciar con 'pytest - v' o 'pytest'
from add import add
from add import sum_lista


def test_add():
    resultado = add(1, 3)
    assert (
        resultado == 4
    )  # Si le sustituyo el valor por un incorrecto (5) me da un error


# Creamos otro método para probar con pytest sum_lista
def test_sumalista():
    lista1 = []
    lista2 = [1, 89]
    resultado = sum_lista(lista2)
    assert resultado == 90


# IMPORTANTE -> NO SE PUEDE TESTEAR UN MÉTODO QUE NO RETORNA NADA
# Osea que el método DEBE finalizar con un return y no con un print
