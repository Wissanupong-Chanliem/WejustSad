"""File Watcher for Development"""
import subprocess
import json
import os
import glob
with open('watcher.json', 'r') as file:
    watcher_setting = json.load(file)
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
