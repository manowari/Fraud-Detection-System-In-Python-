  GitHub has a recommended maximum file size of 50 MB, and a hard limit of 100 MB for individual files.

To address this issue, you can follow these steps:

1. **Use Git LFS (Large File Storage):**
   - Git LFS is a Git extension for managing large files. It replaces large files with text pointers inside Git, while the actual files are stored on a Git LFS server. GitHub supports Git LFS.
   - Install Git LFS on your local machine by following the instructions: [Installing Git LFS](https://git-lfs.github.com/)
   - Initialize Git LFS for your repository:
     ```bash
     git lfs install
     ```
   - Track large files using Git LFS. For example:
     ```bash
     git lfs track "src/data/raw_data_files/*.csv"
     ```
   - Commit and push the changes:
     ```bash
     git add .gitattributes
     git commit -m "Use Git LFS for large files"
     git push origin master
     ```
   
2. **Remove Large Files from Git History:**
   - If you want to remove the large files from the Git history entirely, you can use tools like `filter-branch` or `filter-repo`. However, be cautious as rewriting history can have consequences, especially if you're working in a shared repository.
   - Backup your repository before proceeding.
   - Install `filter-repo`:
     ```bash
     pip install --user filter-repo
     ```
   - Run `filter-repo` to remove large files:
     ```bash
     filter-repo --strip-blobs-bigger-than 50M
     ```
   - Force-push the changes:
     ```bash
     git push -f origin master
     ```

Choose the approach that best fits your needs. If you are working in a collaborative environment, it's advisable to communicate with your team about any changes to the repository history.