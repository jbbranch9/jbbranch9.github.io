import json

reset_vocabulary = {
            'stats':
                {
                'word count': 2,
                'phrase count': 2,
                'user_prompt count': 2,
                'bot_response count': 2,
                 },
            'words':
                [
                'hello',
                'world',
                ],
            'phrases':
                [
                [0, 1],
                [1, 0],
                ],
            'user_prompts':
                [
                [0, 1],
                [1, 0],
                ],
            'bot_responses':
                [
                [0, 1],
                [1, 0],
                ],
              }

##    with open("gabo_vocabulary.json", "w") as write_file:
##            json.dump(vocabulary, write_file)
##
##reset_vocabulary['stats']['word count'] = len(reset_vocabulary['words'])
##reset_vocabulary['stats']['phrase count'] = len(reset_vocabulary['phrases'])
##reset_vocabulary['stats']['user_prompt count'] = len(reset_vocabulary['user_prompts'])
##reset_vocabulary['stats']['bot_response count'] = len(reset_vocabulary['bot_responses'])