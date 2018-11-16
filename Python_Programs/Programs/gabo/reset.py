import json

reset_vocabulary = {
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
                [['cipher', []],
                 ['phrases', []],
                 ['punctuation', []],
                 ['cross ref. ID', []],
                 ['raw string', []]],
                ],
            'bot_responses':
                [
                [['cipher', []],
                 ['phrases', []],
                 ['punctuation', []],
                 ['cross ref. ID', []],
                 ['raw string', []]],
                
                [['cipher', []],
                 ['phrases', []],
                 ['punctuation', []],
                 ['cross ref. ID', []],
                 ['raw string', []]],
                ],
              }

##    with open("gabo_vocabulary.json", "w") as write_file:
##            json.dump(vocabulary, write_file)
##
##reset_vocabulary['stats']['word count'] = len(reset_vocabulary['words'])
##reset_vocabulary['stats']['phrase count'] = len(reset_vocabulary['phrases'])
##reset_vocabulary['stats']['user_prompt count'] = len(reset_vocabulary['user_prompts'])
##reset_vocabulary['stats']['bot_response count'] = len(reset_vocabulary['bot_responses'])