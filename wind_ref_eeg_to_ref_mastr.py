from osm_bot_abstraction_layer.generic_bot_retagging import run_simple_retagging_task
from edit_functions import edit_element_eeg_to_mastr
import pandas as pd

mastr_data = None

# read pre-computed mastr data
# Should at least contain the ref:EEG and ref:mastr
def read_csv_to_pandas(file):
    global mastr_data
    mastr_data = pd.read_csv(file, dtype=str)


def main():
    file = "REF_EEG_MASTR.csv"
    read_csv_to_pandas(file)
    run_simple_retagging_task(
        max_count_of_elements_in_one_changeset=25,
        objects_to_consider_query="""
[out:xml][timeout:25000];
area["name"="name"="Deutschland"]->.boundaryarea;
(
  nw(area.boundaryarea)["generator:source"="wind"];
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
        edit_element_function=edit_element_eeg_to_mastr,
        source="Marktstammdatenregister Bundesnetzagentur",
        other_tags_dict = { "cases_where_human_help_is_required": "",},
    )

main()
