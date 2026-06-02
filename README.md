# Sistema Inteligente de Transporte Autônomo para Zonas de Risco

## Descrição do Projeto

Este projeto propõe uma solução inspirada nas tecnologias utilizadas em missões espaciais para realizar o transporte autônomo de suprimentos em áreas de risco.

A solução utiliza técnicas de Inteligência Artificial e Machine Learning para classificar riscos, prever tempos de entrega, agrupar regiões semelhantes e tomar decisões autônomas durante uma missão.

O objetivo é reduzir a exposição de equipes humanas a ambientes perigosos, como regiões afetadas por enchentes, incêndios, deslizamentos e outros desastres.

---

# Diagrama da Solução

Coleta de Dados
↓
Sistema Especialista
↓
Classificação de Risco (Naive Bayes)
↓
Clustering (K-Means)
↓
Previsão de Tempo (Regressão Linear)
↓
Rede Neural MLP
↓
Agente Inteligente
↓
Entrega dos Suprimentos

---

# Objetivo da Solução

## Objetivo de Negócio

Permitir a entrega segura de suprimentos em áreas de risco, reduzindo custos operacionais e minimizando a exposição de equipes de resgate a situações perigosas.

## Objetivo Técnico

Desenvolver um sistema baseado em Inteligência Artificial capaz de analisar dados do ambiente, classificar riscos, prever tempos de entrega e tomar decisões autônomas.

---

# Bibliotecas Utilizadas

* pandas
* numpy
* scikit-learn

## Função das Bibliotecas

### pandas

Manipulação e análise dos dados utilizados nos experimentos.

### numpy

Operações matemáticas e geração de dados simulados.

### scikit-learn

Implementação dos algoritmos de Machine Learning:

* Regressão Linear
* Naive Bayes
* K-Means
* MLP

---

# Funcionamento do Pipeline

## 1. Coleta de Dados

O sistema recebe informações como:

* Distância
* Obstáculos
* Clima
* Nível de bateria

## 2. Sistema Especialista

Aplica regras de decisão.

Exemplo:

* Se bateria < 20%, retornar à base.
* Se risco = alto, evitar rota.

## 3. Classificação de Risco

Utilização do algoritmo Naive Bayes para classificar o risco da missão.

Saídas possíveis:

* Baixo
* Médio
* Alto

## 4. Agrupamento de Regiões

O algoritmo K-Means agrupa regiões com características semelhantes.

## 5. Previsão de Tempo

A Regressão Linear estima o tempo necessário para completar a missão.

## 6. Rede Neural

A MLP calcula a probabilidade de sucesso da missão.

## 7. Agente Inteligente

Responsável por tomar decisões automáticas durante a execução.

---

# Pipeline de Visão Computacional

Nesta versão do projeto foi utilizada uma simulação baseada em dados estruturados.

Em uma implementação real, o pipeline de visão computacional funcionaria da seguinte forma:

Câmera
↓
Captura de Imagem
↓
Pré-processamento
↓
Detecção de Obstáculos
↓
Classificação do Ambiente
↓
Atualização da Rota
↓
Navegação Autônoma

Exemplos de obstáculos:

* Veículos
* Pessoas
* Árvores
* Escombros
* Áreas alagadas

---

# Instruções de Execução

## Criar ambiente virtual

Windows

python -m venv venv

venv\Scripts\activate

Linux

python3 -m venv venv

source venv/bin/activate

---

## Instalar dependências

pip install -r requirements.txt

---

## Executar o projeto

python projeto_completo.py

---

# Estrutura do Projeto

projeto/

├── missoes.csv

├── main.py

├── requirements.txt

└── README.md

---

# Integrantes

- Augusto Rogel / RM 557709
- Heitor Prestes / RM 554823
- Lucca Ribeiro / RM 556668


---

# Resultados Esperados

O sistema deverá:

* Classificar riscos.
* Agrupar regiões semelhantes.
* Prever tempos de entrega.
* Estimar probabilidade de sucesso.
* Simular tomadas de decisão autônomas.

---

# Desafios Futuros

* Integração com sensores reais.
* Utilização de GPS em tempo real.
* Implementação de visão computacional com OpenCV.
* Uso de drones autônomos.
* Aplicação de Deep Learning para reconhecimento de obstáculos.
* Integração com mapas geográficos.
* Comunicação em tempo real entre múltiplos veículos autônomos.
