import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import warnings

warnings.filterwarnings("ignore")

# 1. Load dataset
df = pd.read_csv("C:/Users/91960/Documents/College/DSA- Intern Prep/Python Projects/Historical Product Demand.csv")
print("First 5 rows:\n", df.head())

# 2. Preprocessing
df.columns = df.columns.str.lower()
df['date'] = pd.to_datetime(df['date'])

# 3. Basic info
print("\nData types and missing values:")
print(df.info())
print("\nMissing values per column:\n", df.isnull().sum())

# 4. Plot sales value counts
plt.figure(figsize=(10,5))
df['sales'].astype(str).value_counts().head(20).plot(kind='bar')
plt.title('Top 20 Sales Values Frequencies')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# 5. Filter for one store-item pair for ARIMA
store_id = 1
item_id = 1
df_filtered = df[(df['store'] == store_id) & (df['item'] == item_id)].copy()

# 6. Aggregate daily sales (time series)
df_daily = df_filtered.groupby('date')['sales'].sum().asfreq('D').fillna(0)

# 7. Plot daily sales
plt.figure(figsize=(12,5))
df_daily.plot(title=f'Daily Sales for Store {store_id}, Item {item_id}')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# 8. ARIMA model for forecasting
train = df_daily[:-90]
test = df_daily[-90:]

model = ARIMA(train, order=(5,1,0))
model_fit = model.fit()
forecast = model_fit.forecast(steps=90)
forecast.index = test.index

plt.figure(figsize=(12,5))
plt.plot(train.index, train, label='Train')
plt.plot(test.index, test, label='Test', color='green')
plt.plot(forecast.index, forecast, label='ARIMA Forecast', color='red')
plt.title(f'ARIMA Sales Forecast for Store {store_id}, Item {item_id}')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()

print("ARIMA Model Performance:")
rmse_arima = mean_squared_error(test, forecast) ** 0.5  # manual RMSE calculation
r2_arima = r2_score(test, forecast)
print(f"Test RMSE: {rmse_arima:.2f}")
print(f"Test R2 Score: {r2_arima:.2f}")

# --- Regression based ML model on whole dataset ---

print("\n--- Regression Model Training ---")

# 9. Feature engineering
df['day_of_week'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month
df['day_of_month'] = df['date'].dt.day
df['week_of_year'] = df['date'].dt.isocalendar().week.astype(int)

# 10. Features and target
features = ['store', 'item', 'day_of_week', 'month', 'day_of_month', 'week_of_year']
target = 'sales'

X = df[features]
y = df[target]

# 11. Split data into train and test sets (e.g., 80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 12. Train Random Forest Regressor
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 13. Predict and evaluate
y_pred = rf.predict(X_test)

print(f"Random Forest Regression Performance:")
rmse_rf = mean_squared_error(y_test, y_pred) ** 0.5  # manual RMSE
r2_rf = r2_score(y_test, y_pred)
print(f"Test RMSE: {rmse_rf:.2f}")
print(f"Test R2 Score: {r2_rf:.2f}")

# 14. Plot actual vs predicted (sample of 1000 points for clarity)
plt.figure(figsize=(10,6))
plt.scatter(y_test[:1000], y_pred[:1000], alpha=0.5)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Random Forest Regression: Actual vs Predicted Sales (Sample)")
plt.plot([0, max(y_test[:1000])], [0, max(y_test[:1000])], color='red')  # diagonal line
plt.show()
