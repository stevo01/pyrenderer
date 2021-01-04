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


def move_file(indir, filename):

    src = filename
    dst = "./tmp/" + filename

    shutil.move(src, dst)


def main():

    # determine files for rendering
    files = list()
    for file in glob.glob("*.osm"):

        filesize = os.stat(file).st_size
        if filesize < 100:
            log.info("renderer skipped for {}".format(file))
            # move file to osm tmp dir
            move_file(args.indir, file)
            continue

        files.append(file)

    file_sum_cnt = len(files)
    render_cnt = 0
    render_error_cnt = 0
    log.info("start renderer for rendering of {} tiles".format(file_sum_cnt))

    for file in files:

        res = file[:-4].split('-')
        x = int(res[0])
        y = int(res[1])
        z = int(res[2])

        convert_cmd = "java -jar ./extutils/jrender.jar {} {} {} {} {} ".format(args.indir, args.outdir, z, x, y)
        outstr, ret = ExecuteCmdExt(convert_cmd, cwd)

        if ret != 0:
            log.error("generation failed for file: {} {}/{}/{}".format(file, render_cnt, render_error_cnt, file_sum_cnt))
            log.error(convert_cmd)
            log.error(outstr)
            render_error_cnt += 1
        else:
            log.info("generation passed for file: {} {}/{}/{}".format(file, render_cnt, render_error_cnt, file_sum_cnt))
            render_cnt += 1

        move_file(args.indir, file)


if __name__ == '__main__':

    start = timeit.default_timer()
    log = logger_init("pyrenderer",
                      "pyrenderer.log",
                      level_file=DEBUG,
                      level_console=INFO)

    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-i',
                        dest='indir',
                        default="./workingdir/osm-extracts/",
                        help='directory with osm extracts')

    parser.add_argument('-o',
                        dest='outdir',
                        default="./workingdir/tiles/",
                        help='output directory for storage of generated tiles')

    parser.add_argument('-d', '--daemon', action='store_true')

    args = parser.parse_args()

    log.info("pyrender")
    log.info("input  directory: {}".format(args.indir))
    log.info("output directory: {}".format(args.outdir))

    cwd = os.getcwd()
    os.chdir(args.indir)

    ensure_dir("./tmp/")

    while(True):
        main()
        if args.daemon is True:
            break
        sleep(1.0)

    stop = timeit.default_timer()
    log.info('pyrenderer ready / runtime: {:.2} s'.format(stop - start))
