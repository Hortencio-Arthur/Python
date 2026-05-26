# Sistema de Gerenciamento Acadêmico

Este é um motor de lógica modular desenvolvido em Python para automação e consolidação de relatórios escolares. O sistema adota as melhores práticas de desenvolvimento, aplicando o **Princípio da Responsabilidade Única (SRP)** e seguindo as diretrizes de estilo da **PEP 8**.

---

## O que o Sistema Faz

O sistema processa dados de estudantes de forma automatizada por meio de três funções principais:
1. **`calcular_media(notas)`**: Realiza o cálculo aritmético com proteção integrada contra listas vazias.
2. **`verificar_aprovacao(media, media_minima)`**: Valida a situação do aluno com base em um critério de corte flexível (padrão `7.0`).
3. **`gerar_relatorio(alunos)`**: Consolida as informações e exibe um relatório formatado e limpo no terminal.

---

## Pré-requisitos

Para executar este projeto, você precisa ter instalado em sua máquina:
* **Python 3.8** ou superior.
* Um terminal (Prompt de Comando, PowerShell ou Terminal do Linux/macOS).

*Nota: O sistema utiliza exclusivamente módulos nativos do Python, portanto, não é necessária a instalação de dependências externas.*

---

## Como Executar o Código e o Ambiente de Testes

Para rodar a aplicação e visualizar o relatório com os dados de teste formatados, execute os comandos abaixo diretamente no seu terminal:

```bash
# 1. Navegue até a pasta onde o arquivo sistema_academico.py foi salvo
cd /caminho/da/sua/pasta

# 2. Execute o script principal para gerar o relatório no terminal
python sistema_academico.py