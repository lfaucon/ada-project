# Function to have a friendly way to print the events
def eventToString(event):
    return {
        "Problem": lambda x: "(P "+str(event['ProblemID'])+")",
        "Video": lambda x: "(V "+str(event['VideoID'])+")",
        "Forum": lambda x: "(F)"
    }[event['EventType']](event)