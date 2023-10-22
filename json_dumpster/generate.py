import random
import json
import os

def generate_bp_data():
    # Parameters
    days = 30
    samples_per_day = 24
    flag_count = 0

    # Initialize the dataset
    bp_data = {
        "blood_pressure_data": {
            "blood_pressure_samples": [],
            "daily_avg_systolic": [],
            "daily_avg_diastolic": []
        }
    }

    # Generate the dataset
    for day in range(days):
        daily_total_systolic = 0
        daily_total_diastolic = 0
        for sample in range(samples_per_day):
            flag_count += 1
            if flag_count > 24:
                flag_count = 1

            # Generate systolic and diastolic values within the typical range for a healthy individual
            systolic_bp = round(random.uniform(90, 120), 2)
            diastolic_bp = round(random.uniform(60, 80), 2)

            daily_total_systolic += systolic_bp
            daily_total_diastolic += diastolic_bp

            entry = {
                "diastolic_bp": diastolic_bp,
                "systolic_bp": systolic_bp,
                "timestamp": f"2023-10-{day+21}T{sample:02}:00:00.000000+00:00"
            }
            bp_data["blood_pressure_data"]["blood_pressure_samples"].append(entry)

        # Calculate daily averages
        daily_avg_systolic = daily_total_systolic / samples_per_day
        daily_avg_diastolic = daily_total_diastolic / samples_per_day

        bp_data["blood_pressure_data"]["daily_avg_systolic"].append(round(daily_avg_systolic, 2))
        bp_data["blood_pressure_data"]["daily_avg_diastolic"].append(round(daily_avg_diastolic, 2))

    return bp_data

def save_to_file(data, directory="output_data", filename="bp_data.json"):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Define the full file path
    file_path = os.path.join(directory, filename)
    
    # Save data to JSON file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {file_path}")

# Run the function and save the output
if __name__ == "__main__":
    dataset = generate_bp_data()
    save_to_file(dataset)
