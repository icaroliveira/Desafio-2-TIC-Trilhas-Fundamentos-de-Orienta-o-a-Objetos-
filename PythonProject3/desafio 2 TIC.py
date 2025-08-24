class Mouse:
    """
    Representa um mouse com cor e quantidade de botões.
    Os atributos são acessados através de properties.
    """
    def __init__(self, cor, qtd_botoes):
        """
        Construtor da classe Mouse.

        Args:
            cor (str): A cor do mouse.
            qtd_botoes (int): A quantidade de botões do mouse.
        """
        # Atributos privados, por convenção, iniciam com um underscore (_)
        self._cor = cor
        self._qtd_botoes = qtd_botoes

    # --- Getter e Setter para o atributo 'cor' ---

    @property
    def cor(self):
        """Este é o método GETTER para a cor."""
        print(f"Acessando a cor: '{self._cor}'")
        return self._cor

    @cor.setter
    def cor(self, nova_cor):
        """Este é o método SETTER para a cor."""
        print(f"Alterando a cor de '{self._cor}' para '{nova_cor}'")
        self._cor = nova_cor

    # --- Getter e Setter para o atributo 'qtd_botoes' ---

    @property
    def qtd_botoes(self):
        """Este é o método GETTER para a quantidade de botões."""
        print(f"Acessando a quantidade de botões: {self._qtd_botoes}")
        return self._qtd_botoes

    @qtd_botoes.setter
    def qtd_botoes(self, novo_valor):
        """Este é o método SETTER para a quantidade de botões."""
        # Podemos adicionar validações no setter, uma de suas grandes vantagens
        if isinstance(novo_valor, int) and novo_valor > 0:
            print(f"Alterando a quantidade de botões de {self._qtd_botoes} para {novo_valor}")
            self._qtd_botoes = novo_valor
        else:
            print("Erro: A quantidade de botões deve ser um número inteiro e positivo.")

# --- Exemplo de Utilização da Classe ---

# 1. Criando uma instância (objeto) da classe Mouse
print("--- Criando o objeto 'mouse_gamer' ---")
mouse_gamer = Mouse(cor="Preto", qtd_botoes=6)
print("-" * 20)

# 2. Acessando os atributos usando os getters (@property)
# Note que você acessa como se fosse um atributo público, mas o método getter é chamado por trás.
print("\n--- Acessando os valores iniciais (getters) ---")
cor_atual = mouse_gamer.cor
botoes_atuais = mouse_gamer.qtd_botoes
print("-" * 20)


# 3. Alterando os atributos usando os setters (@<nome>.setter)
# Note que você atribui um novo valor como se fosse um atributo público,
# mas o método setter é chamado.
print("\n--- Alterando os valores (setters) ---")
mouse_gamer.cor = "Branco com RGB"
mouse_gamer.qtd_botoes = 7
print("-" * 20)


# 4. Verificando os novos valores
print("\n--- Verificando os valores alterados ---")
mouse_gamer.cor
mouse_gamer.qtd_botoes
print("-" * 20)

# 5. Testando a validação do setter de qtd_botoes
print("\n--- Testando a validação do setter ---")
mouse_gamer.qtd_botoes = -2 # Tentando atribuir um valor inválido
print(f"Valor final de botões (não foi alterado): {mouse_gamer._qtd_botoes}")
print("-" * 20)