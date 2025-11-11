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
<!-- README.md -->
<h1 align="center">👋 Hi, I'm Parbat Karki</h1>
<h3 align="center">A passionate developer & entrepreneur from Pokhara, Nepal 🇳🇵</h3>

---

### 💫 About Me  
- 🔭 I’m currently working on **NepTrade Hub**  
- 🌱 I’m learning **React, Tailwind CSS, Node.js, and MongoDB**  
- 💬 Ask me about **Dropshipping, Web Development, or Business Ideas**  
- ⚡ Fun fact: I love creating online businesses and designing digital products  

📧 **Reach me at:** [karkiparbat048@gmail.com](mailto:karkiparbat048@gmail.com)  
🌐 **Connect with me:** [LinkedIn](https://linkedin.com/in/karkiparbat) | [Portfolio](https://karkiparbat.github.io)

---

### 🛠️ Languages & Tools  
<p align="center">
  <img src="https://skillicons.dev/icons?i=html,css,js,react,nodejs,express,mongodb,tailwind,git,github,vscode,figma,python" />
</p>

---

### 📊 GitHub Stats  

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=karkiparbat&show_icons=true&theme=tokyonight&hide_border=true" alt="GitHub Stats" />
  <img src="https://streak-stats.demolab.com?user=karkiparbat&theme=tokyonight&hide_border=true" alt="GitHub Streak" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=karkiparbat&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" />
</p>

---

### 🐍 GitHub Contribution Snake  
<p align="center">
  <img src="https://raw.githubusercontent.com/karkiparbat/karkiparbat/output/github-contribution-grid-snake.svg" alt="snake animation" />
</p>

---

⭐️ **From [karkiparbat](https://github.com/karkiparbat)**
name: Update GitHub Contribution Snake

on:
  schedule:
    - cron: '0 * * * *' # Every hour run
  workflow_dispatch:

jobs:
  update-snake:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install matplotlib numpy requests pillow

      - name: Generate snake SVG
        run: python .github/scripts/generate_snake_svg.py

      - name: Commit and Push
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add output/github-contribution-grid-snake.svg
          git commit -m "Update contribution snake" || echo "No changes to commit"
          git push



