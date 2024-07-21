import pandas as pd

#You can change your existing dataset with this python file

# Read the existing CSV file
df_train = pd.read_csv('C:\\Users\\hp\\Desktop\\mini_project2\\updated_train.csv')

# Display the existing DataFrame
print("Existing DataFrame:")
print(df_train)

# Create a DataFrame from new records
new_records = [
    {'textID': '1234567', 'text': 'He is not so ugly', 'selected_text': 'not so ugly', 'sentiment': 'neutral'},
    {'textID': '1234568', 'text': 'Fan movie was not so good', 'selected_text': 'not so good', 'sentiment': 'negative'},
    {'textID': '1234569', 'text': 'That movie was not worth watching', 'selected_text': 'not worth', 'sentiment': 'negative'},
    {'textID': '1234570', 'text': 'Todays weather is kind of mid', 'selected_text': 'is kind of', 'sentiment': 'neutral'},
    {'textID': '1234571', 'text': 'Social Media is ruining our life', 'selected_text': 'ruining', 'sentiment': 'negative'},
    {'textID': '1234572', 'text': 'Not ruining a perfectly good day with unnecessary worries, just focusing on the positive vibes! ', 'selected_text': 'Not ruining a perfectly good day', 'sentiment': 'positive'},
    {'textID': '1234573', 'text': 'Feeling frustrated with this never-ending rain. Its really ruining my plans for the weekend. ', 'selected_text': 'Feeling frustrated', 'sentiment': 'negative'},
    {'textID': '1234574', 'text': 'Just had the worst customer service experience ever', 'selected_text': 'worst', 'sentiment': 'negative'},
    {'textID': '1234575', 'text': 'He is not the worst', 'selected_text': 'not the worst', 'sentiment': 'neutral'},
    {'textID': '1234576', 'text': 'China Attacks Taiwan!', 'selected_text': 'attacks', 'sentiment': 'negative'},
    {'textID': '1234577', 'text': 'justice prevailed', 'selected_text': 'justice prevailed', 'sentiment': 'positive'}
]

new_df = pd.DataFrame(new_records)

# Concatenate the existing DataFrame with the new DataFrame
df_train_updated = pd.concat([df_train, new_df], ignore_index=True)

# Display the updated DataFrame
print("\nUpdated DataFrame:")
print(df_train_updated)

# Save the updated DataFrame to a new CSV file
df_train_updated.to_csv('C:\\Users\\hp\\Desktop\\updatedtrain.csv', index=False)

print("\nNew CSV file saved successfully.")
