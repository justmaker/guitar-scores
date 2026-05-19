# 🎸 吉他譜集

個人吉他學習譜集，使用 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 建置。

## 本地預覽

```bash
pip install mkdocs-material
mkdocs serve
```

瀏覽 http://localhost:8000

## 新增譜

在 `docs/` 對應難度資料夾下新增 `.md` 檔，push 到 main 即自動部署。

## 部署

GitHub Pages 自動透過 GitHub Actions 部署。

首次設定：repo Settings → Pages → Source 選「GitHub Actions」。
