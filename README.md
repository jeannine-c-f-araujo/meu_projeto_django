# 🧑‍💼 Gerenciador de Funcionários — Django

Projeto desenvolvido em **Django** com o objetivo de realizar o **cadastro, listagem, edição e exclusão de funcionários**, aplicando conceitos fundamentais do framework, como **Views baseadas em classe, Templates, Filtros e Tags customizadas, Middleware e Bootstrap**.

---

## 📌 Funcionalidades

- Página inicial do sistema
- Cadastro de funcionários
- Listagem de funcionários
- Edição de dados
- Exclusão de registros
- Uso de **templates base**
- Filtro customizado (`primeira_letra`)
- Tag customizada (`tempo_atual`)
- Middleware simples para logging
- Interface estilizada com **Bootstrap**

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **Django 5.2**
- HTML5
- CSS3
- Bootstrap
- SQLite (banco de dados padrão)
- Git / GitHub

---

## 📂 Estrutura do Projeto

```text
meu_projeto_django/
├── manage.py
├── website/
│   ├── templates/
│   │   └── website/
│   │       ├── _layouts/
│   │       │   └── base.html
│   │       ├── index.html
│   │       ├── lista.html
│   │       └── cria.html
│   ├── templatetags/
│   │   ├── primeira_letra.py
│   │   └── tempo_atual.py
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   └── urls.py
├── static/
│   └── website/
│       ├── css/
│       └── js/
└── db.sqlite3
