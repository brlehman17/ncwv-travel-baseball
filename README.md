# NCWV Travel Baseball

Static, interactive 2026 leaderboards for NCWV 8U, 9U, and 10U travel baseball.

## Refresh the data

From the GameChangerCrawler project root:

```powershell
python github-pages/ncwv-travel-baseball/scripts/build_data.py
```

Commit and push the regenerated JSON files. GitHub Actions will deploy the update.

## GitHub Pages setup

In the repository, open **Settings → Pages** and set **Source** to **GitHub Actions**. The workflow in `.github/workflows/pages.yml` deploys on every push to `main`.

The expected address is `https://brlehman17.github.io/ncwv-travel-baseball/`.
