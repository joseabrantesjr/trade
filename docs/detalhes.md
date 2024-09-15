---
title: Detalhe
---

# Detalhamento do Código

Este documento descreve o funcionamento de um código que utiliza um modelo baseado em uma **Rede Neural LSTM** para prever o preço de fechamento de ações nos próximos 5 dias úteis. O código também usa um modelo de otimização de portfólio baseado na **Teoria Moderna de Portfólios (Modelo de Markowitz)** para sugerir a melhor alocação de ativos de acordo com os retornos previstos.

## 1. Importação de Bibliotecas

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from keras.optimizers import Adam
from scipy.optimize import minimize
import yfinance as yf
from datetime import datetime, timedelta
```

- **NumPy** e **Pandas**: Usados para manipulação de arrays e dados.
- **MinMaxScaler**: Da biblioteca **sklearn**, utilizado para normalizar os dados.
- **Sequential**, **LSTM**, **Dense** e **Dropout**: Da **Keras**, formam a base do modelo LSTM.
- **Adam**: Otimizador usado para ajustar os pesos da rede neural.
- **minimize**: Da **scipy.optimize**, realiza a otimização do portfólio.
- **yfinance**: Usado para baixar dados de mercado.
- **datetime** e **timedelta**: Manipulam datas.

## 2. Função de Pré-processamento dos Dados: `preprocess_data`

```python
def preprocess_data(data, window_size=20):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data[['Close']])
    
    X, y = [], []
    for i in range(len(scaled_data) - window_size):
        X.append(scaled_data[i:i+window_size])
        y.append(scaled_data[i+window_size])
    
    return np.array(X), np.array(y), scaler
```

### Descrição:
- **Normalização**: Usa `MinMaxScaler` para escalar os preços de fechamento entre 0 e 1.
- **Criação de janelas deslizantes**: Divide os dados em janelas de 20 dias. O modelo tentará prever o preço do dia seguinte para cada janela.

## 3. Criação do Modelo LSTM: `create_lstm_model`

```python
def create_lstm_model(input_shape):
    model = Sequential([
        LSTM(256, activation='tanh', return_sequences=True, input_shape=input_shape),
        Dropout(0.4),
        LSTM(256, activation='tanh'),
        Dropout(0.4),
        Dense(1)
    ])
    model.compile(optimizer=Adam(), loss='mean_squared_error')
    return model
```

### Descrição:
- **Camadas LSTM**: Com 256 unidades, utilizando a ativação `tanh` (comum em redes neurais recorrentes).
- **Dropout**: Ajuda a prevenir overfitting, desativando 40% dos neurônios durante o treino.
- **Camada Dense**: Saída única, representando a previsão do preço de fechamento.
- Compilação do modelo com a função de perda **mean squared error (MSE)** e o otimizador **Adam**.

## 4. Treinamento do Modelo: `train_model`

```python
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = create_lstm_model((X.shape[1], 1))
    model.fit(X_train, y_train, epochs=300, batch_size=64, validation_split=0.2, verbose=0)
    
    return model, X_test, y_test
```

### Descrição:
- Divide os dados em treino (80%) e teste (20%) com `train_test_split`.
- Treina o modelo LSTM por 300 épocas com um tamanho de lote de 64.

## 5. Avaliação do Modelo: `evaluate_model`

```python
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = np.mean((predictions - y_test) ** 2)
    mae = np.mean(np.abs(predictions - y_test))
    return mse, mae
```

### Descrição:
- Calcula o **MSE (Mean Squared Error)** e **MAE (Mean Absolute Error)** para avaliar a precisão do modelo.

## 6. Previsão da Próxima Semana: `predict_next_week`

```python
def predict_next_week(model, last_window, scaler):
    last_window_scaled = scaler.transform(last_window)
    predictions = []
    
    for _ in range(5):  # Predict next 5 business days
        next_pred = model.predict(last_window_scaled.reshape(1, -1, 1))
        predictions.append(next_pred[0, 0])
        last_window_scaled = np.roll(last_window_scaled, -1)
        last_window_scaled[-1] = next_pred
    
    return scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
```

### Descrição:
- Utiliza os últimos 20 dias de dados para prever os preços de fechamento dos próximos 5 dias úteis.
- A cada previsão, a janela de dados é atualizada com o valor previsto.

## 7. Otimização de Portfólio: `optimize_portfolio`

```python
def optimize_portfolio(returns, expected_returns, risk_tolerance):
    num_assets = len(returns.columns)
        
    def portfolio_volatility(weights, returns):
        return np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    
    def portfolio_return(weights, expected_returns):
        return np.sum(expected_returns * weights) * 252
    
    def objective(weights, returns, expected_returns, risk_tolerance):
        return -portfolio_return(weights, expected_returns) + risk_tolerance * portfolio_volatility(weights, returns)
    
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for _ in range(num_assets))
    initial_weights = np.array([1/num_assets] * num_assets)
    
    result = minimize(objective, initial_weights, args=(returns, expected_returns, risk_tolerance),
                      method='SLSQP', bounds=bounds, constraints=constraints)
    
    return result.x
```

### Descrição:
- Implementa a otimização de portfólio de Markowitz, ajustando os pesos dos ativos para maximizar o retorno esperado e minimizar a volatilidade (risco).

## 8. Função Principal: `main`

```python
def main():
    simbolo_empresa = input("Digite o símbolo da empresa (por exemplo, AAPL para Apple Inc.): ")
    data_atual = datetime.today().strftime('%Y-%m-%d')
    
    dados = yf.download(simbolo_empresa, start='2023-01-01', end=data_atual)
    
    if dados.empty:
        print("Não foi possível obter dados para o símbolo fornecido.")
        return
    
    print(f"Preço de Fechamento Atual: ${dados['Close'].iloc[-1]:.2f}")
    
    dates, prices, mse, mae, optimal_weight = identificar_melhor_compra(dados)
    
    print("\nPrevisão de preços para a próxima semana:")
    for date, price in zip(dates, prices):
        print(f"{date.strftime('%d/%m/%Y')}: ${price:.2f}")
    
    print(f"\nErro Quadrático Médio (MSE) do modelo: {mse:.4f}")
    print(f"Erro Absoluto Médio (MAE) do modelo: {mae:.4f}")
    
    ultimo_preco_real = dados['Close'].iloc[-1]
    ultimo_preco_previsto = prices[-1]
    variacao_percentual = ((ultimo_preco_previsto - ultimo_preco_real) / ultimo_preco_real) * 100
    
    print(f"\nVariação percentual prevista: {variacao_percentual:.2f}%")
    
    if variacao_percentual > 0:
        print("Recomendação: Considere comprar. O modelo prevê uma tendência de alta.")
    elif variacao_percentual < 0:
        print("Recomendação: Considere vender ou manter. O modelo prevê uma tendência de baixa.")
    else:
        print("Recomendação: Manter. O modelo prevê estabilidade no preço.")
    
    print(f"\nPeso ótimo da ação na carteira (segundo o modelo de Markowitz): {optimal_weight:.2%}")
```

### Descrição:
- Pede ao usuário um símbolo de ação, baixa dados históricos usando `yfinance`, calcula previsões e exibe os resultados:
  - Preço de fechamento previsto para a próxima semana.
  - Erro Quadrático Médio e Erro Absoluto Médio.
  - Variação percentual prevista no preço.
  - Recomendação de compra, venda ou manutenção.
  - Alocação ótima de ativos no portfólio.

---

Este código usa técnicas avançadas de **machine learning** e **otimização de portfólio** para prever o preço de ações e sugerir alocações ideais, automatizando decisões financeiras.
```

Esse conteúdo agora pode ser salvo no arquivo `detalhes.md`.