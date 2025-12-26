# Shopee Auto-Reply & Scraper

## 📋 Sobre o Projeto
Conjunto de scripts desenvolvidos para automatizar a gestão de reputação em marketplace (Shopee), focando em responder avaliações pendentes e extrair dados para análise.

## 🚀 O Desafio
Ao assumir uma demanda no setor de Marketplace (Terabyte), deparei-me com um backlog de avaliações de clientes acumulado há dois meses. O objetivo era responder a todos e estruturar os dados em planilha para análise de satisfação.

## 💡 A Evolução da Solução
O desenvolvimento passou por três estágios de otimização até atingir a performance ideal:

1.  **Tentativa com Selenium:** Inicialmente escolhido, mas apresentou instabilidade na interação com elementos dinâmicos (botão 'Responder') da Shopee.
2.  **MVP com PyAutoGUI:** Desenvolvi uma automação visual. Funcionou, mas com baixa performance (média de 20 segundos por resposta), o que era inviável para o volume de dados.
3.  **Solução Final com Playwright:** Migrei para o Playwright devido à sua velocidade e capacidade de lidar com renderização moderna. Esta foi a versão definitiva.

## ✨ Funcionalidades

### 1. Auto-Reply (Playwright)
* Navegação e interação com elementos dinâmicos.
* **Performance:** Resposta em massa de aproximadamente **2000 avaliações em poucos minutos**.

### 2. Data Extraction (Selenium)
Script complementar para auditar as respostas e gerar relatórios. Extrai:
* Nome do Cliente
* Nome do Produto comprado
* Comentário original (caso exista)
* Resposta enviada pelo vendedor

## 🛠️ Tecnologias Utilizadas
* **Python**
* **Playwright** (Automação de alta performance)
* **Selenium WebDriver** (Scraping de dados estruturados)
* **PyAutoGUI** (Prototipagem inicial)

---
*Este projeto foi desenvolvido com o auxílio de IA para resolver uma demanda real de negócio, reduzindo drasticamente o tempo operacional de SAC.*
