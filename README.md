# LuminaryHomesKL — KL Housing Price Prediction

A machine learning web app that predicts residential property prices in Kuala Lumpur. The project covers the full pipeline: raw data cleaning, model training/comparison (Linear Regression, Random Forest, XGBoost), and a Streamlit web app for predictions and market insights.

## Features

- **Prediction** — Enter a property's location, rooms, bathrooms, car parks, type, furnishing, and size to get an estimated price (RM) from a trained XGBoost model.
- **Dashboard** — Interactive Plotly charts (average price by location, room/bathroom/car-park distribution by furnishing, size-type split, price by property type) built from the cleaned KL housing dataset.
- **About** — Background information on the project.
- **Power BI dashboard** (`dashboard.pbix`) — an additional, standalone visual dashboard of the housing data.

## Project Structure

```
KL_Housing_Price/
├── main.py                          # Streamlit app entry point (sidebar menu, routing, styling)
├── prediction_page.py                # Price prediction form + model inference
├── dashboard_page.py                 # Plotly-based analytics dashboard
├── dashboard_page_pbix.py            # Embeds/links the Power BI dashboard
├── about_page.py                     # About page content
├── recommendation_page.py            # Recommendation page (not currently wired into main.py)
├── KL__Housing_Price_XGBoost.ipynb   # Data cleaning, EDA, and model training notebook
├── house_price_prediction_model.sav  # Trained model (pickle), loaded by prediction_page.py
├── housing_data.csv                  # Cleaned/encoded dataset used to train the model
├── housing_info.csv                  # Human-readable dataset (unencoded labels), used by the dashboard
├── dashboard.pbix                    # Power BI dashboard file
├── image/                            # Background and illustration images used in the UI
├── requirements.txt                  # Python dependencies
└── package.json                      # Front-end dependency (bootstrap-icons) used for menu icons
```

## Data & Model

The dataset is scraped Kuala Lumpur property listings. In the notebook (`KL__Housing_Price_XGBoost.ipynb`):

1. **Cleaning** — prices converted from `"RM 1,250,000"` strings to numeric, location strings trimmed to the main area name, room counts like `"4+1"` parsed and averaged, size strings (e.g. `"Built-up : 1,335 sq. ft."`) split into `SizeType` and `SizeValue`, and missing `Car Parks`/`Furnishing` values imputed.
2. **Encoding** — categorical columns (`Location`, `Property Type`, `Furnishing`, `SizeType`) label-encoded to numeric IDs.
3. **Modeling** — Linear Regression, Random Forest, and XGBoost were trained and compared using `GridSearchCV` for hyperparameter tuning; XGBoost gave the best R² and error metrics and was selected as the final model.
4. **Export** — the trained XGBoost model is serialized with `pickle` to `house_price_prediction_model.sav`, which the Streamlit app loads directly.

**Model input order:** `Location (encoded), Rooms, Bathrooms, Car Parks, Property Type (encoded), Furnishing (encoded), SizeType (encoded), SizeValue`

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation
```bash
cd KL_Housing_Price
pip install -r requirements.txt
```

### Run the app
```bash
streamlit run main.py
```
The app will open in your browser (default: `http://localhost:8501`).

## Tech Stack

- **App/UI:** Streamlit, streamlit-option-menu, Bootstrap Icons
- **Data & ML:** pandas, NumPy, scikit-learn, XGBoost
- **Visualization:** Plotly Express, Power BI
- **Model persistence:** pickle

## Notes

- The location dropdown in `prediction_page.py` currently lists a small subset of areas; the underlying model was trained on many more locations (see `housing_info.csv` for the full list and their encoded IDs), so this list can be extended to match.
- `recommendation_page.py` exists in the codebase but isn't currently linked from the sidebar menu in `main.py`.
