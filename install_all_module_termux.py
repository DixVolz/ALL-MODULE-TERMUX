import subprocess

def install_package(package_name):
    try:
        subprocess.check_call(['pkg', 'install', '-y', package_name])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}: {e}")
        return False
    return True

def install_python_package(package_name):
    try:
        subprocess.check_call(['pip', 'install', package_name])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}: {e}")
        return False
    return True

def get_all_termux_packages():
    try:
        output = subprocess.check_output(['pkg', 'list-all'])
        packages = [line.split('/')[0] for line in output.decode().splitlines() if line and ' ' not in line]
        return packages
    except subprocess.CalledProcessError as e:
        print(f"Failed to get Termux package list: {e}")
        return []
        
def get_all_python_packages():
    try:
        # This command lists all available packages on PyPI. It's very long and impractical to install all.
        output = subprocess.check_output(['pip', 'search', 'a']) # This is just an example and not practical for all packages
        packages = [line.split()[0] for line in output.decode().splitlines() if line]
        return packages
    except subprocess.CalledProcessError as e:
        print(f"Failed to get Python package list: {e}")
        return []

def main():
    print("Updating and upgrading Termux packages...")
    try:
        subprocess.check_call(['pkg', 'update'])
        subprocess.check_call(['pkg', 'upgrade'])
    except subprocess.CalledProcessError as e:
        print(f"Failed to update/upgrade Termux: {e}")
        return

     # Install all Termux packages
    termux_packages = get_all_termux_packages()
    if not termux_packages:
        print("No Termux packages found or failed to retrieve package list.")
    else:
        print("Installing all Termux packages...")
        for package in termux_packages:
            if not install_package(package):
                print(f"Skipping remaining installations due to error in {package}")
                return

    # Install all Python packages
    python_packages = get_all_python_packages()
    if not python_packages:
        print("No Python packages found or failed to retrieve package list.")
    else:
        print("Installing all Python packages...")
        for package in python_packages:
            if not install_python_package(package):
                print(f"Skipping remaining installations due to error in {package}")
                return

    print("All packages installed successfully!")

if __name__ == "__main__":
    main()