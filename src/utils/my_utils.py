def create_init_files(root_dir):
    '''Creates Init  files '''
    
    for foldername, subfolders, filenames in os.walk(root_dir):
        # Exclude venv folder
        if 'venv' in subfolders:
            subfolders.remove('venv')
        
        init_file_path = os.path.join(foldername, '__init__.py')
        
        # Skip if __init__.py already exists in the subfolder
        if not os.path.exists(init_file_path):
            with open(init_file_path, 'w'):
                pass
            print(f"Created __init__.py in {foldername}")
