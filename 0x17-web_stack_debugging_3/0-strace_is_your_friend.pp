# 0-strace_is_your_friend.pp
# Puppet manifest to fix Apache 500 error related to permissions

# Install strace package
package { 'strace':
  ensure => installed,
}

# Execute strace on the Apache process to identify the issue
exec { 'strace_apache':
  command => '/usr/bin/strace -o /tmp/strace_output.txt -p $(pgrep apache2)',
  path    => ['/bin', '/usr/bin'],
  require => Package['strace'],
}

# Fix the identified issue (example: fixing permissions)
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],
  require => Exec['strace_apache'],
}

# Get the Apache process ID using a Puppet fact
$apache_pid = $::service_apache2 ? {
  true  => $::service_apache2_pid,
  false => fail('Apache service not found'),
}

# Restart Apache to apply the fix
service { 'apache2':
  ensure    => 'running',
  enable    => true,
  require   => Exec['fix-wordpress'],
  hasstatus => true,
  subscribe => Exec['fix-wordpress'],
  pidfile   => $apache_pid,
}
