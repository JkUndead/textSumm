import os
import json

def data_loader():
    f = open('/Users/jamesto/Text_summ/textSumm/Multi-XScience-master/data/test.json')
    data = json.load(f)

    prompt = []
    completion = []
    keys = ('prompt', 'completion')
    train_data = []


    for item in data:
        # Get the prompt
        values = []
        prompt_text = item['abstract']
        ref_abs = ''
        for ref in item['ref_abstract'].values():
            ref_abs += (ref['abstract'])
        prompt_text += ref_abs.strip('\n')
        values.append(prompt_text)

        # Get the completion
        completion_text = item['related_work']
        values.append(completion_text)
        
        # Append to the list
        # prompt.append(prompt_text)
        # completion.append(completion_text)
        pair = dict(zip(keys,values))
        train_data.append(pair)

    
    
    
    # train_data = dict(zip(prompt,completion))
    
    with open("/Users/jamesto/Text_summ/textSumm/Multi-XScience-master/data/test_gpt.json", "w") as outfile:
        json.dump(train_data, outfile)


    # first_item = data[0]
    # prompt = first_item['abstract']
    # ref_abs = ''
    # for ref in first_item['ref_abstract'].values():
    #     # print(ref['abstract'])
    #     ref_abs += (ref['abstract'])
    # prompt += ref_abs.strip('\n')
    # print(prompt.strip('\n'))

    f.close()
    # return prompt


# def reference_loader():
#     f = open('/Users/jamesto/Text_summ/textSumm/Multi-XScience-master/data/test.json')
#     data = json.load(f)

#     first_item = data[0]
#     reference = first_item['related_work']
#     return reference

data_loader()
