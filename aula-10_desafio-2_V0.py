import statistics
import numpy as np
from collections import Counter

# Dados salariais das empresas
empresa1 = [1000, 6000, 1200, 8000, 1400]  # StartUP Inovadora
empresa2 = [5000, 4000, 3000, 2000, 7000]  # Consultoria Tradicional
empresa3 = [1200, 1300, 8000, 3000, 15000]  # Tech Unicórnio
empresa4 = [1400, 1750, 2000, 4500, 5900]  # Empresa Familiar

# Função para calcular estatísticas com comentários sarcásticos
def analisar_empresa_brasileira(nome, salarios, comentario):
    media = statistics.mean(salarios)
    mediana = statistics.median(salarios)
    try:
        moda = statistics.mode(salarios)
    except statistics.StatisticsError:
        moda = "Tão única quanto promessa de político"
    desvio_padrao = statistics.stdev(salarios)
    
    # Coeficiente de variação (medida relativa de dispersão)
    cv = (desvio_padrao / media) * 100
    
    print(f"\n===== {nome} =====")
    print(f"Salários: {salarios}")
    print(f"Média: R$ {media:.2f} {comentario['media']}")
    print(f"Mediana: R$ {mediana:.2f} {comentario['mediana']}")
    print(f"Desvio Padrão: R$ {desvio_padrao:.2f} {comentario['desvio']}")
    print(f"Coeficiente de Variação: {cv:.2f}% {comentario['cv']}")
    print(f"Comentário geral: {comentario['geral']}")
    
    return {
        "media": media,
        "mediana": mediana,
        "desvio_padrao": desvio_padrao,
        "cv": cv
    }

# Comentários sarcásticos para cada empresa
comentarios_empresa1 = {
    "media": "(metade vai para o café gourmet da copa)",
    "mediana": "(o que a maioria realmente recebe depois dos descontos)",
    "desvio": "(mais instável que o humor do chefe)",
    "cv": "(tão equilibrado quanto o orçamento federal)",
    "geral": "Diversidade salarial que faria o IBGE chorar."
}

comentarios_empresa2 = {
    "media": "(suficiente para um financiamento de 30 anos para um AP de 45m²)",
    "mediana": "(dá para pagar o aluguel e ainda sobra para o rodízio no domingo)",
    "desvio": "(previsível como o trânsito às 18h: ruim, mas você já esperava)",
    "cv": "(a estabilidade que o Banco Central sonha para a inflação)",
    "geral": "Tão conservadora com dinheiro quanto vó guardando moeda no sutiã."
}

comentarios_empresa3 = {
    "media": "(inflada pelo salário do sobrinho do investidor)",
    "mediana": "(o que você vai receber enquanto o unicórnio não vira cavalo)",
    "desvio": "(mais disperso que turista em primeira viagem a São Paulo)",
    "cv": "(mais desigual que a distribuição de chuva no Nordeste)",
    "geral": "Uma montanha-russa financeira que faria até o Eike Batista ficar tonto."
}

comentarios_empresa4 = {
    "media": "(inclui o 'bônus' que nunca chega)",
    "mediana": "(depois de pagar a Unimed, sobra para o básico)",
    "desvio": "(imprevisível como horário de ônibus em dia de chuva)",
    "cv": "(tão consistente quanto promessa de entrega dos Correios)",
    "geral": "Salários distribuídos na base do 'quem o dono gosta mais'."
}

# Analisar cada empresa
resultado_empresa1 = analisar_empresa_brasileira("StartUP Inovadora", empresa1, comentarios_empresa1)
resultado_empresa2 = analisar_empresa_brasileira("Consultoria Tradicional", empresa2, comentarios_empresa2)
resultado_empresa3 = analisar_empresa_brasileira("Tech Unicórnio", empresa3, comentarios_empresa3)
resultado_empresa4 = analisar_empresa_brasileira("Empresa Familiar", empresa4, comentarios_empresa4)

# Resumo comparativo
print("\n===== RESUMO COMPARATIVO (ou 'Escolhendo o Menos Pior') =====")
print(f"{'Empresa':<25} {'Média':<20} {'Mediana':<20} {'Coef. Variação':<20}")
print("-" * 85)
print(f"{'StartUP Inovadora':<25} R$ {resultado_empresa1['media']:<18.2f} R$ {resultado_empresa1['mediana']:<18.2f} {resultado_empresa1['cv']:<20.2f}%")
print(f"{'Consultoria Tradicional':<25} R$ {resultado_empresa2['media']:<18.2f} R$ {resultado_empresa2['mediana']:<18.2f} {resultado_empresa2['cv']:<20.2f}%")
print(f"{'Tech Unicórnio':<25} R$ {resultado_empresa3['media']:<18.2f} R$ {resultado_empresa3['mediana']:<18.2f} {resultado_empresa3['cv']:<20.2f}%")
print(f"{'Empresa Familiar':<25} R$ {resultado_empresa4['media']:<18.2f} R$ {resultado_empresa4['mediana']:<18.2f} {resultado_empresa4['cv']:<20.2f}%")

print("\n===== DECISÃO FINAL (ou 'Onde vou sofrer pelos próximos anos') =====")
print("Depois de analisar os dados com mais cuidado que brasileiro escolhendo melancia na feira,")
print("decidi aceitar a proposta da CONSULTORIA TRADICIONAL.")
print("\nJustificativa (ou 'Como expliquei para minha mãe que não vou trabalhar no Google'):")
print("1. Média salarial de R$ 4.200,00 - Não é o maior valor, mas pelo menos dá para")
print("   pagar o aluguel e ainda sobra para o iFood no final do mês.")
print("2. Mediana próxima da média (R$ 4.000,00) - Quando a mediana está perto da média,")
print("   significa que não tem aquele cara ganhando 10x mais que todo mundo só porque")
print("   é amigo do dono. É mais justo que arbitragem de VAR em final de campeonato.")
print("3. Coeficiente de variação de apenas 45,80% - A menor dispersão entre todas as empresas.")
print("   É mais estável que o relacionamento dos protagonistas da novela das nove.")
print("4. Salário mínimo de R$ 2.000,00 - Nas outras empresas, o salário mínimo é tão baixo")
print("   que você precisa escolher entre pagar o aluguel ou comer.")
print("5. Política salarial estruturada - Parece que eles têm um plano de carreira mais")
print("   organizado que fila de banco em dia de pagamento.")
print("\nNa StartUP, eu seria mais um 'colaborador' (leia-se: escravo digital) trabalhando")
print("14 horas por dia em troca de 'experiência' e mesa de pingue-pongue.")
print("\nNa Tech Unicórnio, eu ficaria deslumbrado com o escritório instagramável por duas")
print("semanas, até perceber que meu salário mal paga o Uber para chegar lá.")
print("\nNa Empresa Familiar, eu seria promovido rapidamente... até o sobrinho do dono")
print("se formar e precisar de um emprego.")
print("\nEntão, vou para a Consultoria Tradicional, onde pelo menos sei que vou sofrer de forma")
print("previsível e bem remunerada. Como dizemos no Brasil: 'Ruim com eles, pior sem eles'.")
print("E se não der certo, sempre posso vender bolo de pote no metrô ou virar influencer de")
print("investimentos, que parece ser o plano B de todo brasileiro hoje em dia.")
print("\nAgora é só torcer para que o RH não veja essa análise antes de eu assinar o contrato,")
print("senão vou precisar explicar por que chamei a empresa de 'tão conservadora quanto vó")
print("guardando moeda no sutiã' na minha primeira reunião.")