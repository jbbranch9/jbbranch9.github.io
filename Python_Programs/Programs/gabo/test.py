vocabulary = {
        'bot_1': {
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

print(vocabulary)
print(len(vocabulary))

vocabulary['bot_2'] = {
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
                 ['raw string', 'yo']],
                ],
            'bot_responses':
                [
                [['cipher', [0]],
                 ['phrases', [0]],
                 ['punctuation', [['declarative.', False], ['interrogative?', False], ['exclamatory!', False], ['imperative.!', False]]],
                 ['cross ref. ID', 0],
                 ['raw string', 'yo']],
                ],
          }

print(vocabulary)
print(len(vocabulary))

name = 'bot_2'

print(vocabulary[name]['user_prompts'][0][4][1])
print(vocabulary['bot_1']['user_prompts'][0][4][1])