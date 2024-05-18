# DANIEL RODRIGUEZ ESPINOSA

## Portfolio

```diff
+ Firsts steps with Reflex. +
```

<div align="center">
<img src="https://raw.githubusercontent.com/reflex-dev/reflex/main/docs/images/reflex_dark.svg#gh-light-mode-only" alt="Reflex Logo" width="150px">
<img src="https://raw.githubusercontent.com/reflex-dev/reflex/main/docs/images/reflex_light.svg#gh-dark-mode-only" alt="Reflex Logo" width="150px">

<hr>

### **✨ Performant, customizable web apps in pure Python. Deploy in seconds. ✨**
[![PyPI version](https://badge.fury.io/py/reflex.svg)](https://badge.fury.io/py/reflex)
![versions](https://img.shields.io/pypi/pyversions/reflex.svg)
[![Documentation](https://img.shields.io/badge/Documentation%20-Introduction%20-%20%23007ec6)](https://reflex.dev/docs/getting-started/introduction)
</div>

---

[English](https://github.com/reflex-dev/reflex/blob/main/README.md) | [简体中文](https://github.com/reflex-dev/reflex/blob/main/docs/zh/zh_cn/README.md) | [繁體中文](https://github.com/reflex-dev/reflex/blob/main/docs/zh/zh_tw/README.md) | [Türkçe](https://github.com/reflex-dev/reflex/blob/main/docs/tr/README.md) | [हिंदी](https://github.com/reflex-dev/reflex/blob/main/docs/in/README.md) | [Português (Brasil)](https://github.com/reflex-dev/reflex/blob/main/docs/pt/pt_br/README.md) | [Italiano](https://github.com/reflex-dev/reflex/blob/main/docs/it/README.md) | [Español](https://github.com/reflex-dev/reflex/blob/main/docs/es/README.md) | [한국어](https://github.com/reflex-dev/reflex/blob/main/docs/kr/README.md) | [日本語](https://github.com/reflex-dev/reflex/blob/main/docs/ja/README.md)

---

# Reflex

Reflex is a library to build full-stack web apps in pure Python.

Key features:
* **Pure Python** - Write your app's frontend and backend all in Python, no need to learn Javascript.
* **Full Flexibility** - Reflex is easy to get started with, but can also scale to complex apps.
* **Deploy Instantly** - After building, deploy your app with a [single command](https://reflex.dev/docs/hosting/deploy-quick-start/) or host it on your own server.

## ⚙️ Installation

Open a terminal and run (Python 3.8+):

```bash
pip install reflex
```

### 🥳 Create your first app

Installing `reflex` also installs the `reflex` command line tool.

Test that the install was successful by creating a new project. (Replace `my_app_name` with your project name):

```bash
mkdir my_app_name
cd my_app_name

python -m venv .venv
.venv\Scripts\activate

reflex init
```

This command initializes a template app in your new directory. 
You can run this app in development mode:

```bash
reflex run
```

You should see your app running at http://localhost:3000.

Now you can modify the source code in `link_bio_web/link_bio_web.py`. Reflex has fast refreshes so you can see your changes instantly when you save your code (**WSL**).


## 🫧 Example App

Let's go over an example: creating an image generation UI around [DALL·E](https://platform.openai.com/docs/guides/images/image-generation?context=node). For simplicity, we just call the [OpenAI API](https://platform.openai.com/docs/api-reference/authentication), but you could replace this with an ML model run locally.

&nbsp;

<div align="center">
<img src="https://raw.githubusercontent.com/reflex-dev/reflex/main/docs/images/dalle.gif" alt="A frontend wrapper for DALL·E, shown in the process of generating an image." width="550" />
</div>