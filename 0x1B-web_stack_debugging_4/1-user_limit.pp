# Puppet manifest to change OS configuration for holberton user

# Change the open files limit for the holberton user
exec { 'change-os-configuration-for-holberton-user':
  command => 'ulimit -n 4096',
  user    => 'holberton',
  path    => '/usr/local/bin/:/bin/',
}
