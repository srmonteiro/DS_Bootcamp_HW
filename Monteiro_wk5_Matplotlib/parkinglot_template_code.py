###

Terminal Commands _________________________________________________________

    cd  
    ls 
    touch 
    mv  


Virtual Environments _________________________________________________________

    source activate PythonDataScience
    conda install -c conda-forge gmaps
    jupyter nbextension enable --py gmaps
    jupyter notebook list
    jupyter notebook stop
    pip install
    pip list

#___jupyter shortcuts_______________________
    b  # new row below
    a  # new row above
    dd # Delete row
    shift + enter  



MPLib MODULES _______________________________________________________________________

    %matplotlib notebook
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd


MPLib READ FILES _______________________________________________________________________

    df = pd.read_csv("Resources/filename.csv")
    df.head()

MPLib / Pandas Manipulators _________________________________________________________

    df.sum()
    df.mean()
    df['column name'].value_counts()
    df['column name'.numunique()
    df['column name'].unique()
    df.add(otherdf, fill_value = 0)
    df.groupby()
    df.groupby().agg({})
    df.keys
    df.set_index('column name')
    df.loc
    df.drop(df.index[])
    pd.to_numeric
    pd.merge(file1, file2, on='column name')                                         # or if col name diff // left_on = "colname"    right_on = "col name"
    del df['column']
    df.rename(columns={'column original':'Country Code'})
    df.shape                                                                         # number of rows, number of columns in a dataframe
    df.isna().sum()                                                                  # count of NaN missing values in each column
    df.dtypes                                                                        # the type of content in each column


MPLib PLOT TYPES ____________________________________________________________________

    plt.plot(kind=' ', )
    plt.bar()
    plt.pie()                                                                        # (members, explode=explode, labels=' ', colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.scatter()
    plt.xticks()
    plt.show()
    plt.legend(handles[]. loc="best)

MPLib / Pandas PLOT TYPES ___________________________________________________________



MPLib EMPTY ARRAY FOR X LABELS ______________________________________________________

    x_axis = np.arange
    tick_locations = []
    for x in x_axis 
        tick_locations

    x_axis = np.arange(len(rain_df))
    tick_locations = [value for value in x_axis]    

MPLib PLOT FORMATTING _______________________________________________________________

    plt.title(' ')
    plt.axis("equal")
    plt.xlabel(' ')
    plt.ylabel(' ')
    plt.hlines(0, 0, x_lim, alpha = 0.2)
    plt.xlim(-0.75, len()-0.25)
    plt.ylim(-0.75, len()-0.25)
    plt.tight_layout


MPLib EXPORT FILES _______________________________________________________________

    plt.savefig("../Images/lineConfig.png")



Pandas & MPLib PLOT _______________________________________________________________



# API week 6 session 1 _______________________________________________________________

#  #   API  :  Application Programming Interface
#              Basic Idea, you tell the computer to go find info on a server, the API pulls the request and sends it back to you
#              Data is stored in entries that resemble Python Dictionary / Key-pairs
#              

#  #    Start of code notation ---------------------------------------------

#       url = "api_url"                                        # To import API
#       requests.get(url)                                      # API response object
#       requests.get(url).json()                               # Cleans up API response object
#       requests.get(url + "specific_api_key")                 # Calls single entry based on specific api key
#       json.dumps(_____, indent=#, sort_keys=True)            # prints out API in JSON with indented format
#       reponse_json['key index'][# of index]['sub index']
#       print(f"some text string {pipe} string)

#  #    gflAuK75xVQRMEQLpPyueZmtLpAyXIxG    0r2GHTXJ6VZR3NDM

#  /articlesearch.json?q={query}&fq={filter}
#  https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key=yourkey

#  #   

#  #   params = {                          #  Storing details as a dictionary to pass into url
#               ""
# 
#               }

#  #   

#  #   

#  #   

###

MySQL ________________________________________________

    shell> mysql --help
    shell> mysql -h host -u user -p
    Enter password: ********
    mysql> QUIT

Hypothesis testing ________________________________

    Hypothesis (Educated Guess)
    Null Hypothesis (Framing hypothesis as a negative answer)
    Perform test 
    Get p-value

    stats.ttest_ind( , , equal_var=False)


###

#### MySQL Template Code!!!

LAUNCHING MySQL from Terminal ________________________________

    echo 'export PATH="$PATH:/usr/local/mysql/bin"' >> ~/.bash_profile
    source ~/.bash_profile
    mysql -u root -p

CORE OPERATIONS ________________________________

    SELECT - extracts data from a database
    UPDATE - updates data in a database
    DELETE - deletes data from a database
    INSERT INTO - inserts new data into a database
    CREATE DATABASE - creates a new database
    ALTER DATABASE - modifies a database
    CREATE TABLE - creates a new table
    ALTER TABLE - modifies a table
    DROP TABLE - deletes a table
    CREATE INDEX - creates an index (search key)
    DROP INDEX - deletes an index

Database ________________________________

    CREATE DATABASE <db name>;
    DROP DATABASE <db name>;
    USE <db name>;
    CREATE TABLE <table name> (
        col_1 DATATYPE BOOLEAN, 
        col_2 DATATYPE BOOLEAN,
        col_3 DATATYPE BOOLEAN,
        col_4 DATATYPE BOOLEAN
    )

VEIWING & Manipulating TABLES ________________________________

    SELECT * FROM <db name>;

    example:
        INSERT INTO people (name, has_pet, pet_name, pet_age)
        VALUES ("Jacob", true, "Misty", 10);

    UPDATE <table>
    SET <field> command
    WHERE <field> = "value"

    DELETE from <table>
    Where <field> = "value";

JOINING SQL TABLES ________________________________

    INNER JOIN <table 1> on <table 2>.<column ID 1> =  
    LEFT JOIN
    RIGHT JOIN

    example: 
         SELECT column(s) FROM table_1
         INNER JOIN table_2
         ON table_1.column_name = table_2.column_name;

QUERIES ________________________________

    SELECT * FROM table_1
    WHERE column_a = value;  ##  AND , OR , IN , NOT IN









