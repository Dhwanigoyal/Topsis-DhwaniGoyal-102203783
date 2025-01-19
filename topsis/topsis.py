import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, result_file):
    # Read the input CSV file
    df = pd.read_csv(input_file)
    
    # Check that there are at least 3 columns
    if df.shape[1] < 3:
        raise ValueError("Input file must have at least 3 columns.")

    # Split the weights and impacts into lists
    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')
    
    # Validate the number of weights and impacts match the number of criteria (columns)
    if len(weights) != df.shape[1] - 1:
        raise ValueError("The number of weights must match the number of criteria.")
    
    if len(impacts) != df.shape[1] - 1:
        raise ValueError("The number of impacts must match the number of criteria.")
    
    # Check for non-numeric values in the data (except the first column)
    for col in df.columns[1:]:
        if not pd.to_numeric(df[col], errors='coerce').notnull().all():
            raise ValueError(f"Column '{col}' contains non-numeric values.")
    
    # Normalize the decision matrix
    norm_df = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').values
    norm = np.linalg.norm(norm_df, axis=0)
    norm_df = norm_df / norm
    
    # Weighted normalized decision matrix
    weighted_norm_df = norm_df * weights
    
    # Determine ideal and negative-ideal solutions
    ideal_solution = []
    negative_ideal_solution = []
    for i, impact in enumerate(impacts):
        if impact == '+':
            ideal_solution.append(np.max(weighted_norm_df[:, i]))
            negative_ideal_solution.append(np.min(weighted_norm_df[:, i]))
        else:
            ideal_solution.append(np.min(weighted_norm_df[:, i]))
            negative_ideal_solution.append(np.max(weighted_norm_df[:, i]))
    
    # Calculate the distance to the ideal and negative-ideal solutions
    dist_ideal = np.sqrt(np.sum((weighted_norm_df - ideal_solution) ** 2, axis=1))
    dist_negative_ideal = np.sqrt(np.sum((weighted_norm_df - negative_ideal_solution) ** 2, axis=1))
    
    # Calculate the Topsis score and rank
    topsis_score = dist_negative_ideal / (dist_ideal + dist_negative_ideal)
    df['Topsis Score'] = topsis_score
    df['Rank'] = topsis_score.rank(ascending=False)
    
    # Save the result to the specified output file
    df.to_csv(result_file, index=False)
    print(f"Result saved to {result_file}")
