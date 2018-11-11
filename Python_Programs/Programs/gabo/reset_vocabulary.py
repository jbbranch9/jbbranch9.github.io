import json

vocabulary = {
            'stats':
                {
                'word count': len(['words']),
                'phrase count': len(['phrases']),
                'user_prompt count': len(['user_prompts']),
                'bot_response count': len(['bot_responses'])
                 },
            'words':
                {
                'w_0': 'Hello',
                'w_1': 'World',
                },
            'phrases':
                {
                'p_0': [0, 1],
                },
            'user_prompts':
                {
                'u_0': [0, 1],
                },
            'bot_responses':
                {
                'b_0': [0, 1],
                },
              }

with open("gabo_vocabulary.json", "w") as write_file:
        json.dump(vocabulary, write_file)

print(vocabulary)