# Puppet manifest to change OS configuration for holberton user

# Set open files limit for holberton user

# Increase hard file limit
exec { 'increase-hard-file-limit':
  command => '/bin/sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

# Increase soft file limit
exec { 'increase-soft-file-limit':
  command => '/bin/sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
