"""
EXERCÍCIOS COM FUNÇÕES

Este arquivo contém 7 exercícios diferentes usando funções em Python.
Cada função tem seu próprio comentário explicativo e interage com o usuário através de inputs.
"""

def comparar_numeros():
    """
    EXERCÍCIO 1: Comparar 2 números (par ou ímpar)
    
    Objetivo: Criar uma função que recebe dois números e verifica se são pares ou ímpares.
    Utiliza variáveis locais dentro da função.
    """
    print("\n=== Comparando Números ===")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    if num1 % 2 == 0 and num2 % 2 == 0:
        return f"Ambos os números {num1} e {num2} são pares"
    elif num1 % 2 != 0 and num2 % 2 != 0:
        return f"Ambos os números {num1} e {num2} são ímpares"
    else:
        return f"O número {num1} é {'par' if num1 % 2 == 0 else 'ímpar'} e o número {num2} é {'par' if num2 % 2 == 0 else 'ímpar'}"

def multiplicar_tres_numeros():
    """
    EXERCÍCIO 2: Multiplicar 3 números
    
    Objetivo: Criar uma função que multiplica três números e retorna o resultado.
    """
    print("\n=== Multiplicando Três Números ===")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    
    resultado = num1 * num2 * num3
    return f"A multiplicação de {num1} x {num2} x {num3} = {resultado}"

def calcular_potencia():
    """
    EXERCÍCIO 3: Calcular potência de um número
    
    Objetivo: Criar uma função que calcula a potência de um número.
    """
    print("\n=== Calculando Potência ===")
    base = float(input("Digite o número base: "))
    expoente = float(input("Digite o expoente: "))
    
    resultado = base ** expoente
    return f"{base} elevado a {expoente} = {resultado}"

def verificar_idade():
    """
    EXERCÍCIO 4: Verificar idade e mostrar mensagem personalizada
    
    Objetivo: Criar uma função que verifica se a idade é 18 anos e mostra uma mensagem personalizada.
    """
    print("\n=== Verificando Idade ===")
    idade = int(input("Digite sua idade: "))
    
    if idade == 18:
        return "Parabéns! Você acabou de atingir a maioridade!"
    elif idade > 18:
        return f"Você já é maior de idade há {idade - 18} anos"
    else:
        return f"Faltam {18 - idade} anos para você atingir a maioridade"

def calcular_idade():
    """
    EXERCÍCIO 5: Calcular idade de uma pessoa
    
    Objetivo: Criar uma função que calcula a idade atual baseada no ano e mês de nascimento.
    Considera o mês atual para calcular a idade corretamente.
    """
    print("\n=== Calculando Idade ===")
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    mes_nascimento = int(input("Digite seu mês de nascimento (1-12): "))
    
    # Validação do mês
    if mes_nascimento < 1 or mes_nascimento > 12:
        return "Mês inválido! Digite um número entre 1 e 12."
    
    from datetime import datetime
    data_atual = datetime.now()
    ano_atual = data_atual.year
    mes_atual = data_atual.month
    
    # Calcula a idade
    idade = ano_atual - ano_nascimento
    
    # Se ainda não chegou o mês do aniversário, subtrai 1 ano
    if mes_atual < mes_nascimento:
        idade -= 1
        meses_restantes = mes_nascimento - mes_atual
        return f"Você tem {idade} anos e faltam {meses_restantes} meses para seu aniversário"
    # Se já passou o mês do aniversário
    elif mes_atual > mes_nascimento:
        meses_passados = mes_atual - mes_nascimento
        return f"Você tem {idade} anos e já se passaram {meses_passados} meses do seu aniversário"
    # Se é o mês do aniversário
    else:
        return f"Você tem {idade} anos e está no mês do seu aniversário!"

def verificar_copa_1999():
    """
    EXERCÍCIO 6: Verificar resultado da Copa de 1999
    
    Objetivo: Criar uma função que verifica se o Brasil ganhou a Copa de 1999.
    Utiliza dados oficiais da FIFA para validação.
    """
    print("\n=== Verificando Copa de 1999 ===")
    
    # Dados oficiais das Copas do Mundo (FIFA)
    copas_mundo = {
        1930: "Uruguai",
        1934: "Itália",
        1938: "França",
        1950: "Brasil",
        1954: "Suíça",
        1958: "Suécia",
        1962: "Chile",
        1966: "Inglaterra",
        1970: "México",
        1974: "Alemanha Ocidental",
        1978: "Argentina",
        1982: "Espanha",
        1986: "México",
        1990: "Itália",
        1994: "Estados Unidos",
        1998: "França",
        2002: "Coreia do Sul/Japão",
        2006: "Alemanha",
        2010: "África do Sul",
        2014: "Brasil",
        2018: "Rússia",
        2022: "Catar"
    }
    
    # Verifica se 1999 está na lista de Copas
    if 1999 in copas_mundo:
        return f"Em 1999, a Copa do Mundo foi realizada em {copas_mundo[1999]}"
    else:
        # Encontra as Copas mais próximas de 1999
        anos = sorted(copas_mundo.keys())
        copa_anterior = max([ano for ano in anos if ano < 1999])
        copa_posterior = min([ano for ano in anos if ano > 1999])
        
        return f"""O Brasil não participou da Copa do Mundo de 1999, pois a Copa do Mundo é realizada a cada 4 anos.
A última Copa antes de 1999 foi em {copa_anterior} em {copas_mundo[copa_anterior]}.
A próxima Copa após 1999 foi em {copa_posterior} em {copas_mundo[copa_posterior]}.
Em 1999, o Brasil estava se preparando para a Copa de {copa_posterior}."""

def sistema_restaurante():
    """
    EXERCÍCIO 7: Sistema de Restaurante
    
    Objetivo: Criar um sistema de restaurante onde o cliente pode escolher entre diferentes opções de pratos.
    """
    print("\n=== Sistema de Restaurante ===")
    print("CARDÁPIO:")
    print("1. Salada - R$ 15,00")
    print("2. Macarronada - R$ 25,00")
    print("3. Sanduíche - R$ 20,00")
    print("4. Sorvete - R$ 10,00")
    
    opcao = input("\nEscolha o número do prato desejado: ")
    
    if opcao == "1":
        return "Você escolheu Salada - R$ 15,00"
    elif opcao == "2":
        return "Você escolheu Macarronada - R$ 25,00"
    elif opcao == "3":
        return "Você escolheu Sanduíche - R$ 20,00"
    elif opcao == "4":
        return "Você escolheu Sorvete - R$ 10,00"
    else:
        return "Opção inválida!"

# Menu principal para testar as funções
def menu():
    """
    Menu principal para testar todas as funções
    """
    while True:
        print("\n=== MENU DE EXERCÍCIOS ===")
        print("1. Comparar números (par/ímpar)")
        print("2. Multiplicar três números")
        print("3. Calcular potência")
        print("4. Verificar idade")
        print("5. Calcular idade")
        print("6. Verificar Copa 1999")
        print("7. Sistema de Restaurante")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção (0-7): ")
        
        if opcao == "0":
            print("Programa encerrado!")
            break
        elif opcao == "1":
            print(comparar_numeros())
        elif opcao == "2":
            print(multiplicar_tres_numeros())
        elif opcao == "3":
            print(calcular_potencia())
        elif opcao == "4":
            print(verificar_idade())
        elif opcao == "5":
            print(calcular_idade())
        elif opcao == "6":
            print(verificar_copa_1999())
        elif opcao == "7":
            print(sistema_restaurante())
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu() 