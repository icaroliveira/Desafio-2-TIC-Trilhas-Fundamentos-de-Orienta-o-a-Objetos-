# Modelagem de Classes: Copo e Copo_com_canudo em Python

Este projeto simples em Python demonstra os conceitos de Programação Orientada a Objetos (POO), incluindo a criação de classes, atributos, métodos e herança.

## 📝 Descrição do Projeto

O objetivo é modelar duas classes:

* **`Copo`**: Uma classe base que representa um copo com uma capacidade específica em mililitros (ml).
* **`Copo_com_canudo`**: Uma classe derivada que herda de `Copo` e adiciona a característica de um canudo colorido.

## ✨ Funcionalidades

### Classe `Copo`

#### Atributos
* `capacidade`: (int) A capacidade máxima do copo em ml.

#### Métodos
* `__init__(self, capacidade)`: Construtor que define a capacidade do copo.
* `encher(self, volume)`: Tenta preencher o copo com um determinado volume. Se o volume exceder a capacidade, exibe uma mensagem de erro.

### Classe `Copo_com_canudo`

#### Herança
* Herda todos os atributos e métodos da classe `Copo`.

#### Atributos Adicionais
* `cor_do_canudo`: (str) A cor do canudo do copo.

#### Métodos
* `__init__(self, capacidade, cor_do_canudo)`: Construtor que inicializa tanto a `capacidade` (usando o construtor da classe pai) quanto a `cor_do_canudo`.

## 🚀 Como Usar

Para utilizar as classes, basta importar o arquivo Python em seu projeto ou executá-lo diretamente. O exemplo abaixo demonstra como instanciar objetos de cada classe e testar suas funcionalidades.

```python
# 1. Crie uma instância da classe base 'Copo'
copo_simples = Copo(capacidade=300)

# 2. Use o método 'encher' com um volume válido
copo_simples.encher(200)
# Saída esperada: O copo foi preenchido com 200ml.

# 3. Tente encher com um volume que excede a capacidade
copo_simples.encher(350)
# Saída esperada: Este volume excede a capacidade do copo.

# 4. Crie uma instância da classe derivada 'Copo_com_canudo'
copo_divertido = Copo_com_canudo(capacidade=200, cor_do_canudo="Verde")

# 5. Acesse os atributos de ambas as classes (pai e filha)
print(f"Capacidade: {copo_divertido.capacidade}ml")
print(f"Cor do Canudo: {copo_divertido.cor_do_canudo}")

# 6. Teste o método herdado 'encher'
copo_divertido.encher(250)
# Saída esperada: Este volume excede a capacidade do copo.
```

## ⚙️ Executando o Código de Teste

O arquivo principal já inclui um bloco de teste para validar a implementação. Ao executar o script, você verá a seguinte saída:

```
--- Testando a classe Copo ---
Copo 1 criado com capacidade de 250ml.
O copo foi preenchido com 100ml.
Este volume excede a capacidade do copo.

==============================

--- Testando a classe Copo_com_canudo ---
Copo 2 criado com capacidade de 200ml e canudo da cor Azul.
O copo foi preenchido com 150ml.
Este volume excede a capacidade do copo.
```

