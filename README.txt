Evaluation of clustering as a pre-processing method for forecasting Covid-19 infection trends.

If a country could predict Covid-19 infection trends, it would be more prepared in the form of e.g. capacity in testing facilities and officials could take timely and preventable measures and thus ensure the country's safety. However, there doesn't exist a lot of Covid-19 data on infection trends for a forecasting method to be trained on. Thus, if one could cluster countries based on their similarity of infection trends, the forecasting might perform better because it would have more training data that is similar.

This project researches exactly this. The project develops clusters using both the K-means and Hierarchical Agglomerative Clustering (HAC) method. The forecasting is performed using the Catboost Regressor model. Countries are being clustered based on how similar their time series of infection trend are. To test the forecasts, four test countries were selected as randomly as possible, while still making sure that other conditions remained as fair as possible. Thus, each distinct cluster only contains one of the four test countries each. Thus, if test country 1 belongs to cluster 1 in K-means, then test country 2 could only belong to either cluster 2, 3, or 4 in K-means. To evaluate, the forecasting based on clustering are compared with the forecast based on both all countries as an input and a single country as an input.


The dataset used for this project, Data.csv, is downloaded from: 
https://www.kaggle.com/sambelkacem/covid19-algeria-and-world-dataset
The data.csv file was downloaded the 21st of September and had been updated on the downloadpage since. To reproduce the results, use the data.csv file stored in data -> data_raw.csv. This is the raw dataframe which was downloaded on the 21st of September.

How to look at the project:
In combination with project paper:
    Raw data: data -> data_raw.csv
    Pre-prossesing: pre_processing folder -> preprocessing notebook -> forecasting_format_cases per day notebook -> adding_features notebook. All resulting dataframes are stored in data folder.
    Hyperparameter optimization: clustering -> determining_k. clustering -> parameter_selection -> k_means_parameter_testing, hierarchical_parameter_testing and cluster_evaluation_results
    Alternative clustering appraoches: clustering -> parameter_selection -> gmm_forecasting_testing and k_shape_forecasting_testing.
    Clustering (objective resutls): clustering-> clustering_k_means and clustering_hierarchical. All obtained result dataframes stored in results -> clustering_results
    Forecasting (objective results): forecasting-> forecasting_w_catboost_all_countries, forecasting_w_catboost_clusters and forecasting_w_catboost_single_country. All obtained result dataframes stored in results -> forecasting_results
    
For reproduability:
The project is build up of notebooks that have dependencies between them if execution without saved results is desirable. Following the described order to regenerate all results. 
    -pre_processing -> preprocessing
        Notebook goes through all the preprocessing steps that have been performed on the raw dataset.
    -pre_processing -> forecasting_format_cases per day
        Changes the format of the preprocessed data to a format that can be used for forecasting.
    -pre_processing -> adding_features 
        Takes pre-processed data in forecasting format and adds features.
    
    -clustering -> determining_k
        Notebook that determines optimal k using elbow method.
    -clustering -> parameter_selection (file)
        Five notbooks in total. Three notbooks, k_means_parameter_testing and hierarchical_parameter_testing both used to test different hyperparameter combinations for the two clustering methods. Clusters are formed and used as input to forecast to compare achieved accuracy. Results from all executions are stored in cluster_evaluation_results notebook. Last to notebooks, respectivly k_shape_forecasting_testing and gmm_forecasting_testing, used to test clustering based on k-shape and gmm in combination with forecasting.
    -clustering -> clustering_hierarchical and clustering_k_means
        Notebooks that perform respectively hierarchical and k-means clustering using the optimal parameters found in parameter_selection. Results saved to be used in forecasting.
   
    -forecasting -> forecasting_w_catboos_all_countries
        Notebook executing forecasting with Catboost regressor. The model is trained and tested four times, trained on all available data, tested on the four test countries.
    -forecasting -> forecasting_w_catboos_single_country
        Notebook executing forecasting with Catboost regressor. The model is trained and tested four times, trained on 4 single countries and tested on the same four test countries.
    -forecasting -> forecasting_w_catboos_clusters
        Notebook executing forecasting with Catboost regressor. The model is trained and tested eight times, trained on each of the k-means and hierarchical clusters, and tested on the four test countries.

All clustering and forecasting results from running respectively notebooks (parquet files) can be found in 'results' folder, results (parquet files) of running notebooks in pre_processing folder can be found in 'data' folder.

Additional material:
    -misc -> cluster_mapping and cluster_mapping_func
        Notebook with function to generate map of cluster results
    -misc -> country_mapping and country_mapping_func
        Notebook with function to generate map to visualize all countries that the project has data for
    -misc -> generating_lookup_tabel and extract_func
        Notebook with function to extract information about each country including: 'Continent', 'Latitude', 'Longitude', 'Average temperature per year', 'Hospital beds per 1000 people', 'Medical doctors per 1000 people', 'GDP/Capita','Population', 'Median age', 'Population aged 65 and over (%)'
