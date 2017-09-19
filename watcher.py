# -*- coding:utf8 -*-

import urllib2
import json
import time
import ConfigParser

def download():
    """
    Download data from PM25.in
    """
    cf = ConfigParser.ConfigParser()
    cf.read('config.ini')
    pm25_uri = cf.get('pm25', 'pm25_uri')
    token = cf.get('pm25', 'token')
    data_file = cf.get('storage', 'file_pattern')

    # uri & save file
    pm25_url = pm25_uri + '?token=' + token
    save_fn = data_file % time.strftime('%Y-%m-%d-%H')

    # do fetch and save
    print '* read url %s' % pm25_url
    rsp = urllib2.urlopen(pm25_url)
    data = rsp.read()

    print '* save data to %s' % save_fn
    # save to local file
    f = open(save_fn, 'w')
    f.write(data)
    f.close()

    print '* done!'

if __name__=='__main__':
    download()