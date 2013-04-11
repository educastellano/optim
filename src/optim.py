import os
import sys
import json

def usage():
    print 'usage: ' + os.path.basename(__file__) + ' json_file'

def loadConf(json_file):
    global conf, absPath, absPathAll, absPathMin
    # Load File
    file = open(json_file)
    conf = json.load(file)
    file.close()
    # Get absolute path of the json file
    absJsonFile = os.path.abspath(json_file)
    path = absJsonFile.split('/')
    path = path[:len(path)-1]
    absPathJsonFile = '/'.join(path)
    absPath = absPathJsonFile + '/' + conf['basepath']
    slash = '' if conf['output'][len(conf['output'])-1] == '/' else '/'
    absPathOutput = absPathJsonFile + '/' + conf['output'] + slash + conf['app']
    absPathAll = absPathOutput + '.all.js'
    absPathMin = absPathOutput + '.min.js'

def join():
    fileOut = open(absPathAll, 'w')
    code = ''
    for file in conf['files']:
        file = open(absPath + file, 'r')
        code += file.read() + '\n'
        file.close()
    fileOut.write(code)
    fileOut.close()

def minify():
    os.system('java -jar yuicompressor-2.4.2.jar ' + absPathAll + ' -o ' + absPathMin)

if len(sys.argv) > 1:
    loadConf(sys.argv[1])
    join()
    minify()
else:
    usage()


