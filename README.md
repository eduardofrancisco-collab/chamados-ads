# API de Chamados de Suporte (chamados-ads)

**Instituição:** Universidade Federal do Cariri - UFCA  
**Curso:** Análise e Desenvolvimento de Sistemas - ADS  
**Disciplina:** Desenvolvimento WEB  
**Aluno:** Francisco Eduardo da Silva  
**Matrícula:** 2023009600  

## Objetivo
Estrutura inicial da API de chamados de suporte desenvolvida com Python e Flask, com gerenciamento de ambiente e dependências via `uv`.

## Pré-requisitos
- Python 3.14+
- [uv](https://docs.astral.sh/uv/) instalado

## Instalação das Dependências
Com o `uv` instalado, execute na raiz do projeto:

```bash
uv sync --locked
```

## Execução da Aplicação
Para executar localmente:

```bash
uv run flask --app app run
```

Para executar no GitHub Codespaces:

```bash
uv run flask --app app run --host=0.0.0.0 --port=5000
```

## Acesso à Rota Inicial e Resposta Esperada
Com o servidor em execução, acesse a rota `GET /` pelo navegador (`http://localhost:5000/`) ou pelo terminal:

```bash
curl -i http://localhost:5000/
```

**Resposta esperada:**
- **Status HTTP:** `200 OK`
- **Cabeçalho:** `Content-Type: application/json`
- **Corpo (JSON):**
```json
{
  "mensagem": "API de chamados em funcionamento"
}
```


