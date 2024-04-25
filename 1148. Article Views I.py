import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views.rename(columns ={'author_id':'id'},inplace = True)
    views = views.sort_values('id')
    return views[views['id']==views['viewer_id']].drop_duplicates(subset=['id'])[['id']]



'''
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result = views.loc[views['author_id'] == views['viewer_id']]
    unique_id = result['author_id'].unique()
    unique_id = sorted(unique_id)
    result_id = pd.DataFrame(unique_id, columns = ['id'])
    return result_id
'''