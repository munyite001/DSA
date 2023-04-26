tests = [
    {
        'input': { 
            'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
            'query': 7
        },
        'output': 3
    },

    #   Query  occurs in the middle
    {
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 1
        },
        'output': 6
    },

    #   Query is the first element
    {
        'input': {
            'cards': [4, 2, 1, -1],
            'query': 4
        },
        'output': 0
    },

    #   Query is the last element
    {
        'input': {
            'cards': [3, -1, -9, -127],
            'query': -127
        },
        'output': 3
    },

    #   Query contains just one element query
    {
    'input': {
            'cards': [6],
            'query': 6
        },
        'output': 0
    },

    #   Cards doesn't contain query
    {'input': {
            'cards': [9, 7, 5, 2, -9],
            'query': 4
        },
        'output': -1
    },

    #   cards is empty 
    {
        'input': {
            'cards': [],
            'query': 7
        },
        'output': -1
    },

    #   Numbers can repeat in cards
    {
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 3
        },
        'output': 7
    },

    #   Query can occur multiple times in card
    {
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 3
        },
        'output': 7
    }
]

def run_tests():
    for test in tests:
        cards = test["input"]["cards"]
        query = test["input"]["query"]
        output = test["output"]
        result = locate_card_linear(cards, query)

        if result == output:
            print("Passed")