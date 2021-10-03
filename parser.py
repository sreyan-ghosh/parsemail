import pandas as pd

filepath = './data/data.csv'

def parsefile(filepath):
    """
    param: takes the filepath of the data (supports csv only, change pd.read_method for others)
    returns: list of email addresses

    This function reads through a csv file and captures the email id column into a pd.Series object.
    The object is converted into a list and returned.
    Change the code of the function to suit the schema of the dataset. Usually done by providing the right column-name.
    """
    df = pd.read_csv(filepath)
    maillist = df.Email
    maillist = list(maillist)
    print(type(maillist)) # type checking to verify is maillist is of type <class.list>
    return maillist

if __name__ == '__main__':
    parsefile(filepath)