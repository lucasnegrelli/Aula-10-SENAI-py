import statistics
from collections import Counter

class SistemaNotas:
    def __init__(self):
        self.notas = []
    
    def calcular_media(self):
        """Calcula a média aritmética das notas."""
        if not self.notas:
            return 0
        return statistics.mean(self.notas)
    
    def calcular_moda(self):
        """Calcula a moda (valor mais frequente) das notas."""
        if not self.notas:
            return None
        
        contador = Counter(self.notas)
        max_freq = max(contador.values())
        
        # Se todas as frequências são iguais, não há moda
        if list(contador.values()).count(max_freq) == len(contador):
            return None
        
        # Retorna todos os valores com a frequência máxima
        return [k for k, v in contador.items() if v == max_freq]
    
    def calcular_desvio_padrao(self):
        """Calcula o desvio padrão das notas."""
        if len(self.notas) <= 1:
            return 0
        return statistics.stdev(self.notas)
    
    def menor_nota(self):
        """Encontra a menor nota."""
        if not self.notas:
            return None
        return min(self.notas)
    
    def maior_nota(self):
        """Encontra a maior nota."""
        if not self.notas:
            return None
        return max(self.notas)
    
    def adicionar_nota(self, nota):
        """Adiciona uma nota à lista."""
        self.notas.append(nota)
    
    def adicionar_varias_notas(self, notas_lista):
        """Adiciona várias notas de uma vez."""
        self.notas.extend(notas_lista)
    
    def limpar_notas(self):
        """Limpa todas as notas."""
        self.notas = []
    
    def exibir_estatisticas(self):
        """Exibe todas as estatísticas das notas."""
        if not self.notas:
            print("\nNenhuma nota fornecida.")
            return
        
        print("\n===== ESTATÍSTICAS DAS NOTAS =====")
        print(f"Notas: {self.notas}")
        print(f"Média: {self.calcular_media():.2f}")
        
        moda = self.calcular_moda()
        if moda:
            print(f"Moda: {moda}")
        else:
            print("Moda: Não há moda (todas as notas têm a mesma frequência)")
        
        print(f"Desvio Padrão: {self.calcular_desvio_padrao():.2f}")
        print(f"Menor Nota: {self.menor_nota()}")
        print(f"Maior Nota: {self.maior_nota()}")
        print("=" * 40)

def entrada_notas_individual(sistema):
    """Permite ao usuário inserir notas uma por uma."""
    print("\nInsira as notas dos alunos uma por uma.")
    print("Digite 'fim' quando terminar de inserir todas as notas.")
    
    contador = 1
    while True:
        entrada = input(f"Nota do aluno #{contador} (ou 'fim' para terminar): ")
        if entrada.lower() == 'fim':
            break
        
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:  # Assumindo que as notas estão entre 0 e 10
                sistema.adicionar_nota(nota)
                print(f"Nota {nota} adicionada com sucesso!")
                contador += 1
            else:
                print("Por favor, insira uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def entrada_notas_conjunto(sistema):
    """Permite ao usuário inserir todas as notas de uma vez, separadas por vírgula."""
    print("\nInsira todas as notas separadas por vírgula (ex: 7.5, 8.0, 9.5)")
    entrada = input("Notas: ")
    
    try:
        # Divide a string por vírgulas e converte cada parte em float
        notas = [float(nota.strip()) for nota in entrada.split(',')]
        
        # Verifica se todas as notas estão no intervalo válido
        notas_invalidas = [nota for nota in notas if nota < 0 or nota > 10]
        if notas_invalidas:
            print(f"As seguintes notas estão fora do intervalo válido (0-10): {notas_invalidas}")
            return
        
        sistema.adicionar_varias_notas(notas)
        print(f"{len(notas)} notas adicionadas com sucesso!")
    except ValueError:
        print("Entrada inválida. Certifique-se de que todas as notas são números válidos separados por vírgula.")

def menu():
    sistema = SistemaNotas()
    
    while True:
        print("\n===== SISTEMA DE NOTAS ESCOLARES =====")
        print("1. Adicionar notas (uma por uma)")
        print("2. Adicionar notas (todas de uma vez)")
        print("3. Ver estatísticas")
        print("4. Limpar notas")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            entrada_notas_individual(sistema)
        
        elif opcao == "2":
            entrada_notas_conjunto(sistema)
        
        elif opcao == "3":
            sistema.exibir_estatisticas()
        
        elif opcao == "4":
            sistema.limpar_notas()
            print("Todas as notas foram removidas.")
        
        elif opcao == "5":
            print("Saindo do sistema. Até logo!")
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Exemplo de uso direto (sem menu)
def exemplo_direto():
    # Criar um conjunto de notas de exemplo
    notas_exemplo = [7.5, 8.0, 6.5, 9.0, 7.5, 8.5, 6.0, 7.0, 8.0, 9.5]
    
    # Inicializar o sistema e adicionar as notas
    sistema = SistemaNotas()
    sistema.adicionar_varias_notas(notas_exemplo)
    
    # Exibir as estatísticas
    sistema.exibir_estatisticas()

if __name__ == "__main__":
    print("Bem-vindo ao Sistema de Estatísticas de Notas Escolares!")
    print("Este sistema calcula estatísticas como média, moda e desvio padrão das notas dos alunos.")
    
    # Descomente uma das linhas abaixo para escolher o modo de execução
    menu()  # Executa o sistema com menu interativo
    # exemplo_direto()  # Executa um exemplo direto com notas predefinidas