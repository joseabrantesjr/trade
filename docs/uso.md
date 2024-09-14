
#### **3.3. `docs/uso.md`**

```markdown
---
title: Como Usar
---

# Como Usar

Este projeto permite prever preços de ações e otimizar seu portfólio de investimentos. Veja abaixo um guia rápido de como utilizar o programa.

## 📈 Previsão de Preços

1. **Executar o Script**:
   ```bash
   python run.py
   ```

2. **Inserir o Símbolo da Empresa**:
Exemplo: AAPL para Apple Inc.

Visualizar Resultados:
Previsão de preços para os próximos 5 dias úteis.
Métricas de desempenho do modelo (MSE e MAE).
Recomendação de compra ou venda.
Peso ótimo da ação na carteira.
🛠️ Exemplos de Uso

Exemplo 1: Prevendo Ações da Apple (AAPL)
plaintext
Copiar código
Digite o símbolo da empresa (por exemplo, AAPL para Apple Inc.): AAPL
Preço de Fechamento Atual: $149.55

Previsão de preços para a próxima semana:
18/09/2023: $150.22
19/09/2023: $151.10
20/09/2023: $150.78
...

Recomendação: Considere comprar. O modelo prevê uma tendência de alta.

Peso ótimo da ação na carteira (segundo o modelo de Markowitz): 15.23%
