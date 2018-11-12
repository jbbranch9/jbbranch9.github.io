import json

vocabulary = {
            'stats':
                {
                'word count': 0,
                'phrase count': 0,
                'user_prompt count': 0,
                'bot_response count': 0,
                 },
            'words':
                [
                'hello',
                'world',
                ],
            'phrases':
                [
                [0, 1],
                [0, 1],
                ],
            'user_prompts':
                [
                [0, 1],
                [0, 1],
                ],
            'bot_responses':
                [
                [0, 1],
                [0, 1],
                ],
              }

with open("gabo_vocabulary.json", "w") as write_file:
        json.dump(vocabulary, write_file)

print(vocabulary)

vocabulary['stats']['word count'] = len(vocabulary['words'])
vocabulary['stats']['phrase count'] = len(vocabulary['phrases'])
vocabulary['stats']['user_prompt count'] = len(vocabulary['user_prompts'])
vocabulary['stats']['bot_response count'] = len(vocabulary['bot_responses'])

print(vocabulary)