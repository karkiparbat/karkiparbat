## Hi there 👋

<!--
**karkiparbat/karkiparbat** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
<h1 align="center">I'm Parbat Karki! 👋</h1>

<p align="center">
A passionate learner & developer from Nepal 🇳🇵  
</p>

---

### 🚀 About Me  
- 🔭 I’m currently working on **Web Projects & GitHub Automation**  
- 🌱 I’m learning **JavaScript, React, Tailwind, Firebase**  
- 💬 Ask me about **Coding, GitHub, Automation, Free Fire sensitivity 😄**  
- ⚡ Fun fact: **I fix errors faster than I create them!**

---

### 📫 Connect With Me  
<p align="left">
  <a href="mailto:karkiparbat048@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Portfolio-FF6F00?style=for-the-badge&logo=firefox-browser&logoColor=white" />
  </a>
</p>

---

## 🛠️ Languages • Frameworks • Tools  
<p align="left">
  <img src="https://skillicons.dev/icons?i=js,html,css,python,nodejs,react,bootstrap,github,git,firebase,mongodb,mysql,php,java,c,cpp,vscode" />
</p>

---

## 🐍 GitHub Contribution Snake  
![snake gif](https://github.com/karkiparbat/karkiparbat/blob/output/github-contribution-grid-snake.svg)
name: Generate Snake Animation

on:
  schedule:
    - cron: "0 */12 * * *"
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  generate:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Generate Snake
        uses: Platane/snk@v3
        with:
          github_user_name: karkiparbat
          outputs: |
            dist/github-contribution-grid-snake.svg

      - name: Push to main branch
        uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: main
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
