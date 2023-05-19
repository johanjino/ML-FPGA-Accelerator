import flowgraph
import h5py
import json


def graph(filename="test/test_ML.h5"):
    model_info = h5py.File(filename, 'r')

    model_config_json = json.loads(model_info.attrs['model_config'])
    activation_lookup_dict = {item['config']["name"]: item['config']["activation"] 
                            for item in model_config_json['config']['layers'] 
                            if 'activation' in item['config'].keys()}
    model_weights = dict(model_info['model_weights'])
    del model_weights['top_level_model_weights']


    head = flowgraph.node(name='head', type='head')
    previous = head
    for layer in model_weights.keys():
        bias = model_weights[layer][layer]["bias:0"]
        kernel = model_weights[layer][layer]["kernel:0"]
        activation = activation_lookup_dict[layer].lower()
        next = flowgraph.node(kernel=kernel, bias=bias, activation=activation, name=str(layer))
        previous.update(next=next)
        previous = next

    return head

# head = graph()
# print(head.propagate([5,5]))
# next = head
# while next!=None:
#     print(next.bias)
#     next=next.next
    


