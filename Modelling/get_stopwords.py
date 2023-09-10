import pandas as pd
from collections import Counter
import nltk
nltk.download('stopwords')

if __name__ == "__main__":
    df = pd.read_excel('db/data.xlsx')
    word_counter = Counter()
    for text in df['Notes'].dropna():
        words = nltk.word_tokenize(text.lower())
        word_counter.update(words)
        
    word_count_df = pd.DataFrame(word_counter.items(), columns=['Word', 'Count'])
    word_count_df = word_count_df.sort_values(by='Count', ascending=False)
    excel_file_path = 'Modelling/word_counts.xlsx'
    word_count_df.to_excel(excel_file_path, index=False)
    print(f"Word counts saved to {excel_file_path}")
