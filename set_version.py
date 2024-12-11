import time
print(time.ctime())
with open('ms_version.txt', 'r') as version_file:
  version_content = version_file.read()
print('CURRENT#########VERSION')
print(version_content)
new_version = version_content.replace('30920', str(time.ctime()))
print('NEW#########VERSION')
with open('ms_version.txt', 'w') as version_file:
  version_file.write(new_version)
print(new_version)
