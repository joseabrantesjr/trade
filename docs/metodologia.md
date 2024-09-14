---
title: Metodologia Científica
---

# Metodologia Científica

Este projeto combina técnicas de **machine learning**, **deep learning** e **otimização de portfólio** para fornecer previsões de preços de ações e recomendações de alocação de ativos.

## Modelos Utilizados

### 1. **Redes Neurais LSTM**

- **Long Short-Term Memory (LSTM)** é uma variante de Redes Neurais Recorrentes (RNN) que é eficaz no processamento de séries temporais.
- **Justificativa**: LSTM é capaz de capturar dependências de longo prazo nos dados, tornando-o adequado para prever preços de ações que dependem de padrões históricos.
- **Referências**:
  - Zhang, G. P., & Hu, M. Y. (2017). Neural networks in business forecasting. *Information & Management*.
  - Nelson, D. M., Pereira, A. C. M., & de Oliveira, R. A. (2017). Stock market's price movement prediction with LSTM neural networks. *International Joint Conference on Neural Networks*.

### 2. **Otimização de Portfólio de Markowitz**

- **Teoria Moderna do Portfólio** desenvolvida por Harry Markowitz (1952) visa otimizar a alocação de ativos para maximizar o retorno esperado para um dado nível de risco.
- **Justificativa**: Fornece uma abordagem matemática robusta para diversificação de investimentos.
- **Referências**:
  - Markowitz, H. (1952). Portfolio selection. *The Journal of Finance*.
  - Fabozzi, F. J., Gupta, F., & Markowitz, H. M. (2002). The legacy of modern portfolio theory. *The Journal of Investing*.

## Processo de Desenvolvimento

1. **Coleta de Dados**:
   - Utilização da biblioteca `yfinance` para obter dados históricos de preços de ações.

2. **Pré-processamento**:
   - Escalonamento dos dados com `MinMaxScaler`.
   - Criação de janelas de dados para alimentar o modelo LSTM.

3. **Treinamento do Modelo**:
   - Divisão dos dados em conjuntos de treino e teste.
   - Treinamento do modelo LSTM com camadas de Dropout para evitar overfitting.

4. **Avaliação do Modelo**:
   - Cálculo de métricas como **Erro Quadrático Médio (MSE)** e **Erro Absoluto Médio (MAE)**.

5. **Previsão e Otimização**:
   - Previsão de preços para os próximos 5 dias úteis.
   - Otimização da alocação de ativos na carteira usando o modelo de Markowitz.

## Considerações Finais

A combinação de LSTM para previsão de preços e a otimização de portfólio de Markowitz proporciona uma abordagem integrada para análise e gestão de investimentos. Essa metodologia é respaldada por estudos científicos que demonstram a eficácia dessas técnicas no mercado financeiro.
