import subprocess

if __name__ == "__main__":
    subprocess.call(['sudo', 'python3', '-m', 'xmlrunner', 'irods.test.test_rule_engine_plugin_project_template_cpp'])

