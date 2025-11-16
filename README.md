<h1 align="center">I'm Parbat Karki! 👋</h1>

<p align="center">
A passionate learner & developer from Nepal 🇳🇵  
</p>

---

### 🚀 About Me  
- 🔭 Currently working on **Web Projects & GitHub Automation**  
- 🌱 Learning **JavaScript, Html,css,python**  
- 💬 Ask me about **Coding, GitHub, Automation**  
- ⚡ Fun fact: **Errors fear me 😎**

---

### 📫 Connect  
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

# ⚡ Stats  
<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=karkiparbat&theme=tokyonight&hide_border=true" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=karkiparbat&show_icons=true&theme=tokyonight&hide_border=true" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=karkiparbat&layout=compact&theme=tokyonight&hide_border=true" />
</p>

---

# Hi there 👋

## 🐍 GitHub Contribution Snake
![snake animation](./dist/snake.svg)
name: Generate Snake Animation

on:
  schedule:
    - cron: "0 */12 * * *"   # updates every 12 hours
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: write     # 🔥 mandatory (fixes commit/push error)

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Generate snake.svg
        uses: Platane/snk/svg-only@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: dist/snake.svg

      - name: Commit and push snake.svg
        run: |
          git config --global user.name "github-actions"
          git config --global user.email "github-actions@github.com"
          git add dist/snake.svg
          git commit -m "🐍 Update snake animation" || echo "No changes to commit"
          git push





