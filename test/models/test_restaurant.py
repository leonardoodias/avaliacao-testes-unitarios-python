from src.models.restaurant import Restaurant
import pytest

def test_describe_restaurant():
    # Validação: Descrição do restaurante
    # Preparação dos dados de teste
    restaurant_name = "La Pizzaria"
    cuisine_type = "Pizza"
    expected_output = f"Esse restaurante chama-se {restaurant_name} e serve {cuisine_type}. Atendeu 0 clientes desde que abriu."

    # Instanciação do objeto de restaurante
    restaurant = Restaurant(restaurant_name, cuisine_type)

    # Chamada do método de teste
    result = restaurant.describe_restaurant()

    # Verificação do resultado
    assert expected_output == result


def test_open_restaurant():
    # Validação: Abrir restaurante
    # Preparação dos dados de teste
    restaurant_name = "Mix Restaurante"
    cuisine_type = "Cozinha Variada"

    # Instanciação do objeto de restaurante
    restaurant = Restaurant(restaurant_name, cuisine_type)

    # Chamada do método de teste
    restaurant.open_restaurant()

    # Verificação do estado do restaurante
    assert restaurant.open
    assert restaurant.number_served == 0


def test_open_restaurant_when_already_open():
    # Validação: Abrir restaurante quando já está aberto
    # Preparação dos dados de teste
    restaurant_name = "TremBão Restaurante"
    cuisine_type = "Cozinha Variada"

    # Instanciação do objeto de restaurante
    restaurant = Restaurant(restaurant_name, cuisine_type)

    # Chamada do método de teste
    restaurant.open_restaurant()

    # Verificação do estado do restaurante
    assert restaurant.open
    assert restaurant.number_served == 0


def test_close_restaurant():
    # Validação: Fechar restaurante
    # Preparação dos dados de teste
    restaurant_name = "Trembão Restaurante"
    cuisine_type = "Cozinha Variada"

    # Instanciação do objeto de restaurante
    restaurant = Restaurant(restaurant_name, cuisine_type)

    # Chamada do método de teste
    restaurant.close_restaurant()

    # Verificação do estado do restaurante
    assert not restaurant.open
    assert restaurant.number_served == 0


def test_close_restaurant_when_already_closed():
    # Validação: Fechar restaurante quando já está fechado
    # Preparação dos dados de teste
    restaurant_name = "Trembão Restaurante"
    cuisine_type = "Cozinha Variada"

    # Instanciação do objeto de restaurante
    restaurant = Restaurant(restaurant_name, cuisine_type)

    # Fechando o restaurante
    restaurant.close_restaurant()

    # Chamada do método de teste quando o restaurante já está fechado
    restaurant.close_restaurant()

    # Verificação do estado do restaurante
    assert not restaurant.open
    assert restaurant.number_served == 0


def test_set_number_served():
    # Validação: Definir número de clientes atendidos
    # Preparação dos dados de teste
    restaurant_name = "Trembão Restaurante"
    cuisine_type = "Cozinha Variada"

    # Instanciação do objeto de restaurante
    restaurant = Restaurant(restaurant_name, cuisine_type)

    # Chamada do método de teste
    restaurant.set_number_served(10)

    # Verificação do número de clientes atendidos
    assert restaurant.number_served == 10


def test_set_number_served_invalid_when_open():
    # Validação: Definir número de clientes atendidos inválido quando o restaurante está aberto
    # Preparação dos dados de teste
    restaurant_name = "Trembão Restaurante"
    cuisine_type = "Cozinha Variada"

    # Instanciação do objeto de restaurante
    restaurant = Restaurant(restaurant_name, cuisine_type)

    # Chamada do método de teste com número de clientes atendidos negativo quando o restaurante está aberto
    restaurant.set_number_served(-10)

    # Verificação do número de clientes atendidos
    assert restaurant.number_served == 0


def test_increment_number_served():
    # Validação: Incrementar número de clientes atendidos
    # Preparação dos dados de teste
    restaurant_name = "Trembão Restaurante"
    cuisine_type = "Cozinha Variada"

    # Instanciação do objeto de restaurante
    restaurant = Restaurant(restaurant_name, cuisine_type)

    # Abre o restaurante para permitir o incremento do número de clientes atendidos
    restaurant.open_restaurant()

    # Chamada do método de teste
    restaurant.increment_number_served(5)

    # Verificação do número de clientes atendidos
    assert restaurant.number_served == 5


def test_increment_number_served_exceed_capacity():
    # Validação: Incrementar número de clientes atendidos que excede a capacidade máxima
    # Preparação dos dados de teste
    restaurant_name = "Trembão Restaurante"
    cuisine_type = "Cozinha Variada"

    # Instanciação do objeto de restaurante
    restaurant = Restaurant(restaurant_name, cuisine_type)

    # Abre o restaurante para permitir o incremento do número de clientes atendidos
    restaurant.open_restaurant()

    # Obtendo o número de clientes atendidos antes do incremento
    previous_number_served = restaurant.number_served

    # Chamada do método de teste com número de clientes atendidos que excede a capacidade máxima
    restaurant.increment_number_served(1000)

    # Verificação do número de clientes atendidos
    assert restaurant.number_served == previous_number_served + 1000


def test_increment_number_served_when_closed():
    # Validação: Incrementar número de clientes atendidos quando o restaurante está fechado
    # Preparação dos dados de teste
    restaurant_name = "Trembão Restaurante"
    cuisine_type = "Cozinha Variada"

    # Instanciação do objeto de restaurante
    restaurant = Restaurant(restaurant_name, cuisine_type)

    # Fechando o restaurante
    restaurant.close_restaurant()

    # Obtendo o número de clientes atendidos antes do incremento
    previous_number_served = restaurant.number_served

    # Chamada do método de teste quando o restaurante está fechado
    restaurant.increment_number_served(10)

    # Verificação do número de clientes atendidos
    assert restaurant.number_served == previous_number_served


def test_increment_number_served_negative():
    # Validação: Incrementar número de clientes atendidos com valor negativo
    # Preparação dos dados de teste
    restaurant_name = "Trembão Restaurante"
    cuisine_type = "Cozinha Variada"

    # Instanciação do objeto de restaurante
    restaurant = Restaurant(restaurant_name, cuisine_type)

    # Abre o restaurante para permitir o incremento do número de clientes atendidos
    restaurant.open_restaurant()

    # Chamada do método de teste com número de clientes atendidos negativo
    restaurant.increment_number_served(-5)

    # Verificação do número de clientes atendidos
    assert restaurant.number_served == 0


def test_increment_number_served_invalid_when_closed():
    # Validação: Incrementar número de clientes atendidos inválido quando o restaurante está fechado
    # Preparação dos dados de teste
    restaurant_name = "Trembão Restaurante"
    cuisine_type = "Cozinha Variada"

    # Instanciação do objeto de restaurante
    restaurant = Restaurant(restaurant_name, cuisine_type)

    # Fechando o restaurante
    restaurant.close_restaurant()

    # Chamada do método de teste para incrementar o número de clientes atendidos quando o restaurante está fechado
    restaurant.increment_number_served(5)

    # Verificação do número de clientes atendidos
    assert restaurant.number_served == 0
