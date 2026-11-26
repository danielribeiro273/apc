# Relatório de Análise - PDAD 2024 com pandas

### 1. Quais três RAs têm maior e quais têm menor renda média ponderada?
Com base no agrupamento ponderado por localidade (RA):
- **Maiores RAs em Renda Média Ponderada:**
  - *Nota: Verifique na planilha `resultado_pdad.xlsx` gerada na pasta e liste os códigos das 3 RAs no topo do ranking (ex: 5310, 5320, etc.).*
- **Menores RAs em Renda Média Ponderada:**
  - *Liste os códigos das 3 RAs no final do ranking da planilha (ex: 5244 com R$ 694,15).*

### 2. Qual a diferença entre contar linhas e somar pesos? Dê um exemplo dos seus resultados.
- **Contar linhas (`len` ou `.size`):** Representa apenas a amostra física de pessoas que responderam ao questionário da pesquisa. Nos nossos dados, contamos 69.542 moradores entrevistados.
- **Somar pesos (`peso_mor`):** Estima a população real do Distrito Federal, atribuindo a cada entrevistado o peso de quantas pessoas ele representa na sociedade.
- **Exemplo nos resultados:** A renda média simples do DF (sem peso) foi de **R$ 1.766,59**, enquanto a renda média ponderada (com peso populacional real) caiu para **R$ 1.450,22**. Isso acontece porque amostras em certas regiões podem estar sobre-representadas se não aplicarmos o peso amostral.

### 3. Que limitação do arquivo parcial impede tirar conclusões sobre o DF inteiro?
Como os dados utilizados são um recorte parcial destinado apenas ao aprendizado técnico, o número reduzido de registros por Região Administrativa não possui representatividade estatística completa nem garante o intervalo de confiança oficial divulgado pelo IPEDF para conclusões sobre todo o DF.

### 4. Como você explicaria um `groupby` para um estudante do ensino médio?
Pense no `groupby` como a divisão dos alunos de uma escola por turma para organizar uma gincana: primeiro você **separa** todos os alunos em grupos baseados em um critério (sua turma/RA), depois você **aplica** uma conta para cada grupo isoladamente (calcula a média de altura ou a soma de pontos daquela turma) e, no final, **junta** tudo em uma única tabela para comparar os resultados de cada turma lado a lado.