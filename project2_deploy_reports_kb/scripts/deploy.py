#!/usr/bin/env python3
import os, shutil, subprocess, sys, json, datetime

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'project1_operations_platform'))
STAGING = os.path.join(REPO_DIR, 'staging_deploy')
BUILD_DIR = os.path.join(REPO_DIR, 'frontend')

def run(cmd):
    print('>>', cmd)
    res = subprocess.run(cmd, shell=True)
    if res.returncode != 0:
        print('Command failed:', cmd)
        sys.exit(res.returncode)

def prepare_staging():
    if os.path.exists(STAGING):
        shutil.rmtree(STAGING)
    os.makedirs(STAGING, exist_ok=True)
    # copy backend & frontend as a simple deploy
    shutil.copytree(os.path.join(REPO_DIR,'backend'), os.path.join(STAGING,'backend'))
    shutil.copytree(os.path.join(REPO_DIR,'frontend'), os.path.join(STAGING,'frontend'))
    print('Staging prepared at', STAGING)

def run_tests():
    # Placeholder for running tests
    print('Running basic smoke tests...')
    # e.g., check files exist
    assert os.path.exists(os.path.join(STAGING,'backend','server.js'))
    print('Tests passed')

def create_deploy_report(success, notes=''):
    report = {
        'timestamp': datetime.datetime.utcnow().isoformat() + 'Z',
        'success': success,
        'notes': notes
    }
    with open(os.path.join(STAGING, 'deploy_report.json'), 'w') as f:
        json.dump(report, f, indent=2)
    print('Deploy report written')

if __name__ == '__main__':
    try:
        prepare_staging()
        run_tests()
        # Simulate build step
        print('Building assets (simulated)...')
        create_deploy_report(True, 'Deployed to staging (simulated).')
        print('Deployment complete.')
    except Exception as e:
        create_deploy_report(False, str(e))
        raise
