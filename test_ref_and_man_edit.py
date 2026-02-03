import inspect
from edit_functions import *

def create_test_list():
    w = {gensource:"winde",genmethod:turbine, mantype: 'E-111'} 
    v = {gensource:wind,genmethod:"horizontal", ref: 'bla'} 
    a = {gensource:wind,genmethod:turbine, model: 'blub'} 
    b = {gensource:wind,genmethod:turbine, ref: 'Easdf0'} 
    c = {gensource:wind,genmethod:turbine, ref: 'Vxxxxx', mantype: 'V137', model: 'V137'} 
    d = {gensource:wind,genmethod:turbine, ref: 'E4183201RS50601064000066515800027'} 
    e = {gensource:wind,genmethod:turbine, 'ref:eeg': 'Exxxxxxxx', mantype: 'V137XX', model: 'V137-YY'} 
    f = {gensource:wind,genmethod:turbine, refEEG: 'Exxxxxxxx'} 
    g = {gensource:wind,genmethod:turbine, refEEG: 'Exxxxxxxx', mantype: 'N175'} 
    h = {gensource:wind,genmethod:turbine, refEEG: 'E4183201RS50434254000091798500009'} 
    i = {genmethod:turbine, refEEG:'E4183201RS50434254000091798500009'} 
    j = {genmethod:turbine, ref:'E4183201RS50434254000091798500009'} 
    k = {gensource:wind, refEEG: 'E4183201RS50434254000091798500009'} 
    l = {gensource:wind, ref: 'Vxxxxx'} 
    test_list = [a, b, c, d, e, f, g, h, i, j, k, l, w, v]
    return test_list

def main():
    #full_args = inspect.getfullargspec(edit_element_man)
    #if 
    #print(inspect.getfullargspec(edit_element_ref))
    

    print("TESTING ref -> ref:EEG -----------")
    for x in create_test_list():
        print(x)
        y = edit_element_ref_pv(x)
        print(y)
        print("----")
    print("\n\n\n")
    print("TESTING manufacturer:type -> model -----------")
    for x in create_test_list():
        print(x)
        y = edit_element_man(x)
        print(y)
        print("----")

main()

