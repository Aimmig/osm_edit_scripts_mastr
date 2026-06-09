import re
import inspect

gensource = 'generator:source'
plantsource = 'plant:source'
genmethod = 'generator:method'
plantmethod = 'plant:method'
ref = 'ref'
refmastr = 'ref:mastr'
refEEG = 'ref:EEG'
wind = "wind"
turbine = "wind_turbine"
solar = "solar"
pv = "photovoltaic"
mantype = 'manufacturer:type'
model = 'model'


def edit_element_ref_wind(tags):
    if tags.get(gensource) != (wind):
        #print("source not matching nothing done")
        return tags
    if tags.get(genmethod) != (turbine):
        #print("method not matching nothing done")
        return tags
    if tags.get(ref) and re.match(r'E[-0-9a-zA-Z]{32}$', tags.get(ref)) and not refEEG in tags:
        #print("updating tag")
        tags[refEEG] = tags.get(ref)
        tags.pop(ref, None)
        return tags
    return tags

def edit_element_ref_pv(tags):
    if tags.get(gensource) != (solar) and tags.get(plantsource) != (solar):
        #print("source not matching nothing done")
        return tags
    if tags.get(genmethod) != (pv) and tags.get(plantmethod) != (pv):
        #print("method not matching nothing done")
        return tags
    if tags.get(ref) and re.match(r'E[-0-9a-zA-Z]{32}$', tags.get(ref)) and not refEEG in tags:
        #print("updating tag")
        tags[refEEG] = tags.get(ref)
        tags.pop(ref, None)
        return tags
    return tags

def edit_element_man(tags):
    if tags.get(gensource) != (wind) and tags.get(genmethod) != (turbine):
        return tags
    if mantype in tags and model in tags:
        if tags[model] != tags[mantype]:
            #print("model and man:type both exist but missmatch. Nothing done")
            return tags
        else:
            print("model was correct, remove manunfacturer:type")
            #tags.pop(mantype, None)
            return tags
    elif mantype in tags:
        #print("model didn't exist, renaming man:type -> model")
        tags[model] = tags[mantype]
        tags.pop(mantype, None)
        return tags
    return tags



# read pre-computed mastr data
# Should at least contain the node_id and ref for import
# or ref:EEG and ref:mastr for conversion
def read_csv_to_pandas(file):
    global mastr_data
    mastr_data = pd.read_csv(file, dtype=str)

# helper function to extract only the node id from url
def get_node_id(url):
    return url.split("/")[-1].strip()

def edit_element_import_ref_mastr(tags, url):
    if tags.get(gensource) != (wind):
        return tags
    if tags.get(genmethod) != (turbine):
        return tags
    if refmastr in tags:
        return tags
    node_id = get_node_id(url)
    if not node_id in mastr_data['id'].values:
        return tags
    else:
        ref_mastr = mastr_data.query('id==@node_id')["ref:mastr_mastr"].values[0]
        tags[refmastr] = ref_mastr
        return tags
