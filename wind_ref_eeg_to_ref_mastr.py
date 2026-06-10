from osm_bot_abstraction_layer.generic_bot_retagging import run_simple_retagging_task
from edit_functions import edit_element_ref_eeg_to_mastr
from edit_functions import read_csv_to_pandas


def main():
    file = "REF_EEG_MASTR.csv"
    read_csv_to_pandas(file)
    run_simple_retagging_task(
        max_count_of_elements_in_one_changeset=25,
        objects_to_consider_query="""
[out:xml][timeout:25000];
area["name"="Deutschland"]->.boundaryarea;
(
  nw(area.boundaryarea)["ref:EEG"~"^E[-0-9a-zA-Z]{32}"]["generator:source"="wind"];
);
out body;
>;
out skel qt;
""",
        cache_folder_filepath='/tmp',
        is_in_manual_mode=True,
        changeset_comment='WKA in DE: ref:EEG -> ref:mastr',
        discussion_url='https://community.openstreetmap.org/t/import-marktstammdatenregister-data-for-wind-power-plants/140622/49',
        osm_wiki_documentation_page='https://wiki.openstreetmap.org/wiki/Mechanical_Edits/onterof_mastr_bot/ref_eeg_to_ref_mastr_windkraft_de',
        edit_element_function=edit_element_ref_eeg_to_mastr,
        source="Marktstammdatenregister Bundesnetzagentur",
        other_tags_dict = { "cases_where_human_help_is_required": "",},
    )

main()
