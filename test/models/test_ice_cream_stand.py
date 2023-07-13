from src.models.ice_cream_stand import IceCreamStand

def test_flavors_available_empty():
    """Testa se a mensagem correta é exibida quando a lista de sabores está vazia."""
    ice_cream_stand = IceCreamStand("Sorveteria", "Sorvetes", [])
    assert ice_cream_stand.flavors_available() == None

def test_flavors_available():
    """Testa se a lista de sabores é exibida corretamente."""
    flavors = ["Chocolate", "Morango", "Baunilha"]
    ice_cream_stand = IceCreamStand("Sorveteria", "Sorvetes", flavors)
    expected_output = "\nNo momento temos os seguintes sabores de sorvete disponíveis:\n\t- Chocolate\n\t- Morango\n\t- Baunilha"
    assert ice_cream_stand.flavors_available() == None

def test_find_flavor_available():
    """Testa se o sabor disponível é encontrado corretamente."""
    flavors = ["Chocolate", "Morango", "Baunilha"]
    ice_cream_stand = IceCreamStand("Sorveteria", "Sorvetes", flavors)
    assert ice_cream_stand.find_flavor("Chocolate") == None

def test_find_flavor_not_available():
    """Testa se o sabor não disponível não é encontrado."""
    flavors = ["Chocolate", "Morango", "Baunilha"]
    ice_cream_stand = IceCreamStand("Sorveteria", "Sorvetes", flavors)
    assert ice_cream_stand.find_flavor("Coco") == None

def test_add_flavor_already_available():
    """Testa se o sabor já disponível não é adicionado novamente."""
    flavors = ["Chocolate", "Morango", "Baunilha"]
    ice_cream_stand = IceCreamStand("Sorveteria", "Sorvetes", flavors)
    assert ice_cream_stand.add_flavor("Chocolate") == None

def test_add_flavor_new():
    """Testa se um novo sabor é adicionado corretamente."""
    flavors = ["Chocolate", "Morango", "Baunilha"]
    ice_cream_stand = IceCreamStand("Sorveteria", "Sorvetes", flavors)
    ice_cream_stand.add_flavor("Coco")
    assert "Coco" in ice_cream_stand.flavors

def test_add_flavor_multiple_new():
    """
    Testa se múltiplos sabores novos são adicionados corretamente.
    """
    flavors = ["Chocolate", "Morango", "Baunilha"]
    ice_cream_stand = IceCreamStand("Sorveteria", "Sorvetes", flavors)
    ice_cream_stand.add_flavor("Coco")
    ice_cream_stand.add_flavor("Limão")
    assert "Coco" in ice_cream_stand.flavors
    assert "Limão" in ice_cream_stand.flavors

