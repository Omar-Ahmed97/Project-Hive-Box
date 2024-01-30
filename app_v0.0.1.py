
def get_app_name_version(file_path=__file__):
    file_path_component = file_path.split('\\')
    file_name_and_extension = file_path_component[-1].rsplit('v', -1)
    return file_name_and_extension[-1].removesuffix('.py')

    




print ('the version : {}'.format(get_app_name_version()))
