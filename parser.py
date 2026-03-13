# helper functions to parse speciesnet output

def get_classes(result_dict: dict): # returns ALL identified animals, helper function not useful elsewhere
    classes = result_dict.get('predictions')[0].get('classifications').get('classes')
    output_classes = classes.copy()
    for i in range(len(classes)):
        output_classes[i] = classes[i].partition(';')[2]
    return output_classes


def get_highest_result(result_dict:dict): # return the highest identified thing, alongside its confidence
    classes = result_dict.get('predictions')[0].get('classifications').get('classes')
    scores = result_dict.get('predictions')[0].get('classifications').get('scores')
    highest_output = classes.copy()[0].partition(';')[2]
    output = (highest_output, scores[0]) # tuples are immutable, which is fine here
    return output