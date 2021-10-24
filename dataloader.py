import json
import bz2
import pandas as pd

def load_quotes(path, limit = None, columns = None):
    """Function to load the quotes of a compressed json file into a pd.DataFrame

    Args:
        path (Path): Path to the compressed json.bz2 file of quotes
        limit (Int, optional): Maximum number of item to load . Defaults to None.
        cols (List[String], optional): Columns to load into the dataframe. Defaults to None.

    Returns:
        pd.Datframe: Panda Dataframe that contains the limit-first quotes with the colums cols.

    Remark: 
        Originally all the columns are
            ['quoteID', 'quotation', 'speaker', 'qids', 'date', 'numOccurences', 'probas', 'urls', 'phase']
    """
    with bz2.open("data/quotes-2020.json.bz2", "rt", encoding = "utf8") as bzinput:
        quotes = []
        for i, line in enumerate(bzinput):
            if limit != None and i == limit: break

            quote = json.loads(line)

            if columns == None:
                columns = list(quote.keys())
                
            new_quote = []
            for col in columns:
                new_quote.append(quote[col])
            quotes.append(new_quote)

    return pd.DataFrame(quotes,columns=columns)