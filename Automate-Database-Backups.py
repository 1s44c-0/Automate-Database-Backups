import subprocess
import datetime
import os

def backup_mysql_db(db_name, user, password, backup_dir):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"{db_name}_backup_{timestamp}.sql")
    
    try:
        command = f"mysqldump -u {user} -p{password} {db_name} > {backup_file}"
        subprocess.run(command, shell=True, check=True)
        print(f"Database {db_name} backed up successfully to {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during backup: {e}")

if __name__ == "__main__":
    db_name = "your_database"
    user = "your_username"
    password = "your_password"
    backup_dir = "/path/to/backup/directory"
    
    backup_mysql_db(db_name, user, password, backup_dir)
  
