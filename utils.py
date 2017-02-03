
def reOrderProblemID(id):
    return {7:1, 21:2, 24:3, 23:4, 25:5, 22:6}[id]

# INPUT: Comma separated string
def getHardCloseTime(x):
    data = x.split(',')
    return (int(data[8]),{ 'HardCloseTime': int(data[11]), 'OpenTime': int(data[13]) })

# INPUT: Comma separated string
def parse_problems(x):
    data = x.split(',')
    return {
        'Grade':float(data[5]),
        'TimeStamp':int(data[6]),
        'DataPackageID':data[7],
        'ProblemID':int(data[8]),
        'ProblemType':data[10],
        'HardCloseTime':int(data[11]),
        'EventType':data[14].split('.')[0],
        'EventSubType':data[14].split('.')[1],
        'Title':data[15],
        'SessionUserID':data[16]
    }

# INPUT: Comma separated string
def parse_videos(x):
    data = x.split(',')
    return {
        'TimeStamp':int(data[6]),
        'DataPackageID':data[7],
        'VideoID':int(data[10]),
        'EventType':data[14].split('.')[0],
        'EventSubType':data[14].split('.')[1],
        'SessionUserID':data[15]
    }

# INPUT: Comma separated string
def parse_forums(x):
    data = x.split(',')
    return {
        'AccountUserID':data[3],
        'TimeStamp':int(data[4]),
        'DataPackageID':data[5],
        'EventType':data[11].split('.')[0],
        'EventSubType':data[11].split('.')[1]
    }

# INPUT: Comma separated string
def filter_problems(x):
    data = x.split(',')
    return (
        # Some problem event are quiz inside video, we decide to not consider these
        (data[10]=='Assignment')
        # We remove IDs of assignments that have been used by the teaching staff for testing the platform
        and (not data[8] in ['1','2','3','4','5'])
        # Discard assignments with no grade
        and (not data[5] in ['None'])
    )

# INPUT: Comma separated string
def filter_videos(x):
    data = x.split(',')
    return (
        # We remove video that do not belong to the MOOC lectures or ar just Setup videos
        (data[10] not in ['9','12','11','10','13','2','29','25','21','27','23'])
        # Remove Download events
        and (data[14].split('.')[1] not in ['Download'])
    )

# INPUT: Comma separated string
def filter_forums(x):
    data = x.split(',')
    return (
        True
    )

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

def patternToString(pattern, verbosity='normal'):
    link = "" if verbosity == 'minimal' else "-" if verbosity == 'normal' else '\n-> '
    return link.join([eventToString(event,verbosity) for event in pattern])
