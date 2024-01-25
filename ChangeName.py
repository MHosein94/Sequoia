import os

configs_files = os.listdir()
for config_file in configs_files:
    if '.x' in config_file:
        new_proxies=''
        service_name='Sakura' if config_file != 'Sequoia.x' else 'Sequoia'
        with open(config_file, 'r') as f:
            proxies = f.readlines()
            for i, proxy in enumerate(proxies):
                new_proxies+=proxy.split('#')[0] + f'#{service_name}{i+1}\n'
                
        with open(config_file, 'w') as f:
            f.write(new_proxies)