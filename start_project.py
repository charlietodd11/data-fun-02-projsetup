'''Start a data analytics project.'''

#Start with imports from the Python Standard Library
import pathlib

#Then, import your own modules
def create_project_directory(directory_name: str) -> None:
    """Create project sub-directory. 
    :param directory_name: Name of the directory to be created, e.g."test"
    """
    pathlib.Path(directory_name).mkdir(exist_ok=True)


#Define your functions here




#Define your functions here
def main():
    '''Scaffold a project'''
    create_project_directory(directory_name='test')
    create_project_directory(directory_name='docs')
#Add module block at the bottom

if __name__=='__main__':
    main()