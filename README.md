
---

# 📈 Previsão de preço de ações e otimização de portfólio com LSTM e modelo de Markowitz

[![Stars](https://img.shields.io/github/stars/seu_usuario/seu_repositorio.svg?style=social)](https://github.com/seu_usuario/seu_repositorio/stargazers)
[![Forks](https://img.shields.io/github/forks/seu_usuario/seu_repositorio.svg?style=social)](https://github.com/seu_usuario/seu_repositorio/network/members)

Preveja o preço de ações da próxima semana e otimize seu portfólio de investimentos utilizando modelos avançados de redes neurais LSTM e o Modelo de Otimização de Markowitz.

## 🔥 O que este projeto faz?

Este projeto combina a **previsão de séries temporais** com **LSTM** e a **otimização de portfólios** com o **Modelo de Markowitz**, permitindo que você:

- Preveja os preços de ações da próxima semana com base em dados históricos.
- Avalie o desempenho do modelo utilizando métricas de erro como MSE e MAE.
- Otimize a alocação do seu portfólio com base no retorno esperado e no risco.

### Recursos:

- 🚀 **LSTM Model**: Treina um modelo para prever preços de ações futuros.
- 📊 **Portfolio Optimization**: Utiliza o Modelo de Markowitz para recomendar a melhor alocação de ativos com base na previsão.
- 🔮 **Price Prediction**: Prevê o preço de ações para os próximos 5 dias úteis.
- 💡 **Fácil de usar**: Apenas insira o símbolo da ação (ex: AAPL para Apple Inc.) e veja a previsão de preços e a recomendação de compra/venda.

## 🚀 Como começar?

### 1. Clone o repositório

Primeiro, faça o clone deste repositório:

```bash
git clone https://github.com/joseabrantesjr/trade.git
cd trade
```

### 2. Instale as dependências

Use o `pip` para instalar as dependências listadas no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 3. Execute o programa

Rode o script Python diretamente no terminal e insira o símbolo de uma empresa listada na bolsa para prever seus preços e otimizar seu portfólio:

```bash
python run.py
```

## ✨ Exemplos de Uso

1. **Prever preços de ações**:

   Após rodar o programa, insira um símbolo de ação, como `AAPL`, e veja as previsões de preços para os próximos 5 dias úteis, junto com recomendações de compra ou venda:

   ```
    Digite o símbolo da empresa (por exemplo, AAPL para Apple Inc.): PBR
    Preço de Fechamento Atual: $14.53

    Previsão de preços para a próxima semana:
    16/09/2024: $14.53
    17/09/2024: $14.56
    18/09/2024: $14.60
    19/09/2024: $14.64
    20/09/2024: $14.69

    Erro Quadrático Médio (MSE) do modelo: 0.0019
    Erro Absoluto Médio (MAE) do modelo: 0.0329

    Variação percentual prevista: 1.07%
    Recomendação: Considere comprar. O modelo prevê uma tendência de alta.
    
   ```

2. **Otimizar Portfólio**:

   O modelo de Markowitz calcula o peso ideal da ação na sua carteira com base nas previsões de retorno e no seu nível de tolerância ao risco.

   ```
   Peso ótimo da ação na carteira: 15.23%
   ```

## 📄 Estrutura do Código

O projeto está estruturado da seguinte forma:

- **`preprocess_data`**: Pré-processamento dos dados, incluindo escalonamento e criação de janelas de dados para treinamento.
- **`create_lstm_model`**: Criação do modelo LSTM.
- **`train_model`**: Treinamento do modelo e divisão dos dados em treino e teste.
- **`predict_next_week`**: Previsão de preços para os próximos 5 dias úteis.
- **`optimize_portfolio`**: Otimização da carteira utilizando o modelo de Markowitz.

## 🧠 Aprenda Mais

Se você quiser aprender mais sobre as técnicas utilizadas neste projeto, confira:

- [Documentação do LSTM](https://en.wikipedia.org/wiki/Long_short-term_memory)
- [Otimização de Portfólio de Markowitz](https://en.wikipedia.org/wiki/Modern_portfolio_theory)

## 🤝 Contribuições

Sinta-se à vontade para contribuir com este projeto! Aqui está como você pode ajudar:

1. **Dê uma estrela ⭐**: Se este projeto ajudou você, dê uma estrela no GitHub!
2. **Fork este repositório**: Crie sua própria cópia deste projeto e adicione novos recursos.
3. **Envie um Pull Request**: Quer sugerir uma melhoria? Faça um fork, adicione sua melhoria e envie um pull request.
4. **Reportar Problemas**: Encontrou um bug ou um erro? Abra uma [issue](https://github.com/seu_usuario/seu_repositorio/issues) no GitHub.

### Como contribuir

1. Faça o **fork** deste repositório.
2. Crie um **branch** com sua feature: `git checkout -b minha-feature`.
3. Faça o **commit** das suas mudanças: `git commit -m 'Adiciona minha feature'`.
4. Faça o **push** para o branch: `git push origin minha-feature`.
5. Envie um **Pull Request**.

## 🎯 Objetivos do Projeto

Nosso objetivo é criar um projeto de código aberto robusto, onde todos possam colaborar e aprender sobre **redes neurais**, **séries temporais** e **otimização de portfólio**. Esperamos que este projeto se torne uma referência para quem deseja entender essas técnicas aplicadas ao mercado financeiro.

## 🌟 Mantenha-se Atualizado

- [Siga-me no GitHub](https://github.com/seu_usuario) para mais projetos como este!
- **Gostou deste projeto?** Dê uma estrela 🌟 e compartilhe com seus amigos!

---

**Licença**: Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### ⚡ Fork Now and Contribute to the Next Big Feature!
---

Este README incentiva a comunidade a se envolver através de uma abordagem clara e detalhada, proporcionando um caminho fácil para contribuir e aprender, enquanto promove o engajamento via estrelas, forks, e pull requests.