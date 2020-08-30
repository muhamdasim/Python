def FunctionName():
    df=pd.read_csv('filname.csv')
    emails=df['coulmn-name'].values.tolist()

    return emails
