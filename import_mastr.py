from osm_bot_abstraction_layer.generic_bot_retagging import run_simple_retagging_task
from edit_functions import edit_element_import_ref_mastr
from edit_functions import read_csv_to_pandas

def main():
    file = "test_rlp_sample.csv"
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
        source="Marktstammdatenregister Bundesnetzagentur",
        other_tags_dict = { "cases_where_human_help_is_required": "",},
    )

main()
