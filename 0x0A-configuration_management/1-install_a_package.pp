# Puppet Manifest: 1-install_a_package.pp
# Description: Install Flask from pip3 with version 2.1.0

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
