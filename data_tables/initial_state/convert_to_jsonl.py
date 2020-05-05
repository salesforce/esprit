import jsonlines
import os

with open('/Users/nazneen.rajani/workspace/esprit_old/phyre/data/split/task_ids_test_annotation.txt', 'r') as f:
    l = f.read().splitlines()


with jsonlines.open('test.jsonl','w') as w:
    out = {}
    for i in l:
        pt = i.split(":")
        path_sim = '/Users/nazneen.rajani/workspace/phyre/phyre/data/solution_csv_json_imgs/' + pt[0]+ "/" + pt[1] + "/initial.json"
        #path_init = '/Users/nazneen.rajani/workspace/esprit_old/phyre/data/annotation/initial_state_description/' + pt[0]+ "-" + pt[1] + ".txt"
        #path_salient = '/Users/nazneen.rajani/workspace/esprit_old/phyre/data/annotation/salient_event/' + pt[0]+ "-" + pt[1] + ".txt"
        #with open(path_init,'r') as ini, open(path_sim,'r') as si, open(path_salient,'r') as sal:
        dir_name= pt[0] + '-' + pt[1]
        #os.system("mkdir "+dir_name)
        os.system("cp "+ path_sim +' ' + dir_name+'.json')
            # o2 = ini.read().strip()
            # tmp = sal.read().splitlines()
            # o1 = ','.join(tmp)
            # o3 = si.read().strip()
            # out['id'] = i
            # out['salient_frames'] = o1
            # out['initial_state_description'] = o2
            # out['salient_events_description'] = o3
            # w.write(out)
