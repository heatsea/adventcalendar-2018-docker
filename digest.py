#!/usr/bin/python

import os
import hashlib
import urlparse
# import sys

if 'QUERY_STRING' in os.environ:
    qs = urlparse.parse_qs(os.environ['QUERY_STRING'])
else:
    qs = {}

st = qs['str'][0]
hash_md5 = hashlib.md5()
hash_sha256 = hashlib.sha256()
hash_sha512 = hashlib.sha512()


if st is None:
    print 'Status: 400 Bad Request'
else:
    hash_md5.update(st)
    hash_sha256.update(st)
    hash_sha512.update(st)
    for i in range(1000000):
        #        sys.stderr.write('hello' + st + 'i:' + str(i) + '\r\n')
        hash_md5.update(hash_md5.hexdigest())
        hash_sha256.update(hash_sha256.hexdigest())
        hash_sha512.update(hash_sha512.hexdigest())

print('Content-type: text/plain; charset=UTF-8\r\n')
print(hash_md5.hexdigest())
print(hash_sha256.hexdigest())
print(hash_sha512.hexdigest())