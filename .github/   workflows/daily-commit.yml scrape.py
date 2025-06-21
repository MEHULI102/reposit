name: Daily Commit by 23f3003748@ds.study.iitm.ac.in

on:
  schedule:
    - cron: '5 0 * * *'  # Every day at 00:05 UTC
  workflow_dispatch:

jobs:
  auto-commit:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Modify dummy file - 23f3003748@ds.study.iitm.ac.in
        run: |
          echo "Update at $(date)" >> daily-log.txt

      - name: Commit and push changes
        run: |
          git config --local user.name "github-actions[bot]"
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git add daily-log.txt
          git commit -m "Daily auto-update [skip ci]" || echo "No changes to commit"
          git push
