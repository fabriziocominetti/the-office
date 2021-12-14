#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_all_lines_from_the_office():
  """This gets all lines from the first four seasons of The Office. 
  Returns:
      list: A list of a dictionary containing every line.
  """
  base_url = 'http://officequotes.net/no'
  list_all_lines = list()

  for season in range(1,10):
    half_of_url = base_url + str(season) + '-'
    
    for episode in range(1,27):
      if episode <= 9:
        full_url = half_of_url + '0' + str(episode) + '.php'
      else:
        full_url = half_of_url + str(episode) + '.php'

      #Removes any 404 Page Not Found messages or other similar errors.
      error_message_404 = '\n<p align="center"><img src="img/dwight_ahh.jpg" /></p>\n<p align="center"><font size="8">404 Page Not Found</font></p>\n<p align="center">(Did you ask yourself "Would an idiot do that?" before you typed in the URL?)</p>\n'
      full_url_response = requests.get(full_url).content.decode(errors='ignore')

      if error_message_404 in full_url_response:
        pass
      else:
        soup = BeautifulSoup(full_url_response, 'html.parser')
        for b_tag in soup.find_all('b')[13:]:
          dict_episode = dict()
          dict_episode['Character'] = b_tag.text
          dict_episode['Line'] = b_tag.next_sibling
          dict_episode['Season'] = season
          dict_episode['Episode_Number'] = episode
          list_all_lines.append(dict_episode)

  return list_all_lines

def list_to_pandas_df(list_data):
  pandas_df = pd.DataFrame(list_data)

  return pandas_df

def clean_all_lines(pandas_df):
  """This cleans lines and character misspellings from The Office using pandas
  Args:
      pandas_df (pandas dataframe): This is the intial pandas data to be cleaned
  Returns:
      [pandas dataframe]: This returns a cleaned pandas dataframe
  """
  pandas_df_cleaned = pandas_df[~pandas_df['Character'].str.contains("^(Deleted|Season|Main|None|Other)")]
  pandas_df_cleaned.dropna(subset=['Line'], inplace=True)
  
  pandas_df_cleaned = pandas_df_cleaned.replace('\\n',' ', regex=True) 
  pandas_df_cleaned = pandas_df_cleaned.replace('\\t','', regex=True) 

  #Fix the "Character" column for misspellings.
  pandas_df_cleaned['Character'] = pandas_df_cleaned['Character'].str.title()
  pandas_df_cleaned['Character'] = [character.strip() for character in pandas_df_cleaned['Character']]
  pandas_df_cleaned['Character'] = [character.strip('"') for character in pandas_df_cleaned['Character']]
  pandas_df_cleaned['Character'] = [character.strip(':') for character in pandas_df_cleaned['Character']]
  pandas_df_cleaned.replace({'Character':{'Michel:':'Michael:', 'Darry:' : 'Darryl:'}}, inplace=True)

  return pandas_df_cleaned

def main():
  list_all_lines = get_all_lines_from_the_office()
  pandas_df = list_to_pandas_df(list_all_lines)
  the_office_df_cleaned = clean_all_lines(pandas_df)
  print(the_office_df_cleaned)
  the_office_df_cleaned.to_csv('the-office_lines.csv')

if __name__ == "__main__":
  main()