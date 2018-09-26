#! /usr/bin/python
#-*-coding:utf8-*-

import os


class SplitType:
    ROW = 0
    BYTE = 1
    FILE = 2


class FileUtil:
    '''util for file'''
    @staticmethod
    def exists(file_path):
        return os.path.exists(file_path)

    @staticmethod
    def is_file(file_path):
        return os.path.isfile(file_path)

    @staticmethod
    def delete(file_path):
        os.unlink(file_path)

    @staticmethod
    def clear(file_path):
        if FileUtil.exists(file_path):
            with open(file_path, "w+") as f:
                pass

    @staticmethod
    def create(file_path, overwrite=True):
        try:
            if FileUtil.exists(file_path):
                if overwrite:
                    FileUtil.clear(file_path)

                flag_create = False
            else:
                with open(file_path, "w+") as f:
                    pass
        except Exception as e:
            raise e

    @staticmethod
    def get_row_count(file_path):
        try:
            with open(file_path, 'r') as fs:
                return len(fs.readlines())
        except Exception as e:
            raise e

    @staticmethod
    def split(file_path, size, dir_path="./", split_type=SplitType.ROW):
        if split_type == SplitType.ROW:
            FileUtil.__split_by_row(file_path, size, dir_path)
        elif split_type == SplitType.FILE:
            FileUtil.__split_by_file(file_path, size, dir_path)

    @staticmethod
    def __split_by_row(file_path, size, dir_path="./tmp/"):
        part_num = 0
        part_size = 0
        create_new_part = True
        fs = None

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        if FileUtil.exists(file_path):
            with open(file_path, 'r') as total:
                for line in total:
                    if create_new_part:
                        if fs:
                            fs.close()
                            fs = None

                        fs = open(dir_path + file_path + ".%s" %
                                  part_num, 'w+')
                        part_num += 1
                        part_size = 0
                        create_new_part = False

                    fs.write(line)
                    part_size += 1

                    if part_size == size:
                        create_new_part = True

                if fs:
                    fs.close()
                    fs = None

        @staticmethod
        def __split_by_file(file_path, size, dir_path="./tmp/"):
            part_num = 0
            part_size = 0
            create_new_part = True
            fs = None
            row_count_total = FileUtil.get_row_count(file_path)
            row_count_part = row_count_total // size
            row_need_adding = row_count_total % size
            flag_add = row_need_adding

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            if FileUtil.exists(file_path):
                with open(file_path, 'r') as total:
                    for line in total:
                        if create_new_part:
                            if fs:
                                fs.close()
                                fs = None

                            fs = open(dir_path + file_path + ".%s" %
                                      part_num, 'w+')
                            part_num += 1
                            part_size = 0
                            create_new_part = False

                            if row_need_adding > 0:
                            	flag_add = True

                        fs.write(line)
                        part_size += 1

                        if part_size >= row_count_part:
                        	if not flag_add:
	                        	create_new_part = True
	                        	flag_add = False

                        	row_need_adding -= 1

                    if fs:
                        fs.close()
                        fs = None


if __name__ == '__main__':
    FileUtil.split("test.txt", 3)
