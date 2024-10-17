import os

directory = r'D:\HocTap\projectDrVuDucLy\final\patd-results\scan-results\bincapz\wolfi-apks'


all_files = [f for f in os.listdir(directory) if f.endswith('.json')]
print(len(all_files))
print(len(set(all_files)))