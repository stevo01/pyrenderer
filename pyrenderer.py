'''
Created on Dec 31, 2020

@author: stevo
'''
import glob
import os
import argparse
import timeit
from utils.glog import logger_init
from logging import INFO, DEBUG
from utils.proc import ExecuteCmdExt
import shutil
from utils.file_and_folder import ensure_dir
from time import sleep
import concurrent.futures


def move_file(indir, filename, dir_name="./tmp/"):

    src = filename
    dst = dir_name + filename
    ensure_dir(dir_name)
    shutil.move(src, dst)


def render(file):
        
        res = file[:-4].split('-')
        x = int(res[0])
        y = int(res[1])
        z = int(res[2])

        convert_cmd = "java -jar ./extutils/jrender.jar {} {} {} {} {} ".format(args.indir, args.outdir, z, x, y)
        log.info(convert_cmd)
        outstr, ret = ExecuteCmdExt(convert_cmd, cwd)

        if ret is 0:
            move_file(args.indir, file, "./pass/")
        else:
            move_file(args.indir, file, "./fail/")          
        
        return ret, file, outstr

def main():

    # determine files for rendering
    files = list()
    for file in glob.glob("*.osm"):

        filesize = os.stat(file).st_size
        if filesize < 100:
            log.info("renderer skipped for {}".format(file))
            # move file to osm tmp dir
            move_file(args.indir, file, "./pass/")
            continue

        files.append(file)

    file_sum_cnt = len(files)
    render_cnt = 0
    render_error_cnt = 0
    log.info("start renderer for rendering of {} tiles".format(file_sum_cnt))


    with concurrent.futures.ThreadPoolExecutor(max_workers = args.threads) as executor:
        futures = []
            
    
        for file in files:
            futures.append(executor.submit(render, file))
                
        for future in concurrent.futures.as_completed(futures):
            ret, file, outstr = future.result()
        
            if ret != 0:
                log.error("generation failed for file: {} {}/{}/{}".format(file, render_cnt, render_error_cnt, file_sum_cnt))
                log.error(outstr)
                render_error_cnt += 1
            else:
                log.info("generation passed for file: {} {}/{}/{}".format(file, render_cnt, render_error_cnt, file_sum_cnt))
                render_cnt += 1


if __name__ == '__main__':

    start = timeit.default_timer()
    
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-i',
                        dest='indir',
                        default="./workingdir/osm-extracts/",
                        help='directory with osm extracts')

    parser.add_argument('-o',
                        dest='outdir',
                        default="./workingdir/tiles/",
                        help='output directory for storage of generated tiles')
    
    parser.add_argument('-l',
                        dest='logfilename',
                        default="./log/pyrenderer.log",
                        help='logfile')
    
    parser.add_argument('-t',
                        dest='threads',
                        type=int,
                        default=1,
                        help='number of parallel threads')

    parser.add_argument('-d', '--daemon', action='store_true')

    args = parser.parse_args()

    ensure_dir(args.logfilename)

    log = logger_init("pyrenderer",
                      args.logfilename,
                      level_file=DEBUG,
                      level_console=INFO)

    log.info("pyrender")
    log.info("input  directory: {}".format(args.indir))
    log.info("output directory: {}".format(args.outdir))

    cwd = os.getcwd()
    os.chdir(args.indir)

    ensure_dir("./tmp/")
    
    # print java version
    get_version_cmd = "java -version"
    outstr, ret = ExecuteCmdExt(get_version_cmd, cwd)
    log.info(outstr)

    while(True):
        main()
        if args.daemon is False:
            break
        sleep(1.0)

    stop = timeit.default_timer()
    log.info('pyrenderer ready / runtime: {} s'.format(stop - start))
