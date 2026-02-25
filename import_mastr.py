from osm_bot_abstraction_layer.generic_bot_retagging import run_simple_retagging_task
import pandas as pd

mastr_data = None
gensource = "generator:source"
genmethod = "generator:method"
wind = "wind"
turbine = "wind_turbine"

# read pre-computed mastr data
# Should at least contain the node_id and ref
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
    if "ref:mastr" in tags:
        return tags
    node_id = get_node_id(url)
    if not node_id in mastr_data['id'].values:
        return tags
    else:
        ref_mastr = mastr_data.query('id==@node_id')["ref:mastr_mastr"].values[0]
        tags["ref:mastr"] = ref_mastr
        return tags


def main():
    file = "xyz.csv"
    read_csv_to_pandas(file)
    run_simple_retagging_task(
        max_count_of_elements_in_one_changeset=25,
        objects_to_consider_query="""
[out:xml][timeout:25000];
area["name"="Rheinland-Pfalz"]->.boundaryarea;
(
  nwr(area.boundaryarea)["generator:source"="wind"]["generator:method"="wind_turbine"];
);
out body;
>;
out skel qt;
""",
        cache_folder_filepath='/tmp',
        is_in_manual_mode=True,
        changeset_comment='TO-DO ... Import ref:mastr für WKA wenn TO-DO übereinstimmt',
        discussion_url='TO-DO',
        osm_wiki_documentation_page='TO-DO',
        edit_element_function=edit_element_import_ref_mastr,
    )

main()
