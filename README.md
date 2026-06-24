# Project Kelly — Absenteeism Forecast Dashboard

Dashboard interattiva per il monitoraggio e la previsione dell'assenteismo nei magazzini Luxottica/EssilorLuxottica.

---

## Prerequisiti

- **Python 3.11** (consigliato) o Python 3.10+
- Connessione internet (solo al primo avvio, per scaricare i dati meteo)

---

## Installazione (solo la prima volta)

Apri un terminale nella cartella `kelly_dashboard/` ed esegui:

```bash
cd kelly_dashboard
pip install -r requirements.txt
```

> Consiglio: usa un ambiente virtuale per non sporcare il tuo Python di sistema.
>
> ```bash
> python -m venv .venv
> # Windows:
> .venv\Scripts\activate
> # Mac/Linux:
> source .venv/bin/activate
>
> pip install -r requirements.txt
> ```

---

## Avvio

```bash
cd kelly_dashboard
python app.py
```

Poi apri il browser su **http://localhost:8050**

---

## Struttura

```
kelly_dashboard/          ← entra qui prima di eseguire
├── app.py                ← entry point
├── requirements.txt
├── theme.py              ← palette colori e layout Plotly
├── warehouses.py         ← lista magazzini (id, città, lat/lon)
├── data_loader.py        ← carica Excel o genera dati mock
├── weather_loader.py     ← API Open-Meteo (meteo 8 giorni, CSV cache)
├── holidays_loader.py    ← API Nager.Date (festività per paese)
├── pages/
│   ├── landing.py        ← pagina globo (selezione magazzino)
│   ├── forecast.py       ← dashboard previsione assenteismo
│   └── performance.py    ← analisi drift AI vs reale
├── components/           ← widget riusabili (grafici, meteo, festività)
├── assets/               ← CSS, font, JS
└── weather_data/         ← CSV generati automaticamente (cache meteo)
```

---

## Dati

- **Columbus (OH)**: dati reali da file Excel (`Kelly_Columbus_v1.3_daily_05-24-2026.xlsx`). Posiziona il file nella cartella `kelly_dashboard/`.
- **Atlanta, Dallas, Sedico, Tijuana**: dati mock generati automaticamente.

---

## Note

- Il meteo viene scaricato automaticamente la prima volta che apri un magazzino e salvato in `weather_data/`. Le chiamate successive usano la cache locale.
- Le festività vengono caricate in tempo reale dall'API pubblica [Nager.Date](https://date.nager.at) (no token richiesto).
- Per Databricks Apps: usa la variabile `server` esportata da `app.py`.
