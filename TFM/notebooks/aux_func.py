import os
import pickle
import geopandas as gpd
import fiona
from sklearn.neighbors import BallTree
import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt

def save_data(data, filename):
    """a function that saves geodataframe as geojson and pickle file.both files will have save name and different format"""
    # Set the directory path
    dir_path = '../data/processed'
    
    # If the directory does not exist, create it
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)    
    
    # saving in geojson format
    # Infer the schema from your GeoDataFrame
    schema = gpd.io.file.infer_schema(data)

    geojson_path = os.path.join(dir_path, f"{filename}.geojson")
    with fiona.open(geojson_path, 'w', 
                    driver='GeoJSON', 
                    crs='EPSG:4326', 
                    schema=schema) as file:
        # Iterate over each row (record) in the GeoDataFrame
        for record in data.iterfeatures():
            file.write(record)

    # Save data to a pickle file to be called from other notebooks.
    pickle_path = os.path.join(dir_path, f"{filename}.pickle")
    with open(pickle_path, 'wb') as f:
        pickle.dump(data, f)
        
    print(f"Data saved as {geojson_path} and {pickle_path}")

# Example usage:
# save_data(data, "dataset")



def add_nearest_distance(data, data_reference, lat_column='latitude', lon_column='longitude', new_column='nearest_distance', metric='euclidean'):
    """A funcion that adds a column to a DataFrame with the euclidian distance to the nearest point in another DataFrame."""
    # Extract latitude and longitude from geometry if not already present
    for df in [data, data_reference]:
        if lat_column not in df.columns or lon_column not in df.columns:
            if 'geometry' in df.columns:
                df[lon_column] = df['geometry'].centroid.x
                df[lat_column] = df['geometry'].centroid.y
            else:
                raise ValueError(f"Both '{lat_column}' and '{lon_column}' are missing and there is no 'geometry' column to calculate them from.")

    # Create a BallTree with the reference data
    tree = BallTree(data_reference[[lat_column, lon_column]].values, metric=metric)

    # Query the BallTree for the nearest point in data_reference for each point in data
    dist, ind = tree.query(data[[lat_column, lon_column]].values, k=1) # k=1 means find only the nearest point

    # 'dist' will contain the distances to the nearest points. We flatten it before adding to the DataFrame
    # These distances are in the same units as the latitude and longitude
    data[new_column] = dist.flatten()

    return data

def data_summary(df):
    """
    This function takes a DataFrame and prints the data types, number of missing values
    and percentage of missing values for each column.
    """
    summary = pd.DataFrame(df.dtypes, columns=['Dtype'])
    summary = summary.reset_index()
    summary['Column'] = summary['index']
    summary = summary[['Column','Dtype']]
    summary['Missing'] = df.isnull().sum().values    
    summary['Missing Percentage'] = (df.isnull().sum().values / df.shape[0]) * 100
    summary['Distinct Count'] = df.nunique().values
    return summary


def plot_and_show_last(data):
    # Plot the data
    data.plot()
    plt.show()

    # Display the last 5 lines of the data
    return data.tail()

# Example usage:
# plot_and_show_last(data_elbistan)



def plot_continuous_for_damage_level(data, column, damage_level):
    """
    Plot the distribution of a continuous variable for different damage levels using boxplots.

    Parameters:
    - data: DataFrame containing the information.
    - column: The name of the continuous column.
    - damage_level: Column name that contains the damage levels.
    """

    plt.figure(figsize=(10,6))
    
    sns.boxplot(
        data=data, 
        x=damage_level, 
        y=column, 
        palette="coolwarm"
    )

    plt.title(f"Boxplot of {column} for different {damage_level}")
    plt.ylabel(column)
    plt.xlabel(damage_level)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.show()

# Example usage:
# Assuming 'building_height' is a continuous variable and 'damage_status' is the target variable.
# plot_continuous_for_damage_level(data, 'building_height', 'damage_status')

def remove_duplicates(df):
    """
    This function takes a DataFrame and returns a new DataFrame with duplicate rows removed.
    """
    print("Before removing duplicates, number of rows: ", df.shape[0])
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    print("After removing duplicates, number of rows: ", df.shape[0])
    
    return df


def plot_for_damage_level(data, column, damage_level):
    """
    Plot the distribution for the given damage level.

    Parameters:
    - data: DataFrame containing the information.
    - damage_level: Column name that contains the damage levels.
    """

    grouped_data = data.groupby([column, damage_level]).size().reset_index(name='count')

    distinct_values = grouped_data[damage_level].unique()

    for value in distinct_values:
        filtered_data = grouped_data[grouped_data[damage_level] == value]

        # Sort the filtered_data by 'count' in descending order
        filtered_data = filtered_data.sort_values(by='count', ascending=False)

        # Create the plot
        plt.figure(figsize=(10,6))
        sns.barplot(
            data=filtered_data, 
            x=column, y='count', 
            color="gray", alpha=.6
        )

        plt.title(f"Graph for {damage_level}: {value}")
        plt.ylabel("Count")
        plt.xlabel(f"Building Damage with {column}")
        plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
        plt.show()
    