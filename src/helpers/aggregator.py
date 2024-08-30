
def aggregate_reports(data):
    aggregate = {}

    for row in data:
        for result in row['results']:
            aggregate_key = ''

            if('dimensions' in result):
                for key in result['dimensions']:
                    aggregate_key+= result['dimensions'][key] + '|'

                aggregate_key = aggregate_key[:-1]

                if(aggregate_key not in aggregate):
                    aggregate[aggregate_key] = {}
                
                for key in result['metrics']:
                    if(key in aggregate[aggregate_key]):
                        aggregate[aggregate_key][key] += result['metrics'][key]
                    else:
                        aggregate[aggregate_key][key] = result['metrics'][key]
            else:
                for key in result['metrics']:
                    if(key in aggregate):
                        aggregate[key] += result['metrics'][key]
                    else:
                        aggregate[key] = result['metrics'][key]
                
  
    return aggregate