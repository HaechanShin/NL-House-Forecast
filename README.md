# NL-House-Forecast
For the best investment in Netherlands

## Overview
This project aims to forecast house prices in the Netherlands using data from Funda.nl. The pipeline includes data collection, cleaning, modeling, and deployment.

## Project Structure
```
NL-House-Forecast/
├── data/
│   ├── raw/          # Raw scraped data from Funda
│   └── processed/    # Cleaned and processed data
├── notebooks/        # Jupyter notebooks for exploration
├── scripts/          # Data collection and utility scripts
├── src/              # Source code for models and utilities
├── requirements.txt  # Project dependencies
└── README.md
```

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your preferred settings
```

## Data Collection

### Using Funda Scraper
The project uses the `funda-scraper` library to collect house listing data from Funda.nl.

**Important Note:** This is for educational/research purposes only. Please respect Funda's terms of service.

### Collect Data from Single City
```bash
cd scripts
python collect_funda_data.py
```

Edit the script to uncomment the desired collection method:
- **Option 1:** Single city (Amsterdam, Rotterdam, etc.)
- **Option 2:** Multiple cities combined

### Available Cities
- amsterdam
- rotterdam
- utrecht
- den-haag
- eindhoven
- And more...

## Pipeline Stages

### 1. Data Collection ✓
- Scrape house listings from Funda.nl
- Multiple cities support
- Save raw data to CSV

### 2. Data Cleaning (Coming Soon)
- Handle missing values
- Feature engineering
- Outlier detection

### 3. Price Forecasting (Coming Soon)
- Model options:
  - Machine Learning (XGBoost, Random Forest)
  - Deep Learning (Neural Networks)
  - Statistical Models (ARIMA, Prophet)

### 4. Deployment (Coming Soon)
- REST API
- Web interface
- Model serving

## Usage

### Collect Data
```python
from funda_scraper import FundaScraper

scraper = FundaScraper(area="amsterdam", want_to="buy", n_pages=5)
df = scraper.run()
df.to_csv("data/raw/amsterdam_houses.csv", index=False)
```

## Contributing
Feel free to open issues or submit pull requests!

## License
See LICENSE file for details.

## Disclaimer
This project is for educational purposes only. Please respect the terms of service of data sources.
