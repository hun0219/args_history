import pandas as pd
from tabulate import tabulate

def read_data(path='~/data/parquet'):
    df = pd.read_parquet(path)
    df.dropna(inplace=True) #NaN 에러, na=결측값, inplace=대체
    #df = df.dropna()
    return df

def top(cnt, dt, pretty=False):
    df = read_data()
    fdf = df[df['dt'] == dt]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(cnt)
    ddf = sdf.drop(columns=['dt'])
    pty = tabulate(ddf, headers=["cmd","cnt"], tablefmt="outline")
    
    if pretty:
        # 참일떄
        r = tabulate(ddf, headers=["cmd","cnt"], tablefmt="outline")
        return r 
    else:  #거짓 일떄 
        r = ddf.to_string(index=False)
        return r

def count(query):
    df = read_data()
    fdf = df[df['cmd'].str.contains(query)]
    cnt = fdf['cnt'].sum()
    return cnt

