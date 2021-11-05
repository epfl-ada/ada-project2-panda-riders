import json
import bz2
import pandas as pd
import os
import gdown


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

    path = os.path.join(os.getcwd(),path)
    if not os.path.isfile(path):
        filename = os.path.split(path)[-1]
        files = { \
            'quotes-2008.json.bz2': '1wIdrR0sUGw7gAKCo_S-iL3q_V04wHzrP', \
            'quotes-2009.json.bz2': '1Wds32frDJ6PJgP1ruU2ctDvvlcOF4k3i', \
            'quotes-2010.json.bz2': '1dUMLpB7rVRF3nY6X2GmVNO57Zm1RVZRB', \
            'quotes-2011.json.bz2': '1sPlhxtt9VJROcaD97DmzHsFROGBOCpK6', \
            'quotes-2012.json.bz2': '1M3arwVzCNz9n92wJVl9c3rTOU5oh1xFQ', \
            'quotes-2013.json.bz2': '1PZEmS85TAHtNwXoMgm-7MDC58oS3cK73', \
            'quotes-2014.json.bz2': '1axK0PRItbbQW4V-T1fDa3J75bKZJHVLI', \
            'quotes-2015.json.bz2': '1ujF5vgppXUu5Ph81wqrwY12DrszVmCGe', \
            'quotes-2016.json.bz2': '1iyYhemohtPBwFyWck8SMHdaHoJMZShsI', \
            'quotes-2017.json.bz2': '1823mXyPsLDK7i1CQ7CtjzJaJ8rxeEulp', \
            'quotes-2018.json.bz2': '1X609SehGUxgoB0LfwazAeySjWDc-VhcZ', \
            'quotes-2019.json.bz2': '1KUXgpssbM7mXGx5RqturDKdtdS_KxIB8', \
            'quotes-2020.json.bz2': '1kBPm86V1_9z-9rTi3F-ENgxGvUod0olI'}
        url = f'https://drive.google.com/uc?id={files[filename]}'
        gdown.download(url, path, quiet=False)


    with bz2.open(path, "rt", encoding = "utf8") as bzinput:
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