# Function to have a friendly way to print the events
def eventToString(event,verbosity='normal'):
    if verbosity == 'minimal':
        out = {
            "Problem": lambda x:"P",
            "Video": lambda x:"V",
            "Forum": lambda x:"F",
        }
    if verbosity == 'normal':
        out = {
            "Problem": lambda x:"P"+str(x['ProblemID']),
            "Video": lambda x:"V"+str(x['VideoID']),
            "Forum": lambda x:"F",
        }
    if verbosity == 'dates':
        out = {
            "Problem": lambda x:"P"+str(x['ProblemID'])+"."+str(x['Date']),
            "Video": lambda x:"V"+str(x['VideoID'])+"."+str(x['Date']),
            "Forum": lambda x:"F"+"."+str(x['Date']),
        }
    return out[event['EventType']](event)

def patternToString(pattern,verbosity='normal'):
    link = "" if verbosity == 'minimal' else "-" if verbosity == 'normal' else '\n-> '
    return link.join([eventToString(event,verbosity) for event in pattern])
