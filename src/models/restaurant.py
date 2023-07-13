class Restaurant:
    """Modelo de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = True  # Correção: Alterado de False para True para indicar que o restaurante está aberto.

    def describe_restaurant(self):
        """Retorna uma descrição simples da instância do restaurante."""
        # Correção: Aprimorado para retornar a descrição em vez de imprimir diretamente.
        description = f"Esse restaurante chama-se {self.restaurant_name} e serve {self.cuisine_type}."
        description += f" Atendeu {self.number_served} clientes desde que abriu."
        return description

    def open_restaurant(self):
        """Imprime uma mensagem indicando que o restaurante está aberto para negócios.
        O atributo open é definido como False no construtor, mas no método open_restaurant ele é alterado para True caso o restaurante não esteja aberto.
        Essa lógica parece inversa. O valor padrão do atributo open deve ser True e ser alterado para False quando o restaurante estiver fechado."""

        if not self.open:
            self.open = True  # Correção para exibir corretamente o status do restaurante de False para True.
            self.number_served = 0  # Correção: Alterado de -2 para 0 para reiniciar o contador de clientes.
            print(f"{self.restaurant_name} está agora aberto!")  # Correção da mensagem de exibição.
        else:
            print(f"{self.restaurant_name} já está aberto!")

    def close_restaurant(self):
        """Imprime uma mensagem indicando que o restaurante está fechado para negócios."""

        if self.open:
            self.open = False
            self.number_served = 0
            print(f"{self.restaurant_name} está agora fechado!")  # Correção da mensagem de exibição.
        else:
            print(f"{self.restaurant_name} já está fechado!")

    def set_number_served(self, total_customers):
        """Define o número total de pessoas atendidas por este restaurante até o momento."""
        """Adicionado verificação para garantir que o número de clientes atendidos seja maior ou igual a zero."""
        """Caso contrário, o número de clientes atendidos não pode ser negativo."""

        if self.open:
            if total_customers >= 0:
                self.number_served = total_customers
            else:
                print("O número de clientes atendidos não pode ser negativo.")
        else:
            print(f"{self.restaurant_name} está fechado!")

    def increment_number_served(self, more_customers):
        """Aumenta o número total de clientes atendidos por este restaurante.
        Correção da atribuição self.number_served = more_customers para self.number_served += more_customers para incrementar corretamente o número de clientes atendidos.
        Adicionado verificação para garantir que o número de clientes atendidos seja maior ou igual ao número atual de clientes atendidos."""

        if self.open:
            if more_customers >= 0:
                self.number_served += more_customers
            else:
                print("O número de clientes atendidos não pode ser menor que o número atual.")
        else:
            print(f"{self.restaurant_name} está fechado!")
