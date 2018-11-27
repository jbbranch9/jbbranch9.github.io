import json

vocabulary = {
        'Gabo': {
        'identifiers':
            {
            'user_name': 'User',
            'bot_name': 'Gabo',
            },
        'stats':
            {
            'word count': 1,
            'phrase count': 1,
            'user_prompt count': 1,
            'bot_response count': 1,
             },
        'words':
            [
            'hello',
            ],
        'phrases':
            [
            [0],
            ],
        'user_prompts':
            [
            [['cipher', [0]],
             ['phrases', [0]],
             ['punctuation', [['declarative.', False], ['interrogative?', False], ['exclamatory!', False], ['imperative.!', False]]],
             ['cross ref. ID', 0],
             ['raw string', 'hello']],
            ],
        'bot_responses':
            [
            [['cipher', [0]],
             ['phrases', [0]],
             ['punctuation', [['declarative.', False], ['interrogative?', False], ['exclamatory!', False], ['imperative.!', False]]],
             ['cross ref. ID', 0],
             ['raw string', 'hello']],
            ],
          },
    }

with open("gabo_vocabulary.json", "w") as write_file:
        json.dump(vocabulary, write_file)