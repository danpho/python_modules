import pkg_resources


class ck(object):
    def ck_lib(lib_name=None):
        installed_packages = pkg_resources.working_set
        installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
        for lib in installed_packages_list:
            size = len(lib_name)
            flag = False
            if lib_name == lib[:size]:
                flag = True
                break
        if flag:
            print("installed")
        else:
            print("not installed")
        return flag


flg = ck_lib("numba")
