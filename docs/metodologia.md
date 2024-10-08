---
title: Metodologia Científica
---

# Metodologia Científica

Esta programação é projetada para realizar a previsão de preços de ações e otimização de portfólio utilizando técnicas avançadas de **machine learning** e **deep learning**, além de aplicar a teoria de **otimização de portfólio de Markowitz**. Aqui está uma descrição detalhada do seu propósito e da eficácia, baseada em evidências científicas:

## Objetivo

Este script tem como foco a previsão de preços de ações com base em dados históricos do mercado financeiro, seguido da recomendação de estratégias de compra ou venda. Ele também incorpora um modelo de otimização de portfólio para identificar a alocação ideal de ativos em uma carteira, de acordo com a **Teoria Moderna do Portfólio** (Markowitz, 1952).

### Funcionalidades Principais:

1. **Previsão de Preços com Redes Neurais (LSTM)**:
    - Utiliza redes neurais recorrentes (RNN) do tipo **LSTM** (Long Short-Term Memory) para prever os preços das ações para os próximos cinco dias úteis.
    - O LSTM é eficaz na modelagem de séries temporais financeiras devido à sua capacidade de capturar dependências de longo prazo nos dados, conforme evidenciado por estudos em **modelagem de séries temporais financeiras** (Zhang et al., 2017; Nelson et al., 2017).

2. **Avaliação de Desempenho do Modelo**:
    - O modelo é avaliado usando métricas como o **Erro Quadrático Médio (MSE)** e o **Erro Absoluto Médio (MAE)**, que são amplamente utilizados em estudos para medir a precisão de modelos preditivos.
    - O **MSE** penaliza grandes erros de previsão, tornando-se uma escolha robusta para avaliar a eficácia do modelo.

3. **Otimização de Portfólio**:
    - Utiliza o modelo de Markowitz, que busca maximizar os retornos esperados para um dado nível de risco. A formulação clássica da otimização de portfólio é baseada na minimização da volatilidade, como definido por Markowitz (1952), e tem sido corroborada por décadas de pesquisas acadêmicas.
    - O uso de dados históricos de retornos e variância estimada para determinar a alocação ideal de ativos é uma prática padrão no setor financeiro e tem suporte robusto na literatura científica (Fabozzi et al., 2002).

### Comparação com Estudos Científicos

1. **Previsão com LSTM vs. Modelos Tradicionais**:
    - A previsão de séries temporais financeiras usando **LSTM** tem demonstrado maior acurácia em relação a modelos lineares tradicionais, como **ARIMA** e **GARCH**, especialmente em dados de alta volatilidade. Zhang et al. (2017) mostraram que LSTM pode capturar dependências de longo prazo nos dados financeiros, algo que os modelos lineares lutam para replicar.
    - Estudos também indicam que LSTM supera redes neurais artificiais tradicionais (ANN) quando se trata de previsão de preços de ações (Nelson et al., 2017).

2. **Otimização de Portfólio com Markowitz**:
    - A Teoria Moderna do Portfólio, introduzida por Markowitz (1952), continua sendo a base para a alocação de ativos, apesar do surgimento de modelos mais sofisticados. Isso ocorre porque o modelo de Markowitz é computacionalmente eficiente e oferece uma abordagem simples para otimizar o risco e retorno, conforme validado por Fabozzi et al. (2002).
    - A alocação sugerida pelo modelo de Markowitz considera não apenas a tendência de preço dos ativos, mas também o **retorno esperado e a volatilidade (risco)** de cada ativo, além da **correlação** entre os ativos. Mesmo que um ativo tenha uma previsão de baixa a curto prazo, ele pode ser útil na composição do portfólio por causa de três principais fatores:

        ### 1. **Diversificação do Risco**
        A carteira de Markowitz é construída para **minimizar o risco** para um dado nível de retorno esperado, levando em conta a **correlação** entre os ativos. Um ativo com tendência de baixa pode ter baixa correlação com outros ativos na carteira, ajudando a reduzir o risco total. Assim, mesmo com uma previsão negativa, ele pode **equilibrar o risco** da carteira e, portanto, ainda ser recomendado para alocação.

        ### 2. **Volatilidade Baixa**
        Ativos com tendências de baixa podem ter **volatilidade (risco)** menor em relação a outros ativos. Se o ativo tem um comportamento estável e previsível, mesmo em tendência de queda, ele pode ser incluído na carteira para **reduzir a volatilidade total** da carteira. Isso ajuda a suavizar as oscilações dos preços, promovendo mais estabilidade.

        ### 3. **Retorno de Longo Prazo**
        Embora a previsão de preços seja para a próxima semana, a alocação de Markowitz está mais focada em um horizonte de longo prazo. Um ativo que está caindo agora pode ter retornos melhores no futuro, e o modelo pode levar isso em consideração ao sugerir que o ativo seja mantido no portfólio.

        ### 4. **Diversificação de Risco com Ações de Baixa Correlação**
        Se esses ativos de baixa tendência atual forem **descorrelacionados** ou até negativamente correlacionados com outros ativos da carteira, eles ajudam a diminuir o risco sistêmico. Em outras palavras, mesmo que um ativo esteja em queda, ele pode **reduzir a exposição ao risco geral da carteira** quando combinado com outros ativos.

        Em resumo, o modelo de Markowitz não foca apenas nas tendências de curto prazo, mas na **diversificação do risco** e na **otimização do portfólio** como um todo, buscando equilibrar ativos que se complementam para maximizar o retorno e minimizar o risco.

### Eficácia da Solução

Este sistema apresenta uma combinação poderosa de técnicas de **machine learning** para previsão e **teoria de otimização de portfólio** para decisões de alocação de ativos, sendo uma solução eficaz para traders e gestores de portfólio. Em termos de acurácia preditiva, o uso de LSTM é respaldado por estudos que demonstram sua capacidade superior em prever séries temporais complexas e não lineares, especialmente no mercado financeiro, que é conhecido por sua natureza volátil e imprevisível.

### Limitações e Melhorias Potenciais

- **Dependência de dados históricos**: Assim como em qualquer modelo preditivo financeiro, a precisão das previsões depende da qualidade e representatividade dos dados históricos.
- **Volatilidade do mercado**: Em condições extremas, como crises financeiras, a acurácia dos modelos pode ser reduzida, uma vez que os padrões observados no passado podem não ser aplicáveis no futuro.
- Melhorias podem ser feitas com a inclusão de variáveis exógenas (notícias financeiras, dados macroeconômicos) para melhorar as previsões.

### Conclusão

A combinação de redes neurais LSTM e a otimização de portfólio de Markowitz, conforme implementada neste projeto, oferece uma abordagem cientificamente robusta e eficaz para previsão e gestão de ativos financeiros. É especialmente útil para traders e investidores que buscam automatizar a análise de mercado e otimizar suas decisões de alocação de ativos com base em previsões de curto prazo e uma sólida gestão de risco.

## Referências:
- Zhang, G. P., & Hu, M. Y. (2017). Neural networks in business forecasting. Information & Management.
- Nelson, D. M., Pereira, A. C. M., & de Oliveira, R. A. (2017). Stock market's price movement prediction with LSTM neural networks. **International Joint Conference on Neural Networks**.
- Fabozzi, F. J., Gupta, F., & Markowitz, H. M. (2002). The legacy of modern portfolio theory. **The Journal of Investing**.
- Markowitz, H. (1952). Portfolio selection. **The Journal of Finance**.
``` 

Essa descrição apresenta a programação em um contexto acadêmico e técnico, mostrando que o uso de LSTM e o modelo de Markowitz são baseados em fundamentos científicos amplamente reconhecidos na literatura financeira e de machine learning.