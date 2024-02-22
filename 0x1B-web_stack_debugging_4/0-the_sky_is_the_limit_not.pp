# Puppet manifest to optimize Nginx configuration

# Ensure Nginx package is installed
package { 'nginx':
  ensure => 'installed',
}

# Use sed to modify the Nginx worker connections in /etc/default/nginx
exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Notify Nginx service to restart upon configuration changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Exec['fix--for-nginx'],
}
