import os
import sys
import json

def usage():
    print '> usage: ' + os.path.basename(__file__) + ' json_file [tool]'
    print ''
    print '     tool => [ yui | uglifyjs | nocompress (default) ]'
    print ''

def loadConf(json_file):
    global conf, path_base, path_all, path_min
    # Load File
    _file = open(json_file)
    conf = json.load(_file)
    _file.close()
    # Get absolute path of the json file
    abs_conf_file = os.path.abspath(json_file)
    path_aux = abs_conf_file.split('/')
    path_aux = path_aux[:len(path_aux)-1]
    path = '/'.join(path_aux)
    path_base = path + '/' + conf['base']
    path_output = path + '/' + conf['output']
    path_base = path_base if path_base.endswith('/') else path_base + '/'
    path_output = path_output if path_output.endswith('/') else path_output + '/'
    if not os.path.exists(path_output):
    	os.makedirs(path_output)
    path_all = path_output + 'app.all.js'
    path_min = path_output + 'app.min.js'

def join():
    fileOut = open(path_all, 'w')
    code = ''
    for _file in conf['files']:
	path = path_base + _file
	path = path.replace('//', '/')
        _file = open(path, 'r')
        code += _file.read() + '\n'
        _file.close()
    fileOut.write(code)
    fileOut.close()

def minify(tool):
    if tool == 'yui':
        os.system('java -jar yuicompressor-2.4.2.jar %s -o %s' % (path_all, path_min))
    elif tool == 'uglifyjs':
        os.system('uglifyjs %s > %s ' % (path_all, path_min))
    elif tool == 'nocompress':
        os.system('cp %s %s' % (path_all, path_min))
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
