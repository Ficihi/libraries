# libraries
Tento projekt obsahuje extraktor dát z API Golemio (https://api.golemio.cz/docs/openapi/#/%F0%9F%8F%A2%EF%B8%8F%20Municipal%20Libraries%20(v2)), ktorý beží automaticky každý deň o 7:00 ráno (pražského času) cez GitHub Actions.

Workflow je definovaný v súbore:
  .github/workflows/extractor.yml

Skript je možné spustiť aj manuálne cez GitHub:
  - prejdite na záložku "Actions"
  - vyberte "Daily Extractor"
  - kliknite na tlačidlo "Run workflow"
