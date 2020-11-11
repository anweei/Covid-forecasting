Project title: 

If a country could predict Covid-19 cases which will occur the next day(s), the county would be more prepared in the form of e.g. capacity in testing facilities. However,there doesn't exist a lot of Covid-19 data on infection trends for a forecasting method to be trained. Therefore, if it would be possible to cluster different countries together which have similar infections trends, more training data could be generated.

This project researches exactly this. The project forms clusters both using the K-means and hierarchical clustering method. The forecasting is performed using the Catboost Regressor model. To evaluate, the forecasting is performed when training on all data, four individual countries and the respective clusters. To test the forecasts, four test countries were selected as random as possible, with the criteria that each country needed to be present in only one of the four clusters. Eg. K-means produced four clusters, and therefore test country 1 could only be present in one of these clusters, test country 2 could only be present in one of the clusters and not in the same cluster as test country 1 and so on. 

The dataset used for this project, Data.csv, is downloaded from: 
https://www.kaggle.com/sambelkacem/covid19-algeria-and-world-dataset

How to look at the project:
The project is build up of notebooks that have dependencies between them if execution without saved results is desirabel. Following the descirbed order to regenerat all results. 
    -pre_processing -> preprocessing
        Notebook goes through all the the preprocessing steps that have been performed on the raw dataset.
    -pre_processing -> forecasting_format_cases per day
        Changes the format of the preprocessed data to a format that can be used for forecasting.
    -pre_processing -> adding_features 
        Takes pre-processed data in forecasting format and adds features.
    -clustering -> determining_k
        Notebook that determines optimal k using elbow method.
    -clustering -> parameter_selection (file)
        Three notbooks, k_means_parameter_testing and hierarchical_parameter_testing both used to test different hyperparameter combinations for the two clustering methods. Clusters are formed and used as input to forecast to compare achived accurazy. Results from all executions are stored in cluster_evaluation_results notebook. 
    -clustering -> clustering_hierarchical and clustering_k_means
        Notebooks that perform respectivly hierarchical and k-means clustering using the optimal parameters found in parameter_selection. Results saved to be used in forecasting.
    -forecasting -> forecasting_w_catboos_all_countries
        
    -forecasting -> forecasting_w_catboos_single_country
    -forecasting -> forecasting_w_catboos_clusters

All results from running notevooks (parquet files) can be found under results.

Additional material:
    -misc -> cluster_mapping and cluster_mapping_func
    -misc -> country_mapping and country_mapping_func
    -misc -> generating_lookup_tabel and extract_func
