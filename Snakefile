DATA_FILES = ['item_categories', 'items', 'sales_train', 'sample_submission', 'shops', 'test']

rule data:
    input:
    output:
        expand('data/raw/{filename}.csv', filename=DATA_FILES), 'data/external/num_residents.csv'
    shell:
        """ 
        mkdir -p data/external
        mkdir -p data/interim
        mkdir -p data/processed
        mkdir -p data/raw
        kaggle competitions download -c competitive-data-science-predict-future-sales -p data/raw
        unzip data/raw/* -d data/raw
        rm data/raw/competitive-data-science-predict-future-sales.zip
        kaggle datasets download dmitrybunin/predict-future-sales-num-residents -p data/external --unzip
        """
