# 🤝 Contributing to Cliff-Pay

Thank you for your interest in contributing to **Cliff-Pay**! Contributions are what make the open-source community an amazing place to learn, inspire, and create. Every contribution — whether it's a bug fix, a feature, or a documentation improvement — is valued.

---

## 📋 Table of Contents

- [Code of Conduct](#-code-of-conduct)
- [Getting Started](#-getting-started)
- [How to Contribute](#-how-to-contribute)
- [Development Workflow](#-development-workflow)
- [Style Guide](#-style-guide)
- [Commit Messages](#-commit-messages)
- [Pull Request Process](#-pull-request-process)

---

## 📜 Code of Conduct

By participating in this project, you agree to maintain a welcoming, respectful, and harassment-free environment. Be kind, be constructive, and assume good intentions.

---

## 🚀 Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/Cliff-Pay.git
   cd Cliff-Pay
   ```
3. **Set up** the development environment (see [README.md](README.md#-local-setup--installation) for full instructions):
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
4. **Create a branch** for your work:
   ```bash
   git checkout -b feature/your-feature-name
   ```

---

## 💡 How to Contribute

### 🐛 Report Bugs

- Search [existing issues](https://github.com/cliff-de-tech/Cliff-Pay/issues) first to avoid duplicates.
- Open a new issue with a clear title, steps to reproduce, expected behavior, and actual behavior.

### ✨ Suggest Features

- Open an issue with the **Feature Request** label.
- Describe the problem you're trying to solve and your proposed solution.

### 🔧 Submit Code

- Fix a bug, implement a feature, or improve documentation.
- Follow the [Development Workflow](#-development-workflow) below.

---

## 🔄 Development Workflow

1. Make sure your fork is up to date with the `main` branch:
   ```bash
   git remote add upstream https://github.com/cliff-de-tech/Cliff-Pay.git
   git fetch upstream
   git merge upstream/main
   ```
2. Make your changes in a dedicated feature branch.
3. **Test your changes** — ensure the server runs and endpoints work as expected:
   ```bash
   python manage.py test
   ```
4. Commit and push:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   git push origin feature/your-feature-name
   ```
5. Open a **Pull Request** against the `main` branch.

---

## 🎨 Style Guide

- **Python**: Follow [PEP 8](https://peps.python.org/pep-0008/). Use 4-space indentation.
- **Django/DRF**: Follow Django's coding conventions. Use class-based views where appropriate.
- **Naming**: Use descriptive names for variables, functions, and classes. Avoid abbreviations.
- **Imports**: Group imports in this order — standard library, third-party, local — separated by blank lines.

---

## 📝 Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

| Prefix     | Usage                                |
|------------|--------------------------------------|
| `feat:`    | A new feature                        |
| `fix:`     | A bug fix                            |
| `docs:`    | Documentation changes only           |
| `style:`   | Formatting, whitespace (no logic)    |
| `refactor:`| Code change that neither fixes nor adds |
| `test:`    | Adding or updating tests             |
| `chore:`   | Maintenance tasks, configs           |

**Example:**
```
feat: add transaction history pagination
fix: prevent negative balance on P2P transfer
docs: update API endpoints table in README
```

---

## 🔀 Pull Request Process

1. Ensure your branch is up to date with `main`.
2. Fill out the PR description — explain **what** you changed and **why**.
3. Reference any related issues (e.g., `Closes #12`).
4. Wait for a review. Be open to feedback and requested changes.
5. Once approved, your PR will be merged. 🎉

---

## 🙏 Thank You

Your contributions make Cliff-Pay better for everyone. Whether it's your first open-source PR or your hundredth — welcome, and thank you!
