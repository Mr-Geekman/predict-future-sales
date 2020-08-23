DATA_FILES = ['item_categories', 'items', 'sales_train', 'sample_submission', 'shops', 'test']

rule data:
    input:
    output:
        expand('data/raw/{filename}.csv', filename=DATA_FILES)
    shell:
        """ 
        mkdir data
        mkdir data/raw
        mkdir data/external
        mkdir data/interim
        mkdir data/processed
        cd data/raw
        kaggle competitions download -c competitive-data-science-predict-future-sales
        unzip competitive-data-science-predict-future-sales.zip
        rm competitive-data-science-predict-future-sales.zip
        """
