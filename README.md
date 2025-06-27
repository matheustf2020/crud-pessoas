# 📝 Sistema CRUD com Django

Este é um sistema simples de cadastro de pessoas, desenvolvido com Django como prática para consolidar conhecimentos em lógica de programação, views, URLs, templates, formulários e integração com banco de dados usando ORM.
Desenvolvido Por Matheus Trindade.
---

## ✨ Funcionalidades

- ✅ Cadastro de pessoas com nome, email e senha
- ✅ Listagem de todas as pessoas cadastradas
- ✅ Edição de dados com validações
- ✅ Exclusão de pessoas com confirmação
- ✅ Validação para nome duplicado e senha com mínimo de 4 caracteres
- ✅ Interface simples e responsiva com HTML + CSS puro

---

## 🛠 Tecnologias utilizadas

- [Python 3.10+](https://www.python.org/)
- [Django 4+](https://www.djangoproject.com/)
- [SQLite3](https://www.sqlite.org/) (banco de dados embutido)
- HTML5 e CSS3 (sem frameworks)

---
27-06-2025 (Adicionado)
---

## 🔁 Relacionamentos criados

- `Pessoa` ↔ `Projetos` → **ManyToManyField**
- Uma pessoa pode participar de vários projetos
- Um projeto pode conter várias pessoas na equipe

---

## 💻 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/matheustf2020/crud-pessoas.git
cd crud-pessoas

2. Crie e ative um ambiente virtual (recomendado)
python -m venv venv
# Ativando no Windows
venv\Scripts\activate
# Ativando no Linux/macOS
source venv/bin/activate

3. Instale as dependências
pip install -r requirements.txt

4. Rode as migrações
python manage.py migrate

5. Inicie o servidor local
python manage.py runserver
