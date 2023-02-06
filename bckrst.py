#!/usr/bin/env python3.8

import os
import tarfile
import datetime
import shutil

def backup_ansible():
    ansible_dir = "/opt/ansible"
    ansible_cfg = "/etc/ansible/"
    backup_dir = "/backup/ansible/"
    restore_dir = "/backup/ansible/restore/"
    retention = 15

    # Get the current date and time
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d-%H-%M-%S")

    # Create the backup file name
    backup_file = "ansible_backup_{}.tar.gz".format(date_str)
    backup_path = os.path.join(backup_dir, backup_file)

    # Compress the ansible directory and configuration file into a tar.gz archive
    with tarfile.open(backup_path, "w:gz") as tar:
        tar.add(ansible_dir, arcname=os.path.basename(ansible_dir))
        tar.add(ansible_cfg, arcname=os.path.basename(ansible_cfg))

    # Remove backup files that are older than the retention period
    for f in os.listdir(backup_dir):
        file_path = os.path.join(backup_dir, f)
        if os.path.isfile(file_path) and f != backup_file:
            file_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if (now - file_time).days >= retention:
                os.remove(file_path)

def restore_ansible(backup_file):
    ansible_dir = "/opt/ansible/"
    ansible_cfg = "/etc/ansible/"
    restore_dir = "/backups/ansible/restore/"

    # Extract the backup file to the restore ansible directory and configuration file
    with tarfile.open(os.path.join(restore_dir, backup_file), "r:gz") as tar:
        tar.extractall("/")

    # Move the extracted files to their correct locations
    shutil.move("/{}".format(os.path.basename(ansible_dir)), ansible_dir)
    shutil.move("/{}".format(os.path.basename(ansible_cfg)), ansible_cfg)

# Call the backup function
backup_ansible()

# To restore, call the restore function and pass in the backup file name
# restore_ansible("ansible_backup_2021-01-01-12-00-00.tar.gz")

                                                                                                                                                                             1,1           Top
