from configparser import ConfigParser
def save_config():
    with open(CONFIG, 'w') as fp:
        config.write(fp)
config = ConfigParser()
CONFIG = '/etc/php.ini'
config.read(CONFIG)
phpmemory = config['PHP']['memory_limit']
uploadlimit = config['PHP']['upload_max_filesize']
if phpmemory == 'M':
    config['PHP']['memory_limit'] = '128M'
if uploadlimit == 'M':
    config['PHP']['upload_max_filesize'] = '128M'
config['Session']['session.name'] = 'WTF'
save_config()
print('ReConfig OK')