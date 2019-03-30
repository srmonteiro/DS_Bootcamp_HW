
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



