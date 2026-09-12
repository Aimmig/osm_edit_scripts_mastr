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
        changeset_comment='RLP: Import ref:mastr for wind turbines based on matching start_date',
        discussion_url='https://community.openstreetmap.org/t/import-marktstammdatenregister-data-for-wind-power-plants/140622',
        osm_wiki_documentation_page='https://wiki.openstreetmap.org/wiki/Mechanical_Edits/onterof_mastr_bot/import_ref_mastr_wind_plants_DE',
        edit_element_function=edit_element_import_ref_mastr,
        source="Marktstammdatenregister Bundesnetzagentur",
        other_tags_dict = { "cases_where_human_help_is_required": "",
                           "source:license": "Deutschlandlizenz By-2.0",
                           "source:url": "https://www.marktstammdatenregister.de/MaStR",
                           },
    )

main()
