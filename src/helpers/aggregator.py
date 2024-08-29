
def aggregate_reports(data):
    aggregate = {}

    for row in data:
        for result in row['results']:
            for key in result:
                if(key in aggregate):
                    aggregate[key] += result[key]
                else:
                    aggregate[key] = result[key]
  
    return aggregate