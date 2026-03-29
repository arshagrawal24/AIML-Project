import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

def main():
    
    print("="*50)
    print("  AI REAL ESTATE PREDICTION ENGINE ONLINE  ")
    print("="*50)

    print("\n[STATUS] Accessing Dataset.csv...")
    df = pd.read_csv("Dataset.csv")
    
    features = ['Area', 'BHK', 'Bathroom', 'Parking', 'Per_Sqft']
    target = 'Price'
    

    initial_count = len(df)
    df = df[features + [target]].dropna()
    cleaned_count = len(df)
    
    print(f"[DATA] Total Records Found: {initial_count}")
    print(f"[DATA] Cleaned Records Available: {cleaned_count}")
    print(f"[DATA] Features Selected: {', '.join(features)}")

    

    print("\n[TRAINING] Initializing Linear Regression Model...")
    X = df[features]
    y = df[target]

    # Splitting data into Training (80%) and Testing (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    print("[SUCCESS] Model Weights and Intercepts Calculated.")

    print("\n[EVALUATION] Validating Model Accuracy...")
    predictions = model.predict(X_test)
    
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)

    print(f"📈 R-Squared Score: {round(r2, 4)} ({round(r2 * 100, 2)}%)")
    print(f"📈 Mean Absolute Error (MAE): ₹{round(mae, 2)}")

    print("\n[READY] Entering User Input Interface...")
    print("="*50)

    while True:
        try:
            print("\n--- Enter Property Specifications ---")
            area = float(input("   ➤ Total Area (sq ft): "))
            bhk  = int(input("   ➤ Number of BHK: "))
            bath = int(input("   ➤ Number of Bathrooms: "))
            park = int(input("   ➤ Parking Spaces: "))
            psq  = float(input("   ➤ Price Per Sq Ft: "))

            user_input = pd.DataFrame([[area, bhk, bath, park, psq]], columns=features)
            
            
            result = model.predict(user_input)[0]

            print("-" * 40)
            print(f"   ESTIMATED MARKET VALUE: ₹{round(result, 2):,}")
            print("-" * 40)

        except ValueError:
            print("⚠️ ERROR: Please enter valid numerical values.")
            continue
        
        
        retry = input("\nWould you like to run another prediction? (y/n): ").lower()
        if retry != 'y':
            break

    print("\n" + "="*50)
    print("   AI PREDICTION ENGINE SHUTTING DOWN. GOODBYE!  ")
    print("="*50)

if __name__ == "__main__":
    main()