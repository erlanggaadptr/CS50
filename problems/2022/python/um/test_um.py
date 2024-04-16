from um import count


def test_count():
    io = [
        {"input": "um", "output": 1},
        {"input": "Hello, um, world", "output": 1},
        {"input": "This is, um... CS50.", "output": 1},
        {"input": "Um... what are regular expressions?", "output": 1},
        {"input": "Um, thanks, um, regular expressions make sense now.", "output": 2},
        {"input": "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?", "output": 2},
    ]

    for i in range(len(io)):
        assert count(io[i]["input"]) == io[i]["output"]
