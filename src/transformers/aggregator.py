# TODO: Refactor this module to reduct the complexity in this logic
# Aggregate reports takes in an array of results and merges them into a object adding metrics together to give a single set of results
def aggregate_reports(data):
    aggregate = {}

    for row in data:
        for result in row['results']:
            aggregate_key = ''

            # If dimensions are included then join the keys from each into a single flattened string
            if('dimensions' in result):
                for key in result['dimensions']:
                    aggregate_key+= result['dimensions'][key] + '|'

                aggregate_key = aggregate_key[:-1]

                if(aggregate_key not in aggregate):
                    aggregate[aggregate_key] = {}
                
                # If a metric is already in the aggregate dictionary then add the values together, otherwise add it as a new result
                for key in result['metrics']:
                    if(key in aggregate[aggregate_key]):
                        aggregate[aggregate_key][key] += result['metrics'][key]
                    else:
                        aggregate[aggregate_key][key] = result['metrics'][key]
            else:
                # Dimensions are optional, this logic handles results without dimensions
                # If a metric is already in the aggregate dictionary then add the values together, otherwise add it as a new result
                for key in result['metrics']:
                    if(key in aggregate):
                        aggregate[key] += result['metrics'][key]
                    else:
                        aggregate[key] = result['metrics'][key]
                
  
    return aggregate