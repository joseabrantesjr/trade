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

def preprocess_data(data, window_size=20):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data[['Close']])
    
    X, y = [], []
    for i in range(len(scaled_data) - window_size):
        X.append(scaled_data[i:i+window_size])
        y.append(scaled_data[i+window_size])
    
    return np.array(X), np.array(y), scaler

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

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = create_lstm_model((X.shape[1], 1))
    model.fit(X_train, y_train, epochs=300, batch_size=64, validation_split=0.2, verbose=0)
    
    return model, X_test, y_test

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = np.mean((predictions - y_test) ** 2)
    mae = np.mean(np.abs(predictions - y_test))
    return mse, mae

def predict_next_week(model, last_window, scaler):
    last_window_scaled = scaler.transform(last_window)
    predictions = []
    
    for _ in range(5):  # Predict next 5 business days
        next_pred = model.predict(last_window_scaled.reshape(1, -1, 1))
        predictions.append(next_pred[0, 0])
        last_window_scaled = np.roll(last_window_scaled, -1)
        last_window_scaled[-1] = next_pred
    
    return scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

def optimize_portfolio(returns, expected_returns, risk_tolerance):
    if isinstance(returns, pd.Series):
        returns = returns.to_frame()  # Converte para DataFrame se for Series
    
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

def identificar_melhor_compra(data):
    X, y, scaler = preprocess_data(data)
    model, X_test, y_test = train_model(X, y)
    mse, mae = evaluate_model(model, X_test, y_test)
    
    last_window = data['Close'].values[-20:].reshape(-1, 1)
    proxima_semana_prices = predict_next_week(model, last_window, scaler)
    proxima_semana_dates = pd.date_range(start=data.index[-1] + timedelta(days=1), periods=5, freq='B')
    
    expected_returns = (proxima_semana_prices[-1] - data['Close'].values[-1]) / data['Close'].values[-1]
    
    risk_tolerance = 1.0
    optimal_weight = optimize_portfolio(data['Close'].pct_change().dropna(), expected_returns, risk_tolerance)
    
    return proxima_semana_dates, proxima_semana_prices.flatten(), mse, mae, optimal_weight[0]

def main():
    simbolo_empresa = input("Digite o símbolo da empresa (por exemplo, AAPL para Apple Inc.): ")
    data_atual = datetime.today().strftime('%Y-%m-%d')
    
    dados = yf.download(simbolo_empresa, start='2023-01-01', end=data_atual)
    
    if dados.empty:
        print("Não foi possível obter dados para o símbolo fornecido.")
        
    
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

if __name__ == "__main__":
    main()