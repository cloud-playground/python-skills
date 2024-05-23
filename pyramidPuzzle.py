def get_key(line):
    return int(line.split()[0])

def decode(message_file):
    step = 1
    pyramid = []
    words = []
    secretmessage = ""
    lines = sorted(message_file, key=get_key)
    while step < len(lines):
        pyramid.append(lines[0:step])
        lines = lines[step:]
        step += 1
    for sublist in pyramid:
        words.append(sublist[-1])
    for word in words:
        phrase = word.split()
        secret = phrase[1]
        phrases = (secretmessage, secret)
        secretmessage = " ".join(phrases)
    print(secretmessage)

content = open("pyramidPuzzle.txt")
message_file = content.readlines()

decode(message_file)
