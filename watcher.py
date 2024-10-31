"""File Watcher for Development"""
import subprocess
import json
import os
import glob

def install_dependencies(dependencies_list:list[str]):
    if not os.path.exists("dependencies.txt"):
        open('dependencies.txt', 'w')
    with open('dependencies.txt', 'r') as dependencies_file:
        lines = dependencies_file.readlines()
        lines = [l.replace("\n","") for l in lines ]
    need = [l for l in dependencies_list if l not in lines]
    print(need)
    if need:
        os.system(f"pip install {" ".join(need)}")
    with open('dependencies.txt', 'w') as dependencies_file:
        dependencies_file.write("\n".join(dependencies_list))
def watch():
    with open('watcher.json', 'r') as file:
        watcher_setting = json.load(file)
    install_dependencies(watcher_setting["dependencies"])
    watch_list = {}
    for directory in watcher_setting["watchlist"]:
        glob_list = glob.glob(directory,recursive=True)
        for file in glob_list:
            watch_list[file]=os.path.getmtime(file)
    process = subprocess.Popen(watcher_setting["run"].split())
    while True:
        seen = []
        for directory in watcher_setting["watchlist"]:
            glob_list = glob.glob(directory,recursive=True)
            seen.extend(glob_list)
            for file in glob_list:
                if os.path.exists(file):
                    current_mtime = os.path.getmtime(file)
                    if file in watch_list and current_mtime == watch_list[file]:
                        continue
                    watch_list[file] = current_mtime
                    if not process.poll():
                        process.terminate()
                    process = subprocess.Popen(watcher_setting["run"].split())
        watch_list = dict([pair for pair in watch_list.items() if pair[0] in seen])
watch()