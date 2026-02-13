from osm_bot_abstraction_layer.generic_bot_retagging import run_simple_retagging_task
from edit_functions import *

#  nwr(area.boundaryarea)["ref:eeg"~"^E[-0-9a-zA-Z]{32}"]["plant:source"="solar"]["plant:method"="photovoltaic"];
#  nwr(area.boundaryarea)["ref:eeg"~"^E[-0-9a-zA-Z]{32}"]["generator:source"="solar"]["generator:method"="photovoltaic"];

def main():
    run_simple_retagging_task(
        max_count_of_elements_in_one_changeset=25,
        objects_to_consider_query="""
[out:xml][timeout:25000];
area["name"="Deutschland"]->.boundaryarea;
(
  nwr(area.boundaryarea)["ref"~"^E[-0-9a-zA-Z]{32}$"]["generator:source"="solar"]["generator:method"="photovoltaic"];
  nwr(area.boundaryarea)["ref"~"^E[-0-9a-zA-Z]{32}$"]["plant:source"="solar"]["plant:method"="photovoltaic"];
);
out body;
>;
out skel qt;
""",
        cache_folder_filepath='/tmp',
        is_in_manual_mode=True,
        changeset_comment='PV-Anlagen in DE: ref -> ref:EEG, wenn Exx...xx',
        discussion_url='https://community.openstreetmap.org/t/import-marktstammdatenregister-data-for-wind-power-plants/140622/10',
        osm_wiki_documentation_page='https://wiki.openstreetmap.org/wiki/Mechanical_Edits/onterof_mastr_bot/migrate_some_ref_to_ref_eeg_solar_wind_germany',
        edit_element_function=edit_element_ref_pv,
    )

main()
