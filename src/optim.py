import os
import sys
import json

def usage():
    print 'usage: ' + os.path.basename(__file__) + ' json_file [tool]'
    print '  > tool = yui | uglifyjs | nocompress (default)'

def loadConf(json_file):
    global conf, absPath, absPathAll, absPathMin
    # Load File
    _file = open(json_file)
    conf = json.load(_file)
    _file.close()
    # Get absolute path of the json file
    absJsonFile = os.path.abspath(json_file)
    path = absJsonFile.split('/')
    path = path[:len(path)-1]
    absPathJsonFile = '/'.join(path)
    absPath = absPathJsonFile + '/' + conf['basepath']
    absPathOutput = absPathJsonFile + '/build/app'
    absPathAll = absPathOutput + '.all.js'
    absPathMin = absPathOutput + '.min.js'

def join():
    fileOut = open(absPathAll, 'w')
    code = ''
    for _file in conf['files']:
        _file = open(absPath + _file, 'r')
        code += _file.read() + '\n'
        _file.close()
    fileOut.write(code)
    fileOut.close()

def minify(tool):
    if tool == 'yui':
        os.system('java -jar yuicompressor-2.4.2.jar %s -o %s' % (absPathAll, absPathMin))
    elif tool == 'uglify':
        os.system('uglifyjs %s > %s ' % (absPathAll, absPathMin))
    elif tool == 'nocompress':
        os.system('cp %s %s' % (absPathAll, absPathMin))
    else:
        exit(tool + ' not supported')

def main():
    if len(sys.argv) > 1:
        loadConf(sys.argv[1])
        join()
        minify_tool = sys.argv[2] if len(sys.argv) > 2 else 'nocompress'
        minify(minify_tool)
    else:
        usage()

if __name__ == '__main__':
    main()
