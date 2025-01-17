import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pgbackrest(host):
    with host.sudo("postgres"):
        result = host.run('cd /var/lib/postgresql/ && pgbackrest/test/test.pl --pgsql-bin=/usr/lib/postgresql/15/bin --no-valgrind --log-level-test-file=off --no-coverage-report --module=command --module=storage --vm-out --vm=none --no-coverage')
        print(result.stdout)
        if result.rc != 0:
            print(result.stderr)
            raise AssertionError


