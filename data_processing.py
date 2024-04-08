import pandas as pd
import io

def process_csv_file(uploaded_file):
    #sv_content = uploaded_file.getvalue()
    df = pd.read_csv(io.BytesIO(uploaded_file.read()))

    #df = pd.read_csv(io.StringIO(csv_content.decode('utf-8')))
    #df=pd.read_csv(uploaded_file)

    filtered_data = df[['Source', 'Screenname', 'Sentiment', 'Content']]
    removed = ['Fino Payments Bank', 'finopaymentsbank', 'Fino Payments Bank Ltd', 'FinoPaymntsBank']
    filtered_data = filtered_data[~filtered_data['Screenname'].isin(removed)]
    sources_req = ['Twitter.com', 'youtube.com', 'linkedin', 'Facebook.com', 'Instagram']
    filtered_data = filtered_data[filtered_data['Source'].isin(sources_req)]
    #filtered_data = df.sample(n=300, random_state=42)


    return filtered_data
