import re
import inspect

gensource = 'generator:source'
genmethod = 'generator:method'
ref = 'ref'
refEEG = 'ref:EEG'
wind = "wind"
turbine = "wind_turbine"
solar = "solar"
pv = "photovoltaic"
mantype = 'manufacturer:type'
model = 'model'


def edit_element_ref_wind(tags):
    if tags.get(gensource) != (wind):
        print("source not matching nothing done")
        return tags
    if tags.get(genmethod) != (turbine):
        print("method not matching nothing done")
        return tags
    if tags.get(ref) and re.match(r'E[-0-9a-zA-Z]{32}$', tags.get(ref)) and not refEEG in tags:
        print("updating tag")
        tags[refEEG] = tags.get(ref)
        tags.pop(ref, None)
        return tags
    return tags

def edit_element_ref_pv(tags):
    if tags.get(gensource) != (solar):
        print("source not matching nothing done")
        return tags
    if tags.get(genmethod) != (pv):
        print("method not matching nothing done")
        return tags
    if tags.get(ref) and re.match(r'E[-0-9a-zA-Z]{32}$', tags.get(ref)) and not refEEG in tags:
        print("updating tag")
        tags[refEEG] = tags.get(ref)
        tags.pop(ref, None)
        return tags
    return tags

def edit_element_man(tags, debug=False):
    if tags.get(gensource) != (wind):
        print("source not matching nothing done")
        return tags
    if tags.get(genmethod) != (turbine):
        print("method not matching nothing done")
        return tags
    if mantype in tags and model in tags:
        if tags[model] != tags[mantype]:
            print("model and man:type both exist but missmatch. Nothing done")
            return tags
        else:
            print("model was correct, remove manunfacturer:type")
            tags.pop(mantype, None)
            return tags
    elif mantype in tags:
        print("model didn't exist, renaming man:type -> model")
        tags[model] = tags[mantype]
        tags.pop(mantype, None)
        return tags
    return tags
